#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 16-08-2016                                                                #
# Thread Sample Usage                                                              #
# ##################################################################################

import os, sys
import glob, random
from random import randint
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

#====================================================================================================================================================== 

locked = RLock()
# workQueue = Queue.Queue(10)

#========================================================================================================================= Thread Instance ( container )

class __THREAD__INSTANCE__():

	def __init__(self, *args):  
		self.type_process = 'stack'
		self.with_locked  = False
		try:
		    self.type_process = args[2]
		except:
		  pass
		try:
		    self.with_locked = args[3]
		except:
		  pass
		self.threads  	= []
		arguments     	= []
		for arg in args[1]:
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

#================================================================================================================================ Class Thread ( Worker )

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
			result = __FUNCTIONS__TOTHREAD__(self.args,self.with_locked)
		except AttributeError:
		    print AttributeError
		    return None

	def stop(self):
		self.Terminated 	= 1

#=========================================================================================================================== Class __FUNCTIONS__TOTHREAD__

class __FUNCTIONS__TOTHREAD__():
    '''Dont Touch'''  
    def __init__(self, args, with_locked=True):
        self.args = args
        self.with_locked = with_locked # True force process ending before to execute the next
        self.run()

    def run(self):
	'''Dont Touch'''
	# print self.args 
	if self.with_locked == True:
	    with locked: 
		self.your_function()
	else:
	    self.your_function()
		

# ###################################################################################################
# YOUR FUNCTION                                                                                     #                                                                                                                         #
# ###################################################################################################
    def your_function(self):
	'''Your Code Here'''
	#self.arg[0] = 'grinch'
	#self.arg[1] = 'pets'
	#self.arg[2] = 'lorax'
	#self.arg[3] = 'dm1'
	#self.arg[4] = 'dm2'
	#self.arg[5] = 'dm3'
	#self.arg[6] = 'pets'
	for arg in self.args:
	    for lettre in arg:
		print lettre
		delay = 0.05
		delay += random.randint(1, 60) / 100
		time.sleep(delay)

#==================================================================================================================================== end __FUNCTIONS__TOTHREAD__
		
# ###################################################################################################
# METHOD                                                                                            #                                                                                                                        #
# ###################################################################################################

#============================= type of sharing ressources process | optional ( default stack ) 
# type_process = 'stack' 	# thread are executed in order
type_process = 'parallel'	# thread are executed simultaneous

#=========================================== lock process | optional ( default True (faster) )
with_locked = False		# lock and wait end of run threading process function

#============================================================== var(s) for threading process 1
film0 = 'grinch'
film1 = 'pets'
film2 = 'lorax'
film3 = 'dm1'
film4 = 'dm2'
film5 = 'dm3'
film6 = 'pets'
args = [film0,film1,film2,film3,film4,film5,film6]

#============================================================== var(s) for threading process 2
xvar0 = 'LORAX'
xvar1 = 'DM3'
xvar2 = 'LASOUPEAUXCHOUX'
xargs = [xvar0,xvar1,xvar2]

#=========== method to run several functions =================================================

__THREAD__INSTANCE__(os.path.basename(__file__),args,type_process,with_locked) 	
__THREAD__INSTANCE__(os.path.basename(__file__),xargs,type_process,with_locked)


