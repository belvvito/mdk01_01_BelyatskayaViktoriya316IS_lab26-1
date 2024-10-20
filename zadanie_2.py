import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QAction
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Function(QMainWindow):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle('')
    self.setGeometry(300, 300, 300, 300)
    central_widget = QWidget()
    self.setCentralWidget(central_widget)
    new_layout = QVBoxLayout(central_widget)

    menubar = self.menuBar()
    file_menu = menubar.addMenu('Файл')
    exit_action = QAction('Выход', self)
    exit_action.setShortcut('Ctrl+Q')
    exit_action.triggered.connect(self.close)
    file_menu.addAction(exit_action)

    layout = QHBoxLayout()
    self.a_input = QLineEdit()
    self.b_input = QLineEdit()
    self.c_input = QLineEdit()
    layout.addWidget(QLabel('a:'))
    layout.addWidget(self.a_input)
    layout.addWidget(QLabel('b:'))
    layout.addWidget(self.b_input)
    layout.addWidget(QLabel('c:'))
    layout.addWidget(self.c_input)
    new_layout.addLayout(layout)

    self.button = QPushButton('Построить график')
    self.button.clicked.connect(self.plot_function)
    new_layout.addWidget(self.button)

    self.figure = plt.figure()
    self.canvas = FigureCanvas(self.figure)
    new_layout.addWidget(self.canvas)

    self.init_empty_plot()

  def init_empty_plot(self):
    self.figure.clear()
    ax = self.figure.add_subplot(111)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)
    self.canvas.draw()

  def plot_function(self):
    try:
      a = float(self.a_input.text())
      b = float(self.b_input.text())
      c = float(self.c_input.text())
      x = np.linspace(-20, 20, 1000)
      y = a * x ** 2 + b * x + c

      self.figure.clear()
      ax = self.figure.add_subplot(111)
      ax.plot(x, y)
      ax.set_title(f'y = {a}x² + {b}x + {c}')
      ax.axhline(y=0, color='k')
      ax.axvline(x=0, color='k')
      ax.grid(True)
      self.canvas.draw()

    except ValueError:
      QMessageBox.warning(self, '', 'Нужно ввести численные значения.')

if __name__ == '__main__':
  app = QApplication(sys.argv)
  plotter = Function()
  plotter.show()
  sys.exit(app.exec())
