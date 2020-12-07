import random


def random_int(min, max):
    return random.randint(min, max)


def random_prime(min_number, max_number):
    random_number = random_int(min_number, max_number)
    # if number is even -> +1
    # if number is odd -> do nothing
    if not is_odd(random_number):
        random_number += 1

    while True:
        # if number is prime -> return it
        # if number is not prime -> +2 and continue loop
        if is_prime(random_number):
            return random_number
        else:
            random_number += 2


def random_bit_prime(bit_lenght):
    # 10000....0000
    # min_number has "1" at the start and (bit_lenght - 1) "0"
    min_number = 2 ** (bit_lenght - 1)
    # 1111....1111
    # max_number has (bit_lenght) "1"
    max_number = 2 ** (bit_lenght + 1) - 1
    return random_prime(min_number, max_number)


def gcd(first_num, second_num):
    if second_num == 0:
        return first_num
    else:
        return gcd(second_num, first_num % second_num)


# Miller-Rabin primality test
def is_prime(n):
    k = 1024
    # prevent potential infinite loop when d = 0
    if n < 2:
        return False

    # Decompose (n - 1) to write it as (2 ** r) * d
    # While d is even, divide it by 2 and increase the exponent.
    d = n - 1
    r = 0

    while not (d & 1):
        r += 1
        d >>= 1

    # Test k witnesses.
    for _ in range(k):
        # Generate random integer a, where 2 <= a <= (n - 2)
        a = random_int(2, n-2)

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                # n is composite.
                return False
            if x == n - 1:
                # Exit inner loop and continue with next witness.
                break
        else:
            # If loop doesn't break, n is composite.
            return False

    return True


def is_odd(number):
    return number % 2 == 1


def opposite(a, mod):
    coefficients = []
    fnumber = a
    snumber = mod
    while snumber != 0:
        temp = snumber
        if fnumber > snumber:
            coefficients.append(fnumber // snumber)
        snumber = fnumber % snumber
        fnumber = temp


    x1 = 1
    x0 = 0
    temp = 0
    for index in range(len(coefficients) - 1):
        temp = x1
        x1 = x1 * -(coefficients[index]) + x0
        x0 = temp
    if x1 < 0:
        x1 = x1 + mod
    return x1
