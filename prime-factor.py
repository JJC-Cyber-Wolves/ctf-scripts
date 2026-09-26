#The Python script is to find RSA p and q values 

import math

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def fermat_factor(n):
    # Fermat works only for odd n
    if n % 2 == 0:
        return 2, n // 2

    a = math.isqrt(n)
    if a * a < n:
        a += 1

    while True:
        b2 = a*a - n
        b = math.isqrt(b2)
        if b * b == b2:
            return a - b, a + b
        a += 1

# --- User Input ---
num_str = input("Enter an integer to factor: ").strip()
n = int(num_str)

# --- Prime Check ---
if is_prime(n):
    print(f"{n} is prime.")
else:
    p, q = fermat_factor(n)
    print("p =", p)
    print("q =", q)
    print("Check:", p * q == n)
