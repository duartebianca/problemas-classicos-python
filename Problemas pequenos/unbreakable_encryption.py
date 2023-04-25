from secrets import token_bytes
from typing import Tuple

def random_key(n: int) -> int:
  #Generate a random bytes sequence.
  tb: bytes = token_bytes(n)
  #Convert the bytes sequence to an integer.
  #"Big" specifies the byte order.
  return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
  #Convert the string to bytes.
  original_bytes: bytes = original.encode()
  #Generate a dummy key of the same length.
  dummy: int = random_key(len(original_bytes))
  #Convert the bytes to an integer.
  original_key: int = int.from_bytes(original_bytes, "big")
  #Apply the XOR operator.
  encrypted: int = original_key ^ dummy
  #Return a tuple with the dummy and encrypted message.
  return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
  #Receive the dummy key and the encrypted message.
  #Use this principle:
  #A^B = C
  #C^A = B
  #C^B = A
  #To obtain original_key (the original message in int).
  decrypted: int = key1^key2
  #Convert the original message in int to bytes.
  temp: bytes = decrypted.to_bytes( (decrypted.bit_length()+ 7) // 8, "big" )
  #Convert the bytes to a string.
  return temp.decode()

key1, key2 = encrypt("One Time Pad!")
result: str = decrypt(key1, key2)
print(result)
