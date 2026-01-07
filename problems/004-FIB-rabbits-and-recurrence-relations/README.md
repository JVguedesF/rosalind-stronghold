# Rabbits and Recurrence Relations (FIB)

**URL:** http://rosalind.info/problems/fib/

## Solução

Calcula o número total de pares de coelhos após $n$ meses utilizando uma variação da sequência de Fibonacci. A solução aplica a relação de recorrência $F_n = F_{n-1} + (k \times F_{n-2})$, onde $k$ representa o tamanho da ninhada (_litter size_), considerando que apenas coelhos com mais de um mês de vida (geração $n-2$) estão aptos a reproduzir.
