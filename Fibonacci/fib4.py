from functools import lru_cache

#decorador que armazena resultados de chamadas anteriores e os retorna imediatamente em vez de recalculá-los
@lru_cache(maxsize=None)

def fib4(n : int) -> int:
  if n < 2:
    return n
  return fib4(n-2) + fib4(n-1)

if __name__ == "__main__":
  print(fib4(996))
