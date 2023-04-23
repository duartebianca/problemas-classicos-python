def calculate_pi(n_terms: int) -> float:
  #Using Leibniz's formula.
  #sum from 0 to n_terms of ( ((-1)^{k}) / (2k+1)).
  numerator: float = 4.0
  denominator: float = 1.0
  operation: float = 1.0
  pi: float = 0.0
  for _ in range(n_terms):
    pi += operation * (numerator/denominator)
    denominator += 2.0
    operation *= -1.0
  return pi

print(calculate_pi(100000))
