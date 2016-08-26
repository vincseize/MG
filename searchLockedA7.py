#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 26-08-2016                                                                #
# Search Locked A7                                                                 #
# ##################################################################################


import argparse
parser = argparse.ArgumentParser(description='login is optional | default is current login')
parser.add_argument('login')
args = parser.parse_args()
#======================================================================================================================================================

import os, sys
from os import stat
from pwd import getpwuid

import ink
import nomen
import ink.proto
import ink.query
import ink.io
import glob, random
from random import randint
import time, datetime
from datetime import datetime
import json
import shutil
import string

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

#============================================================================================== Thread Instance ( container )

class __THREAD__INSTANCE__():

	#================================================================================
	
	# without join:
	# +---+---+------------------                     main-thread
	#     |   |
	#     |   +...........                            child-thread(short)
	#     +..................................         child-thread(long)

	# with join
	# +---+---+------------------***********+###      main-thread
	#     |   |                             |
	#     |   +...........join()            |         child-thread(short)
	#     +......................join()......         child-thread(long)

	# with join and demon thread
	# +-+--+---+------------------***********+###     parent-thread
	#   |  |   |                             |
	#   |  |   +...........join()            |        child-thread(short)
	#   |  +......................join()......        child-thread(long)
	#   +,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,     child-thread(long+demonized)

	# '-' main-thread/parent-thread/main-program execution
	# '.' child-thread execution
	# '#' optional parent-thread execution after join()-blocked parent-thread could 
	#     continue
	# '*' main-thread 'sleeping' in join-method, waiting for child-thread to finish
	# ',' demonized thread - 'ignores' lifetime of other threads;
	#     terminates when main-programs exits; is normally meant for 
	#     join-independent tasks

	#================================================================================

	def __init__(self, *args):  
		self.type_process = 'stack' # default
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

#==================================================================================================== Class Thread ( Worker )

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

#============================================================================================= Class __FUNCTIONS__TOTHREAD__

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
		self.run_myFunction(self.args)
	else:
	    self.run_myFunction(self.args)
		

