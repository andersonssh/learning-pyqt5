import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 50
        self.esquerda = 50
        self.largura = 800
        self.altura = 600
        self.titulo = 'Primeira janela'
        botao1 = QPushButton('Botao 1', self)
        botao1.move(100, 100)
        botao1.resize(100, 50)
        botao1.setStyleSheet('QPushButton{background-color: black; color: white;} QPushButton:hover{ background: orange; font-weight: 600}')
        botao1.clicked.connect(self.b1)

        botao2 = QPushButton('Botao 2', self)
        botao2.move(300, 100)
        botao2.resize(100, 50)
        botao2.setStyleSheet(
            'QPushButton{background-color: black; color: white;} QPushButton:hover{ background: orange; font-weight: 600}')
        botao2.clicked.connect(self.b2)

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def b1(self):
        print('Botao 1 clicado!!!!!!!!!!!')

    def b2(self):
        print('Botao 2 clicado!!!!!!!!!!!!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Janela()
    janela.carregar_janela()
    sys.exit(app.exec_())