import numpy as np
import matplotlib.pyplot as plt
import collections

# Dados de variação das peças (em mm)
dados = [0.8, 1.2, 1.3, 1.5, 1.7, 1.9, 2.0, 2.1, 2.2, 2.4, 2.8, 3.1, 3.3, 3.8, 7.5]

# Estatísticas básicas
media = np.mean(dados)
mediana = np.median(dados)
desvio_padrao = np.std(dados, ddof=1)

print(f"Média = {media:.2f}")
print(f"Mediana = {mediana:.2f}")
print(f"Desvio padrão = {desvio_padrao:.2f}")
