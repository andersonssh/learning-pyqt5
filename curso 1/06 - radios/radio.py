from PyQt5 import uic, QtWidgets

def func_principal():
    if radio.radio_cor.isChecked():
        radio.cor.setStyleSheet('QLabel{background-color: green}')
    elif radio.radio_cor_2.isChecked():
        radio.cor.setStyleSheet('QLabel{background-color: red}')
    elif radio.radio_cor_3.isChecked():
        radio.cor.setStyleSheet('QLabel{background-color: blue}')
    elif radio.radio_cor_4.isChecked():
        radio.cor.setStyleSheet('QLabel{background-color: yellow}')
    elif radio.radio_cor_5.isChecked():
        radio.cor.setStyleSheet('QLabel{background-color: orange}')
    elif radio.radio_cor_6.isChecked():
        radio.cor.setStyleSheet('QLabel{background-color: black}')


app = QtWidgets.QApplication([])
radio = uic.loadUi('radio_cor.ui')

radio.btnEnviar.clicked.connect(func_principal)

radio.show()
app.exec()