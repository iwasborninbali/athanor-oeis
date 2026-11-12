"""Guide's independent checks for OEIS batch 3 (written from the statements, not from the agents' code)."""
from math import comb, log
from fractions import Fraction

# A007097: a(0)=1, a(n+1) = prime(a(n)). Terms from the OEIS snapshot (offset 0).
import re
_seq = open('/Users/iwasborninbali/projects/science/athanor-oeis/tasks/2026-11-12-A007097-primeth-log-product/context/A007097.seq').read()
a = [int(t) for l in re.findall(r'^%[STU] A007097 (.*)$', _seq, re.M) for t in l.strip(',').split(',')]
assert re.search(r'^%O A007097 0', _seq, re.M), 'offset 0 expected'
prod = 1.0
print("A007097: n, P(n)=prod_{k=1..n} log a(k), P/a(n), P/(a(n) loglog a(n))")
for n in range(1, len(a)):
    prod *= log(a[n])
    if n >= 8:
        print(f"  {n:2d} {prod:.6e} {prod / a[n]:.5f} {prod / (a[n] * log(log(a[n]))):.5f}")

# A059442 fence bound at m = n = 74: (2m-1)*T(2m-6+n, m) + m + 1, T(N,k) = partitions of N into exactly k parts.
def parts_exact(N, k):
    # p(N, exactly k parts) = p(N-k, parts <= k)
    M = N - k
    dp = [1] + [0] * M
    for part in range(1, k + 1):
        for s in range(part, M + 1):
            dp[s] += dp[s - part]
    return dp[M]

m = n = 74
T = parts_exact(2 * m - 6 + n, m)
bound = (2 * m - 1) * T + m + 1
lhs = 2 * comb(bound, m)                 # Erdos: R(m,m) > N if 2*C(N,m) < 2^(C(m,2))
rhs = 2 ** comb(m, 2)
print(f"A059442: T(216,74) = {T}; fence bound for R(74,74) = {bound}")
print(f"A059442: 2*C(bound,74) < 2^C(74,2): {lhs < rhs}  (log2 lhs = {lhs.bit_length() - 1}, exponent {comb(m, 2)})")
# smallest diagonal m where the Erdos bound already beats the fence bound
for mm in range(3, 120):
    Tm = parts_exact(3 * mm - 6, mm)
    b = (2 * mm - 1) * Tm + mm + 1
    if 2 * comb(b, mm) < 2 ** comb(mm, 2):
        print(f"A059442: first diagonal m with Erdos > fence: m = {mm} (fence bound {b})")
        break
