import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QPushButton, QVBoxLayout, QWidget, QWidget, QLabel, QRadioButton
from PyQt5 import QtCore as QtCore
import math
from functools import reduce

class LCMCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        #Set window titile and size
        self.setWindowTitle("LCM Calculator")
        self.setGeometry(800, 200, 400, 300)
        self.setStyleSheet("background-color: #8D8190;")

        #create central widget and layout
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        #create title label
        self.titleLabel = QLabel("LCM Calculator", self)
        self.titleLabel.setStyleSheet("font-size: 24px; color: #E8EDF3")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.titleLabel)

        #create input field for numbers
        self.inputField = QLineEdit(self)
        self.inputField.setPlaceholderText("Enter numbers separated by commas")
        self.inputField.setStyleSheet("font-size: 18px; padding: 10px;")
        self.layout.addWidget(self.inputField)

        #create selection label for HCF/LCM
        self.LCMRadioButton = QRadioButton("LCM", self)
        self.HCFRadioButton = QRadioButton("HCF", self)
        self.LCMRadioButton.setStyleSheet("font-size: 18px; color: #E8EDF3;")
        self.HCFRadioButton.setStyleSheet("font-size: 18px; color: #E8EDF3;")
        self.LCMRadioButton.setChecked(True)
        self.layout.addWidget(self.LCMRadioButton)
        self.layout.addWidget(self.HCFRadioButton)

        #create result label
        self.resultLabel = QLabel("result:", self)
        self.resultLabel.setStyleSheet("font-size: 18px; color: #E8EDF3;")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.resultLabel)


        #create button
        self.CalculateButton = QPushButton("Calculate", self)
        self.CalculateButton.setStyleSheet("font-size: 18px; padding: 10px; background-color: #3286F4; color: white;")
        self.CalculateButton.setMinimumSize(100, 40)
        self.CalculateButton.setMaximumSize(100, 40)  
        self.CalculateButton.clicked.connect(self.calculate_LCM)
        self.layout.addWidget(self.CalculateButton)

        #create Exit Button
        self.ExitButton = QPushButton("Exit", self)
        self.ExitButton.setStyleSheet("font-size: 18px; padding: 10px; background-color: #3286F4; color: white;")
        self.ExitButton.clicked.connect(self.close)
        self.ExitButton.setMinimumSize(100, 40)
        self.ExitButton.setMaximumSize(100, 40)
        self.layout.addWidget(self.ExitButton)



       
    def calculate_LCM(self):
        try:
            numbers = list(map(int, self.inputField.text().split(',')))
            if len(numbers) < 2:
                raise ValueError("Please enter at least two numbers.")
            
            if self.LCMRadioButton.isChecked():
                lcm = reduce(self.lcm, numbers)
                self.resultLabel.setText(f"LCM: {lcm}")
            elif self.HCFRadioButton.isChecked():
                hcf = reduce(self.hcf, numbers)
                self.resultLabel.setText(f"HCF: {hcf}")
            else:
                raise ValueError("Please select either LCM or HCF option.")
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e), QMessageBox.Ok)
            self.resultLabel.setText("")
        except Exception as e:
            QMessageBox.critical(self, "Error", "An unexpected error occurred.", QMessageBox.Ok)
            self.resultLabel.setText("")
    
    def lcm(self, a, b):
        return abs( a* b) // math.gcd(a, b)
    
    def hcf(self, a, b):
        return math.gcd(a, b)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LCMCalculator()
    window.show()
    sys.exit(app.exec_())


