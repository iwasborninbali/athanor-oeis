"""Guide's check of A328151: a(2k) = A093195(k), a(2k+1) = 2*A006339(k)^2, by direct counting up to L."""
from math import isqrt
L = 4_000_000
R = bytearray(L + 1)            # ordered positive pairs, capped
D = [0] * (L + 1)               # unordered distinct positive pairs
for x in range(1, isqrt(L) + 1):
    for y in range(1, isqrt(L - x * x) + 1):
        N = x * x + y * y
        R[N] = min(255, R[N] + 1)
        if x < y:
            D[N] += 1
a, b, t = {}, {}, {}
for N in range(L + 1):
    a.setdefault(R[N], N); b.setdefault(D[N], N)
for m in range(1, isqrt(L) + 1):
    t.setdefault(D[m * m], m)       # least hypotenuse with exactly k triangles
bad = []
for n in sorted(a):
    k = n // 2
    if n % 2 == 0 and n > 0 and k in b and a[n] != b[k]: bad.append((n, a[n], b[k]))
    if n % 2 == 1 and k in t and 2 * t[k] ** 2 <= L and a[n] != 2 * t[k] ** 2: bad.append((n, a[n], 2 * t[k] ** 2))
print("a(n) found for n =", sorted(a)[:30], "...; mismatches:", bad)
