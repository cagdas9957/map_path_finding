import sys
import PIL
import matplotlib
import numpy as np
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from canvas import MplCanvas
from PIL import Image
import pyqtgraph as pg


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # image = PIL.Image.open("C:/Users/cagda/OneDrive/Masaüstü/teker/map/map.png")
        # image_array = np.asarray(image)
        # print(image_array)
        
        _in_data = Image.open('C:/Users/cagda/OneDrive/Masaüstü/teker/map/map.png')
        self.img = np.asarray(_in_data, dtype=np.uint8).transpose([1,0,2])

        # self.img = Image.open("C:/Users/cagda/OneDrive/Masaüstü/teker/map/map.png")
        imv = pg.ImageView()
        imv.show()
        imv.setImage(self.img)

        


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()