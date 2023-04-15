from typing import Dict

#Cria nossa memoria com os casos bases.
memoria: Dict[int, int] = {0:0, 1:1}

def fib3(n:int) -> int:
  if n not in memoria:
    #calcula e adiciona o item a nossa memoria
    memoria[n] = fib3(n-1) + fib3(n-2)
  return memoria[n] #apenas retorna o valor calculado


if __name__ == "__main__":
  print(fib3(999))
