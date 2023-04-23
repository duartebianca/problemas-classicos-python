from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Any
from heapq import heappush, heappop
from typing_extensions import Protocol
import time
import random

#Create variable of generic type.
T = TypeVar('T')

def linear_contains (iterable: Iterable[T], key:T) -> bool:
  start_time = time.time()
  for item in iterable:
    if item == key:
      return True, (time.time() - start_time)
  return False, (time.time() - start_time)

C = TypeVar("C", bound = "Comparable")

class Comparable(Protocol):
  def __eq__(self, other: Any) -> bool:
    return self == other
  def __lt__(self: C, other: C) -> bool:
    return self < other
  def __gt__(self: C, other: C) -> bool:
    return (not self < other) and self != other
  def __le__(self: C, other: C) -> bool:
    return (self < other) or self == other
  def __ge__(self: C, other: C) -> bool:
    return (not self < other)

def binary_contains(sequence: Sequence[C], key: C) -> bool:
  start_time = time.time()
  low: int = 0
  high: int = len(sequence) - 1
  while (low <= high):
    mid: int = (low + high)//2
    if (sequence[mid] < key):
      low = mid+1
    elif (sequence[mid]>key):
      high = mid-1
    else:
      return True, (time.time() - start_time)
  return False, (time.time() - start_time)


#Use a list comprehension to generate a list of 1000 elements
list = [random.randint(1, 1000) for _ in range(1000)]

result_linear, time_linear = linear_contains(list, 1)
result_binary, time_binary = binary_contains(list, 1)

print(f'Time to get an answer ({result_linear}) in linear search: {time_linear: .7f}s.')
print(f'Time to get an answer ({result_binary}) in binary search: {time_binary: .7f}s.')
print(f'Binary Search is{time_linear/time_binary: .1f} times faster than linear search.')
