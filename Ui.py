import sys
import design
import Waiter
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QWidget, QApplication

class App(QtWidgets.QWidget, design.Ui_Waiter):

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
		self.SERVE.clicked.connect(self.Serve)
		self.EXIT.clicked.connect(self.Exit)
		self.ENTER.clicked.connect(self.Enter)
		self.check_1.clicked.connect(self.check1)
		self.check_2.clicked.connect(self.check2)
		self.check_3.clicked.connect(self.check3)
		self.check_4.clicked.connect(self.check4)
		self.ADD.clicked.connect(self.add)
		self.CLOSE.clicked.connect(self.close)
		self.RELOAD.clicked.connect(self.reload)
				

			
	def Exit(self):
		self.EXIT.clicked.connect(QCoreApplication.quit)
	import Waiter

		
	def Serve(self):
		while True:
			self.PREVIOUS.clear()
			if  self.ADD.isChecked() == True:
				if self.check_1.isChecked() == True:
					table = 1
				elif self.check_2.isChecked()  == True:
					table = 2
				elif self.check_3.isChecked()  == True:
					table = 3
				elif self.check_4.isChecked()  == True:
					table = 4
				else:
					self.PREVIOUS.addItem("Tick TABLE\n")
					self.PREVIOUS.addItem(str(Waiter.Read()))
					break
				self.PREVIOUS.addItem(Waiter.Show(table))
				
			elif self.CLOSE.isChecked() == True:
				if self.check_1.isChecked() == True:
					table = 1
				elif self.check_2.isChecked()  == True:
					table = 2
				elif self.check_3.isChecked()  == True:
					table = 3
				elif self.check_4.isChecked()  == True:
					table = 4
				else:
					self.PREVIOUS.addItem("Tick TABLE\n")
					self.PREVIOUS.addItem(str(Waiter.Read()))
					break
					
				Waiter.Close(table)
				self.PREVIOUS.clear()
				self.INPUT.clear()
				self.PREVIOUS.addItem(str(Waiter.Read()))
			
			else:
				self.PREVIOUS.addItem("Tick SERVICE\n")
				self.PREVIOUS.addItem(str(Waiter.Read()))
			break
	
	
	def Enter(self):
		while True:
			if self.ADD.isChecked() == True:
				if self.check_1.isChecked() == True:
					table = 1
				elif self.check_2.isChecked()  == True:
					table = 2
				elif self.check_3.isChecked()  == True:
					table = 3
				elif self.check_4.isChecked()  == True:
					table = 4
				else:
					self.PREVIOUS.clear()
					self.PREVIOUS.addItem("Tick TABLE\n")
					break
				if str(self.INPUT.text()) != "":
					Waiter.Input(table, str(self.INPUT.text()))
					self.check_1.setChecked(False)
					self.check_2.setChecked(False)
					self.check_3.setChecked(False)
					self.check_4.setChecked(False)
					self.CLOSE.setChecked(False)
					self.ADD.setChecked(False)
					self.PREVIOUS.clear()
					self.INPUT.clear()
				else:
					self.PREVIOUS.addItem("INPUTE is empy")
					break
			elif self.CLOSE.isChecked() == True:			
				if self.check_1.isChecked() == True:
					table = 1
				elif self.check_2.isChecked()  == True:
					table = 2
				elif self.check_3.isChecked()  == True:
					table = 3
				elif self.check_4.isChecked()  == True:
					table = 4
				else:
					self.PREVIOUS.clear()
					self.PREVIOUS.addItem("Tick TABLE\n")
					break
				if str(self.INPUT.text()) != "":
					Waiter.Input(table, str(self.INPUT.text()))
					self.check_1.setChecked(False)
					self.check_2.setChecked(False)
					self.check_3.setChecked(False)
					self.check_4.setChecked(False)
					self.CLOSE.setChecked(False)
					self.ADD.setChecked(False)
				Waiter.Close(table)
				self.PREVIOUS.clear()
				self.INPUT.clear()
			else:
				
				self.PREVIOUS.clear()
				self.PREVIOUS.addItem("Tick SERVICE\n")
			self.PREVIOUS.addItem(str(Waiter.Read()))
			break



	def reload(self):
		self.PREVIOUS.clear()
		self.INPUT.clear()
		self.PREVIOUS.addItem(str(Waiter.Read()))
	
	def check1(self):
		self.check_4.setChecked(False)
		self.check_2.setChecked(False)
		self.check_3.setChecked(False)
	def check2(self):
		self.check_1.setChecked(False)
		self.check_4.setChecked(False)
		self.check_3.setChecked(False)
	def check3(self):
		self.check_1.setChecked(False)
		self.check_2.setChecked(False)
		self.check_4.setChecked(False)
	def check4(self):
		self.check_1.setChecked(False)
		self.check_2.setChecked(False)
		self.check_3.setChecked(False)
	def close(self):
		self.ADD.setChecked(False)
	def add(self):
		self.CLOSE.setChecked(False)

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			print("escape")
			self.Exit()
			self.close()
		elif event.key() == Qt.Key_Enter:
			print("enter")
			self.Enter()
		elif event.key() == Qt.Key_1:
			self.check_1.setChecked(True)
			self.check1()
		elif event.key() == Qt.Key_2:
			self.check2()
			self.check_2.setChecked(True)
		elif event.key() == Qt.Key_3:
			self.check3()
			self.check_3.setChecked(True)
		elif event.key() == Qt.Key_4:
			self.check4()
			self.check_4.setChecked(True)
		elif event.key() == Qt.Key_A:
			self.CLOSE.setChecked(False)
			self.ADD.setChecked(True)
		elif event.key() == Qt.Key_C:
			self.CLOSE.setChecked(True)
			self.ADD.setChecked(False)
		elif event.key() == Qt.Key_R:
			self.reload()

#########################################################################

#def Read():
#	return('UPDATED!!!!')
	
#def Input(table, enter):
#	print("INPUTE" + str(table) + str(enter))
	

	
#def Close(table):
#	print("CLOSE" + str(table))



#def Show(table):
#	return("MEOW\n" +str(table)+ "\nWOOF")

	

def main():
	app = QtWidgets.QApplication(sys.argv)
	window = App()
	window.show()
	app.exec_()

if __name__ == '__main__':
	main()
