"""Guide's independent checks for OEIS batch 1 (written from the statements, not from the agents' code)."""
import sys

def check_a092506(N):
    phi = list(range(N + 1))
    for p in range(2, N + 1):
        if phi[p] == p:
            for k in range(p, N + 1, p):
                phi[k] -= phi[k] // p
    sols = [x for x in range(2, N + 1) if phi[x] + phi[x - 1] == (3 * x - 2) // 2]
    fermat = [x for x in range(2, N + 1) if phi[x] == x - 1 and (x - 1) & (x - 2) == 0]  # prime and x-1 power of 2
    print(f"A092506: solutions of phi(x)+phi(x-1)=floor((3x-2)/2) for 2<=x<={N}: {sols}; primes 2^n+1: {fermat}; equal: {sols == fermat}")

def max_z_solutions(n):
    """All (x,y,z), 0<x<y<z, 4/n = 1/x+1/y+1/z with the largest z (ties kept)."""
    best, out = 0, []
    x = n // 4 + 1
    while 3 * n > 4 * x * 1 and x * 4 * 1 < 3 * n + 4:  # 1/x > 4/(3n) bound: x < 3n/4
        if 4 * x >= 3 * n:
            break
        # 4/n - 1/x = (4x - n)/(n x) = a/b
        a, b = 4 * x - n, n * x
        y = max(x + 1, b // a + 1)          # need 1/y < a/b
        while 2 * b > a * y:                # y < 2b/a  (since 1/y > 1/z means 1/y > half of a/b)
            r = a * y - b                   # a/b - 1/y = r/(b y)
            if r > 0 and (b * y) % r == 0:
                z = b * y // r
                if z > y:
                    if z > best:
                        best, out = z, [(x, y, z)]
                    elif z == best:
                        out.append((x, y, z))
            y += 1
        x += 1
    return out

def check_a075245(N):
    viol = []
    for n in range(5, N + 1):
        sols = max_z_solutions(n)
        xs = sorted({s[0] for s in sols})
        allowed = {n // 4 + 1} | ({n // 4 + 2} if n % 8 == 1 else set())
        if not set(xs) <= allowed:
            viol.append((n, xs, sols[0]))
    print(f"A075245: n<= {N}: violations of floor(n/4)+d (d=1, or 2 for some n=8k+1): {viol}")
    print("A075245: n=409 max-z solutions:", max_z_solutions(409))

if __name__ == "__main__":
    check_a092506(10**7)
    check_a075245(int(sys.argv[1]) if len(sys.argv) > 1 else 500)
