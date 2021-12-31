from PyQt5 import uic, QtWidgets

def pegar_data():
    dados = janela.calendarWidget.selectedDate()
    data = dados.getDate()
    # top U-u
    janela.data.setText(f'{data[2]}/{data[1]}/{data[0]}')

app = QtWidgets.QApplication([])
janela = uic.loadUi('calendario.ui')

janela.calendarWidget.selectionChanged.connect(pegar_data)

janela.show()
app.exec()