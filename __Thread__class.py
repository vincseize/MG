#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 05-08-2016                                                                #
# ##################################################################################


#=======================================================================================================================  CLASS __QT_KBZ__

import os
import sys
import random
import glob
import time
import json
import shutil
import datetime
from datetime import datetime

from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import QThread

import threading
import Queue
from multiprocessing import Pool, Process, Pipe, Lock, Value, Array, Manager, TimeoutError

#================================ Thread Instance ( container )

class __THREAD__INSTANCE__():

	def __init__(self, *args):  
		self.threads  	= []
		arguments     	= []
		for arg in args:
			arguments.append(arg)
			print arg
		t = __THREAD__WORKER__(arguments, self) # self very Important
		t.start()
		self.threads.append(t)

	def __del__(self):
		for t in self.threads:
			running 	= t.running()
			t.stop()
			if not t.finished():
				t.wait()


#================================ Thread Worker

class __THREAD__WORKER__(threading.Thread): # If QT, no threading.Thread

	def __init__(self,args , receiver):
	  
		# QtCore.QThread.__init__(self) # if in QT
		threading.Thread.__init__(self)
		self.args     			= args	
		self.receiver   		= receiver # receiver ( self ) very Important

		self.Terminated 	= 0

	def run(self):
		# time.sleep(0.1) # to do in thread
		try:
			# result 		= self.run_myFunction(self.args)
			result          = self.run_myFunction_toThread.myFunction_toThread(self.args)
		except:
			pass

	def stop(self):
		self.Terminated 	= 1


    
    
    
    
  
