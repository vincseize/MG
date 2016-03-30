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
import time


class __QT_KBZ__(QtGui.QDialog):
	
	def __init__(self, parent = None): #
		super(__QT_KBZ__, self).__init__(parent) 

	#======================================================================
	#========= Globals Varaiables
	#======================================================================
		self.CURENT_USER 				= os.getenv('USER')
		self.CURENT_PROJECT_lower 		= ink.io.ConnectUserInfo()[2]		
		self.CURENT_PROJECT 			= self.CURENT_PROJECT_lower.upper()

	#======================================================================
	#========= main vlayout
	#======================================================================

		self.mainLayout = QtGui.QVBoxLayout()
		self.mainLayout.setAlignment(QtCore.Qt.AlignTop)

		#=============================================== Top Area container
		self.TopAreaContainer = QtGui.QWidget()
		self.TopAreaContainer.setObjectName("TopAreaContainer")
		#========= Top Area content
		self.construct_TopAreaContent()
		# #========= add Area content to Top Area container
		# self.TopAreaContainer.setLayout(self.TopAreaContent)

		#============================================ Middle Area container
		self.MiddleAreaContainer = QtGui.QWidget()
		self.MiddleAreaContainer.setObjectName("MiddleAreaContainer")
		#========= Tabs Area Widget
		self.construct_MiddleTabsArea()
		# #========= add Area content to middle Area container
		# self.MiddleAreaContainer.setLayout(self.MiddleTabsContent)

		#============================================ Bottom Area container
		self.BottomAreaContainer = QtGui.QWidget()
		self.BottomAreaContainer.setObjectName("BottomAreaContainer")
		#========= Bottom Area content
		self.construct_BottomAreaContent()
		# #========= add Area content to Top Area container
		# self.BottomAreaContainer.setLayout(self.BottomAreaContent)

	#======================================================================
	#========= add all to the main vLayout
	#======================================================================
		self.mainLayout.addWidget(self.TopAreaContainer)
		self.mainLayout.addWidget(self.MiddleAreaContainer)
		self.mainLayout.addWidget(self.BottomAreaContainer)

	#======================================================================
	#========= central widget
	#======================================================================
		self.centralWidget = QtGui.QWidget()
		self.setLayout(self.mainLayout)
		#========= apply stylsheets
		self.apply_Stylesheets()
		self.setPalette(self.palette_darkGrey)

	#===================================================================================================================================
	#========= Functions
	#===================================================================================================================================

	#======================================================================
	#========= Areas Constructions Functions
	#======================================================================

	def construct_TopAreaContent(self):
		'''   '''
		#========= Top Area content
		self.TopAreaContent = QtGui.QHBoxLayout()
		self.TopAreaContent.setObjectName("TopAreaContent")

		#========= Top Area content button
		txtBt = 'SYNC MY SCRIPTS FROM ' + self.CURENT_PROJECT
		self.BT_MAIN_1 = QtGui.QPushButton(txtBt)
		self.BT_MAIN_1.clicked.connect(lambda : self.on_BT_MAIN_clicked('BT_MAIN_1'))		
		txtBt = 'BT2 ' + self.CURENT_PROJECT
		self.BT_MAIN_2 = QtGui.QPushButton(txtBt)
		self.BT_MAIN_2.clicked.connect(self.on_BT_MAIN_clicked)
		txtBt = 'BT3 ' + self.CURENT_PROJECT
		self.BT_MAIN_3 = QtGui.QPushButton(txtBt)
		self.BT_MAIN_3.clicked.connect(self.on_BT_MAIN_clicked)

		#================================================== add button to Top Area content
		self.TopAreaContent.addWidget(self.BT_MAIN_1)
		self.TopAreaContent.addWidget(self.BT_MAIN_2)
		self.TopAreaContent.addWidget(self.BT_MAIN_3)

		#========= add Area content to Top Area container
		self.TopAreaContainer.setLayout(self.TopAreaContent)


	def construct_MiddleTabsArea(self):
		'''   '''
		#========= Middle Area content
		self.MiddleTabsContent = QtGui.QHBoxLayout()
		self.MiddleTabsContent.setObjectName("MiddleTabsContent")

		# #========= Tab Area Widget
		self.MiddleTabsArea = QtGui.QTabWidget()
		self.MiddleTabsArea.setTabPosition(QtGui.QTabWidget.North)
		self.MiddleTabsArea.setObjectName("MiddleTabsArea")

		#=========================== Tab1
		self.Tab1 = QtGui.QTreeWidget()
		self.MiddleTabsArea.addTab(self.Tab1, "Arbo")
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

		#=========================== Tab2		

		#=========================== Tab X

		#================================================== add Tabs to Middle Area content
		self.MiddleTabsContent.addWidget(self.MiddleTabsArea)

		#========================================== add Area content to middle Area container
		self.MiddleAreaContainer.setLayout(self.MiddleTabsContent)


	def construct_BottomAreaContent(self):
		'''   '''
		#========= Top Area content
		self.BottomAreaContent = QtGui.QHBoxLayout()
		self.BottomAreaContent.setObjectName("BottomAreaContent")
		#========= Top Area content button
		now = time.strftime("%Y/%d/%m %H:%M:%S")
		txtLbl = now
		self.labelBottom = QtGui.QLabel()
		self.labelBottom.setText(txtLbl)

		#================================================== add button to Top Area content
		self.BottomAreaContent.addWidget(self.labelBottom)

		#========= add Area content to Top Area container
		self.BottomAreaContainer.setLayout(self.BottomAreaContent)



	# def construct_scrollLayout(self):
	# 	#========= scroll area widget contents - layout
	# 	self.scrollLayout = QtGui.QFormLayout()

	# 	#========= scroll area widget contents
	# 	self.scrollWidget = QtGui.QWidget()
	# 	self.scrollWidget.setLayout(self.scrollLayout)

	# 	#========= scroll area
	# 	self.scrollArea = QtGui.QScrollArea()
	# 	self.scrollArea.setWidgetResizable(True)
	# 	self.scrollArea.setWidget(self.scrollWidget)


	#======================================================================
	#========= Buttons Functions
	#======================================================================

	def on_BT_MAIN_clicked(self,BT):
		if BT == "BT_MAIN_1":
			self.clear_LayoutOrWidget(self.MiddleAreaContainer)
			self.clear_LayoutOrWidget(self.BottomAreaContainer)
		else:
			self.MiddleAreaContainer = QtGui.QWidget()
			self.MiddleAreaContainer.setObjectName("MiddleAreaContainer")
			self.construct_MiddleTabsArea()
			self.BottomAreaContainer = QtGui.QWidget()
			self.BottomAreaContainer.setObjectName("BottomAreaContainer")
			self.construct_BottomAreaContent()
			self.mainLayout.addWidget(self.MiddleAreaContainer)
			self.mainLayout.addWidget(self.BottomAreaContainer)

	def on_Tab1_clicked(self):
		self.printSTD("on_Tab1_clicked")

	def closeWindows(self):
		self.close()

	def printSTD(self,msg):
		print >> sys.__stderr__, msg

	def clear_LayoutOrWidget(self, LW):
		try:
			LW.deleteLater()
		except:
			pass
		try:
			self.clearLayout(LW)
		except:
			pass


	#===================================================================================================================================
	#========= StyleSheets
	#===================================================================================================================================

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

		# other samples
		# pal.setColor(QtGui.QPalette.ColorRole(9),QtGui.QColor("#4B4B4B"))
		# pal.setColor(QtGui.QPalette.ColorRole(6),QtGui.QColor("#CCCCCC"))

	#========= Style Buttons

		hexColor = rvbToHex(25, 44, 50)
		
		# self.BT_MAIN_1.setStyleSheet('QPushButton {background-color: '+hexColor+'; color: white; height: 40px;}')
		self.BT_MAIN_1.setStyleSheet(
								"color: white;"
								"background-color: "+hexColor+";"
								"selection-color: yellow;"
								"selection-background-color: blue;"
								"font: bold 14px;"
								"border-style: outset;"
								"height: 40px;"
							)
		self.BT_MAIN_2.setStyleSheet(
								"color: white;"
								"background-color: "+hexColor+";"
								"selection-color: yellow;"
								"selection-background-color: blue;"
								"font: bold 14px;"
								"border-style: outset;"
								"height: 40px;"
							)
		self.BT_MAIN_3.setStyleSheet(
								"color: white;"
								"background-color: "+hexColor+";"
								"selection-color: yellow;"
								"selection-background-color: blue;"
								"font: bold 14px;"
								"border-style: outset;"
								"height: 40px;"
							)



		# other samples

		# self.BT_MAIN_1.setFlat(True)

		# QPushButton#self.BT_MAIN_1 {
		# 	background-color: red;
		# 	border-style: outset;
		# 	border-width: 2px;
		# 	border-radius: 10px;
		# 	border-color: beige;
		# 	font: bold 14px;
		# 	min-width: 10em;
		# 	padding: 6px;
		# }










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


