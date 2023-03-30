# Arquivo: RicardoCoelho_AD_av1_ex2b
# Autor: Ricardo Veiga Coelho
# TIA: 42241588
# Data: 31/08/22
# Descrição: Avaliação Continuada 1 – Análise exploratória dos dados. - exercicio 2 item b

from RVC_dispersao_funcoes import *

import statistics
import pandas as pd
import numpy

bd=pd.read_csv('ds_salaries.csv')

#calculo da média
calculo=str(round(media(bd['salary_in_usd']),2))
print("\nMédia do conjunto: "+calculo+"\n")

#calculo da mediana
temp=bd.sort_values(by=['salary_in_usd'])#auxiliar usado para ordenar os valores em ordem crescente
calculo=str(round(mediana(temp['salary_in_usd']),2))
print("Mediana do conjunto: "+calculo+"\n")

#calculo da moda
#moda(vetor)

#calculo da variância
calculo=str(round(variancia(bd['salary_in_usd']),2))
print("Variância do conjunto: "+calculo+"\n")

#calculo do desvio-padrão (basta fazer a raiz quadrada da variância)
calculo=str(round(math.sqrt(variancia(bd['salary_in_usd'])),2))
print("Desvio-padrão do conjunto: "+calculo+"\n")

#calculo do coeficiente de variação
calculo=str(round(coefVariacao(bd['salary_in_usd']),2))
print("Coeficiende de variação do conjunto: "+calculo+"%\n")

#calculo dos quartis
#1º quartil
#calculo=str(round(quartil1(temp['salary_in_usd']),2))
#print("1º quartil do conjunto: "+calculo+"\n")
#3º quartil
#calculo=str(round(quartil3(temp['salary_in_usd']),2))
#print("3º quartil do conjunto: "+calculo+"\n")
