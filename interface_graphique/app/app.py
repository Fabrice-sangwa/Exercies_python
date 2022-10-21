from PySide2 import QtWidgets

#Cette classe reprénte la fenêtre
class App(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseur de devise")
        
#création de l'application      
app  = QtWidgets.QApplication([])

win = App()
win.show()

app.exec_()