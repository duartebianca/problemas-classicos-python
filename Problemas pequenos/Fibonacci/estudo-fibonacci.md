# Estudo dos Códigos
## Introdução
Para os códigos ***fib3.py***, ***fib4.py*** e ***fib5.py***, a chamada da função ocorre no número máximo de termos que consegui calcular. Isso me gerou algumas dúvidas do porquê um código conseguia calcular mais que o outro. Por exemplo, fib4 é apontado como mais eficiente, mas fib3 consgue calcular mais termos. Descreverei aqui uma breve comparação entre eles e minhas conclusões. Além disso, trarei comentários sobre ***fib6.py***. Os códigos foram rodados no [replit](https://replit.com/).


* ### fib3.py
  * Utiliza memorização. Usamos o dicionário (Não da forma tradicional, mas sim com Typing.Dict, por uma questão de tipagem estática), com chaves e valores inteiros, para armazenar em cache valores já calculados.
  * O código é eficiente para calcular valores repetidos da sequência, mas pode usar muita memória para armazenar todos os valores. Sua eficiência é limitada pela profundidade da recursão permitida pela linguagem Python.
  * No teste feito, conseguiu calcular até o 999º termo.

* ### fib4.y
  * Também utiliza memorização, mas usando a biblioteca [functools](https://docs.python.org/pt-br/3/library/functools.html) para armazenar apenas os valores mais recentes da sequência de Fibonacci.
  * O código é eficiente para calcular valores repetidos da sequência e é mais eficiente em termos de memória do que *fib3.py*. No entanto, a eficiência desse algoritmo ainda é limitada pela profundidade da recursão permitida pela linguagem Python.
  * No teste feito, conseguiu calcular até o 996º termo.

* ### fib5.y
  *  Usa um algoritmo iterativo que usa apenas duas variáveis para armazenar os valores do termo atual e do termo anterior.
  * Essa técnica é muito mais eficiente do que armazenar todos os valores intermediários em um dicionário ou em cache, pois usa uma quantidade muito menor de memória e não requer a indexação ou pesquisa de um cache. O algoritmo otimizado é mais rápido e pode calcular os termos da sequência de Fibonacci com boa velocidade mesmo para valores muito grandes de n. No entanto, sua precisão é limitada pela precisão dos números inteiros suportados pela linguagem Python.
  * No teste feito, conseguiu calcular até o 20.577º termo.

* ### fib6.y
  *  Gera uma sequência completa dos números de Fibonacci. 
  * Usando um gerador, cada iteração gera um número da sequência. Para isso, é preciso ter familiariedade com a palavra-chave [yield](https://medium.com/@bernardo.costa/quando-usar-o-yield-no-python-ebae18b144ba).
  * Não foi realizado teste de limite.