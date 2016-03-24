# ##################################################################################
# MG ILLUMINATION                                                                  #
# First Crazy Debroussailleur : jDepoortere                                        #
# Author : cPOTTIER                                                                #
# Date : 24-03-2016                                                                #
# ##################################################################################


#=======================================================================================================================  CLASS __QT_GUI_SAMPLE__

import os
import sys
import random
import glob
from PyQt4 import QtGui, QtCore, Qt
import ink
import ink.io


class __QT_GUI_SAMPLE__(QtGui.QDialog):
	
	def __init__(self, parent = None): #
		super(__QT_GUI_SAMPLE__, self).__init__(parent) 


		self.CONNECT_USER_INFOS = ink.io.ConnectUserInfo()
		self.CONNECT_USER1 = self.CONNECT_USER_INFOS[1]

		self.setWindowTitle('Title Sample QT UI')

		self.palOk = QtGui.QPalette()
		self.palOk.setColor(QtGui.QPalette.ColorRole(6),QtGui.QColor("#55FF55"))
		self.palOk.setColor(QtGui.QPalette.ColorRole(9),QtGui.QColor("#999999"))
		self.palErr = QtGui.QPalette()
		self.palErr.setColor(QtGui.QPalette.ColorRole(6),QtGui.QColor("#FF0000"))
		self.palErr.setColor(QtGui.QPalette.ColorRole(9),QtGui.QColor("#999999"))
		sizeFactor_a = 30
		self.filmin = ""
		self.seqin = ""
		self.seqout = ""
		self.shotin = ""
		self.shotout = ""
		self.filein = ""
		self.fileout = ""
		self.inOk = 0
		self.outOk = 0
		self.worka = ink.io.FilePaths()
		self.work = self.worka[1]
		self.resize(400, 300)
		self.layout = QtGui.QVBoxLayout()
		self.setLayout(self.layout)

		self.labelGen = QtGui.QLabel("TITLE")
		self.labelFilmIn = QtGui.QLabel("FILM")
		self.labelSeqIn = QtGui.QLabel("SEQ")
		self.labelComments = QtGui.QLabel("Commentaire")
		self.checkBox1 = QtGui.QCheckBox('OK')
		self.labelShotIn = QtGui.QLabel("SHOT")
		self.labelShotOut = QtGui.QLabel("SHOT")
		self.editFilmIn = QtGui.QLineEdit()
		self.editSeqIn = QtGui.QListWidget()
		self.editSeqOut = QtGui.QLineEdit()
		self.comboShotIn = QtGui.QComboBox()
		self.editShotOut = QtGui.QLineEdit()
		self.editIn = QtGui.QLineEdit()
		self.editOut = QtGui.QLineEdit()

		self.layout.addWidget(self.labelGen)
		self.layout.addWidget(self.labelFilmIn)
		self.layout.addWidget(self.editFilmIn)
		self.layout.addWidget(self.labelSeqIn)
		self.layout.addWidget(self.editSeqIn)
		self.layout.addWidget(self.labelShotIn)
		self.layout.addWidget(self.comboShotIn)
		self.layout.addWidget(self.checkBox1)
		self.layout.addWidget(self.labelComments)
		self.layout.addWidget(self.editSeqOut)






		self.editSeqOut.setText('First Release From ' + self.CONNECT_USER1)


		self.editIn.setReadOnly(1)
		self.editOut.setReadOnly(1)

		self.okButton = QtGui.QPushButton("THIS BUTTON DO NOTHING")
		self.cancelButton = QtGui.QPushButton("Cancel close the custom Tool")
		self.layout.addWidget(self.okButton)
		self.layout.addWidget(self.cancelButton)

		self.cancelButton.connect(self.cancelButton,QtCore.SIGNAL("clicked()"),self.cancel)

		self.checkBox1.setCheckState(True)	
		self.comboShotIn.addItem('001')
		self.comboShotIn.addItem('002')




	def cancel(self):
		self.close()


	def test(self):
		printFromQT(parent)



def start(parent, data):
	print >> sys.__stderr__, "Start QT sample UI"
	main = __QT_GUI_SAMPLE__(parent)
	main.setModal(True)
	main.activateWindow()
	main.raise_()
	main.show()
