#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Last Update : 23-06-2016                                                         #
# ##################################################################################

import os
import sys
import random
import glob
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import QThread
import ink
import ink.io
import ink.proto
import time
import json
import shutil
import datetime
from datetime import datetime


#========================================================================================= CLASS __QT_KBZ__ 

class __QT_KBZ__(QtGui.QDialog):
	
	def __init__(self, parent = None):
		super(__QT_KBZ__, self).__init__(parent) 

	#======================================================================================================
	#========= Globals Variables
	#======================================================================================================
		self.SCREEN 					= QtGui.QDesktopWidget().screenGeometry()
		self.CUR_USER 					= os.getenv('USER')
		self.ALL_PROJECTS	 			= 	{ \
												"gri": [71, 209, 71], 	\
												"lun": [0, 153, 255], 	\
												"dm3": [204, 51, 255], 	\
												"max": [139, 0, 0] 		\
											}
		self.CUR_PROJ_lower 			= ink.io.ConnectUserInfo()[2]
		self.CUR_PROJECT 				= self.CUR_PROJ_lower.upper()
		self.START_DIR_PUBLIC 			= '/u/'+self.CUR_PROJ_lower+'/Users/COM/Presets/Graphs/'
		# self.START_DIR_lcl_LCKD_A7 			= '/u/'+self.CUR_PROJ_lower+'/Users/cpottier/Files/etc'
		# self.START_DIR_lcl_LCKD_A7 			= '/u/'+self.CUR_PROJ_lower+'/Users/COM/Assets/'
		self.START_DIR_USERS 			= '/u/'+self.CUR_PROJ_lower+'/Users/'
		self.START_DIR_lcl_LCKD_A7 	= self.START_DIR_USERS+self.CUR_USER+'/Assets/'
		self.PATH_EXEMPLES				= '/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples'
		self.CUR_SCRIPTS_PATH			= '/u/'+self.CUR_PROJ_lower+self.PATH_EXEMPLES
		self.TMP_FILE_LCKD 				= self.CUR_PROJECT+'_A7LockedBy.tmp'
		self.TMP_PATH_FILE_LCKD 		= self.CUR_SCRIPTS_PATH+'/'+self.TMP_FILE_LCKD
		self.DIR_BACKUP	 				= '_backup'
		self.MYPREFSFILE				= self.CUR_SCRIPTS_PATH+'/kbz_prefs_'+self.CUR_USER+'.json'
		self.MYPREFSJSON				= {}
		self.MYPREFSJSON["scripts"]		= []
		if os.path.isfile(self.MYPREFSFILE) == False :
			self.write_Prefs(self.MYPREFSJSON,False)

		# if self.CUR_PROJECT 	== 'GRI':
		# 	self.HOME_COLOR = self.ALL_PROJECTS['gri']
		# if self.CUR_PROJECT 	== 'LUN':
		# 	self.HOME_COLOR = self.ALL_PROJECTS['lun']
		# if self.CUR_PROJECT 	== 'DM3':
		# 	self.HOME_COLOR = self.ALL_PROJECTS['dm3']
		# if self.CUR_PROJECT 	== 'MAX':
		# 	self.HOME_COLOR = self.ALL_PROJECTS['max']
		self.HOME_COLOR 				= self.ALL_PROJECTS[self.CUR_PROJ_lower]

		self.EXCLUDE_DIR_USERS_LCKD 	= [ \
												'COM', 			\
												'OFF', 			\
												'dm3_contrats' 	\
											]
		self.EXCL_DIR_LCKD 				= [
												self.CUR_PROJECT,
												'LIB','LIBREF',
												'MODELING',
												'PREVIZ',
												'USECASE',
												'USECASEDEV'
											]
		self.INCL_EXT_LCKD 				= 	['CSV','XML','INKGRAPH','A7']

		self.ALL_USERS 					= [] # GLOBVAR
		for root, dirnames, filenames in os.walk(self.START_DIR_USERS):
			for dirname in dirnames:
				if dirname not in self.EXCLUDE_DIR_USERS_LCKD :
					self.ALL_USERS.append(dirname)
			break
		self.ALL_USERS 					= sorted(self.ALL_USERS)
		self.ALL_USERS_COUNT 			= len(self.ALL_USERS)

	#======================================================================================================
	#========= main vlayout
	#======================================================================================================

		self.mainLayout = QtGui.QVBoxLayout()
		self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
		# self.mainLayout.setAlignment(QtCore.Qt.AlignRight) # vertical or horizontal ?

		#=============================================== Top Area container
		self.TopAreaContainer = QtGui.QWidget()
		self.TopAreaContainer.setObjectName("TopAreaContainer")
		#========= Top Area content
		self.construct_TopAreaContent()

		#============================================ Middle Area container
		self.MiddleAreaContainer = QtGui.QWidget()
		self.MiddleAreaContainer.setObjectName("MiddleAreaContainer")
		#========= Tabs Area Widget
		self.construct_MiddleTabsArea()

		#============================================ Bottom Area container
		self.BottomAreaContainer = QtGui.QWidget()
		self.BottomAreaContainer.setObjectName("BottomAreaContainer")
		#========= Bottom Area content
		self.construct_BottomAreaContent()

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

	#======================================================================
	#========= apply stylsheets
	#======================================================================
		#========= 
		self.apply_Stylesheets()
		# self.setPalette(self.palette_darkGrey)


	#======================================================================================================
	#========= check if some files exist and some other check
	#======================================================================================================
		self.check_A7_alwaysLCKD(self.TMP_PATH_FILE_LCKD)

	#======================================================================================================
	#========= get LCKD List
	#======================================================================================================
		self.on_BT_LCKDFILE_lcl_clicked(self.nameBtsee)




	# 	self.overlay = self.paintEvent(self)
	# # 	# self.overlay.hide()

	# def paintEvent(self, event):        
	# 	painter = QtGui.QPainter()
	# 	painter.begin(self)
	# 	painter.setRenderHint(QtGui.QPainter.Antialiasing)
	# 	painter.fillRect(event.rect(), QtGui.QBrush(QtGui.QColor(255, 255, 0, 127)))
	# 	painter.drawLine(self.width()/8, self.height()/8, 7*self.width()/8, 7*self.height()/8)
	# 	painter.drawLine(self.width()/8, 7*self.height()/8, 7*self.width()/8, self.height()/8)
	# 	painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))  


	#======================================================================================================
	#========= UI Areas Constructions Functions
	#======================================================================================================

	def construct_TopAreaContent(self):
		'''   '''
		#========= Top Area content
		self.TopAreaContent = QtGui.QHBoxLayout()
		self.TopAreaContent.setObjectName("TopAreaContent")

		#========= Top Area content button
		txtBt = '<- BACK '
		self.BT_BACK_HOME = QtGui.QPushButton(txtBt)
		self.BT_BACK_HOME.setVisible(False)

		txtBt = 'SCRIPTS ' + self.CUR_PROJECT
		self.BT_HOME_SCRIPTS = QtGui.QPushButton(txtBt)
		name1 = 'BT_HOME_SCRIPTS'
		self.BT_HOME_SCRIPTS.setObjectName(name1)
		self.BT_HOME_SCRIPTS.installEventFilter(self)

		txtBt = 'BT2 ' + self.CUR_PROJECT
		self.BT_MAIN_2 = QtGui.QPushButton(txtBt)
		name2 = 'BT_MAIN_2'
		self.BT_MAIN_2.setObjectName(name2)
		self.BT_MAIN_2.clicked.connect(lambda : self.on_BT_MAIN_clicked(name2))
		self.BT_MAIN_2.installEventFilter(self)

		txtBt = 'BT3 ' + self.CUR_PROJECT
		self.BT_MAIN_3 = QtGui.QPushButton(txtBt)
		name3 = 'BT_MAIN_3'
		self.BT_MAIN_3.setObjectName(name3)
		self.BT_MAIN_3.clicked.connect(lambda : self.on_BT_MAIN_clicked(name3))
		self.BT_MAIN_3.installEventFilter(self)

		#================================================== add button to Top Area content
		self.TopAreaContent.addWidget(self.BT_BACK_HOME)
		self.TopAreaContent.addWidget(self.BT_HOME_SCRIPTS)
		self.TopAreaContent.addWidget(self.BT_MAIN_2)
		self.TopAreaContent.addWidget(self.BT_MAIN_3)

		#========= add Area content to Top Area container
		self.TopAreaContainer.setLayout(self.TopAreaContent)

		#========= apply stylsheets
		self.apply_Stylesheets()
		# self.setPalette(self.palette_darkGrey)


	def construct_MiddleTabsArea(self):
		'''   '''
		#=======================================================================================
		#=========================== Middle Area content
		#=======================================================================================
		self.MiddleTabsContent = QtGui.QHBoxLayout()
		self.MiddleTabsContent.setObjectName("MiddleTabsContent")

		#==========================================================================
		#=========================== Tabs Areas Widget
		#==========================================================================
		self.MiddleTabsArea = QtGui.QTabWidget()
		self.MiddleTabsArea.setTabPosition(QtGui.QTabWidget.North)
		self.MiddleTabsArea.setObjectName("MiddleTabsArea")

		#==================================================
		#=========================== Tab1	
		#==================================================

		#=========================== FileSystem

		self.modelTab1 = QtGui.QFileSystemModel()
		# self.modelTab1.setFilter(QtCore.QDir.AllEntries | QtCore.QDir.AllEntries)
		self.modelTab1.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)			

		# self.modelTab1.setRootPath(self.START_DIR_PUBLIC)
		self.modelTab1.setRootPath(self.START_DIR_lcl_LCKD_A7)
		

		#=========================== Treeview
		self.Tab1 = QtGui.QTreeView()
		# self.connect(self.Tab1, QtCore.SIGNAL("itemClicked (QTreeWidgetItem *,int)"), self.on_TAB_clicked)
		self.Tab1.connect(self.Tab1, QtCore.SIGNAL('clicked(QModelIndex)'), self.Expand_GetLCKD)
		self.Tab1.objectName = "Tab1"
		self.Tab1.setAlternatingRowColors(True)

		#=========================== populate tab1
		self.Tab1.setModel(self.modelTab1)
		self.Tab1.setRootIndex(self.modelTab1.index(self.START_DIR_lcl_LCKD_A7))
		self.Tab1.resizeColumnToContents(0)
		# self.fileTreeView.header().setResizeMode(QHeaderView.ResizeToContents)		
		self.Tab1.setColumnWidth(0, 400)


		#==================================================
		#=========================== Tab2	
		#==================================================

		#=========================== FileSystem
		self.modelTab2 = QtGui.QFileSystemModel()
		self.modelTab2.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)					
		self.modelTab2.setRootPath(self.START_DIR_PUBLIC)

		#=========================== Treeview
		self.Tab2 = QtGui.QTreeView()
		self.connect(self.Tab1, QtCore.SIGNAL("itemClicked (QTreeWidgetItem *,int)"), self.on_TAB_clicked)
		self.Tab2.objectName = "Tab2"
		self.Tab1.setAlternatingRowColors(True)

		#=========================== populate tab2
		self.Tab2.setModel(self.modelTab2)
		self.Tab2.setRootIndex(self.modelTab2.index(self.START_DIR_PUBLIC))
		self.Tab2.resizeColumnToContents(0)
		self.Tab2.setColumnWidth(0, 400)		

		#==================================================
		#=========================== Tab x
		#==================================================


		#========================================================================= add Tabs to MiddleTabsArea
		self.MiddleTabsArea.addTab(self.Tab1, ' Local a7 ')
		self.MiddleTabsArea.addTab(self.Tab2, ' Public a7 ')

		#========================================================== add MiddleTabsArea to Middle Area content
		self.MiddleTabsContent.addWidget(self.MiddleTabsArea)

		#========================================================== add Area content to middle Area container
		self.MiddleAreaContainer.setLayout(self.MiddleTabsContent)

		#========= apply stylsheets
		self.apply_Stylesheets()



	def construct_BottomAreaContent(self):
		'''   '''
		w1 = 200
		h1 = 30

		#========= Bottom Area content
		self.BottomAreaContent = QtGui.QGridLayout()
		self.BottomAreaContent.setObjectName("BottomAreaContent")

		#========= Container logins
		self.listUsers = QtGui.QComboBox()
		self.listUsers.setFixedWidth(w1)
		self.listUsers.setFixedHeight(h1)
		for user in self.ALL_USERS:
			self.listUsers.addItem(user)
		index = self.listUsers.findText(self.CUR_USER, QtCore.Qt.MatchFixedString)
		self.listUsers.setCurrentIndex(index)

		#========= Bottom Area content Buttons
		txtBt = 'See LCKD | Never Published A7'
		self.BT_SEE_LCKDFILE_lcl = QtGui.QPushButton(txtBt)
		self.nameBtsee = 'BT_SEE_LCKDFILE_lcl'
		self.BT_SEE_LCKDFILE_lcl.setObjectName(self.nameBtsee)
		self.BT_SEE_LCKDFILE_lcl.clicked.connect(lambda : self.on_BT_LCKDFILE_lcl_clicked(self.nameBtsee))
		# self.BT_SEE_LCKDFILE_lcl.installEventFilter(self)		
		self.BT_SEE_LCKDFILE_lcl.setFixedSize(w1,h1)

		txtBt = 'Clear Locked A7 Infos'
		self.BT_CLEAR_LCKDFILE_lcl = QtGui.QPushButton(txtBt)
		self.nameBtclear = 'BT_CLEAR_LCKDFILE_lcl'
		self.BT_CLEAR_LCKDFILE_lcl.setObjectName(self.nameBtclear)
		self.BT_CLEAR_LCKDFILE_lcl.clicked.connect(lambda : self.on_BT_LCKDFILE_lcl_clicked(self.nameBtclear))
		self.BT_CLEAR_LCKDFILE_lcl.setFixedSize(w1,h1)

		txtChk = 'Full Search (All Users / by Folders)'
		self.CHK_SEARCH_ALL = QtGui.QCheckBox(txtChk)
		nameChkAll = 'CHK_SEARCH_ALL'
		self.CHK_SEARCH_ALL.setObjectName(nameChkAll)

		txtCpClipbrd = 'Copy to clipboard'
		self.CHKCP_CLIPBRD = QtGui.QCheckBox(txtCpClipbrd)
		nameCopyClipboard = 'CHKCP_CLIPBRD'
		self.CHKCP_CLIPBRD.setObjectName(nameCopyClipboard)
		self.CHKCP_CLIPBRD.stateChanged.connect(self.on_CHKCP_CLIPBRD)
		self.CHKCP_CLIPBRD.setVisible(False)

		#========= checkbox stylesheet , to do better , in fct stylsheet
		self.CHK_SEARCH_ALL.setStyleSheet("color: white")
		self.CHK_SEARCH_ALL.show()
		self.CHKCP_CLIPBRD.setStyleSheet("color: white")
		self.CHKCP_CLIPBRD.show()


		#================================================== add LockedFilesListing and bt		

		#========= Bottom Area content LckdFiles
		self.LckdFiles = QtGui.QTextEdit()
		self.LckdFiles.setObjectName("LckdFiles")		
		self.LckdFiles.setFixedWidth(self.SCREEN.width()-40)
		self.LckdFiles.setFixedHeight(1)		
		self.LckdFiles.setSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
		self.LckdFilesSb = self.LckdFiles.verticalScrollBar()
		self.LckdFilesSb.setValue(self.LckdFilesSb.maximum())
		self.LckdFilesCursor = self.LckdFiles.textCursor()
		self.LckdFiles.setVisible(False)

		#================================================== add Users Bottom Area content
		self.BottomAreaContent.addWidget(self.listUsers)
		# self.BottomAreaContent.addWidget(self.editUserBottom)
		#================================================== add LCKD Buttons to Bottom Area content
		self.BottomAreaContent.addWidget(self.BT_SEE_LCKDFILE_lcl)
		self.BottomAreaContent.addWidget(self.BT_CLEAR_LCKDFILE_lcl)
		self.BottomAreaContent.addWidget(self.CHK_SEARCH_ALL)
		self.BottomAreaContent.addWidget(self.CHKCP_CLIPBRD)
		
		#================================================== add LckdFiles to Bottom Area content
		self.BottomAreaContent.addWidget(self.LckdFiles)

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
		scripts = self.list_Scripts()
		n = 0
		for script in scripts:
			if '.pyc' not in str(script) and '.py~' not in str(script) and '__init__.py' not in str(script) and '_kbz.json' not in str(script):
				if '.py' in str(script) or '.txt' in str(script) or '.json' in str(script) or '.py' in str(script) or '.mel' in str(script) or '.xml' in str(script) or '.csv' in str(script) or '.bat' in str(script) or '.db' in str(script):
					n = n+1
					item = QtGui.QStandardItem(script)
					item.setCheckable(True)
					status_checked = QtCore.Qt.Unchecked
					if n%2 == 0 :
						item.setBackground(QtGui.QColor(self.QStandardItem_Color1))
						# item.setColor(allBlueAndShiny color)
						# item.setForeground(QtGui.QColor('red')) # text color
					else:
						item.setBackground(QtGui.QColor(self.QStandardItem_Color2))
					if str(script) in myChecked:
						status_checked = QtCore.Qt.Checked
						item.setBackground(QtGui.QColor(self.QStandardItem_Color3))
					item.setCheckState(status_checked)

					#========= item Signal
					# # item.emit(QtCore.SIGNAL("self.populate_prefs('scripts')"))
					# item.itemChanged.connect(self.populate_prefs)

					#================================================== add ckecked to List Area content
					self.ScriptsAreaContent.appendRow(item)

		#========= add Area content to Scripts content
		self.ScriptsAreaContainer.setModel(self.ScriptsAreaContent)

		#=========  bt sync
		msg_others_projects = ''
		for p in self.ALL_PROJECTS:
			if str(p).upper != self.CUR_PROJECT.upper():
				msg_others_projects = msg_others_projects + ' | ' + str(p)
		txtBt = 'Click Here to SYNC SCRIPTS ' + self.CUR_PROJECT + ' -> to ' + msg_others_projects + ' | Projects'
		self.BT_SYNC_SCRIPTS = QtGui.QPushButton(txtBt)
		self.BT_SYNC_SCRIPTS.setObjectName("BT_SYNC_SCRIPTS")
		self.BT_SYNC_SCRIPTS.setVisible(True)
		self.BT_SYNC_SCRIPTS.installEventFilter(self)

		#=========  connect fct
		self.ScriptsAreaContent.itemChanged.connect(self.populate_prefs_scripts)

	#======================================================================================================
	#========= Apply stylsheets
	#======================================================================================================
		self.apply_Stylesheets()



	#======================================================================================================
	#========= Functions
	#======================================================================================================
	
	def Expand_GetLCKD(self, index):
		'''   '''
		model = self.modelTab1
		indexItem = model.index(index.row(), 0, index.parent())
		fileName = model.fileName(indexItem)
		filePath = model.filePath(indexItem)
		n_users_real = []

		if self.CHK_SEARCH_ALL.isChecked() == True:	
			startTime = datetime.now()
			
			# first pass to get users real concerned
			n_user = 0
			for USERtoSEARCH in self.ALL_USERS:
				try:
					filePathFromList = filePath.replace(self.CUR_USER,USERtoSEARCH)
					if os.path.exists(filePathFromList):
						n_user += 1
						n_users_real.append(str(n_user))
				except:
					pass

			n_users_tot = len(n_users_real)

			# get LCKD list through thread
			n_user = 0
			for USERtoSEARCH in self.ALL_USERS:
				try:
					filePathFromList = filePath.replace(self.CUR_USER,USERtoSEARCH)					
					if os.path.exists(filePathFromList):
						n_user += 1
						self.Thread_Instance_mutu(filePathFromList, USERtoSEARCH, n_user, n_users_real, n_users_tot)
						n_users_real.remove(str(n_user))
						msg = str(n_user) + ' | ' + str(n_users_tot) + ' - ' + str(USERtoSEARCH) + '\n'
						self.printSTD(str(msg))
				except:
					msg = '################' + filePathFromList + '[ ERROR ] ######################\n'
					self.printSTD(msg)
					pass


			FPusersToSearch_msg = filePath.replace(self.CUR_USER,'USER_A->Z')

			msg = datetime.now() - startTime
			msg = ' ARMAGEDON SEARCH [ '+FPusersToSearch_msg+' ] LCKD FILES LAUNCHED in ' + str(msg) + ' ... Please Wait !\n'

			self.printSTD(' ')
			self.printSTD('\n###########################################################################################')
			self.printSTD(' ')			
			self.printSTD(msg)
			self.printSTD(' ')	
			self.printSTD('#############################################################################################\n')
			self.printSTD(' ')

		else:
			n_user = 1
			n_users_real.append(str(n_user))
			n_users_tot = len(n_users_real)
			self.LckdFilesCursor.movePosition(QtGui.QTextCursor.End)

			getText = self.LckdFiles.toPlainText()
			USERtoSEARCH = self.listUsers.currentText()
			self.printSTD(USERtoSEARCH)
			if str(USERtoSEARCH) != self.CUR_USER:
				filePath = filePath.replace(self.CUR_USER,USERtoSEARCH)

			self.BT_SEE_LCKDFILE_lcl.setVisible(False)
			result = 0
			try:
	 			result = self.readlines_files(self.TMP_PATH_FILE_LCKD)[0]
	 		except:
	 			pass
			if result > 0 : # todo to mutu
				self.BT_SEE_LCKDFILE_lcl.setVisible(True)
				self.on_BT_LCKDFILE_lcl_clicked(self.nameBtsee)

			self.Thread_Instance_mutu(filePath, USERtoSEARCH, n_user, n_users_real, n_users_tot)


	def Thread_Instance_mutu(self, filePath, USERtoSEARCH, n_user, n_users_real, n_users_tot):
		'''   '''
		if os.path.exists(filePath):
			self.printSTD(filePath)
			MY_Thread_Instance = Thread_Instance( \
				unicode(filePath), \
				str(USERtoSEARCH), \
				self.CUR_PROJECT, \
				self.EXCL_DIR_LCKD, \
				self.INCL_EXT_LCKD, \
				self.TMP_PATH_FILE_LCKD, \
				self.CHK_SEARCH_ALL, \
				n_user, n_users_real, \
				n_users_tot \
				)


	def model_changeColor(self, model):
		model.setData(model.index(1, 5), 1)
		model.setData(model.index(2, 5), 2)
		model.emit(QtCore.SIGNAL('dataChanged(QModelIndex,QModelIndex)'), model.index(1, 5), model.index(2, 5))

	def get_fileList(self, source):
		matches = []
		for root, dirnames, filenames in os.walk(source, topdown=False, onerror=None, followlinks=False):
			if not dirnames:      
				for filename in filenames:
					ext = None
					try:
						ext = os.path.splitext(filename)[1][1:]
					except:
						pass  
					if ext.upper() in self.INCL_EXT_LCKD:
						filePath  = os.path.join(root, filename)
						result    = self.get_fileInfo(filePath)
						infoWrite   = result[0]
						infoOwner   = result[1]
						self.printSTD('####################')
						self.printSTD(infoWrite)
						self.printSTD(infoOwner)
						self.printSTD('####################')
						if infoWrite == True and infoOwner == self.CUR_USER:
							matches.append(os.path.join(root, filename))

		return matches


	def get_fileInfo(self, source):
		fileInfo   = QtCore.QFileInfo(source)
		infoWrite = fileInfo.isWritable()
		infoOwner = fileInfo.owner()
		return infoWrite, infoOwner


	def readlines_files(self,_filepath):
		result 	= 0
		lines 	= []
		try:
			with open(_filepath) as f:
				result = sum(1 for _ in f)
			for line in open(_filepath):
				lines.append(line)
		except:
			result = 0
			lines = ['.']
			pass
		return result,lines


	def check_A7_alwaysLCKD(self, _filepathTmpFile):	
		'''   '''	
		if not os.path.exists(_filepathTmpFile):
			# open(_filepathTmpFile, 'a').close()
			f = open(self.TMP_PATH_FILE_LCKD,'a')
			open(_filepathTmpFile, 'a')
			f.write('.\n') # python will convert \n to os.linesep
			f.close()

		else:
			USERtoSEARCH = self.listUsers.currentText()
			matches = []
			try:
				result 	= self.readlines_files(_filepathTmpFile)
				nA7 	= result[0]
				lines 	= result[1]
			except:
				nA7 	= 0
				lines 	= ['.']

			if nA7 > 0 :
				for line in lines:
					filePath = str(line[:-1])
					ext = None

					try:
						ext = filePath.split('.')[1]
					except:
						pass	

					try:					
						if ext.upper() in self.INCL_EXT_LCKD:
							# we check chmod
							result 		= self.get_fileInfo(filePath)
							infoWrite 	= result[0]
							infoOwner 	= result[1]
							if infoWrite == True :
								matches.append(filePath)								
								msg = filePath + ' [ LCKD ]'
					except:
						pass

			if len(matches) > 0:
				# we re write tmp file
				self.on_BT_LCKDFILE_lcl_clicked('BT_CLEAR_LCKDFILE_lcl')		
				# time.sleep(0.8)			
				for line in matches:
					time.sleep(0.1)	
					a7 = str(line)+'\n'
					f = open(self.TMP_PATH_FILE_LCKD,'a')
					f.write(line+'\n') # python will convert \n to os.linesep
					f.close()
				# update textarea
				self.update_TMP_PATH_FILE_LCKD()


	def update_TMP_PATH_FILE_LCKD(self): 
		BottomContent = self.LckdFiles.toPlainText()
		try:
			lines = [line.rstrip('\n') for line in open(self.TMP_PATH_FILE_LCKD)]
		except:
			lines = ['.']
		if len(lines[0])>0: # 1 is point trick to do better

			self.LckdFiles.setVisible(True)
			self.CHKCP_CLIPBRD.setVisible(True)

			for line in lines:
				if str(line) not in str(BottomContent) and len(line)>10: # 10 is path lenght, arbitrary

					self.LckdFilesCursor.movePosition(QtGui.QTextCursor.End)
					self.LckdFiles.insertPlainText(str(line)+'\n')

			self.BT_SEE_LCKDFILE_lcl.setVisible(False)

			# REFRESH BOTTOM TO DO

	#======================================================================================================
	#========= UI Buttons Functions
	#======================================================================================================

	def confirmBox(self,title,msg=''):    
		reply = QtGui.QMessageBox.question(self, title, msg,
		QtGui.QMessageBox.Ok  | QtGui.QMessageBox.Cancel)
		if reply == QtGui.QMessageBox.Ok:
			self.printSTD('\n[ SYNC '+self.CUR_PROJECT+' Script(s) Confirmed ]\n')
			self.on_BT_SYNC_SCRIPTS_clicked()
		else:
			self.printSTD('\n[ SYNC '+self.CUR_PROJECT+' Script(s) Canceled ]\n')

	def back_to_HOME(self):
		self.show_BT_HOME()
		self.delete_TopAndMiddle()
		self.Construct_TopAndMiddle()
		self.on_BT_LCKDFILE_lcl_clicked('BT_SEE_LCKDFILE_lcl')


	def show_BT_HOME(self):
		self.BT_BACK_HOME.setVisible(False)
		self.BT_HOME_SCRIPTS.setVisible(True)
		self.BT_MAIN_2.setVisible(True)
		self.BT_MAIN_3.setVisible(True)
		self.BT_SYNC_SCRIPTS.setVisible(False)

	def hide_BT_HOME(self):
		self.BT_BACK_HOME.setVisible(True)
		self.BT_BACK_HOME.clicked.connect(self.on_BT_BACK_HOME_clicked)
		self.BT_HOME_SCRIPTS.setVisible(False)
		self.BT_MAIN_2.setVisible(False)
		self.BT_MAIN_3.setVisible(False)
		# self.BT_SYNC_SCRIPTS.setVisible(False)

	def on_BT_BACK_HOME_clicked(self):
		self.back_to_HOME()

	def on_BT_MAIN_clicked(self,BT):
		if BT == "BT_HOME_SCRIPTS":
			self.hide_BT_HOME()
			self.delete_TopAndMiddle()
			self.Construct_MiddleScript()
		# if BT == "BT_MAIN_2":
		# 	self.delete_TopAndMiddle()
		# 	self.Construct_TopAndMiddle()
		# if BT == "BT_MAIN_3":
		# 	self.delete_TopAndMiddle()
		# 	self.Construct_TopAndMiddle()

	def on_BT_SYNC_SCRIPTS_clicked(self):
		'''   '''

		def applyUI_OK():
			'''   '''
			modelScript = self.ScriptsAreaContent
			colIndex = 0
			nRows = modelScript.rowCount()
			# self.printSTD(nRows)
			for n in range(nRows):
				Item_QModelIndex = modelScript.index(n, colIndex)
				# self.printSTD(Item_QModelIndex)
				# self.printSTD('------------------------')
				# item = Item_QModelIndex.data # return <built-in method data of QModelIndex object at 0x6102140>
				# self.printSTD(item)
				# item = Item_QModelIndex.data() # return default Qt.DisplayRole = .data(QtCore.Qt.DisplayRole) = text
				# self.printSTD(item)
				itemChecked = Item_QModelIndex.data(QtCore.Qt.CheckStateRole) # 
				if itemChecked == 2: # checked
					# self.printSTD('------------------------')
					# self.printSTD(itemChecked)
					# Item_QModelIndex.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(0, 0, 0)) 
					# ne retourne pas d erreur
					# role = Item_QModelIndex.data(QtCore.Qt.BackgroundRole)  # ne retourne pas d erreur
					# self.printSTD(role)  # ne retourne pas d erreur
					modelScript.setData(
					modelScript.index(n, colIndex),
					QtGui.QColor(QtCore.Qt.green),
					QtCore.Qt.BackgroundColorRole
					)

		#====================================================================== Fin Scripts


		# now = datetime.datetime.now()
		now = datetime.now()
		date = now.strftime("%Y%m%d-%H-%M-%S")

		array_scriptToSync = []
		myPrefs = json.load(open(self.MYPREFSFILE))

		for v in myPrefs["scripts"]:
			array_scriptToSync.append(v)

		for ap in self.ALL_PROJECTS:
			DIR_DISTANT_BACKUP = '/u/'+ap+self.PATH_EXEMPLES+'/'+self.DIR_BACKUP
			if not os.path.exists(DIR_DISTANT_BACKUP):
				os.makedirs(DIR_DISTANT_BACKUP)
			APU = str(ap).upper()
			ap 	= str(ap).lower()		

			if str(self.CUR_PROJ_lower) != str(ap):
				msg = '---------------------------------- SYNC SCRIPTS ' + self.CUR_PROJECT + ' -> ' + APU
				self.printSTD(' ')
				self.printSTD('-----------------------------------------------------------------------')
				self.printSTD(str(msg))
				self.printSTD('-----------------------------------------------------------------------\n\n')
				for s in array_scriptToSync:
					checkCopy 	= False
					filename 	= s.split('.')[0]
					ext 	 	= s.split('.')[1]
					sbackup 	= filename+'_'+date+'.'+ext
					path_lcl 			= '/u/'+self.CUR_PROJ_lower+self.PATH_EXEMPLES+'/'+s
					path_distant 		= '/u/'+ap+self.PATH_EXEMPLES+'/'+s
					path_distant_backup = DIR_DISTANT_BACKUP+'/'+sbackup
					self.printSTD(path_lcl)					
					self.printSTD('->')
					self.printSTD(path_distant)
					try:
						if os.path.isfile(path_lcl):
		#========= 1 - FIRST , IMPORTANT backup distant file before copy
							if os.path.isfile(path_distant):
								shutil.copyfile(path_distant, path_distant_backup)
							if not os.path.isfile(path_distant):
								self.printSTD('---[ NEW FILE ]---')
								checkCopy = True

		#========= 2 -copy sync
							shutil.copyfile(path_lcl, path_distant)
							if os.path.isfile(path_lcl) and os.path.isfile(path_distant) and os.path.isfile(path_distant_backup) and checkCopy == False:	
								applyUI_OK()									
								self.printSTD('[ SYNC OK ]')
							if os.path.isfile(path_lcl) and os.path.isfile(path_distant) and checkCopy == True:	
								applyUI_OK()	
								self.printSTD('[ COPY OK ]')
							if not os.path.isfile(path_distant) and not os.path.isfile(path_distant_backup) and checkCopy == False:
								self.printSTD('[ SYNC ERROR ]')

					except:
						self.printSTD('[ SYNC ERROR ]')

					self.printSTD('-----------------------------------------------------------------------\n')

				msg = '\nEND ' + msg
				self.printSTD(str(msg))

		#========= write liste , for secu, to do better
		self.write_Prefs(myPrefs,False)


	def eventFilter(self, object, event):
		name = object.objectName()
		
		#========= Mouse Click

		if event.type() == QtCore.QEvent.MouseButtonPress:
			if str(name)=='BT_HOME_SCRIPTS':
				self.on_BT_MAIN_clicked(name)
			if str(name)=='BT_SYNC_SCRIPTS':
				# self.on_BT_SYNC_SCRIPTS_clicked()
				self.confirmBox('Confirm Sync')
			return True

		#========= Mouse Over

		if event.type() == QtCore.QEvent.HoverEnter:

			r = self.HOME_COLOR[0]
			g = self.HOME_COLOR[1]
			b = self.HOME_COLOR[2]
			hexColorHome = self.rvbToHex(r, g, b)

			if str(name)=='BT_SYNC_SCRIPTS':
				hexColor = self.rvbToHex(25, 44, 50)
				object.setStyleSheet(
								"color: white;"
								"background-color: "+hexColorHome+";"
								"selection-color: yellow;"
								"selection-background-color: blue;"
								"font: bold 14px;"
								"border-style: outset;"
								"border-radius: 16px;"
								"height: 40px;"						
								"max-width: 600px;"
								)
			else:

				object.setStyleSheet(
								"color: white;"
								"background-color: "+hexColorHome+";"
								"selection-color: yellow;"
								"selection-background-color: blue;"
								"font: bold 14px;"
								"border-style: outset;"
								"height: 40px;"
								"border-radius: 16px;"
								)

			return True

		#========= Mouse Out

		if event.type() == QtCore.QEvent.HoverLeave:
			hexColor = self.rvbToHex(25, 44, 50)
			if str(name)=='BT_SYNC_SCRIPTS':
				object.setStyleSheet(
								"color: white;"
								"background-color: "+hexColor+";"
								"selection-color: yellow;"
								"selection-background-color: blue;"
								"font: bold 14px;"
								"border-style: outset;"
								"border-radius: 16px;"
								"height: 40px;"						
								"max-width: 600px;"
								)

			else:
				object.setStyleSheet(
								"color: white;"
								"background-color: "+hexColor+";"
								"selection-color: yellow;"
								"selection-background-color: blue;"
								"font: bold 14px;"
								"border-style: outset;"
								"height: 40px;"
								"border-radius: 16px;"
								)
			return True

		#========= Mouse ClicK

		# if event.type() == QtCore.QEvent.HoverLeave:
		# 	hexColor = self.rvbToHex(25, 44, 50)
		# 	object.setStyleSheet(
		# 						"color: white;"
		# 						"background-color: "+hexColor+";"
		# 						"selection-color: yellow;"
		# 						"selection-background-color: blue;"
		# 						"font: bold 14px;"
		# 						"border-style: outset;"
		# 						"height: 40px;"
		# 						)
		# 	return True

		#========= 

		return False




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
		self.mainLayout.addWidget(self.BT_SYNC_SCRIPTS, QtCore.Qt.AlignRight)




	def on_CHKCP_CLIPBRD(self):
		'''   '''

		cb = QtGui.QApplication.clipboard() # todo copy bt
		cb.clear(mode=cb.Clipboard )			
		txtClipBoard = cb.text()
		txtClipBoard = ''

		# BottomContent = self.LckdFiles.toPlainText()	

		if self.CHKCP_CLIPBRD.isChecked():
			try:
				lines = [line.rstrip('\n') for line in open(self.TMP_PATH_FILE_LCKD)]
			except:
				lines = ['.']
			if len(lines[0])>0: # 0 is point trick, to do better
				for line in lines:
					if len(line)>10: # 10 is path lenght, arbitrary
						self.LckdFilesCursor.movePosition(QtGui.QTextCursor.End)
						txtClipBoard = str(line) +'\n'+ str(txtClipBoard)

				txtClipBoard = txtClipBoard[:-2]

				cb.setText(txtClipBoard, mode=cb.Clipboard)
				self.LckdFiles.selectAll()

		else:
			cb.setText(txtClipBoard, mode=cb.Clipboard)
			# unSelectAll
			my_text_cursor = self.LckdFiles.textCursor()
			my_text_cursor.clearSelection()
			self.LckdFiles.setTextCursor(my_text_cursor)			


	def on_BT_LCKDFILE_lcl_clicked(self,name):
		'''   '''
		if str(name)=='BT_CLEAR_LCKDFILE_lcl':
			open(self.TMP_PATH_FILE_LCKD, 'w').close()
			time.sleep(1)
			f = open(self.TMP_PATH_FILE_LCKD,'a')
			f.write('.\n') # python will convert \n to os.linesep
			f.close()
			self.LckdFiles.setVisible(True)
			self.LckdFiles.setText('')

		if str(name)=='BT_SEE_LCKDFILE_lcl':

			self.LckdFiles.setFixedHeight(200)
			self.LckdFiles.setSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
			self.LckdFilesCursor.movePosition(QtGui.QTextCursor.End)

			

			# to mutu 
			self.update_TMP_PATH_FILE_LCKD()


			# BottomContent = self.LckdFiles.toPlainText()
			# lines = [line.rstrip('\n') for line in open(self.TMP_PATH_FILE_LCKD)]

			# if len(lines[0])>10: # 10 is path lenght, arbitrary

			# 	self.LckdFiles.setVisible(True)
			# 	self.CHKCP_CLIPBRD.setVisible(True)

			# 	for line in lines:
			# 		# to mutu 
			# 		if str(line) not in str(BottomContent):	

			# 			self.LckdFilesCursor.movePosition(QtGui.QTextCursor.End)
			# 			self.LckdFiles.insertPlainText(str(line)+'\n')

			# 	self.BT_SEE_LCKDFILE_lcl.setVisible(False)


	#======================================================================
	#========= Others Functions
	#======================================================================

	def list_Scripts(self):
		scripts = os.listdir(self.CUR_SCRIPTS_PATH)
		return scripts

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


	#======================================================================================================
	#========= StyleSheets
	#======================================================================================================

	def rvbToHex(self,r,g,b):
		# r = array_rgb[1], g=array_rgb[2], b=array_rgb[3]
		hexColor = '#%02x%02x%02x' % (r, g, b)
		return hexColor


	def apply_Stylesheets(self):

	#======================================================= Globals Colors

	#========= general Colors	
		self.rvb_White = [255, 255, 255]
		self.palette_White = QtGui.QPalette()
		self.palette_White.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 255, 255))

		self.rvb_Black = [0, 0, 0]
		self.palette_Black = QtGui.QPalette()
		self.palette_Black.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(0, 0, 0))

		self.rvb_Grey = [128, 128, 128]
		self.palette_Grey = QtGui.QPalette()
		self.palette_Grey.setColor(QtGui.QPalette.Background,QtCore.Qt.gray)

		self.rvb_hellGrey = [230, 230, 230]
		self.palette_hellGrey = QtGui.QPalette()
		self.palette_hellGrey.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(128, 128, 128))

		self.rvb_darkGrey = [255, 255, 255]
		self.palette_darkGrey = QtGui.QPalette()
		self.palette_darkGrey.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(66, 66, 66))

	#============================================ Complementary blues Colors # http://paletton.com	

	#========= blues Colors
		self.rvb_Blue1 = [97, 114, 141]
		self.palette_Blue1 = QtGui.QPalette()
		self.palette_Blue1.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(97, 114, 141))

		self.rvb_Blue2 = [64, 84, 115]
		self.palette_Blue2 = QtGui.QPalette()
		self.palette_Blue2.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(64, 84, 115))

		self.rvb_Blue3 = [43, 61, 91]
		self.palette_Blue3 = QtGui.QPalette()
		self.palette_Blue3.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(43, 61, 91))

		self.rvb_Blue4 = [25, 44, 75]
		self.palette_Blue4 = QtGui.QPalette()
		self.palette_Blue4.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(25, 44, 75))

		self.rvb_Blue5 = [10, 25, 50]
		self.palette_Blue5 = QtGui.QPalette()
		self.palette_Blue5.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(10, 25, 50))


	#========= blues Colors
		self.rvb_Orange1 = [255, 196, 77]
		self.palette_Orange1 = QtGui.QPalette()
		self.palette_Orange1.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 196, 77))

		self.rvb_Orange2 = [255, 179, 27]
		self.palette_Orange2 = QtGui.QPalette()
		self.palette_Orange2.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 179, 27))

		self.rvb_Orange3 = [255, 170, 0]
		self.palette_Orange3 = QtGui.QPalette()
		self.palette_Orange3.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(255, 170, 0))

		self.rvb_Orange4 = [206, 137, 0]
		self.palette_Orange4 = QtGui.QPalette()
		self.palette_Orange4.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(206, 137, 0))

		self.rvb_Orange5 = [160, 107, 0]
		self.palette_Orange5 = QtGui.QPalette()
		self.palette_Orange5.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(160, 107, 0))


	#========= Tab QStandardItem  Colors
		self.QStandardItem_Color1 = QtGui.QColor(255, 255, 255)
		self.QStandardItem_Color2 = QtGui.QColor(217, 230, 240)
		self.QStandardItem_Color3 = QtGui.QColor(179, 255, 102)

	#========= other samples
		# pal.setColor(QtGui.QPalette.ColorRole(9),QtGui.QColor("#4B4B4B"))
		# pal.setColor(QtGui.QPalette.ColorRole(6),QtGui.QColor("#CCCCCC"))
		# self.BT_HOME_SCRIPTS.setStyleSheet('QPushButton {background-color: '+hexColor+'; color: white; height: 40px;}')

	#========= Style Main
		self.setPalette(self.palette_darkGrey)

	#========= Style Buttons

		#====================================== Main Home  Buttons
		hexColor = self.rvbToHex(25, 44, 50)
		

		self.BT_HOME_SCRIPTS.setStyleSheet(
								"color: white;"
								"background-color: "+hexColor+";"
								"selection-color: yellow;"
								"selection-background-color: blue;"
								"font: bold 14px;"
								"border-style: outset;"
								"height: 40px;"
								"border-radius: 16px;"
							)
		self.BT_MAIN_2.setStyleSheet(
								"color: white;"
								"background-color: "+hexColor+";"
								"selection-color: yellow;"
								"selection-background-color: blue;"
								"font: bold 14px;"
								"border-style: outset;"
								"height: 40px;"
								"border-radius: 16px;"								
							)
		self.BT_MAIN_3.setStyleSheet(
								"color: white;"
								"background-color: "+hexColor+";"
								"selection-color: yellow;"
								"selection-background-color: blue;"
								"font: bold 14px;"
								"border-style: outset;"
								"height: 40px;"
								"border-radius: 16px;"
							)

		# #========= Top Back to Home  Button
		r = self.HOME_COLOR[0]
		g = self.HOME_COLOR[1]
		b = self.HOME_COLOR[2]
		hexColor = self.rvbToHex(r, g, b)
		
		self.BT_BACK_HOME.setStyleSheet(
								"color: white;"
								"background-color: "+hexColor+";"
								"selection-color: yellow;"
								"selection-background-color: blue;"
								"font: bold 14px;"
								"border-style: outset;"
								"height: 40px;"
							)

		#======================================= lcl TAB

		#========= LCKD  Buttons lcl tab
		try:

			#========= sync script lcl tab
			hexColor = self.rvbToHex(25, 44, 50)
			hexColorBg = self.rvbToHex(self.rvb_darkGrey[0], self.rvb_darkGrey[1], self.rvb_darkGrey[2])
			hexColorBorder = self.rvbToHex(self.HOME_COLOR[0], self.HOME_COLOR[1], self.HOME_COLOR[2])
			self.BT_SYNC_SCRIPTS.setStyleSheet(
												"color: white;"
												"background-color: "+hexColor+";"
												"selection-color: yellow;"
												"selection-background-color: blue;"
												"font: bold 14px;"
												"border-style: outset;"
												"border-radius: 16px;"
												"height: 40px;"						
												"max-width: 600px;"
											)
			#========= loked file lcl tab
			self.BT_SEE_LCKDFILE_lcl.setStyleSheet(
												"color: white;"
												"background-color: "+hexColor+";"
												"selection-color: yellow;"
												"selection-background-color: blue;"
												"font: bold 10px;"
												"border-style: outset;"
												"height: 15px;"
								)
			#========= clear lcl tab
			self.BT_CLEAR_LCKDFILE_lcl.setStyleSheet(
												"color: white;"
												"background-color: "+hexColor+";"
												"selection-color: yellow;"
												"selection-background-color: blue;"
												"font: bold 10px;"
												"border-style: outset;"
												"height: 15px;"
								)

			# #========= checkBox lcl tab
			# self.CHK_SEARCH_ALL.setStyleSheet("color: white")
			# self.CHK_SEARCH_ALL.show()
			# self.CHKCP_CLIPBRD.setStyleSheet("color: white")
			# self.CHKCP_CLIPBRD.show()

		except:
			pass


