from PyQt5 import uic, QtWidgets
from time import sleep
from threading import Thread

# bugs por possivel falta de multiprocessamento

def chamada_aumentar():
    ###### aplicar multiprocessamento
    Thread(target=aumentar).start()

stop_progress = False
def aumentar():
    # desativando stop caso tenha sido encerrado
    global stop_progress
    stop_progress = False
    # desabilita botao
    janela.btn_aumentar.setEnabled(False)
    for i in range(101):
        if stop_progress:
            break
        ##### aplicar multithreads com pyqt
        sleep(0.007)
        janela.barra_progresso.setValue(i)
    # reativa botao
    janela.btn_aumentar.setEnabled(True)

def zerar():
    global stop_progress
    stop_progress= True
    ##### aplicar multithreads com pyqt
    # esperando tempo seguro para iniciar proxima funcao
    sleep(0.03)
    janela.barra_progresso.setValue(0)

app = QtWidgets.QApplication([])
janela = uic.loadUi('progresso.ui')
janela.btn_aumentar.clicked.connect(chamada_aumentar)
janela.btn_zerar.clicked.connect(zerar)


janela.show()
app.exec()