# #########################################################################################################################
# YOUR FUNCTION                                                                                                           #
# #########################################################################################################################
    def run_myFunction(self,args):
	'''  get fileList '''

	self.source           		= args[0]
	self.USER_TO_SEARCH		= args[1] # array
	self.CURRENT_PROJECT_lower	= args[2]
	self.DIR_LOCKED			= args[3]
	self.INCLUDE_EXT_LOCKED		= args[4]
	self.TMP_PATH_FILE_LOCKED	= args[5]
	self.n_users_tot		= args[6]
	self.start_time			= args[7]
	# print self.USER_TO_SEARCH
	

	#result_array = self.splitall(source)
	self.directory = self.splitall(self.source)[-1]

	print ' '
	print '===================================> ' + str(self.directory) + ' search in progress, please wait ...'
	print ' '

	matches = []

	path = os.path.normpath(self.source)

	for root, dirnames, filenames in os.walk(self.source, topdown=False, onerror=None, followlinks=True):

	    if not dirnames:   
		
		depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
		# print depth
		
		for filename in filenames:
		    ext = None
		    try:
			ext = os.path.splitext(filename)[1][1:]
		    except:
			pass  
		    try:
			if str(ext).upper() in self.INCLUDE_EXT_LOCKED:
			    pathA7  = os.path.join(root, filename)	
			    filePath = "/".join(pathA7.split('/')[6:])
			    ass = ink.query.Asset(nomen.Cut(filePath))
			    res = ass.GetLockInfos()

			    # assetLockedByMe, filesLockedByMe, assetLocked, assetLockOwner, filesLocked, filesLockOwner, assetBroken, assetStolen, filesBroken, filesStolen
			    # (True, True, True, 'cpottier', True, 'cpottier', False, False, False, False)

			    if res[3]==res[5]:
				if res[3] in str(self.USER_TO_SEARCH):    
				    matches.append(filePath)
				    msg = '\n' + filePath + ' [ LOCKED by '+self.USER_TO_SEARCH+' ]'
				    print msg

		    except:
			# print 'error'
			pass

	    
	matches = list(set(matches))

	print ' '
	print '===================================\ '
	print '====================================| ' + str(self.directory) + ' search DONE in  '
	print '===================================/ '
	endTime = datetime.now()
	totTime = endTime - self.start_time
	print totTime	
	print str(len(matches)) + ' a7 Locked'
	print matches
	print ' '
	
	#print self.CURRENT_PROJECT_lower

	curPath = os.path.abspath('.')
	
	if len(matches) > 0 :
	    
	    try:
		TMP_FILE_LOCKED = str(curPath)+'/LOCKEDA7/'+str(self.CURRENT_PROJECT_lower)+'/'+str(self.TMP_PATH_FILE_LOCKED)
		#self.deleteContent(TMP_FILE_LOCKED)
		# print TMP_FILE_LOCKED
		with open(TMP_FILE_LOCKED) as f:
		    content = f.readlines()
	    except:
		content=['']
		pass

	    f = open(TMP_FILE_LOCKED,'a')

	    for line in matches:
		a7 = str(line)+'\n'
		if a7 not in content:         
		    f = open(TMP_FILE_LOCKED,'a')
		    f.write(line+'\n') # python will convert \n to os.linesep
		    # f.close()

	    f.close()
	  



	#====== verbose mode
	'''
	msg = ' '   
	print >> sys.__stderr__, msg    
	msg = '\n--------------------------------- ' + self.source + ' [ DONE ] \n'
	print >> sys.__stderr__, msg
	msg = str(self.n_user) + ' | ' + str(self.n_users_tot) + '\n'
	print >> sys.__stderr__, msg
	totTime = datetime.now() - startTimeAll
	print >> sys.__stderr__, totTime

	if str(self.n_user) == str(self.n_users_tot):
	    msg = '\n--------------------------------- [ CHECK PUBLISHED AND LOCKED FILE DONE in : ' + totTime + ' ] \n'
	    print >> sys.__stderr__, msg
	'''


    def get_fileInfoQT(self,source):
	fileInfo   = QtCore.QFileInfo(source)
	infoWrite = fileInfo.isWritable()
	infoOwner = fileInfo.owner()
	return infoWrite, infoOwner


    def get_fileInfo(self,source):
	# fileInfo   = getpwuid(stat(source).st_uid).pw_name
	# st = os.stat(source)
	infoWrite = os.access(source, os.R_OK)
	infoOwner = getpwuid(stat(source).st_uid).pw_name
	#print infoWrite
	#print infoOwner	
	return infoWrite, infoOwner

    def splitall(self,path):
	allparts = []
	while 1:
	    parts = os.path.split(path)
	    if parts[0] == path:  # sentinel for absolute paths
		allparts.insert(0, parts[0])
		break
	    elif parts[1] == path: # sentinel for relative paths
		allparts.insert(0, parts[1])
		break
	    else:
		path = parts[0]
		allparts.insert(0, parts[1])
	return allparts



#=============================================================================================== end __FUNCTIONS__TOTHREAD__

# #########################################################################################################################
# Some Functions                                                                                                          #
# #########################################################################################################################

#========================================================================================================================== 		
		
def make_lockedA7dirs():		
  directory = 'LOCKEDA7'
  if not os.path.exists(directory):
      os.makedirs(directory)

  for project in ALL_PROJECTS:
      dp = directory + '/'+project
      if not os.path.exists(dp):
	  os.makedirs(dp)
	  
def deleteContent(fName):
    if os.path.exists(fName):
	with open(fName, "w"):
	    pass
	  
def get_AllUsers():
    ALL_USERS = [] # GLOBVAR
    for user in os.listdir(START_DIR_USERS):
	if str(user) not in EXCLUDE_DIR_USERS_LOCKED:
	    path = os.path.join(START_DIR_USERS, user)
	    if os.path.isdir(path):
		
		if CHK_SEARCH_ALL == True:
		    #ALL_USERS.append('/.mdu/'+user)
		    ALL_USERS.append(user)
		    #print path
		if CHK_SEARCH_ALL == False:
		    #ALL_USERS.append('/.mdu/'+CURRENT_USER)
		    ALL_USERS.append(CURRENT_USER)
		    break        
    return ALL_USERS		
		
		
# #########################################################################################################################
# METHOD                                                                                                                  #
# #########################################################################################################################

#====================================================================================================== Functions to thread

