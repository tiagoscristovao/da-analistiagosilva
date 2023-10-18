import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('gasolina.csv')

anos = data['dia']
preco = data['venda']

plt.figure(figsize=(15, 8))  #tamanho da figura
plt.plot(anos, preco, marker='o', linestyle='-')
plt.title('Variação do preço da Gasolina em 10 dias')
plt.xlabel('dia')
plt.ylabel('venda (R$)')

plt.savefig('gasolina.png')