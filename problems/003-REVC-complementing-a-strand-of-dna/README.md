# Complementing a Strand of DNA (REVC)

**URL:** http://rosalind.info/problems/revc/

## Solução

Gera o complemento reverso da fita de DNA. Utiliza `str.maketrans` e `translate` para realizar a substituição simultânea das bases pares (A ↔ T, C ↔G ) e `[::-1]` para inverter a sequência resultante.
