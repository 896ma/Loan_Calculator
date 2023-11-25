#importinng  libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore ,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
 
 
class  Window(QMainWindow):
    #Creating a constructor 
 def __init__(self):
     #inheriting methods and properties form a superclass  QMAinwindow
     super().__init__()
     #Setting the title
     self.setWindowTitle("LOAN CALCULATOR")
     #Set Geometry App  
     self.width=400
     self.height=500
     self.setGeometry(100,100,self.width,self.height)
     self.UIComponents()
     
     #Showing the window on the screen 
     self.show()
     
 #Function to add  widgets
 def UIComponents(self):
     head=QLabel ("Loan  Calculator \n CYBER BANK" ,self)
     head.setGeometry(0,10,400,60)
     font =QFont('Times' ,15)
     font.setBold(True)
     head.setFont(font)
     head.setAlignment(Qt.AlignCenter)
     color=QGraphicsColorizeEffect(self)
     color.setColor(Qt.darkBlue)
     head.setGraphicsEffect(color)
     
     #interest Label
     
     i_Label= QLabel("Annual Interest" ,self)
     #properties
     
     i_Label.setAlignment(Qt.AlignCenter)
     i_Label.setGeometry(20,100,170,40)
     i_Label.setStyleSheet("QLabel" "{"
                                      "border: 2px solid black;"
                                      "background:rgba(70,70,70,35);"
                                      "}"
                                     )
    
     i_Label.setFont(QFont('Times',9))
     
     #A corresponding input field for input label
     self.rate=QLineEdit(self)
     onlyInt= QIntValidator()# Validation for interest  rate  such that only integers are allowed
     self.rate.setValidator(onlyInt)
     
     
     #Setting properties  for the Input field
     
     self.rate.setGeometry(200,100,180,40)
     self.rate.setAlignment(Qt.AlignCenter)
     self.rate.setFont(QFont('Times',9))
     
     #Number of years 
     n_years =QLabel("Years",self)
     i_Label.setAlignment(Qt.AlignCenter)
     i_Label.setGeometry(20,100,170,40)
     i_Label.setStyleSheet("QLabel" "{"
                                      "border: 2px solid black;"
                                      "background:rgba(70,70,70,35);"
                                      "}"
                                     )
    
     i_Label.setFont(QFont('Times',9))
     
     #A corresponding input field for input label
     self.rate=QLineEdit(self)
     onlyInt= QIntValidator()# Validation for interest  rate  such that only integers are allowed
     self.rate.setValidator(onlyInt)
     
     
     #Setting properties  for the Input field
     
     self.rate.setGeometry(200,100,180,40)
     self.rate.setAlignment(Qt.AlignCenter)
     self.rate.setFont(QFont('Times',9))
     
     
#Create app object

App = QApplication(sys.argv)

#Instantiiate a window class by creating a window object
window = Window()  
     
#Starting the Application
sys.exit(App.exec()) # Starts  the event loop and  blocks everything else untill the  application quits


