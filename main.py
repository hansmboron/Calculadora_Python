import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtCore import Qt


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora Python')
        # self.setFixedSize(430, 550)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 4)
        self.display.setDisabled(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.toolTip()
        self.display.setStyleSheet(
            '* {font-size: 16pt; color: black; font-weight: 300; background: white;}'
        )
        self.setStyleSheet(
            '* {font-size: 12pt; font-weight: 600}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(
            QPushButton('C'), 1, 0, 1, 1, lambda: self.display.setText(''),
            'background: red;'
        )
        self.add_btn(
            QPushButton('<-'), 1, 1, 1, 1, lambda: self.display.setText(self.display.text()[:-1]),
            'background: #353535;'
        )
        self.add_btn(QPushButton('%'), 1, 2, 1, 1, None, 'background: #353535;')
        self.add_btn(QPushButton('/'), 1, 3, 1, 1, None, 'background: #353535;')
        self.add_btn(QPushButton('7'), 2, 0, 1, 1)
        self.add_btn(QPushButton('8'), 2, 1, 1, 1)
        self.add_btn(QPushButton('9'), 2, 2, 1, 1)
        self.add_btn(QPushButton('*'), 2, 3, 1, 1, None, 'background: #353535;')
        self.add_btn(QPushButton('4'), 3, 0, 1, 1)
        self.add_btn(QPushButton('5'), 3, 1, 1, 1)
        self.add_btn(QPushButton('6'), 3, 2, 1, 1)
        self.add_btn(QPushButton('-'), 3, 3, 1, 1, None, 'background: #353535;')
        self.add_btn(QPushButton('1'), 4, 0, 1, 1)
        self.add_btn(QPushButton('2'), 4, 1, 1, 1)
        self.add_btn(QPushButton('3'), 4, 2, 1, 1)
        self.add_btn(QPushButton('+'), 4, 3, 1, 1, None, 'background: #353535;')
        self.add_btn(QPushButton('()'), 5, 0, 1, 1, self.btn_brac, 'background: #353535;')
        self.add_btn(QPushButton('0'), 5, 1, 1, 1)
        self.add_btn(QPushButton('.'), 5, 2, 1, 1, None, 'background: #353535;')
        self.add_btn(
            QPushButton('=='), 5, 3, 1, 1,
            self.btn_igual,
            'background: darkgreen;'
        )

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        if style:
            btn.setStyleSheet(style)

    def btn_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except ZeroDivisionError:
            self.display.setText("Não pode dividir por Zero!")
        except SyntaxError:
            self.display.setText("Expressão Inválida!!!")

    def btn_brac(self):
        if self.display.text().__contains__('('):
            self.display.setText(self.display.text() + ')')
        else:
            self.display.setText(self.display.text() + '(')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
