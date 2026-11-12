#!/usr/bin/env python3
"""Registry of the lab's OEIS contributions and candidates (see ../RULES.md).

  registry.py check [--remote]     validate records, repository names, certificates, status blocks
  registry.py render               write ../REGISTRY.md and the status block of every repository README
  registry.py event ID STATE NOTE  set a record's state and append a dated history line
  registry.py promote REPO ANUM    after submission: rename REPO to oeis-ANUM (local, GitHub, remote), update records
  registry.py list [STATE]         one line per record
"""
import datetime, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REG = HERE / "registry.json"
SCI = HERE.parent.parent                      # ~/projects/science
OWNER = "iwasborninbali"
STATES = ["idea", "candidate", "verified", "queued", "proposed", "reviewed", "approved",
          "rejected", "withdrawn", "superseded", "not-for-oeis"]
SUBMITTED = {"proposed", "reviewed", "approved"}
NEED_CERT = {"verified", "queued", "proposed", "reviewed", "approved"}
KINDS = {"new-sequence", "terms", "bounds", "data", "link", "correction", "proof", "reference", "check", "finding"}
BEGIN, END = "<!-- oeis-status:begin -->", "<!-- oeis-status:end -->"
REQUIRED = ["id", "anum", "repo", "kind", "title", "state", "certificate", "next", "owner", "history"]


def load():
    return json.loads(REG.read_text())


def save(reg):
    reg["updated"] = datetime.date.today().isoformat()
    REG.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + "\n")


def by_repo(reg):
    out = {}
    for r in reg["records"]:
        if r["repo"]:
            out.setdefault(r["repo"], []).append(r)
    return out


def expected_name(recs):
    """Naming rule of RULES.md section 2. Returns a regex the repository name must match."""
    anums = {r["anum"] for r in recs}
    if any(r["state"] in SUBMITTED for r in recs):
        return r"^oeis-A\d{6}$"
    if anums == {None}:
        return r"^oeis-A______-[a-z0-9]+(-[a-z0-9]+)*$"
    return r"^oeis-A\d{6}-unsubmitted$"


def status_block(repo, recs, today):
    lines = [BEGIN]
    if any(r["state"] in SUBMITTED for r in recs):
        head = f"**OEIS status** (lab registry, {today}):"
    elif all(r["anum"] is None for r in recs):
        head = f"**OEIS status: not submitted; no A-number yet** (lab registry, {today})."
    else:
        head = f"**OEIS status: not submitted** (lab registry, {today})."
    lines.append(head)
    lines.append("")
    for r in recs:
        last = r["history"][-1]
        a = f"[{r['anum']}](https://oeis.org/{r['anum']})" if r["anum"] else "A______"
        lines.append(f"- {a}, {r['title']}: **{r['state']}** ({last[0]}: {last[1]}). Certificate: {r['certificate']}.")
    lines.append("")
    lines.append("Rules and the full registry: [athanor-oeis](https://github.com/iwasborninbali/athanor-oeis/blob/main/REGISTRY.md).")
    lines.append(END)
    return "\n".join(lines)


def put_block(readme, block):
    text = readme.read_text()
    if BEGIN in text and END in text:
        new = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda m: block, text, flags=re.S)
    else:                                   # insert after the title line
        head, sep, rest = text.partition("\n")
        new = head + "\n\n" + block + "\n" + rest
    if new != text:
        readme.write_text(new)
        return True
    return False


def cmd_check(reg, remote=False):
    errs, ids = [], set()
    for r in reg["records"]:
        for k in REQUIRED:
            if k not in r:
                errs.append(f"{r.get('id')}: missing field {k}")
        if r["id"] in ids:
            errs.append(f"{r['id']}: duplicate id")
        ids.add(r["id"])
        if r["state"] not in STATES:
            errs.append(f"{r['id']}: unknown state {r['state']}")
        if r["kind"] not in KINDS:
            errs.append(f"{r['id']}: unknown kind {r['kind']}")
        if r["anum"] is not None and not re.fullmatch(r"A\d{6}", r["anum"]):
            errs.append(f"{r['id']}: bad A-number")
        if r["state"] in NEED_CERT and r["certificate"] != "complete":
            errs.append(f"{r['id']}: state {r['state']} needs a complete certificate (has {r['certificate']})")
        if r["state"] in NEED_CERT and not r.get("guide_check"):
            errs.append(f"{r['id']}: state {r['state']} needs the guide's check")
        if r["state"] not in ("approved", "rejected", "withdrawn", "superseded", "not-for-oeis") and not r["next"]:
            errs.append(f"{r['id']}: no next action")
        if r["repo"] is None and not r.get("see_repo") and r["state"] not in ("idea", "not-for-oeis", "superseded"):
            errs.append(f"{r['id']}: state {r['state']} needs a repository")
    remote_names = None
    if remote:
        out = subprocess.run(["gh", "repo", "list", OWNER, "--limit", "300", "--json", "name,visibility"],
                             capture_output=True, text=True, check=True).stdout
        remote_names = {x["name"]: x["visibility"] for x in json.loads(out)}
    for repo, recs in sorted(by_repo(reg).items()):
        rx = expected_name(recs)
        if not re.match(rx, repo):
            errs.append(f"{repo}: name does not match {rx} for states {[r['state'] for r in recs]}")
        m = re.match(r"^oeis-(A\d{6})", repo)
        if m and any(r["anum"] != m.group(1) for r in recs):
            errs.append(f"{repo}: record A-number differs from the repository name")
        d = SCI / repo
        if not (d / ".git").exists():
            errs.append(f"{repo}: no local repository at {d}")
            continue
        for f in ("README.md", "CERTIFICATE.md", "PRIOR-ART.md", "LICENSE.md"):
            if not (d / f).exists():
                errs.append(f"{repo}: {f} missing")
        if (d / "README.md").exists():
            t = (d / "README.md").read_text()
            if BEGIN not in t or END not in t:
                errs.append(f"{repo}: README has no status block (run render)")
            elif status_block(repo, recs, "X").split("\n")[3:] != \
                    t[t.index(BEGIN):t.index(END) + len(END)].split("\n")[3:]:
                errs.append(f"{repo}: README status block is stale (run render)")
        if subprocess.run(["git", "-C", str(d), "status", "--porcelain"], capture_output=True, text=True).stdout.strip():
            errs.append(f"{repo}: uncommitted changes")
        if remote_names is not None:
            if repo not in remote_names:
                errs.append(f"{repo}: not on GitHub")
            elif remote_names[repo] != "PUBLIC":
                errs.append(f"{repo}: GitHub repository is not public")
    for d in sorted(SCI.glob("oeis-A*")):
        if d.name not in by_repo(reg):
            errs.append(f"{d.name}: local repository without a registry record")
    for e in errs:
        print("ERROR", e)
    print(f"{len(reg['records'])} records, {len(by_repo(reg))} repositories, {len(errs)} errors")
    return 1 if errs else 0


