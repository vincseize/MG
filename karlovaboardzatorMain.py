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



		self.layout = QtGui.QVBoxLayout()
		self.setLayout(self.layout)



		# self.palOk = QtGui.QPalette()
		# self.palOk.setColor(QtGui.QPalette.ColorRole(6),QtGui.QColor("#55FF55"))
		# self.palOk.setColor(QtGui.QPalette.ColorRole(9),QtGui.QColor("#999999"))

		# self.palErr = QtGui.QPalette()
		# self.palErr.setColor(QtGui.QPalette.ColorRole(6),QtGui.QColor("#FF0000"))
		# self.palErr.setColor(QtGui.QPalette.ColorRole(9),QtGui.QColor("#999999"))


		self.BT_close = QtGui.QPushButton("Close QT")
		self.layout.addWidget(self.BT_close)

		self.BT_close.connect(self.BT_close,QtCore.SIGNAL("clicked()"),self.closeWindows)



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


