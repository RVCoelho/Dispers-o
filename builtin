# Arquivo: RicardoCoelho_AD_av1_ex1b
# Autor: Ricardo Veiga Coelho
# TIA: 42241588
# Data: 31/08/22
# Descrição: Avaliação Continuada 1 – Análise exploratória dos dados. - exercicio 2 item a

import statistics
from matplotlib import pyplot as plt 
import pandas as pd
import numpy
import math

bd=pd.read_csv('ds_salaries.csv')

print("\nMédia:",round(statistics.mean(bd['salary_in_usd']),2))
print("\nMediana:",round(statistics.median(bd['salary_in_usd']),2))
print("\nVariância",round(statistics.variance(bd['salary_in_usd']),2))
print("\nDesvio padrão:",round(statistics.stdev(bd['salary_in_usd']),2))
Desv=math.sqrt(statistics.variance(bd['salary_in_usd']))
Coef=str(round((Desv/statistics.mean(bd['salary_in_usd'])*100),2))
print("\nCoeficiende de variação do conjunto: "+Coef+"%\n")

print("\n1º Quartil:",numpy.quantile(bd['salary_in_usd'],[0.25]))
print("\n3º Quartil:",numpy.quantile(bd['salary_in_usd'],[0.75]))

numpy.histogram(bd['salary_in_usd'],bins = [0,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000])
bins = numpy.histogram(bd['salary_in_usd'],bins = [0,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000])
plt.hist(bd['salary_in_usd'], bins = [0,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000]) 
plt.title("histograma") 
plt.show()

#plt.boxplot(bd['salary_in_usd'])
#plt.show()
#print(max(bd['salary_in_usd']))
