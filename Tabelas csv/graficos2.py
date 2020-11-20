import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

data = pd.read_csv('table5.csv', sep=',', delimiter=';', usecols=['Categoria', 'Quantidade'])

lista_categoria = [y for y in data['Categoria']]
lista_quantidade = [x for x in data['Quantidade']]

#print(lista_categoria)
#print(lista_quantidade)

indice = []
for i in range(len(lista_categoria)):
    indice.append(i+1)

dimensao = (12, 7)
fig, ax = plt.subplots(figsize=dimensao)
g = sns.barplot(x= indice, y= lista_quantidade, ax= ax, palette = "icefire")
#sns.diverging_palette(250, 30, l=65, center="dark", as_cmap=True)
g.set(xlabel = 'índice das Categorias', ylabel= 'Frequência')
plt.title("""Frequência de Categorias - Documentario 'Pátria Educadora' (2020)""", fontsize=16)
fig.tight_layout()
plt.show()
