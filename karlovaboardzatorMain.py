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

		#######################################
		# Globals
		#######################################
		CURENT_USER 			= os.getenv('USER')
		CURENT_PROJECT_lower 	= ink.io.ConnectUserInfo()[2]		
		CURENT_PROJECT 			= CURENT_PROJECT_lower.upper()
		# print >> sys.__stderr__, CURENT_USER
		# print >> sys.__stderr__, CURENT_PROJECT



		# #######################################
		# # Tabs Widget as Menu
		# #######################################
		# self.tabArea = QtGui.QtabWidget()
		# self.tabArea.setTabPosition(QtGui.QtabWidget.North)
		# # self.tabArea.setTabPosition(QtGui.QtabWidget.West)
		# # self.setWidget(self.tabArea)
		# self.layout.addWidget(self.tabArea)

		# #######################################
		# # Tabs
		# #######################################




	#======================================================================
	#========= main vlayout
	#======================================================================
		self.mainLayout = QtGui.QVBoxLayout()

		#========= Top Bandeau container
		self.TopAreaContainer = QtGui.QWidget()
		#========= Top Bandeau content
		self.TopAreaContent = QtGui.QHBoxLayout()

		#========= Top Bandeau content button
		txtBt1 = 'SYNC MY SCRIPTS FROM ' + CURENT_PROJECT
		self.BT_MAIN_1 = QtGui.QPushButton(txtBt1)
		self.BT_MAIN_1.clicked.connect(self.on_BT_MAIN_clicked)		
		txtBt2 = 'BT2 ' + CURENT_PROJECT
		self.BT_MAIN_2 = QtGui.QPushButton(txtBt2)
		self.BT_MAIN_2.clicked.connect(self.on_BT_MAIN_clicked)
		txtBt3 = 'BT3 '
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




def start(parent, data):
	print >> sys.__stderr__, "__QT_KBZ__"
	main = __QT_KBZ__(parent)
	main.setWindowTitle('KARLOVA TOOLZ')
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


