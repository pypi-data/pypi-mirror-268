
from typing import overload


@overload
def xor_encrypt(data : str, key):
    ...

@overload
def xor_encrypt(data : bytes, key):
    ...

def xor_encrypt(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
