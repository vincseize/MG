#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 28-03-2016                                                                #
# ##################################################################################


#=======================================================================================================================  CLASS __QT_KBZ__

import os
import sys
import random
import glob
from PyQt4 import QtGui, QtCore, Qt
import ink
import ink.io


class __QT_KBZ__(QtGui.QDialog):
	
	def __init__(self, parent = None): #
		super(__QT_KBZ__, self).__init__(parent) 

	#======================================================================
	#========= Globals Varaiables
	#======================================================================
		self.CURENT_USER 				= os.getenv('USER')
		self.CURENT_PROJECT_lower 		= ink.io.ConnectUserInfo()[2]		
		self.CURENT_PROJECT 			= self.CURENT_PROJECT_lower.upper()
		# self.printSTD(self.CURENT_USER)
		# self.printSTD(self.CURENT_PROJECT)

	#======================================================================
	#========= main vlayout
	#======================================================================
		self.mainLayout = QtGui.QVBoxLayout()

		#========= Top Bandeau container
		self.TopAreaContainer = QtGui.QWidget()

		#========= Top Bandeau content
		self.TopAreaContent = QtGui.QHBoxLayout()

		#========= Top Bandeau content button
		txtBt1 = 'SYNC MY SCRIPTS FROM ' + self.CURENT_PROJECT
		self.BT_MAIN_1 = QtGui.QPushButton(txtBt1)
		self.BT_MAIN_1.clicked.connect(self.on_BT_MAIN_clicked)		
		txtBt2 = 'BT2 ' + self.CURENT_PROJECT
		self.BT_MAIN_2 = QtGui.QPushButton(txtBt2)
		self.BT_MAIN_2.clicked.connect(self.on_BT_MAIN_clicked)
		txtBt3 = 'BT3 ' + self.CURENT_PROJECT
		self.BT_MAIN_3 = QtGui.QPushButton(txtBt3)
		self.BT_MAIN_3.clicked.connect(self.on_BT_MAIN_clicked)

		#========= add button to Bandeau content
		self.TopAreaContent.addWidget(self.BT_MAIN_1)
		self.TopAreaContent.addWidget(self.BT_MAIN_2)
		self.TopAreaContent.addWidget(self.BT_MAIN_3)

		#========= add Bandeau content to bandeau container
		self.TopAreaContainer.setLayout(self.TopAreaContent)


		# #========= Tab Area Widget
		self.tabArea = QtGui.QTabWidget()
		self.tabArea.setTabPosition(QtGui.QTabWidget.North)
		# self.tabArea.setTabPosition(QtGui.QTabWidget.West)
		# self.setWidget(self.tabArea)


		# #=========================== Tab1

		self.Tab1 = QtGui.QTreeWidget()
		self.tabArea.addTab(self.Tab1, "Arbo")
		# self.connect(self.Tab1, QtCore.SIGNAL("itemDoubleClicked (QTreeWidgetItem *,int)"), self.on_Tab1_double_clicked)
		self.connect(self.Tab1, QtCore.SIGNAL("itemClicked (QTreeWidgetItem *,int)"), self.on_Tab1_clicked)

		self.Tab1.setAnimated(True)
		self.Tab1.setRootIsDecorated(True)
		self.Tab1.setAlternatingRowColors(False)
		self.Tab1.header().setStretchLastSection(True)
		self.Tab1.headerItem().setText(0, "")
		self.Tab1.headerItem().setText(1, "Property")
		self.Tab1.headerItem().setText(2, "Value")
		self.Tab1.setColumnWidth(0, 100)
		self.Tab1.setColumnWidth(1, 150)

		# #=========================== Tab2









		# #========= scroll area widget contents - layout
		# self.scrollLayout = QtGui.QFormLayout()

		# #========= scroll area widget contents
		# self.scrollWidget = QtGui.QWidget()
		# self.scrollWidget.setLayout(self.scrollLayout)

		# #========= scroll area
		# self.scrollArea = QtGui.QScrollArea()
		# self.scrollArea.setWidgetResizable(True)
		# self.scrollArea.setWidget(self.scrollWidget)

	#======================================================================
	#========= add all to the main vLayout
	#======================================================================
		self.mainLayout.addWidget(self.TopAreaContainer)
		self.mainLayout.addWidget(self.tabArea)
		# self.mainLayout.addWidget(self.scrollArea)

	#======================================================================
	#========= central widget
	#======================================================================
		self.centralWidget = QtGui.QWidget()
		self.setLayout(self.mainLayout)
		#========= apply stylsheets
		self.apply_Stylesheets()
		self.setPalette(self.palette_darkGrey)

	#======================================================================
	#========= Functions
	#======================================================================

	#========= Buttons

	def on_BT_MAIN_clicked(self):
		print >> sys.__stderr__, "on_BT_MAIN_clicked"


	def on_Tab1_clicked(self):
		print >> sys.__stderr__, "on_Tab1_clicked"


	def closeWindows(self):
		self.close()

	def printSTD(self,msg):
		print >> sys.__stderr__, msg



	#======================================================================
	#========= StyleSheets
	#======================================================================

	def apply_Stylesheets(self):

		def rvbToHex(r,g,b):
			# r = array_rgb[1], g=array_rgb[2], b=array_rgb[3]
			hexColor = '#%02x%02x%02x' % (r, g, b)
			return hexColor



	#======================================================= Globals Colors

	#========= general Colors	

		self.palette_White = QtGui.QPalette()
		self.palette_White.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 255, 255))

		self.palette_Black = QtGui.QPalette()
		self.palette_Black.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(0, 0, 0))

		self.palette_grey = QtGui.QPalette()
		self.palette_grey.setColor(QtGui.QPalette.Background,QtCore.Qt.gray)

		self.palette_mediumGrey = QtGui.QPalette()
		self.palette_mediumGrey.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(128, 128, 128))

		self.palette_darkGrey = QtGui.QPalette()
		self.palette_darkGrey.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(66, 66, 66))

	#============================================ Complementary blues Colors # http://paletton.com	

	#========= blues Colors

		self.palette_Blue1 = QtGui.QPalette()
		self.palette_Blue1.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(97, 114, 141))

		self.palette_Blue2 = QtGui.QPalette()
		self.palette_Blue2.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(64, 84, 115))

		self.palette_Blue3 = QtGui.QPalette()
		self.palette_Blue3.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(43, 61, 91))

		self.palette_Blue4 = QtGui.QPalette()
		self.palette_Blue4.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(25, 44, 75))

		self.palette_Blue5 = QtGui.QPalette()
		self.palette_Blue5.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(10, 25, 50))

	#========= blues Colors

		self.palette_orange1 = QtGui.QPalette()
		self.palette_orange1.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 196, 77))

		self.palette_orange2 = QtGui.QPalette()
		self.palette_orange2.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 179, 27))

		self.palette_orange3 = QtGui.QPalette()
		self.palette_orange3.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 170, 0))

		self.palette_orange4 = QtGui.QPalette()
		self.palette_orange4.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(206, 137, 0))

		self.palette_orange5 = QtGui.QPalette()
		self.palette_orange5.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(160, 107, 0))


	#========= Style Buttons

		hexColor = rvbToHex(25, 44, 75)
		self.BT_MAIN_1.setStyleSheet('QPushButton {background-color: '+hexColor+'; color: white;}')
		self.BT_MAIN_2.setStyleSheet('QPushButton {background-color: '+hexColor+'; color: white;}')
		self.BT_MAIN_3.setStyleSheet('QPushButton {background-color: '+hexColor+'; color: white;}')



#===================================================================================================================================
#========= Start QT 
#===================================================================================================================================


def start(parent, data):
	print >> sys.__stderr__, "__QT_KBZ__"
	main = __QT_KBZ__(parent)
	array_welcome = ['Welcome Dear', 'Welcome', 'Willkommen', 'Welkom']
	array_welcome = array_welcome + ['Bienvenue', 'Bienvenue Fulgence']
	array_welcome = array_welcome + ['Xos', 'Ongietorri', 'I mirepritur']
	welcome = random.choice(array_welcome)
	main.setWindowTitle( ink.io.ConnectUserInfo()[2].upper() + ' | KARLOVA DASHBOARDZATOR | '+ welcome +' ' + os.getenv('USER') )
	main.showMaximized()
	# sG = QtGui.QApplication.desktop().screenGeometry()
	# w = sG.width
	# h = sG.height
	# main.resize(250, 150)
	# main.move(300, 300)
	# main.setGeometry(300, 300, 150, 200)

	main.setModal(True)
	main.activateWindow()
	main.raise_()
	main.show()


