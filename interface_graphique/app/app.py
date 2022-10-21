from PySide2 import QtWidgets

#Cette classe reprénte la fenêtre
class App(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseur de devise")
        self.setup_ui()
        
        
    #Créateur de composants de l'interface
    def setup_ui(self):
        #on crée un layout horizontal du parent(self)
        self.layout = QtWidgets.QHBoxLayout(self)
        #on crée un widget combobox, on a pas besoin de placer le self, on l'ajouter au layout à la fin 
        self.cbb_devisesFrom = QtWidgets.QComboBox()
        #on crée un autre widget spinbox 
        self.spn_montant = QtWidgets.QSpinBox()
        #encore un autre comboBox et un spinBox
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        #on crée un bouton avec le texte à afficher sur le bouton
        self.btn_inverser = QtWidgets.QPushButton("Inverser les devises")
        
        #on va ensuite insérer les widgets dans le layout 
        
        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)
        
        
    
        
#création de l'application      
app  = QtWidgets.QApplication([])

win = App()
win.show()

app.exec_()