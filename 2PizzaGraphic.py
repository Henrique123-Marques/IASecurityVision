#Cores: #27C4B7 #28365D #161C2E #6699CC
import matplotlib.pyplot as plt

#6 - Consideraria usar o IASV algum dia?
legenda = ['Sim', 'Não']
dados = [824, 176]
cores_grafico = ['#27c4b7', '#28365D']
fig, ax = plt.subplots(figsize=(6, 5), subplot_kw=dict(aspect="equal"))
fig = plt.gcf()
fig.canvas.set_window_title('2° Gráfico')
ax.pie(dados, autopct='%0.1f%%', pctdistance=1.15, colors=cores_grafico)
ax.legend(legenda, title="Gastos", loc="center left",bbox_to_anchor=(1.25, 0, 0.5, 1))  
ax.set_title("2 - Consideraria usar o I.A. Security Vision algum dia?")
ax.legend(legenda, title = "Resultados:", loc = 'center left', bbox_to_anchor = (0.97,0,0.5,1))
plt.show()
