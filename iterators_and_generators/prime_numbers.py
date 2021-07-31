def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_primes(seq):
    primes = filter(lambda n: is_prime(n), seq)
    for num in primes:
        yield num

