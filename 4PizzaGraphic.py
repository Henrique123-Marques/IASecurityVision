import numpy as np
import matplotlib.pyplot as plt

#6 - Consideraria usar o IASV algum dia?
legenda = ['Sim', 'Não']
dados = [735, 265]
cores_grafico = ['#27c4b7', '#28365D']
fig, ax = plt.subplots(figsize=(9, 4), subplot_kw=dict(aspect="equal"))
fig = plt.gcf()
fig.canvas.set_window_title('4° Gráfico')
ax.pie(dados, autopct='%0.1f%%', pctdistance=1.15, colors=cores_grafico)
ax.legend(legenda, title="Gastos", loc="center left",bbox_to_anchor=(1.25, 0, 0.5, 1))  
ax.set_title("4 - Acha possível a possibilidade de substituição de porteiros por sistemas de reconhecimento facial?")
ax.legend(legenda, title = "Resultados:", loc = 'center left', bbox_to_anchor = (0.97,0,0.5,1))

plt.show()