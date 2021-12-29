# Aprendendo pyqt5

Contém meus testes e programas feitos durante meu aprendizado básico de pyqt5.

**processo de instalação do qt design no linux**

```bash
$ sudo apt install python3-pyqt5 pyqt5-dev-tools qttools5-dev-tools
```

**processo de conversao do arquivo gerado pelo qt design (arquivo .ui) para arquivo .py**
Após salvar a gui em um arquivo .ui, no terminal digite:
```bash
$ pyuic5 -x ArquivoQt.ui -o ArquivoPython.py
```
