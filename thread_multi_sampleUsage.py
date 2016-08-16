#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 16-08-2016                                                                #
# ##################################################################################

import os, sys, random
import glob
import time, datetime
from datetime import datetime
import json
import shutil

from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import QThread

import threading
from threading import *
import Queue
from Queue import Queue
from multiprocessing import Pool, Process, Pipe, Lock, Value, Array, Manager, TimeoutError

#========================================================================================================================== 

if '__FUNCTIONS__TOTHREAD__' in sys.modules:
    del(sys.modules["__FUNCTIONS__TOTHREAD__"])
    import thread_multi_sampleUsage
    from thread_multi_sampleUsage import *
    # from thread_multi_sampleUsage import __FUNCTIONS__TOTHREAD__
else:
    import thread_multi_sampleUsage
    from thread_multi_sampleUsage import *
    # from thread_multi_sampleUsage import __FUNCTIONS__TOTHREAD__
    
locked = RLock()
# workQueue = Queue.Queue(10)

#============================================================================================= Thread Instance ( container )

class __THREAD__INSTANCE__():

	def __init__(self, *args): 
		self.type_process = 'stack'
		self.with_locked  = False
		try:
		    self.type_process = args[1]
		except:
		  pass
		try:
		    self.with_locked = args[2]
		except:
		  pass
		self.threads  	= []
		arguments     	= []
		for arg in args[0]:
			arguments.append(arg)
		t = __THREAD__WORKER__(arguments, self.with_locked, self) # self very Important
		t.start()
		self.threads.append(t)
		if self.type_process == 'stack':
			for t in self.threads:
				t.join()

	def __del__(self):
		for t in self.threads:
			running 	= t.running()
			t.stop()
			if not t.finished():
				t.wait()


#======================================================================================================= Thread ( Worker )

class __THREAD__WORKER__(threading.Thread): # If QT, no threading.Thread

	def __init__(self,args ,with_locked, receiver):
	  
		# QtCore.QThread.__init__(self) # if in QT
		threading.Thread.__init__(self)
		self.args     		= args
		self.with_locked	= with_locked
		self.receiver   	= receiver # receiver ( self ) very Important

		self.Terminated 	= 0

	def run(self):
		try:
			FUNCTIONS__TOTHREAD = thread_multi_sampleUsage.__FUNCTIONS__TOTHREAD__(self.args,self.with_locked)
		except AttributeError:
		    print AttributeError
		    return None

	def stop(self):
		self.Terminated 	= 1


