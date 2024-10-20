import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow, QTextEdit, QDialog, QMessageBox

class Calculator(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle('')
    self.setGeometry(300, 300, 300, 300)

    layout = QVBoxLayout()

    self.input_fields = []
    for i in range(3):
      label = QLabel(f'{i+1} значение:')
      input_field = QLineEdit()
      layout.addWidget(label)
      layout.addWidget(input_field)
      self.input_fields.append(input_field)

    calculate_button = QPushButton('Посчитать сумму')
    calculate_button.clicked.connect(self.show_result)
    layout.addWidget(calculate_button)

    self.setLayout(layout)

  def show_result(self):
    result_window = Result(self.input_fields)
    result_window.exec()


class Result(QDialog):
  def __init__(self, input_fields, parent=None):
    super().__init__(parent)
    self.setWindowTitle('Результат')
    self.setGeometry(300, 300, 300, 300)

    layout = QVBoxLayout()
    try:
      numbers = [int(field.text()) for field in input_fields]
      result = sum(numbers)
      layout.addWidget(QLabel(f'Ответ: {result}'))
    except ValueError:
      QMessageBox.warning(self, '', 'Нужно ввести целые значения.')

    self.setLayout(layout)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Calculator()
  window.show()
  sys.exit(app.exec())
