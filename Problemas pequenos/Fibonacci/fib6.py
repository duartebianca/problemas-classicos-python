from typing import Generator

def fib6(n : int) -> Generator[int, None, None]: #gera valores inteiros, não recebe nenhum argumento de entrada, não retorna um valor de saída
  yield 0 #caso especial
  if n>0: yield 1 #caso especial
  last: int = 0
  next: int = 1
  for _ in range(1, n):
    #Evita uso de variável temporária. Ao mesmo tempo:
    #last recebe valor antigo de next
    #next recebe o valor antigo de last + seu próprio valor antes dessa operação.
    last, next = next, last+next
    yield next

if __name__ == "__main__":
  for i in fib6(50):
    print(i)
