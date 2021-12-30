from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

def msgbox():
    entrada = janela.lineEdit.text()
    # apagando conteudo inserido após clicar no botao
    janela.lineEdit.setText('')
    if entrada:
        QMessageBox.about(janela, 'Bem-vindo', f'Olá {entrada}, seja bem-vindo!')
    else:
        QMessageBox.about(janela, 'Alerta', 'Insira algum dado')


app = QtWidgets.QApplication([])
janela = uic.loadUi('msgbox.ui')

janela.pushButton.clicked.connect(msgbox)
janela.show()
app.exec()