class CompressedGene:
  def __init__(self, gene: str) -> None:
    self._compress(gene)
  def _compress(self, gene: str) -> None:
    self.bit_string: int = 1 #sentinel
    for nucleotide in gene.upper():
      #For each character, we will shift
      #our bit string 2 bits to the left,
      #adding 00 to the right.
      #We will check which character this is,
      #and by using the | (or), we guarantee that
      #00 will always be replaced by the suggested values,
      #as 0 or 0 is 0, 0 or 1 is 1.
      self.bit_string <<= 2
      if nucleotide == 'A':
        self.bit_string |= 0b00
      elif nucleotide == 'C':
        self.bit_string |= 0b01
      elif nucleotide == 'G':
        self.bit_string |= 0b10
      elif nucleotide == 'T':
        self.bit_string |= 0b11
      else:
        raise ValueError("Invalid Nucleotide:{}".format(nucleotide))
  def descompress(self) -> str:
    gene: str = ''
    #Usando -1 para excluir a sentinela:
    for i in range(0, self.bit_string.bit_length() - 1, 2):
      bits: int  = self.bit_string >> i & 0b11 
      if bits == 0b00: #A
        gene += 'A'
      elif bits == 0b01: #C
        gene += 'C'
      elif bits == 0b10: #G
        gene += 'G'
      elif bits == 0b11: #T
        gene += 'T'
      else:
        raise ValueError("Invalid bits:{}".format(bits))
    return gene[::-1] #return inverted string.
  def __str__(self) -> str:
    return self.descompress()


if __name__ == "__main__":
  from sys import getsizeof
  original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
  print("original is {} bytes".format(getsizeof(original)))
  compressed: CompressedGene = CompressedGene(original)
  print("compressed is {} bytes".format(getsizeof(compressed)))
  print (compressed)
  print("original and descompressed are the same: {}".format(original==compressed.descompress()))
