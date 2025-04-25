import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes_fractal(max_p):
    primes = []
    for n in range(1, int(np.sqrt(max_p))):
        candidate = 6 * n * (1 + np.sin(n * np.pi / 3)) - 1
        if is_prime(candidate):
            primes.append(candidate)
    return primes

# Plotando em coordenadas polares
primes = generate_primes_fractal(1000)

theta = [p % (2 * np.pi) for p in primes]
r = [np.log(p) for p in primes]

plt.figure(figsize=(10, 10))
plt.polar(theta, r, 'o', markersize=2)
plt.title("DNA Fractal dos Primos (Ressonância Áurea)")
plt.show()