#============================================================================================== end Class QT__QT_KBZ__ 



#====================================================================================================== Thread Classes

#================================ Thread Instance ( container )

class Thread_Instance():

	def __init__(self, *args):  
		self.threads  	= []
		arguments     	= []
		for arg in args:
			arguments.append(arg)

		t = Thread_Worker(arguments, self) # self very Important
		t.start()
		self.threads.append(t)

	def __del__(self):
		for t in self.threads:
			running 	= t.running()
			t.stop()
			if not t.finished():
				t.wait()

#================================ Thread Worker

class Thread_Worker(QtCore.QThread):

	def __init__(self, args, receiver):
		QtCore.QThread.__init__(self)

		self.args     	= args
		self.receiver   = receiver # receiver ( self ) very Important
		self.Terminated 	= 0

	def run(self):
		time.sleep(0.1) # to do in thread
		try:
			result 		= self.run_myFunction(self.args)
		except:
			pass

	def stop(self):
		self.Terminated 	= 1

#================================ functions

	def run_myFunction(self,args):
		'''  get fileList '''

		self.source           		= args[0]
		self.USER_TO_SEARCH       	= args[1]
		self.CUR_PROJECT      	= args[2]
		self.EXCL_DIR_LCKD     = args[3]
		self.INCL_EXT_LCKD     = args[4]
		self.TMP_PATH_FILE_LCKD   = args[5]
		self.CHK_SEARCH_ALL       	= args[6]
		self.n_user           		= args[7]
		self.n_users_real       	= args[8]
		self.n_users_tot        	= args[9]

		startTimeAll = datetime.now()

		msg = '\n----- Search [ ' + self.USER_TO_SEARCH + ' ] LCKD-UnPublished Files, Work in Progress! Please wait ...\n'
		print >> sys.__stderr__, msg
		randwait = ['.','..','...'] # for deco

		matches = []

		for root, dirnames, filenames in os.walk(self.source, topdown=False, onerror=None, followlinks=False):
			if not dirnames:      
				for filename in filenames:
					ext = None
					try:
						ext = os.path.splitext(filename)[1][1:]
					except:
						pass  
					try:
						if ext.upper() in self.INCL_EXT_LCKD:
							filePath  = os.path.join(root, filename)
							result    = self.get_fileInfo(filePath)
							infoWrite   = result[0]
							infoOwner   = result[1]
							# matches.append(os.path.join(root, filename))
							if infoWrite == True and infoOwner == self.USER_TO_SEARCH:
								matches.append(os.path.join(root, filename))                
								msg = '\n' + filePath + ' [ LCKD ]\n'
								print >> sys.__stderr__, msg
					except:
						pass

		matches = list(set(matches))

		if len(matches) > 0 :
			try:
				with open(self.TMP_PATH_FILE_LCKD) as f:
					content = f.readlines()
			except:
				content=['.']
				pass

			for line in result:
				a7 = str(line)+'\n'
				if a7 not in content:         
					f = open(self.TMP_PATH_FILE_LCKD,'a')
					f.write('\n' +line+'\n') # python will convert \n to os.linesep
					f.close()

		#====== verbose mode
		msg = ' '   
		print >> sys.__stderr__, msg    
		msg = '\n--------------------------------- ' + self.source + ' [ DONE ] \n'
		print >> sys.__stderr__, msg
		msg = str(self.n_user) + ' | ' + str(self.n_users_tot) + '\n'
		print >> sys.__stderr__, msg
		totTime = datetime.now() - startTimeAll
		print >> sys.__stderr__, totTime

		if str(self.n_user) == str(self.n_users_tot):
			msg = '\n--------------------------------- [ CHECK PUBLISHED AND LCKD FILE DONE in : ' + totTime + ' ] \n'
			print >> sys.__stderr__, msg


	def get_fileInfo(self,source):
		fileInfo   = QtCore.QFileInfo(source)
		infoWrite = fileInfo.isWritable()
		infoOwner = fileInfo.owner()
		return infoWrite, infoOwner


