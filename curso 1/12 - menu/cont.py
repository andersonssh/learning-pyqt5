from PyQt5 import uic, QtWidgets

def cor_verde():
    janela.escolha.setText('verde')

def cor_azul():
    janela.escolha.setText('azul')

def cor_vermelho():
    janela.escolha.setText('vermelha')

app = QtWidgets.QApplication([])
janela = uic.loadUi('menu.ui')

janela.action_verde.triggered.connect(cor_verde)
janela.action_azul.triggered.connect(cor_azul)
janela.action_vermelho.triggered.connect(cor_vermelho)
janela.show()
app.exec()