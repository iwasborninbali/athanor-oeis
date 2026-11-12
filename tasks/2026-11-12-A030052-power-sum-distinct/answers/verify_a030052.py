"""Guide's independent check of the A332101/A078607 claim at n0 = 777451915729368 (own code, directed-rounding Decimal).

Claim: A078607(n0) = k = 1121626023352384 and A332101(n0) = k + 1, so A332101(n0) = A078607(n0) + 1, not + 2.
Needed: 2*((k-1)/k)^n0 < 1, 2*(k/(k+1))^n0 > 1, and sum_{h=1..120} ((N-h)/N)^n0 > 1 with N = k + 1.
"""
from decimal import Decimal, getcontext, ROUND_FLOOR, ROUND_CEILING, localcontext

PREC = 90
getcontext().prec = PREC  # printed differences at full precision
n0 = 777451915729368
k = 1121626023352384
N = k + 1


def div(p, q, mode):
    with localcontext() as c:
        c.prec, c.rounding = PREC, mode
        return Decimal(p) / Decimal(q)


def mul(a, b, mode):
    with localcontext() as c:
        c.prec, c.rounding = PREC, mode
        return a * b


def power(p, q, e, mode):
    """Rigorous one-sided bound of (p/q)^e: mode FLOOR gives a lower bound, CEILING an upper bound (0 < p/q < 1)."""
    base = div(p, q, mode)
    result = Decimal(1)
    while e:
        if e & 1:
            result = mul(result, base, mode)
        e >>= 1
        if e:
            base = mul(base, base, mode)
    return result


up_prev = power(k - 1, k, n0, ROUND_CEILING)      # upper bound of ((k-1)/k)^n0
lo_cur = power(k, k + 1, n0, ROUND_FLOOR)         # lower bound of (k/(k+1))^n0
lo_sum = Decimal(0)
for h in range(1, 121):
    term = power(N - h, N, n0, ROUND_FLOOR)
    with localcontext() as c:
        c.prec, c.rounding = PREC, ROUND_FLOOR
        lo_sum = lo_sum + term

print("2*((k-1)/k)^n0 - 1  <=", 2 * up_prev - 1, "(must be < 0)")
print("2*(k/(k+1))^n0 - 1  >=", 2 * lo_cur - 1, "(must be > 0)")
print("sum_{h<=120} ((N-h)/N)^n0 - 1 >=", lo_sum - 1, "(must be > 0)")
# exact Decimal comparisons (no rounding): the margins are about 1e-32
ok = (up_prev < Decimal("0.5")) and (lo_cur > Decimal("0.5")) and (lo_sum > Decimal(1))
print("certificate holds:", ok, "=> A078607(n0) =", k, ", A332101(n0) =", k + 1)

# Small-range cross-check of the definitions: A332101(n) = A078607(n) + 2 for 2 <= n <= 300?
def B(n):
    m, s = 1, 0
    while m ** n > s:
        s += m ** n; m += 1
    return m

def C(n):
    x = 1
    while 2 * x ** n <= (x + 1) ** n:
        x += 1
    return x

print("n in 1..300 with A332101 != A078607 + 2:", [(n, B(n), C(n)) for n in range(1, 301) if B(n) != C(n) + 2])
