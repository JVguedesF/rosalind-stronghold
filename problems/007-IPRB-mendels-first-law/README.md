# Mendel's First Law (IPRB)

## Problem Description

Link: [http://rosalind.info/problems/iprb/](http://rosalind.info/problems/iprb/)

## Solution Logic

Calculamos a probabilidade de obter um descendente com fenótipo **recessivo** e subtraímos esse valor de 1 (probabilidade complementar).

Considerando a população total $t = k + m + n$ e a escolha de dois organismos sem reposição, somamos as probabilidades dos pares que geram alelos recessivos:

- **Recessivo ($n$) e Recessivo ($n$):** 100% de chance (peso 1).
- **Recessivo ($n$) e Heterozigoto ($m$):** 50% de chance.
- **Heterozigoto ($m$) e Heterozigoto ($m$):** 25% de chance (peso 0.25).

A fórmula final divide essa soma pelo número total de pares possíveis $t(t-1)$.
