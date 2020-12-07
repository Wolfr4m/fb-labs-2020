from rsa_math import *


def generate_key_pair(key_length):
    first_prime = random_bit_prime(key_length)
    second_prime = random_bit_prime(key_length)
    modulus = first_prime * second_prime
    euler = (second_prime - 1) * (first_prime - 1)

    public_exponent = random_int(2, (euler - 1))

    while gcd(public_exponent, euler) > 1:
        public_exponent += 1
        if public_exponent + 1 == euler:
            public_exponent = random_int(2, (euler - 1))

    secret = opposite(public_exponent, euler)

    public_key = (public_exponent, modulus)
    private_key = (secret, modulus)

    return public_key, private_key


def encrypt():
    pass


def decrypt():
    pass


def sign():
    pass


def verify():
    pass


def send_key():
    pass


def recive_key():
    pass
