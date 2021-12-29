import sys
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QPushButton,
                             QToolTip,
                             QLabel)

from PyQt5 import QtGui


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 50
        self.esquerda = 50
        self.largura = 800
        self.altura = 600
        self.titulo = 'Primeira janela'
        self.gera_labels()
        self.gera_botoes()
        self.gera_imagens()


    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def gera_botoes(self):
        # botoes
        botao1 = QPushButton('Botao 1', self)
        botao1.move(100, 100)
        botao1.resize(100, 50)
        botao1.setStyleSheet(
            'QPushButton{background-color: white; color: black;} QPushButton:hover{ background: orange; font-weight: 600;}')
        botao1.clicked.connect(self.b1)

        botao2 = QPushButton('Botao 2', self)
        botao2.move(300, 100)
        botao2.resize(100, 50)
        botao2.setStyleSheet(
            'QPushButton{background-color: blue; color: white;} QPushButton:hover{ background: orange; font-weight: 600}')
        botao2.clicked.connect(self.b2)

    def gera_labels(self):
        self.l1 = QLabel(self)
        self.l1.setText('Clique em um botao')
        self.l1.move(50, 50)
        self.l1.setStyleSheet('QLabel{font: bold; font-size: 20px;}')
        self.l1.resize(250, 50)

    def gera_imagens(self):
        self.carro = QLabel(self)
        self.carro.move(25, 200)
        self.carro.resize(450, 337)
        self.carro.setPixmap(QtGui.QPixmap('carro.jpg'))

    def b1(self):
        # forma 1
        self.carro.setPixmap(QtGui.QPixmap('carro.jpg'))


    def b2(self, l):
        # forma 2
        self.carro.setPixmap(QtGui.QPixmap('carro2.jpg'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Janela()
    janela.carregar_janela()
    sys.exit(app.exec_())