def cmd_render(reg):
    today = datetime.date.today().strftime("%-d %b %Y")
    changed = []
    for repo, recs in sorted(by_repo(reg).items()):
        readme = SCI / repo / "README.md"
        if readme.exists() and put_block(readme, status_block(repo, recs, today)):
            changed.append(repo)
    order = {s: i for i, s in enumerate(["proposed", "reviewed", "queued", "verified", "candidate", "idea", "approved",
                                         "superseded", "rejected", "withdrawn", "not-for-oeis"])}
    titles = {"proposed": "Open drafts (proposed)", "reviewed": "Open drafts (reviewed by an editor)",
              "queued": "Queued for submission", "verified": "Verified, not yet queued",
              "candidate": "Candidates (repository exists, verification not complete)", "idea": "Ideas (no repository yet)",
              "approved": "Approved", "superseded": "Superseded", "rejected": "Rejected", "withdrawn": "Withdrawn",
              "not-for-oeis": "Findings that are not OEIS items"}
    out = ["# Registry of OEIS contributions and candidates", "",
           f"Generated by `registry/registry.py render` from `registry/registry.json` on {today}. Do not edit by hand. Rules: [RULES.md](RULES.md).",
           "", "Counts: " + ", ".join(f"{s} {n}" for s in order
                                      for n in [sum(r["state"] == s for r in reg["records"])] if n) + ".", ""]
    for s in sorted(order, key=order.get):
        recs = [r for r in reg["records"] if r["state"] == s]
        if not recs:
            continue
        out += [f"## {titles[s]}", "", "| Entry | Repository | Kind | What | Certificate | Next (owner) |", "|---|---|---|---|---|---|"]
        for r in recs:
            a = f"[{r['anum']}](https://oeis.org/{r['anum']})" if r["anum"] else "A______"
            rp = f"[{r['repo']}](https://github.com/{OWNER}/{r['repo']})" if r["repo"] else "—"
            if r.get("see_repo"):
                rp = f"see [{r['see_repo']}](https://github.com/{OWNER}/{r['see_repo']})"
            what = r["title"] + (": " + r["claim"] if r.get("claim") else "")
            if r.get("prior_art"):
                what += f" *Prior art: {r['prior_art']}*"
            nxt = (r["next"] or "—") + (f" ({r['owner']})" if r["next"] else "")
            out.append(f"| {a} | {rp} | {r['kind']} | {what.replace('|', '/')} | {r['certificate']} | {nxt.replace('|', '/')} |")
        out.append("")
    (HERE.parent / "REGISTRY.md").write_text("\n".join(out))
    print("REGISTRY.md written; status blocks updated in:", ", ".join(changed) or "none")


def cmd_event(reg, rid, state, note):
    r = next(x for x in reg["records"] if x["id"] == rid)
    assert state in STATES, state
    r["state"] = state
    r["history"].append([datetime.date.today().isoformat(), note])
    save(reg)
    print(rid, "->", state)


def cmd_promote(reg, repo, anum):
    assert re.fullmatch(r"A\d{6}", anum), anum
    new = f"oeis-{anum}"
    src, dst = SCI / repo, SCI / new
    assert src.exists() and not dst.exists(), (src, dst)
    subprocess.run(["gh", "repo", "rename", new, "--repo", f"{OWNER}/{repo}", "--yes"], check=True)
    src.rename(dst)
    subprocess.run(["git", "-C", str(dst), "remote", "set-url", "origin", f"https://github.com/{OWNER}/{new}.git"], check=True)
    for r in reg["records"]:
        if r["repo"] == repo:
            r["repo"], r["anum"] = new, anum
            r["history"].append([datetime.date.today().isoformat(), f"repository renamed {repo} -> {new}"])
    save(reg)
    print(f"renamed {repo} -> {new}; now set the state with `event`, fix the README title, run render, commit and push")


def main(argv):
    reg = load()
    cmd = argv[1] if len(argv) > 1 else "check"
    if cmd == "check":
        return cmd_check(reg, "--remote" in argv)
    if cmd == "render":
        return cmd_render(reg)
    if cmd == "event":
        return cmd_event(reg, argv[2], argv[3], argv[4])
    if cmd == "promote":
        return cmd_promote(reg, argv[2], argv[3])
    if cmd == "list":
        for r in reg["records"]:
            if len(argv) < 3 or r["state"] == argv[2]:
                print(f"{r['state']:13} {r['anum'] or 'A______'} {r['repo'] or '-':52} {r['title']}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
