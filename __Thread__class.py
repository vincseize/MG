#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 12-08-2016                                                                #
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

if '__FUNCTIONS__TOTHREAD__' in sys.modules:
    del(sys.modules["__FUNCTIONS__TOTHREAD__"])
    import thread_multi_sampleUsage
    #from thread_multi_sampleUsage import __FUNCTIONS__TOTHREAD__
    from thread_multi_sampleUsage import *
    #import thread_multi_sampleUsage.__FUNCTIONS__TOTHREAD__
else:
    import thread_multi_sampleUsage
    #from thread_multi_sampleUsage import __FUNCTIONS__TOTHREAD__
    from thread_multi_sampleUsage import *
    #import thread_multi_sampleUsage.__FUNCTIONS__TOTHREAD__
#===================================================================================================



class __THREAD__INSTANCE__():

	def __init__(self, *args):  
		self.threads  	= []
		arguments     	= []
		for arg in args[1]:
			arguments.append(arg)
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
		try:
			FUNCTIONS__TOTHREAD = thread_multi_sampleUsage.__FUNCTIONS__TOTHREAD__(self.args)
		except AttributeError:
		    print AttributeError
		    return None

	def stop(self):
		self.Terminated 	= 1


    
    
    
    
  
