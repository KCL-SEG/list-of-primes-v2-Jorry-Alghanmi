"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def is_prime(num):
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def primes(number_of_primes):
    if number_of_primes<=0:
        raise ValueError("Enter a postive number that is more than 0")
    list = []
    num=2
    while len(list)<(number_of_primes):
       if is_prime(num):
           list.append(num)
       num+=1
    return list


