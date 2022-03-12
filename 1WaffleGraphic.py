import matplotlib.pyplot as plt
from pywaffle import Waffle

#5 - Usaria um sistema de reconhecimento facial?
colors = ['#27C4B7', '#28365D']
fig= plt.figure(FigureClass=Waffle, rows=4, columns = 10, 
	values={'Sim': 31, 'Não':3},
	legend={'loc':'upper left','bbox_to_anchor':(1.05,1)}, figsize=(9,3), colors = colors)
fig = plt.gcf()
fig.canvas.set_window_title('1° Gráfico')

fig.set_tight_layout(False)
plt.title('1 - Usaria um sistema de reconhecimento facial?')
plt.show()