# Computing GC Content (GC)

**URL:** http://rosalind.info/problems/gc/

## Solução

Lê o arquivo FASTA utilizando uma função auxiliar `read_fasta` implementada com leitura linha a linha (streaming) para eficiência de memória. Itera sobre o dicionário resultante calculando a porcentagem de bases 'G' e 'C' e identifica o registro com o maior conteúdo GC através de comparação direta.
