from person import *
from rsa import *
import requests

def pretty_hexed(num):
    return "0" + hex(num)[2:]

alice = Person(256)
message = 123456789

rec = requests.get(f"http://asymcryptwebservice.appspot.com/rsa/encrypt"
                   f"?modulus={pretty_hexed(alice.public_key[1])}"
                   f"&publicExponent={pretty_hexed(alice.public_key[0])}"
                   f"&message={pretty_hexed(message)}")

print(f"Check if messages encrypts same with api and local "
      f"{int(rec.json()['cipherText'], 16) == encrypt(message, alice.public_key)}")
