#importinng  libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore ,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import 

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
     head=QLabel ("G_oaTeD \n CyBer BanK" ,self)
     head.setGeometry(0,10,400,60)
     font =QFont('Times' ,15)
     font.setBold(True)
     head.setFont(font)
     head.setAlignment(Qt.AlignCenter)
     color=QGraphicsColorizeEffect(self)
     color.setColor(Qt.darkBlue)
     head.setGraphicsEffect(color)
     
     #interest Label
     
     i_Label= QLabel("Annual Interest(%)" ,self)
     #properties
     
     i_Label.setAlignment(Qt.AlignCenter)
     i_Label.setGeometry(20,100,170,40)
     i_Label.setStyleSheet("QLabel" "{"
                                      "border: 2px solid black;"
                                      "background:rgba(70,70,70,35);"
                                      "}"
                                     )
    
     i_Label.setFont(QFont('Times',9))
     
     #A corresponding input field for input 
     self.rate=QLineEdit(self)
     onlyInt= QIntValidator()# Validation for interest  rate  such that only integers are allowed
     self.rate.setValidator(onlyInt)
     
     
     #Setting properties  for the Input field
     
     self.rate.setGeometry(200,100,180,40)
     self.rate.setAlignment(Qt.AlignCenter)
     self.rate.setFont(QFont('Times',9))
     
     #Number of years 
  
     n_Label =QLabel("Years",self)
     n_Label.setAlignment(Qt.AlignCenter)
     n_Label.setGeometry(20,150,170,40)
     n_Label.setStyleSheet("QLabel" "{"
                                      "border: 2px solid black;"
                                      "background:rgba(70,70,70,35);"
                                      "}"
                                     )
    
     n_Label.setFont(QFont('Times',9))
     
     #A corresponding input field for number of years
     self.years=QLineEdit(self)
     onlyInt= QIntValidator()# Validation for interest  rate  such that only integers are allowed
     self.years.setValidator(onlyInt)
     
     
     #Setting properties  for the Input field
     
     self.years.setGeometry(200,150,180,40)
     self.years.setAlignment(Qt.AlignCenter)
     self.years.setFont(QFont('Times',9))
     
     
     #Create  a  Loan mount LAbel
     a_Label=QLabel("Amount",self)
     a_Label.setAlignment(Qt.AlignCenter)
     a_Label.setGeometry(20,200,170,40)
     a_Label.setStyleSheet("QLabel" "{"
                                      "border: 2px solid black;"
                                      "background:rgba(70,70,70,35);"
                                      "}"
                                     )
    
     a_Label.setFont(QFont('Times',9))
     
     #A corresponding input field for the Loan amount
     self.amount=QLineEdit(self)
     onlyInt= QIntValidator()# Validation for interest  rate  such that only integers are allowed
     self.amount.setValidator(onlyInt)
     
     
     #Setting properties  for the Input field
     
     self.amount.setGeometry(200,200,180,40)
     self.amount.setAlignment(Qt.AlignCenter)
     self.amount.setFont(QFont('Times',9))
     
     
     
     #/////////Calculate Payment ///////
     #Creating compute Button
     calculate =QPushButton("Compute Payment",self)
     #Set Geometry for the PushButton
     calculate.setGeometry(125,270,150,40)
     
     #Add action to the button 
     calculate.clicked.connect(self.calculate_action)
     #////////output Widgets///
     
     #Monthly payment calculation
     
     
     self.m_payment =QLabel(self)
     
     self.m_payment.setAlignment(Qt.AlignCenter)
     self.m_payment.setGeometry(50,340,300,60)
     self.m_payment.setStyleSheet("QLabel" "{"
                                      "border: 3px solid black;"
                                      "background:white"
                                      "}"
                                     )
    
     self.m_payment.setFont(QFont('Times',11))
     
     
     #Total Payment label
     self.t_payment =QLabel(self)
     
     self.t_payment.setAlignment(Qt.AlignCenter)
     self.t_payment.setGeometry(50,410,300,60)
     self.t_payment.setStyleSheet("QLabel" "{"
                                      "border: 3px solid black;"
                                      "background:white"
                                      "}"
                                     )

     self.t_payment.setFont(QFont('Times',11))
     
     
 def calculate_action(self):
       
       #Getting Annual interest rate
       annualInterestRate  = self.rate.text()
       #To check if fileds are empty
       if len(annualInterestRate)==0 or  annualInterestRate=='0':
           QMessageBox.critical(self,"Error!","Input Fields cannot be Empty or set to zero ")
           
          #Getting Annual interest rate
       numberofyears = self.years.text()
       #To check if fileds are empty
       if len(numberofyears)==0 or  numberofyears=='0':
           QMessageBox.critical(self,"Error!","Input Fields cannot be Empty or set to zero ")
        
          #Getting Annual interest rate
       loanAmount = self.amount.text()
       #To check if fileds are empty
       if len(loanAmount)==0 or loanAmount=='0':
           QMessageBox.critical(self,"Error!","Input Fields cannot be Empty or set to zero ")
           
        #Get calculations
        #Convert text into integers
       annualInterestRate= int(annualInterestRate)
       numberofyears= int(numberofyears)
       loanAmount= int(loanAmount)
       
       
       #Monthly Interest Calculation(12monthsx100%)
       monthlyInterestRate =annualInterestRate/1200
       
       #calculate monthly payment
       monthlyPayment=loanAmount * monthlyInterestRate /  (1-1 /(1+ monthlyInterestRate) ** (numberofyears *12))
       
       #Monthly payment format(2dp float)
       monthlyPayment ="{:.2f}".format(monthlyPayment)
       #Set  monthlypayment as text plus the calculation
       
       self.m_payment.setText("Monthly Payment (Ksh) :"+ str(monthlyPayment))
        #Getting total Payment
       totalPayment= float(monthlyPayment) *12* numberofyears
       totalPayment ="{:.2f}".format(totalPayment)
       self.t_payment.setText("Total Payment(Ksh) :"+ str(totalPayment))
       
#Create app object

App = QApplication(sys.argv)

#Instantiiate a window class by creating a window object
window = Window()  
     
#Starting the Application
sys.exit(App.exec()) # Starts  the event loop and  blocks everything else untill the  application quits


