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
		self.mainLayout.setAlignment(QtCore.Qt.AlignTop)

		#=============================================== Top Area container
		self.TopAreaContainer = QtGui.QWidget()
		self.TopAreaContainer.setObjectName("TopAreaContainer")

		#========= Top Area content
		self.construct_TopAreaContent()
		#========= add Area content to Top Area container
		self.TopAreaContainer.setLayout(self.TopAreaContent)

		#============================================ Middle Area container
		self.MiddleAreaContainer = QtGui.QWidget()
		self.MiddleAreaContainer.setObjectName("MiddleAreaContainer")
		#========= Tabs Area Widget
		self.construct_MiddleTabsArea()
		#========= add Area content to middle Area container
		self.MiddleAreaContainer.setLayout(self.MiddleTabsContent)


	#======================================================================
	#========= add all to the main vLayout
	#======================================================================
		self.mainLayout.addWidget(self.TopAreaContainer)
		self.mainLayout.addWidget(self.MiddleAreaContainer)
		# self.mainLayout.addWidget(self.scrollArea)


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
	#========= Areas Constructions
	#======================================================================

	def construct_TopAreaContent(self):

		#========= Top Area content
		self.TopAreaContent = QtGui.QHBoxLayout()

		#========= Top Area content button
		txtBt1 = 'SYNC MY SCRIPTS FROM ' + self.CURENT_PROJECT
		self.BT_MAIN_1 = QtGui.QPushButton(txtBt1)
		self.BT_MAIN_1.clicked.connect(self.on_BT_MAIN_clicked)		
		txtBt2 = 'BT2 ' + self.CURENT_PROJECT
		self.BT_MAIN_2 = QtGui.QPushButton(txtBt2)
		self.BT_MAIN_2.clicked.connect(self.on_BT_MAIN_clicked)
		txtBt3 = 'BT3 ' + self.CURENT_PROJECT
		self.BT_MAIN_3 = QtGui.QPushButton(txtBt3)
		self.BT_MAIN_3.clicked.connect(self.on_BT_MAIN_clicked)

		#================================================== add button to Top Area content
		self.TopAreaContent.addWidget(self.BT_MAIN_1)
		self.TopAreaContent.addWidget(self.BT_MAIN_2)
		self.TopAreaContent.addWidget(self.BT_MAIN_3)


	def construct_MiddleTabsArea(self):

		#========= Middle Area content
		self.MiddleTabsContent = QtGui.QHBoxLayout()


		# #========= Tab Area Widget
		self.MiddleTabsArea = QtGui.QTabWidget()
		self.MiddleTabsArea.setTabPosition(QtGui.QTabWidget.North)
		self.MiddleTabsArea.setObjectName("nameEdit")

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

		#=========================== TabX



		#================================================== add button to Middle Area content
		self.MiddleTabsContent.addWidget(self.MiddleTabsArea)

