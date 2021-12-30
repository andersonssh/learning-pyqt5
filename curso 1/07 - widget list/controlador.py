from PyQt5 import uic, QtWidgets

def enviar():
    input_ = lista.lineEdit.text()
    lista.lista.addItem(input_)
    # apaga conteudo digitado
    lista.lineEdit.setText('')

def deletar():
    lista.lista.clear()

app = QtWidgets.QApplication([])
lista = uic.loadUi('lista.ui')

lista.btn_enviar.clicked.connect(enviar)
lista.btn_excluir.clicked.connect(deletar)

lista.show()
app.exec()