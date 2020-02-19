# plt est l'alias par defaut pour pyplot (exemples dans les forums)
import matplotlib.pyplot as plt
import math
import numpy as np

fig, ax = plt.subplots()
ax.plot(np.random.rand(10))


def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

x = range(1000)

print(x)

x = [i + 1 for i in x ]
y1 = [math.sin(i / 100) for i in x]
y2 = [1/ (i/100)*math.sin(i / 100) for i in x]

f,  axarr = plt.subplots(2, sharex=True, sharey=True)
# subplot historique, compatible matlab
#plt.subplot(211)
# les points sont relies entre eux
axarr[0].plot(x , y1 )
#plt.subplot(212)
axarr[1].plot(x, y2)
# nuage de points
#plt.scatter(x, y1)
# bargraph
# plt.bar(x, y )
#plt.scatter(x, y2)
f.subplots_adjust(hspace=0)
plt.ginput(4)
# plt.show()
