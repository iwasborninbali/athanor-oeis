"""Guide's independent checks for OEIS batch 2 (written from the statements, not from the agents' code)."""
from math import factorial

def primes(n):
    s = bytearray([1]) * (n + 1); s[:2] = b'\0\0'
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i*i::i] = bytes(len(range(i*i, n + 1, i)))
    return [i for i in range(n + 1) if s[i]]

# A007540: Lerch's congruence sum_{a<p} a^(p-1) == (p-1)! + p (mod p^2), hence the Ordowski-Resta criterion.
bad, wil, crit = [], [], []
for p in primes(10000)[1:]:
    m = p * p
    s = sum(pow(a, p - 1, m) for a in range(1, p)) % m
    f = 1
    for k in range(2, p): f = f * k % m
    if s != (f + p) % m: bad.append(p)
    if f == m - 1: wil.append(p)
    if s == (p - 1) % m: crit.append(p)
print(f"A007540: odd p<1e4: Lerch congruence failures {bad}; Wilson primes {wil}; criterion primes {crit}; equal {wil == crit}")

# A064591: 2*s0(n) - s1(n) = 1  <=>  n = 4P with P perfect (checked exactly for n <= N).
N = 2 * 10 ** 6
sig = [0] * (N + 1)
for d in range(1, N + 1):
    for k in range(d, N + 1, d): sig[k] += d
sols = []
for n in range(1, N + 1):
    a, m = 0, n
    while m % 2 == 0: m //= 2; a += 1
    if a >= 1 and (2 ** (a - 1) - 1) * sig[m] == 2 ** (a - 1) * m:  # (1 - 2^(1-a)) sigma(m)/m = 1
        sols.append(n)
perfect4 = [4 * p for p in range(1, N // 4 + 1) if sig[p] == 2 * p]
print(f"A064591: n<={N} with 2*s0-s1=1: {sols}; 4*perfect: {perfect4}; equal {sols == perfect4}")

# Direct check from divisors with exact fractions (independent of the closed form), n <= 20000.
from fractions import Fraction
direct = [n for n in range(1, 20001)
          if 2 * sum(Fraction(1, d) for d in range(2, n + 1, 2) if n % d == 0)
             - sum(Fraction(1, d) for d in range(1, n + 1, 2) if n % d == 0) == 1]
print("A064591: direct n<=20000:", direct)
