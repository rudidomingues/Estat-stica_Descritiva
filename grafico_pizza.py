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

# --- GRÁFICO DE PIZZA ---

# Classificação das peças por faixa
categorias = {
    "A (≤1.5 mm)": [x for x in dados if x <= 1.5],
    "B (1.5–2.5 mm)": [x for x in dados if 1.5 < x <= 2.5],
    "C (2.5–4.0 mm)": [x for x in dados if 2.5 < x <= 4.0],
    "D (>4.0 mm)": [x for x in dados if x > 4.0]
}

# Frequência por categoria
labels = categorias.keys()
sizes = [len(v) for v in categorias.values()]

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
plt.title("Distribuição das Peças por Faixa de Variação (mm)")
plt.show()
