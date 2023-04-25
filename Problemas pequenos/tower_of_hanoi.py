#-------------------------------------------------
#TOWER OF HANOI
#In this problem, we have three towers: A, B, and C. Tower A contains n discs of varying sizes, which need to be transferred to tower C according to the following rules:

#Only one disc can be moved at a time.
#The disc at the top of any tower is the only one available for movement.
#A larger disc cannot be placed on top of a smaller one.

#It is important to note that disc 1 is the largest and starts at the bottom of tower A. Disc 2 is smaller than disc 1 and is positioned directly on top of it. Disc 3 is smaller than disc 2 and is placed on top of it, and so on.

#Note that these towers can be treated as stacks. A stack is a data structure based on Last-In-First-Out (LIFO) principle. This means that the last item added to the stack (the one on top) is the first to be removed. The two basic operations of a stack are push (adds an item) and pop (removes the last item).

#If you need to visualize tower of Hanoi to understand better this code, acess: https://www.mathsisfun.com/games/towerofhanoi.html
#-------------------------------------------------

from typing import TypeVar, Generic, List

#Define Generic Variable.
T = TypeVar('T')

class Stack(Generic[T]):
  def __init__(self) -> None:
    #Start an empty list.
    self._container: List[T] = []
  
  def push(self, item:T) -> None:
    #Add the item on the top.
    self._container.append(item)
  
  def pop(self) -> T:
    #remove the disc on the top.
    return self._container.pop()
  
  def __repr__(self) -> str:
    #returns a textual representation of a Python object.
    return repr(self._container)

num_discs = 3

tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1, num_discs + 1):
  tower_a.push(i)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n:int) -> None:
  if n==1:
    #begin.pop() removes the disc from the top of tower a.
    #end.push() adds the disc on the top of tower c.
    #So, end.push(begin.pop()), removes the disc from a and and adds it on c.
    end.push(begin.pop())
  else:
    #There are 3 steps to solve this problem, independent of the value of num_discs.
    #Move n-1 discs from tower a to tower b using c as temp.
    hanoi(begin, temp, end, n-1)
    #Move the base disc, from a to c.
    hanoi(begin, end, temp, 1)
    #Move n-1 discs from tower b to tower a using c as temp
    hanoi(temp, end, begin, n-1)
    
hanoi(tower_a, tower_c, tower_b, num_discs)
print(tower_a)
print(tower_b)
print(tower_c)
