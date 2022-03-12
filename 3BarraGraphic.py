import numpy as np
import matplotlib.pyplot as plt

condominio = [7]
apartamento = [5]
casa = [22]

barWidth = 0.25
plt.figure(figsize=(5,5))

aux1 = np.arange(len(condominio))
aux2 = [x + barWidth for x in aux1]
aux3 = [x + barWidth for x in aux2]
'''dados = ['Condomínio', 'Apartamento', 'Casa']
valores = [7.0, 5.0, 22.0]
cores = ['#27c4b7', '#28365D', '#efa536']
fig = plt.figure(colors = cores)'''

#plt.xticks(dados)
plt.bar(aux1, condominio, color = '#27c4b7', width = barWidth, label= 'Condomínio')
plt.bar(aux2, apartamento, color = '#28365d', width = barWidth, label= 'Apartamento')
plt.bar(aux3, casa, color = '#efa536', width = barWidth, label= 'Casa')

plt.ylabel('Número de pessoas')
plt.xlabel('Tipo de residência')
plt.legend()
plt.title('Reside em casa, condomínio ou apartamento?')
fig = plt.gcf()
fig.canvas.set_window_title('3° Gráfico')

plt.show()