def search_lockedA7():
    msg = '\n----- Search Locked-UnPublished Files, Work in Progress! Please wait ...\n'
    print msg

    for directory in INCLUDE_DIR_LOCKED:
	#print directory
	startTimeAll = datetime.now()
	print startTimeAll
	# start_time = time.time()
	#START_DIR = START_DIR_OFF_LOCKED_A7 + '/' + directory
	START_DIR = START_DIR_LOCAL_LOCKED_A7+'/' + directory
	args = [START_DIR,ALL_USERS,CURRENT_PROJECT_lower,INCLUDE_DIR_LOCKED,INCLUDE_EXT_LOCKED,TMP_PATH_FILE_LOCKED,n_users_tot,startTimeAll]
	__THREAD__INSTANCE__(os.path.basename(__file__),args,type_process,with_locked)
      
      
	#===================================================== 
	#totTime = datetime.now() - startTimeAll 
	#msg = '\n--------------------------------- [ CHECK PUBLISHED AND LOCKED FILE DONE in : ' + str(totTime) + ' ] \n'    
	#print msg

# ############################################################################################################### Variables

#================================================ type of sharing ressources process | optional ( default stack ) 
# type_process = 'stack' 	# thread are executed in order
type_process = 'parallel'	# thread are executed simultaneous

#================================================ lock process | optional ( default True (longer) )
with_locked = False		# lock and wait end of run threading process function

#================================================

CURRENT_USER 			= os.getenv('USER')
try:
    print sys.argv[1]
    CURRENT_USER 		= sys.argv[1]
except:
    pass
ALL_PROJECTS	 		= {"gri": [71, 209, 71], "lun": [0, 153, 255], "dm3": [204, 51, 255], "max": [139, 0, 0], "pets2": [100, 50, 0] }		
CURRENT_PROJECT_lower 		= ink.io.ConnectUserInfo()[2]		
CURRENT_PROJECT 		= CURRENT_PROJECT_lower.upper()
if CURRENT_PROJECT 		== 'GRI':
    HOME_COLOR = ALL_PROJECTS['gri']
if CURRENT_PROJECT 		== 'LUN':
    HOME_COLOR = ALL_PROJECTS['lun']
if CURRENT_PROJECT 		== 'DM3':
    HOME_COLOR = ALL_PROJECTS['dm3']
if CURRENT_PROJECT 		== 'MAX':
    HOME_COLOR = ALL_PROJECTS['max']
    
START_DIR_USERS 		= '/u/'+CURRENT_PROJECT_lower+'/Users/'	    
START_DIR_PUBLIC 		= START_DIR_USERS+'COM/Presets/Graphs/'
# START_DIR_LOCAL_LOCKED_A7 	= START_DIR_USERS+CURRENT_USER+'/Files/etc'
START_DIR_LOCAL_LOCKED_A7 	= START_DIR_USERS+'COM/Assets'
	
# START_DIR_LOCAL_LOCKED_A7 	= START_DIR_USERS+CURRENT_USER+'/Assets'	
# START_DIR_OFF_LOCKED_A7 	= START_DIR_USERS+'OFF/Assets/'+CURRENT_PROJECT+'/'
START_DIR_OFF_LOCKED_A7 	= START_DIR_USERS+'OFF/Assets'
#PATH_EXEMPLES			= '/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples'
#CURRENT_SCRIPTS_PATH		= '/u/'+CURRENT_PROJECT_lower+PATH_EXEMPLES
TMP_PATH_FILE_LOCKED 		= CURRENT_PROJECT+'A7LockedBy.tmp'
EXCLUDE_DIR_USERS_LOCKED 	= ['COM','OFF','dm3_contrats']
INCLUDE_DIR_LOCKED 		= [CURRENT_PROJECT,'LIB','LIBREF','MODELING','PREVIZ','USECASE','USECASEDEV','LINUP']
#INCLUDE_DIR_LOCKED 		= ['LINUP']
INCLUDE_EXT_LOCKED 		= ['CSV','XML','INKGRAPH','A7']

CHK_SEARCH_ALL  		= False


ALL_USERS = get_AllUsers()
n_users_tot        	= len(ALL_USERS)
make_lockedA7dirs()

curPath = os.path.abspath('.')
TMP_FILE_LOCKED = str(curPath)+'/LOCKEDA7/'+str(CURRENT_PROJECT_lower)+'/'+str(TMP_PATH_FILE_LOCKED)
deleteContent(TMP_FILE_LOCKED)	


# ############################################################################################################### RUN  
	
search_lockedA7()

