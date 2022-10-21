from PySide2 import QtWidgets
import currency_converter

#Cette classe reprénte la fenêtre
class App(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Convertisseur de devise")
        self.setup_ui()
        self.set_default_values()
        self.set_connections()
        
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
        
    #cette fonction permet de mettre les valeurs par defaut
    def set_default_values(self):
        #ajouter des valeurs à la conboBox. Ces valeurs doivent être des chaînes de caractère
        self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))
        #présicer le texte par defaut d'une comboBox
        self.cbb_devisesFrom.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("EUR")
        
        
        #Modifier les montants
        self.spn_montant.setRange(1, 1_000_000)
        self.spn_montantConverti.setRange(1, 1_000_000)
        
        #Mettre les valeurs sur les spinBox
        self.spn_montant.setValue(100)
        self.spn_montantConverti.setValue(100)
        
    #cette methode permet des recupérer toutes les actions sur un les widgets de l'interface graphique
    def set_connections(self):
        #on récupère le signal sur les cbb et spn et on les connecte à des méthodes
        #activates.connect pour les cbb, valueChange.connect pour les spn et cliked.connect pour le btn
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devise)
    
    #cete methode pemert de calculer la conversion 
    def compute(self):
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        
        try:
            resultat = self.c.convert(montant, devise_from, devise_to)
            
        except currency_converter.currency_converter.RateNotFoundError:
            print("La conversion ne passe pas ")
        else :
            self.spn_montantConverti.setValue(resultat)
        
        
        
    #cette methode permet d'inverser les devises
    def inverser_devise(self):
        
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        
        self.cbb_devisesFrom.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)
    
        self.compute()
        
#création de l'application      
app  = QtWidgets.QApplication([])

win = App()
win.show()

app.exec_()