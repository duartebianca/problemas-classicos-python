#----------------------------------
#contexto da questão
#nucleotídeos: A, C, T, G
#códon: 3 nucleotídeos
#gene: composto por vários códons
#problema comum: procurar algum códon em um gene.
#----------------------------------

#----------------------------------
from bisect import bisect_left
from enum import IntEnum
from typing import Tuple, List
#----------------------------------

#----------------------------------
#ESTRUTURAS
Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'T', 'G'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]
#Códons podem ser definidos como tuplas de 3 Nucleotide(s). Um gene é uma lista de Codon(s).
#----------------------------------

#----------------------------------
#FUNÇÕES

#Converte uma string qualquer como um Gene (a estrutura definida anteriormente como uma lista de Códons).
def string_to_gene(s: str) -> Gene:
  gene: Gene = []
  for i in range(0, len(s), 3):
    if (i + 2) >= len(s):
      return gene
    codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
    gene.append(codon)
  return gene

#Busca linear -> verifica todos os elementos da lista. Vamos verificar se um códon está o gene ou não.
def linear_contains(gene: Gene, key_codon: Codon) -> bool:
  for codon in gene:
    if codon == key_codon:
      return True
    return False

#Busca binária -> Tem como referência sempre o meio do trecho analisado até encontrar.
def binary_contais(gene: Gene, key_codon: Codon) -> bool:
  low: int = 0
  high: int = len(gene) - 1
  while (low <= high):
    mid: int = (low + high)//2 #meio do trecho de gene a ser analisado
    if (gene[mid] < key_codon):
    #se o codon procurado é maior que o que temos no meio do gene, significa que ele está para a direita, portanto, devemos mover o limite inferior para a direita desse meio.
      low = mid+1
    elif (gene[mid]>key_codon):
    #se o codon procurado é menor que o que temos no meio do gene, significa que ele está para a esquerda, portanto, devemos mover o limite superior para a esquerda desse meio.
      high = mid-1
    else:
      return True
  return False #não encontramos
#----------------------------------

#----------------------------------
#Variáveis
gene_str: str = 'ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT'
acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gta: Codon = (Nucleotide.G, Nucleotide.T, Nucleotide.A)
my_gene: Gene = string_to_gene(gene_str)
my_sorted_gene: Gene = sorted(my_gene)
#----------------------------------

#----------------------------------
#Exemplo com busca linear procurando ACG.
print('Busca linear de ACG:', linear_contains( my_gene, acg))
#Na prática, o código de busca linear equivale ao operador "in"
print('Usando in para procurar ACG:', acg in my_gene)

#Exemplo com busca binária procurando ACG.
print('Busca binária de ACG:', binary_contais(my_sorted_gene, acg))

#Cálculo utilizando o bisect sugerido pelo livro
index = bisect_left(my_sorted_gene, acg)
using_bisect = index != len(my_sorted_gene) and my_sorted_gene[index] == acg
print('Usando o módulo bisect para procurar ACG:', using_bisect)
#----------------------------------
