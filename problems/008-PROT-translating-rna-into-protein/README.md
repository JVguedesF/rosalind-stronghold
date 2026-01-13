# Translating RNA into Protein (PROT)

## Problem Description

Link: [http://rosalind.info/problems/prot/](http://rosalind.info/problems/prot/)

## Solution Logic

Utiliza uma tabela de busca (dicionário) para mapear cada trinca de nucleotídeos (códon) para o aminoácido correspondente.

Para a leitura, cria-se um iterador sobre a string de RNA e utiliza-se a função `zip` passando o mesmo iterador três vezes, o que agrupa os nucleotídeos em tuplas de 3 sequencialmente. O loop é interrompido (`break`) assim que um códon de parada ("Stop") é encontrado.
