import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import time

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
img = Image.open("C:/Users/cagda/OneDrive/Masaüstü/teker/map/map.png")

# max_lat,max_lon=41.10629,29.02639
# min_lat,min_lon=41.10218,29.01785

# step_y=max_lat-min_lat/img.size[1]
# step_x=max_lon-min_lon/img.size[0]

# y = np.arange(41.10218,41.10629,step_y)
# x = np.arange(29.01785,29.02639,step_x)


fig, ax = plt.subplots()
im = ax.imshow(img, extent=[0, img.size[0], 0, img.size[1]])
# plt.scatter(702.791569086537,126.19708029321566,c='r',s=40)
# ax.set_xticks(np.linspace(29.01785,29.02639,img.size[0]))
# ax.set_yticks(np.linspace(41.10218,41.10629,img.size[1]))

# ax.plot(x, x, ls='dotted', linewidth=2, color='red')
x,y=0,0

def onclick(event):
    global x,y
    x,y=event.xdata,event.ydata
    plt.scatter(x,y,c='r',s=40)


    print(x,y)
    

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
