import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui.ui_main import Ui_MainWindow
from Modules.ScanThread import ScanThread

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ChangeROCustomNMAP()

        # CONNECT BUTTON WITH SLOTS
        # ///////////////////////////////////////////////////////////////
        self.ui.startButton.clicked.connect(self.StartScan)
        self.ui.nmap_comboBox.currentTextChanged.connect(self.ChangeROCustomNMAP)

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Honeypot Detector"
        self.setWindowTitle(title)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

    def StartScan(self):
        """Начинает процесс сканирования IP адресов"""
        All_IPs = self.GetAllIPS()
        for IP in All_IPs:
            print(IP)
            a = ScanThread(IP, self.ui.custom_nmap_lineEdit.text())
            a.start()

    def ChangeROCustomNMAP(self):
        """Изменяет параметры сканирования от выбранного типа сканирования"""
        match (self.ui.nmap_comboBox.currentText()):
            case "Default":
                self.ui.custom_nmap_lineEdit.setText("-p-")
                self.ui.custom_nmap_lineEdit.setReadOnly(True)
            case "Intense":
                self.ui.custom_nmap_lineEdit.setText("-T4 -A -v")
                self.ui.custom_nmap_lineEdit.setReadOnly(True)
            case "Quick":
                self.ui.custom_nmap_lineEdit.setText("-T4 -F")
                self.ui.custom_nmap_lineEdit.setReadOnly(True)
            case "Custom":
                self.ui.custom_nmap_lineEdit.setText("")
                self.ui.custom_nmap_lineEdit.setReadOnly(False)

    def GetAllIPS(self) -> []:
        """Возвращает массив IP адресов"""
        All_IPs = []
        txt = (self.ui.ip_lineEdit.text()).replace(" ", "")
        if ("," in txt):
            All_IPs = txt.split(",")
        else:
            All_IPs = [txt]

        return All_IPs

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec())