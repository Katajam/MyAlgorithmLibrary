# Python 3
# Determine if a number is a prime

import random

def isPrime(n):
    if n == 1: return "Not prime"
    if n == 2: return "Prime"
    if n%2 == 0: return "Not prime"
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0: return "Not prime"
    return "Prime"

# test small numbers
for num in range(5):
	number = random.randint(1, 100)
	print('{} is {}'.format(number, isPrime(number)))

'''one possible output
98 is Not prime
71 is Prime
6 is Not prime
11 is Prime
2 is Prime
'''

# test big numbers
for num in range(5):
	number = random.randint(1, 10**8)
	print('{} is {}'.format(number, isPrime(number)))

'''one possible output
33534874 is Not prime
4727791 is Prime
16557631 is Not prime
56521409 is Not prime
72060120 is Not prime
'''