import hashlib
import io
from typing import overload

@overload
def hash_file(file : str, algorithm='sha256', chunk_size=4096):
    ...
@overload
def hash_file(file : io.IOBase, algorithm='sha256', chunk_size=4096):
    ...

def hash_file(file, algorithm='sha256', chunk_size=4096):
    """Hash a file with the specified algorithm and chunk size."""
    fileIo = file if isinstance(file, io.IOBase) else io.open(file, 'rb')
    hash_algo = hashlib.new(algorithm)
    chunk = fileIo.read(chunk_size)
    while chunk:
        hash_algo.update(chunk)
        chunk = fileIo.read(chunk_size)
    if file is not fileIo:
        fileIo.close()
    return hash_algo.hexdigest()

def hash_bytes(data, algorithm='sha256'):
    """Hash bytes with the specified algorithm."""
    return hashlib.new(algorithm, data).hexdigest()

