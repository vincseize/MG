#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 01-04-2016                                                                #
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
import json
from shutil import copyfile
import datetime


class __QT_KBZ__(QtGui.QDialog):
	
	def __init__(self, parent = None): #
		super(__QT_KBZ__, self).__init__(parent) 

	#======================================================================
	#========= Globals Varaiables
	#======================================================================
		self.CURRENT_USER 				= os.getenv('USER')
		self.ALL_PROJECTS	 			= ['gri','lun','dm3']
		self.CURRENT_PROJECT_lower 		= ink.io.ConnectUserInfo()[2]		
		self.CURRENT_PROJECT 			= self.CURRENT_PROJECT_lower.upper()
		self.PATH_EXEMPLES				= '/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples'
		# self.CURRENT_SCRIPTS_PATH		= '/u/'+self.CURRENT_PROJECT_lower+'/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples'
		self.CURRENT_SCRIPTS_PATH		= '/u/'+self.CURRENT_PROJECT_lower+self.PATH_EXEMPLES
		self.DIR_BACKUP	 				= '_backup'		
		self.MYPREFSFILE				= self.CURRENT_SCRIPTS_PATH+'/kbz_prefs_'+self.CURRENT_USER+'.json'
		self.MYPREFSJSON				= {}
		self.MYPREFSJSON["scripts"]		= []
		if os.path.isfile(self.MYPREFSFILE) == False :
			self.write_Prefs(self.MYPREFSJSON,False)
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
	#========= UI Areas Constructions Functions
	#======================================================================

	def construct_TopAreaContent(self):
		'''   '''
		#========= Top Area content
		self.TopAreaContent = QtGui.QHBoxLayout()
		self.TopAreaContent.setObjectName("TopAreaContent")

		#========= Top Area content button
		txtBt = 'SCRIPTS ' + self.CURRENT_PROJECT
		self.BT_MAIN_1 = QtGui.QPushButton(txtBt)
		self.BT_MAIN_1.clicked.connect(lambda : self.on_BT_MAIN_clicked('BT_MAIN_1'))		
		txtBt = 'BT2 ' + self.CURRENT_PROJECT
		self.BT_MAIN_2 = QtGui.QPushButton(txtBt)
		self.BT_MAIN_2.clicked.connect(lambda : self.on_BT_MAIN_clicked('BT_MAIN_2'))
		txtBt = 'BT3 ' + self.CURRENT_PROJECT
		self.BT_MAIN_3 = QtGui.QPushButton(txtBt)
		self.BT_MAIN_3.clicked.connect(lambda : self.on_BT_MAIN_clicked('BT_MAIN_3'))

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
		self.connect(self.Tab1, QtCore.SIGNAL("itemClicked (QTreeWidgetItem *,int)"), self.on_TAB_clicked)

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
		#========= Bottom Area content
		self.BottomAreaContent = QtGui.QHBoxLayout()
		self.BottomAreaContent.setObjectName("BottomAreaContent")
		#========= Bottom Area content Date
		now = time.strftime("%Y/%d/%m %H:%M:%S")
		txtLbl = now
		self.labelBottom = QtGui.QLabel()
		self.labelBottom.setText(txtLbl)

		#================================================== add Date to Bottom Area content
		self.BottomAreaContent.addWidget(self.labelBottom)

		#========= add Area content to Bottom Area container
		self.BottomAreaContainer.setLayout(self.BottomAreaContent)


	def construct_ScriptsListArea(self):
		'''   '''
		#========= List Area content
		self.ScriptsAreaContent = QtGui.QStandardItemModel()
		self.BottomAreaContent.setObjectName("ScriptsAreaContent")
		# self.ScriptsAreaContent.setAlternatingRowColors(True)

		#========= List Area content ckecked
		myChecked = []
		myPrefs = json.load(open(self.MYPREFSFILE))
		for v in myPrefs["scripts"]:
			myChecked.append(v)
		dirs = self.list_Scripts()
		n = 0
		for script in dirs:
			if '.pyc' not in str(script) and '.py~' not in str(script) and '__init__.py' not in str(script) and '_kbz.json' not in str(script):
				n = n+1
				item = QtGui.QStandardItem(script)
				item.setCheckable(True)
				status_checked = QtCore.Qt.Unchecked
				if n%2 == 0 :
					item.setBackground(QtGui.QColor(255, 255, 255))
				else:
					item.setBackground(QtGui.QColor(217, 230, 240))
				if str(script) in myChecked:
					status_checked = QtCore.Qt.Checked
					item.setBackground(QtGui.QColor(179, 255, 102))
				item.setCheckState(status_checked)

				# item.setColor(allBlueAndShiny color)
				# item.setForeground(QtGui.QColor('red')) # text color

				#========= item Signal
				# # item.emit(QtCore.SIGNAL("self.populate_prefs('scripts')"))
				# item.itemChanged.connect(self.populate_prefs)

				#================================================== add ckecked to List Area content
				self.ScriptsAreaContent.appendRow(item)
		#========= add Area content to Scripts content
		self.ScriptsAreaContainer.setModel(self.ScriptsAreaContent)

		#=========  bt sync
		txtBt = 'Click Here to SYNC SCRIPTS ' + self.CURRENT_PROJECT + ' -> to Others Projects'
		self.BT_SYNC_SCRIPTS = QtGui.QPushButton(txtBt)

		#=========  connect fct
		# self.connect(self.ScriptsAreaContent, QtCore.SIGNAL("itemClicked (QStandardItem *,int)"), self.populate_prefs)
		self.ScriptsAreaContent.itemChanged.connect(self.populate_prefs_scripts)
		self.BT_SYNC_SCRIPTS.clicked.connect(self.on_BT_SYNC_SCRIPTS_clicked)


	#======================================================================
	#========= UI Buttons Functions
	#======================================================================

	def on_BT_MAIN_clicked(self,BT):
		if BT == "BT_MAIN_1":
			self.delete_TopAndMiddle()
			self.Construct_MiddleScript()
		if BT == "BT_MAIN_2":
			self.delete_TopAndMiddle()
			self.Construct_TopAndMiddle()
		if BT == "BT_MAIN_3":
			self.delete_TopAndMiddle()
			self.Construct_TopAndMiddle()

	def on_BT_SYNC_SCRIPTS_clicked(self):

		now = datetime.datetime.now()
		date = now.strftime("%Y%m%d-%H-%M-%S")

		array_scriptToSync = []
		myPrefs = json.load(open(self.MYPREFSFILE))

		for v in myPrefs["scripts"]:
			array_scriptToSync.append(v)

		for ap in self.ALL_PROJECTS:
			dir_distant_backup = '/u/'+ap+self.PATH_EXEMPLES+'/'+self.DIR_BACKUP
			if not os.path.exists(dir_distant_backup):
				os.makedirs(dir_distant_backup)
			APU = str(ap).upper()
			ap 	= str(ap).lower()		

			if str(self.CURRENT_PROJECT_lower) != str(ap):
				msg = '---------------------------------- SYNC SCRIPTS ' + self.CURRENT_PROJECT + ' -> ' + APU
				self.printSTD(' ')
				self.printSTD('-----------------------------------------------------------------------')
				self.printSTD(str(msg))
				self.printSTD('-----------------------------------------------------------------------')
				for s in array_scriptToSync:
					filename = s.split('.')[0]
					ext 	 = s.split('.')[1]
					sbackup = filename+'_'+date+'.'+ext
					path_local 			= '/u/'+self.CURRENT_PROJECT_lower+self.PATH_EXEMPLES+'/'+s
					path_distant 		= '/u/'+ap+self.PATH_EXEMPLES+'/'+s
					path_distant_backup = dir_distant_backup+'/'+sbackup
					self.printSTD(path_local)					
					self.printSTD('->')
					self.printSTD(path_distant)	
					try:
						if os.path.isfile(path_local):
		#========= backup distant file before copy
							if os.path.isfile(path_distant):
								copyfile(path_distant, path_distant_backup)
		#========= copy sync
							copyfile(path_local, path_distant)
							self.printSTD('[ SYNC OK ]')
					except:
						self.printSTD('[ SYNC ERROR ]')


	#======================================================================
	#========= UI Construct Functions
	#======================================================================

	def on_TAB_clicked(self):
		self.printSTD("on_TAB_clicked")

	def closeWindows(self):
		self.close()

	def clear_LayoutOrWidget(self, LW):
		try:
			LW.deleteLater()
		except:
			pass
		try:
			self.clearLayout(LW)
		except:
			pass

	def delete_TopAndMiddle(self):
		try:
			self.clear_LayoutOrWidget(self.MiddleAreaContainer)
		except:
			pass
		try:
			self.clear_LayoutOrWidget(self.BottomAreaContainer)
		except:
			pass
		try:
			self.clear_LayoutOrWidget(self.ScriptsAreaContainer)
		except:
			pass


	def Construct_TopAndMiddle(self):
		self.MiddleAreaContainer = QtGui.QWidget()
		self.MiddleAreaContainer.setObjectName("MiddleAreaContainer")
		self.construct_MiddleTabsArea()
		self.BottomAreaContainer = QtGui.QWidget()
		self.BottomAreaContainer.setObjectName("BottomAreaContainer")
		self.construct_BottomAreaContent()
		self.mainLayout.addWidget(self.MiddleAreaContainer)
		self.mainLayout.addWidget(self.BottomAreaContainer)

	def Construct_MiddleScript(self):
		#========= Scripts Area container
		self.ScriptsAreaContainer = QtGui.QListView()
		self.ScriptsAreaContainer.setObjectName("ScriptsAreaContainer")
		self.construct_ScriptsListArea()
		self.mainLayout.addWidget(self.ScriptsAreaContainer)
		self.mainLayout.addWidget(self.BT_SYNC_SCRIPTS)


	#======================================================================
	#========= Others Functions
	#======================================================================

	def list_Scripts(self):
		dirs = os.listdir(self.CURRENT_SCRIPTS_PATH)
		return dirs

	def populate_prefs_scripts(self,item):
		checkIfExist = False
		#========= check if checked or already exist in list

		#========= get json method 1
		# with open(self.MYPREFSFILE) as json_file:
		# 	myPrefs = json.load(json_file)

		#========= get json method 2
		# s = open(self.MYPREFSFILE, 'r').read()
		# myPrefs = eval(s)

		#========= get json method 3
		myPrefs = json.load(open(self.MYPREFSFILE))
		for key, value in myPrefs.items():
			if str(key) == "scripts" and str(item.text()) in str(value) : # value is a list
				checkIfExist = True

		if checkIfExist == False:
			self.MYPREFSJSON = myPrefs
			self.MYPREFSJSON["scripts"].append(item.text())
			# self.write_Prefs(self.MYPREFSJSON,False)
		if checkIfExist == True:
			new_values = [] 
			for v in myPrefs["scripts"]:
				if str(v) != str(item.text()):
					new_values.append(v)
			self.MYPREFSJSON.pop('scripts', 0) # to do better
			self.MYPREFSJSON["scripts"]		= []
			for v in new_values:
				self.MYPREFSJSON["scripts"].append(v)	

		# self.printSTD(self.MYPREFSJSON["scripts"])
		self.write_Prefs(self.MYPREFSJSON,False)

	def write_Prefs(self,myPrefs,isIndent=False):
		if isIndent == False:
			# with open(self.MYPREFSFILE, 'w') as outfile:
			# 	json.dump(myPrefs, outfile)
			json.dump(myPrefs, open(self.MYPREFSFILE,'w'))
		if isIndent == True:
			# with open(self.MYPREFSFILE, 'w') as outfile:
			# 	json.dump(myPrefs, outfile, indent=4)
			file.write(dumps(self.MYPREFSFILE, file, indent=4))

	def printSTD(self,msg):
		print >> sys.__stderr__, msg

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
		rvb_White = [255, 255, 255]
		self.palette_White = QtGui.QPalette()
		self.palette_White.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 255, 255))

		rvb_Black = [0, 0, 0]
		self.palette_Black = QtGui.QPalette()
		self.palette_Black.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(0, 0, 0))

		rvb_Grey = [128, 128, 128]
		self.palette_Grey = QtGui.QPalette()
		self.palette_Grey.setColor(QtGui.QPalette.Background,QtCore.Qt.gray)

		rvb_hellGrey = [230, 230, 230]
		self.palette_hellGrey = QtGui.QPalette()
		self.palette_hellGrey.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(128, 128, 128))

		rvb_darkGrey = [255, 255, 255]
		self.palette_darkGrey = QtGui.QPalette()
		self.palette_darkGrey.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(66, 66, 66))

	#============================================ Complementary blues Colors # http://paletton.com	

	#========= blues Colors
		rvb_Blue1 = [97, 114, 141]
		self.palette_Blue1 = QtGui.QPalette()
		self.palette_Blue1.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(97, 114, 141))

		rvb_Blue2 = [64, 84, 115]
		self.palette_Blue2 = QtGui.QPalette()
		self.palette_Blue2.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(64, 84, 115))

		rvb_Blue3 = [43, 61, 91]
		self.palette_Blue3 = QtGui.QPalette()
		self.palette_Blue3.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(43, 61, 91))

		rvb_Blue4 = [25, 44, 75]
		self.palette_Blue4 = QtGui.QPalette()
		self.palette_Blue4.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(25, 44, 75))

		rvb_Blue5 = [10, 25, 50]
		self.palette_Blue5 = QtGui.QPalette()
		self.palette_Blue5.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(10, 25, 50))


	#========= blues Colors
		rvb_Orange1 = [255, 196, 77]
		self.palette_Orange1 = QtGui.QPalette()
		self.palette_Orange1.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 196, 77))

		rvb_Orange1 = [255, 179, 27]
		self.palette_Orange2 = QtGui.QPalette()
		self.palette_Orange2.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 179, 27))

		rvb_Orange1 = [255, 170, 0]
		self.palette_Orange3 = QtGui.QPalette()
		self.palette_Orange3.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 170, 0))

		rvb_Orange1 = [206, 137, 0]
		self.palette_Orange4 = QtGui.QPalette()
		self.palette_Orange4.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(206, 137, 0))

		rvb_Orange1 = [160, 107, 0]
		self.palette_Orange5 = QtGui.QPalette()
		self.palette_Orange5.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(160, 107, 0))

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


