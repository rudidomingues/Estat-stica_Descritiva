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

 # --- BOXPLOT ---
plt.figure(figsize=(4,6))
plt.boxplot(dados, vert=True, patch_artist=True,
            boxprops=dict(facecolor='lightgreen', color='black'),
            medianprops=dict(color='darkgreen', linewidth=2),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'),
            flierprops=dict(markerfacecolor='red', marker='o', markersize=8))

# Linhas de referência
plt.axhline(media, color='red', linestyle='--', label=f'Média = {media:.2f}')
plt.axhline(mediana, color='green', linestyle='-', label=f'Mediana = {mediana:.2f}')

plt.title("Boxplot - Variação das Peças (mm)")
plt.ylabel("Variação (mm)")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
