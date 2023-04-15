def fib5(n : int) -> int:
  if n==0: return n
  last: int = 0
  next: int = 1
  for _ in range(1, n):
    #Evita uso de variável temporária. Ao mesmo tempo:
    #last recebe valor antigo de next
    #next recebe o valor antigo de last + seu próprio valor antes dessa operação.
    last, next = next, last+next
  return next

if __name__ == "__main__":
  print(fib5(20577))