#================================ end functions Thread classes

#====================================================================================================== End Thread Classes





#=========================================================================================================================
#========= Start QT 
#=========================================================================================================================


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


	main.resize(800, 800)

	# main.move(300, 300)

	# oX 	= 300
	# oY 	= 300
	# x 	= 150
	# y 	= 200
	# main.setGeometry(oX, oY, x, y)

	main.setModal(True)
	main.activateWindow()
	main.raise_()
	main.show()








############################################   

		# def checklcl_LCKD():
		# 	'''   '''
		# 	for i in range(self.modelTab1.count()):
		# 		yield self.item(i)
		# 		# item1 = self.item(i).text(0) # text at first (0) column
		# 		# self.printSTD(item1)

			# lcl_TreeView = self.Tab1
			# colIndex = 0


			# root = self.modelTab1.invisibleRootItem()
			# child_count = root.childCount()
			# for i in range(child_count):
			# 	item = root.child(i)
			# 	item1 = item.text(0) # text at first (0) column
			# 	# item.setText(1, 'result from %s' % url) # update result column (1)

			# 	self.printSTD(item1)

			# for n in range(nRows):
			# 	Item_QModelIndex = modelScript.index(n, colIndex)
			# 	# self.printSTD(Item_QModelIndex)
			# 	# self.printSTD('------------------------')
			# 	# item = Item_QModelIndex.data # return <built-in method data of QModelIndex object at 0x6102140>
			# 	# self.printSTD(item)
			# 	# item = Item_QModelIndex.data() # return default Qt.DisplayRole = .data(QtCore.Qt.DisplayRole) = text
			# 	# self.printSTD(item)
			# 	itemChecked = Item_QModelIndex.data(QtCore.Qt.CheckStateRole) # 
			# 	if itemChecked == 2: # checked
			# 		# self.printSTD('------------------------')
			# 		# self.printSTD(itemChecked)
			# 		# Item_QModelIndex.setColor(QtGui.QPalette.Background, QtGui.QColor.fromHsv(0, 0, 0)) 
					# ne retourne pas d erreur
			# 		# role = Item_QModelIndex.data(QtCore.Qt.BackgroundRole)  # ne retourne pas d erreur
			# 		# self.printSTD(role)  # ne retourne pas d erreur
			# 		modelScript.setData(
			# 		modelScript.index(n, colIndex),
			# 		QtGui.QColor(QtCore.Qt.green),
			# 		QtCore.Qt.BackgroundColorRole
			# 		)
