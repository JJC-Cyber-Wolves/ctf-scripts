"""
This Python script was created with the assistance of Co-Pilot
This python script allows a user to enter the prime numbers (p and q) along with the encryption (e) key value to produce the decryption (d) key value 
"""

def calculate_d(e, p, q):
    """
    Calculates the private exponent 'd' for RSA.
    """
    phi_n = (p - 1) * (q - 1)
    # d is the modular multiplicative inverse of e modulo phi_n
    # pow(e, -1, phi_n) computes the modular inverse
    d = pow(e, -1, phi_n)
    return d

# Example usage (using standard small example numbers)
p = int(input("Enter p value: ")) # a prime
q = int(input("Enter q value: ")) # another prime
e = int(input("Enter e value: ")) # public exponent, must be coprime to phi_n

d_value = calculate_d(e, p, q)
print(f"The calculated value for d is: {d_value}")

# Verification: (e * d) % phi_n should be 1
phi_n = (p - 1) * (q - 1)
if (e * d_value) % phi_n == 1:
    print("Verification successful: (e * d) % phi_n == 1")
else:
    print("Verification failed")
