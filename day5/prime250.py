# Python 3.7.16
# This program finds prime numbers from 1 - 250 and writes to a file.

import math
from pathlib import Path

primes = []
for i in range(2, 251): 
    root = math.floor((math.sqrt(i)))
    isPrime = True
    for j in range(2, root):
        if(i % j == 0):
            isPrime = False
            break
    if(isPrime):
        primes.append(i)
print(primes)

p = Path(__file__).with_name("results.txt")
with p.open('w') as results:
    results.write(str(primes))
