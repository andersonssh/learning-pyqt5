from PyQt5 import uic, QtWidgets

def chamar_tela():
    segunda_tela.show()


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi('primeira.ui')
# a segunda tela possui tamanho minimo e máximo configurados
segunda_tela = uic.loadUi('segunda.ui')
primeira_tela.pushButton.clicked.connect(chamar_tela)

primeira_tela.show()
app.exec()