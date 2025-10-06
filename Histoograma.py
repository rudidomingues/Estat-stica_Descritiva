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

# --- HISTOGRAMA ---
plt.figure(figsize=(6,4))
plt.hist(dados, bins=np.arange(0, 8.5, 0.5), color='skyblue', edgecolor='black', alpha=0.7)

# Linhas de referência
plt.axvline(media, color='red', linestyle='--', linewidth=2, label=f'Média = {media:.2f}')
plt.axvline(mediana, color='green', linestyle='-', linewidth=2, label=f'Mediana = {mediana:.2f}')

# Personalização
plt.title("Histograma de Frequência - Variação das Peças (mm)")
plt.xlabel("Variação (mm)")
plt.ylabel("Frequência")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
