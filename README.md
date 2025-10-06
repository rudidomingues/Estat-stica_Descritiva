# 📊 Estatística Descritiva com Python – UNISINOS

Este repositório reúne os **códigos e gráficos produzidos na Aula 3 de Probabilidade e Inferência Estatística (UNISINOS)**, ministrada pelo professor **Vilarbo da Silva Junior**.  
A proposta é demonstrar, na prática, o uso de **Python** para representar e interpretar dados estatísticos, aplicando os conceitos de **distribuição de frequência, medidas de posição e dispersão**.

---

## 🎯 Objetivos de Aprendizagem

- Compreender e aplicar conceitos de **estatística descritiva**.  
- Construir diferentes formas de **representação gráfica** de um conjunto de dados.  
- Interpretar distribuições com base em histogramas, boxplots e gráficos de pizza.  
- Aplicar medidas estatísticas como **média, mediana, desvio-padrão, percentis e z-score**.  
- Relacionar os resultados a contextos reais (ex.: controle de qualidade em peças pré-moldadas).

---

## 🧠 Conteúdo do Repositório

| Arquivo | Descrição |
|----------|------------|
| `estatistica_graficos.py` | Códigos em Python para geração dos gráficos (histograma, boxplot e pizza) |
| `dados_pecas.txt` | Conjunto de dados de exemplo (variação em mm) |
| `aula3_estatistica_unisinos.pdf` | Material de referência teórica da aula |
| `relatorio_resultados.pdf` | Saída gerada com gráficos e interpretações (opcional) |

---

## 🧮 Técnicas Estatísticas Utilizadas

- **Histograma de Frequência:**  
  Mostra a distribuição de variações das peças em intervalos de 0,5 mm.  
  > Permite visualizar a concentração de valores e a presença de assimetria.

- **Boxplot (Diagrama de Caixa):**  
  Identifica a **mediana, quartis, amplitude interquartílica (IQR)** e **outliers**.  
  > No conjunto analisado, observou-se um outlier de 7,5 mm.

- **Gráfico de Pizza:**  
  Representa a proporção de peças nas faixas de variação (A, B, C, D).  
  > Facilita a leitura percentual da distribuição das classes.

---

## 🧰 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Collections](https://docs.python.org/3/library/collections.html)
- [SciPy (para z-score e percentil)](https://scipy.org/)

---

## 🚀 Execução do Código

1. Clone o repositório:
   ```bash
   git clone https://github.com/rudidomingues/estatistica-descritiva-unisinos.git
   cd estatistica-descritiva-unisinos
