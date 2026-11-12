"""Independent check of the ChatGPT answer for task 2026-11-12-A111441-mod12 (written by the guide, not copied)."""
import sys

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\0\0"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytes(len(range(i * i, n + 1, i)))
    return [i for i in range(n + 1) if s[i]]

P = primes_upto(15_500_000)[:1_000_000]
assert len(P) == 1_000_000 and P[-1] == 15_485_863

terms, t = [], 0
for k, q in enumerate(P, 1):
    t += q * q
    if t % k == 0:
        terms.append(k)
print("m=2 terms <= 1e6:", terms)
print("any k = 3 or 9 mod 12:", any(k % 12 in (3, 9) for k in terms), "| any multiple of 2 or 3 except 1:", any(k > 1 and (k % 2 == 0 or k % 3 == 0) for k in terms))

for m in (2, 4, 6, 12):
    forb = [p for p in range(2, m + 2) if all(p % d for d in range(2, p)) and m % (p - 1) == 0]
    s, found, bad = 0, [], []
    for k, q in enumerate(P[:100_000], 1):
        s += q ** m
        if s % k == 0:
            found.append(k)
            if any(k % p == 0 for p in forb):
                bad.append(k)
    print(f"m={m} forbidden={forb} terms<=1e5={found} violations={bad}")
