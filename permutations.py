def is_prime(num):
    for i in range(2, num//2):  
        if (num % i) == 0:
            return False
    return True

def find_primes(n)
    primes = set([])
    for i in range(n):
        if is_prime(i):
            arr.add(i)
    return primes

def check_permutation(arr, primes):
    i = 0
    j = len(arr[i] - 1)
    for prime in primes: 