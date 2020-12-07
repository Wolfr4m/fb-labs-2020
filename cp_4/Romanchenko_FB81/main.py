from person import *
from rsa import *

alice = Person(512)

ecnrypted = encrypt(111, alice.public_key)
print(ecnrypted)
decrypted = decrypt(ecnrypted, alice.private_key)
print(decrypted)

signed = sign(111, alice.private_key)
print(signed)
passed_verification = verify(111, signed, alice.public_key)
print(passed_verification)