from rsa import *

class Person:

    def __init__(self, key_lentgh):
        public_key, private_key = generate_key_pair(key_lentgh)
        self.public_key = public_key
        self.private_key = private_key
