#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 16-10-2016                                                                #
# Search Locked Unpublished Broken A7                                              #
# ##################################################################################


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

import socket
import threading
from threading import *
import Queue
from Queue import Queue
from multiprocessing import Pool, Process, Pipe, Lock, Value, Array, Manager, TimeoutError

#======================================================================================================================================================
import argparse

parser = argparse.ArgumentParser(description='Search locked (default), unpublished or brocken a7')
# parser = argparse.ArgumentParser(description='login, bck for searching blocked A7 are optional | default search : current user -> search locked A7 ')

parser.add_argument('login',nargs='?',help='Default is current user', default=os.getenv('USER'))

parser.add_argument('a',nargs='?',help='Search for all users')
parser.add_argument('upb',nargs='?',help='Search Unpublished a7')
parser.add_argument('bck',nargs='?',help='Search brocken a7')
args = parser.parse_args()

#====================================================================================================================================================== 
# my_queue = Queue.Queue()
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
		self.threads.append(t)
		# t.setDaemon(True)
		t.start()
		
		if self.type_process == 'stack':
			for t in self.threads:
				t.setDaemon(True)
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
		
		# self.setDaemon(True) # Daemonize thread
		# self.daemon = True
		
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
	self.START_DIR_LOCAL_LOCKED_A7	= args[3]
	self.DIR_LOCKED			= args[4]
	self.EXCLUDE_DIR_USERS_LOCKED	= args[5]
	self.INCLUDE_EXT_LOCKED		= args[6]
	self.TMP_PATH_FILE		= args[7]
	self.BROKENA7			= args[8]
	self.CURRENT_USER               = args[9]
	self.n_users_tot		= args[10]
	self.start_time			= args[11]
	self.directory = self.splitall(self.source)[-1]

	print ' '
	print '===================================> ' + str(self.directory) + ' search in progress, please wait ...'
	print ' '

	print threading.currentThread().getName()

	self.startTimeInt = datetime.now()
	#exclude = set(self.EXCLUDE_DIR_USERS_LOCKED)
	matches = []
	
	# print self.TMP_PATH_FILE_LOCKED, self.TMP_PATH_FILE_BROKEN, self.TMP_PATH_FILE_UPB
	
	path = os.path.normpath(self.source)
	# print path

	
	for root, dirnames, filenames in os.walk(self.source, topdown=True, onerror=None, followlinks=False): # topdown=False moins efficient que True + break 1min38/59s

	    if not dirnames:   #  and len(intersect) == 0
		depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
		# print depth
		for filename in filenames:
		    # filename = .mdadata
		    ext = None
		    ext = 'a7' # to do
		    filePath = os.path.join(root, filename)
		    if str(self.BROKENA7) == 'upb':
			#TMP_FILE_LOCKED = self.TMP_PATH_FILE_UPB
			#print filePath
			# tmp = filename.split('.')
			#print tmp[1]
			comPublishedFalse = ''
			try:
			    if filename.split('.')[1]=='xml':
				published = self.get_symLinks(filePath,self.CURRENT_PROJECT_lower,self.USER_TO_SEARCH[0])
				if published == False:
				    # /u/dm3/Users/cpottier/Files/etc/LIB/PROPS/VEHICLE/EscapeMachineMinions/Model/EscapeMachineMinions-Model-Ok.xml
				    # => LIB/PROPS/VEHICLE/EscapeMachineMinions/Ok/EscapeMachineMinions-Model-Ok.a7
				    #    LIB/PROPS/VEHICLE/EscapeMachineMinions/Model/EscapeMachineMinions-Model-Ok.a7
				    tmp = filePath.split('/etc/')
				    tmp1 = tmp[1].split('.xml')
				    a7 = tmp1[0] + '.a7'
				    line = str(a7) + str(comPublishedFalse)
				    matches.append(line)
				    msg = '\n' + filePath + ' [ UNPUBLISHED ]'
				    print msg
				    
				    
				    # IroningBoard
				    # print filePath
				    res = None
				    # /U/GRI/USERS/OFF/ASSETS/USECASE/GROOPERT/TEST111/LAYOUT/USECASE_GROOPERT_TEST111-LAYOUT_PRE_CONFIG.A7/0001/.MDA/.MDADATA
				    # normalize name for Ink API => /USECASE/CINDYLOU/EDIT/NasK/USECASE_CINDYLOU_EDIT-NasK_Casting.a7
				    filePath = "/".join(filePath.split('/')[6:]) 
				    tmp =  filePath.split(ext)
				    filePath = str(tmp[0])+str(ext)
				    # InK Method
				    ass = ink.query.Asset(nomen.Cut(filePath))
				    res = ass.GetLockInfos()
				    #print res				    
				    
				    
				    break
			except:
			    pass
			  
		    else:
			try:
			    
			    
			    # /U/GRI/USERS/OFF/ASSETS/USECASE/GROOPERT/TEST111/LAYOUT/USECASE_GROOPERT_TEST111-LAYOUT_PRE_CONFIG.A7/0001/.MDA/.MDADATA
			    result_array = self.splitall(filePath)
			    if self.USER_TO_SEARCH[0] in result_array: # and str(ext).upper() in str(result_array).upper()
				    
				if '.mdu' in result_array: 
				    print filePath
				    result = None
				    result = self.get_fileInfo(filePath)	# ln link -> 
				    # /u/gri/Users/OFF/Assets/USECASE/CINDYLOU/EDIT/NasK/USECASE_CINDYLOU_EDIT-NasK_Casting.a7/0003/USECASE_CINDYLOU_EDIT-NasK_Casting.a7
				    infoWrite = result[0]
				    infoOwner = result[1]

				    if infoWrite == True and str(infoOwner) in str(self.USER_TO_SEARCH):		
					
					# IroningBoard
					# print filePath
					res = None
					# /U/GRI/USERS/OFF/ASSETS/USECASE/GROOPERT/TEST111/LAYOUT/USECASE_GROOPERT_TEST111-LAYOUT_PRE_CONFIG.A7/0001/.MDA/.MDADATA
					# normalize name for Ink API => /USECASE/CINDYLOU/EDIT/NasK/USECASE_CINDYLOU_EDIT-NasK_Casting.a7
					filePath = "/".join(filePath.split('/')[6:]) 
					tmp =  filePath.split(ext)
					filePath = str(tmp[0])+str(ext)
					# ================================================= InK Method
					ass = ink.query.Asset(nomen.Cut(filePath))
					res = ass.GetLockInfos()
					# assetLockedByMe, filesLockedByMe, assetLocked, assetLockOwner, filesLocked, filesLockOwner, assetBroken, assetStolen, filesBroken, filesStolen
					# (True, True, True,   'cpottier', True, 'cpottier', False, False, False, False) => Grabbed
					# (False, False, False, 'nobody', False, 'nobody', False, False, False, False) => unpublished + ln => off
					# =================================================
					comBrokenFalse = ''
					comBrokenTrue = ''
					if str(self.CURRENT_USER) == '-a':
					    comBrokenFalse = ' | ' + str(res[3])
					    comBrokenTrue  = ' | ' + str(self.USER_TO_SEARCH[0])
					# case asset Locked
					if self.BROKENA7 == False:
					    #TMP_FILE_LOCKED = self.TMP_PATH_FILE_LOCKED
					    if res[3]==res[5]:
						if res[3] in str(self.USER_TO_SEARCH): 
						    line = str(filePath) + str(comBrokenFalse)
						    matches.append(line)
						    msg = '\n' + filePath + ' [ LOCKED by '+str(res[3])+' ]'
						    print msg
						    break
					# case asset or file Broken 
					if self.BROKENA7 == True:
					      #TMP_FILE_LOCKED = self.TMP_PATH_FILE_BROKEN
					      if res[6] == True or res[8] == True:
						  line = str(filePath) + str(comBrokenTrue)
						  matches.append(line)
						  msg = '\n' + filePath + ' [ BROKEN ]'
						  print msg
						  break
					# case asset unplished TODO 
					
			except:
			    print 'error'
			    pass
	    
	matches = list(set(matches))

	endTime = datetime.now()
	totTimeInt = endTime - self.startTimeInt
	totTime = endTime - self.start_time
	
	print ' '
	print '=================================================\ '
	print '=================================================|> ' + str(self.directory) + ' search DONE in ' + str(totTimeInt) + ' / '+ str(totTime)
	print '=================================================/ '
	if len(matches)>0:
	    print ' > ' + str(len(matches)) + ' a7 Locked'
	print matches
	print ' '
	
	if len(matches) > 0 :
	    
	    try:
		
		with open(self.TMP_PATH_FILE) as f:
		    content = f.readlines()
	    except:
		content=['']
		pass

	    f = open(self.TMP_PATH_FILE,'a')

	    for line in matches:
		a7 = str(line)+'\n'
		if a7 not in content:         
		    f = open(self.TMP_PATH_FILE,'a')
		    f.write(line+'\n') # python will convert \n to os.linesep

	    f.close()
	  

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
	#print infoWrite, infoOwner
	return infoWrite, infoOwner

    def get_symLinks(self,source,project,user):
	published = True
	'''
	print source 
	published = True
	tmp = source.split('.')		    
	xmlPath = '/u/'+project+'/Users/'+user+'/Files/etc/'+str(tmp[0])+'.xml'
	# /u/gri/Users/cpottier/Files/etc/LIB/CHARS/MAIN/Grinch/Ok/Grinch-Model-Ok.xml
	# xmlPath = '/u/gri/Users/cpottier/Files/etc/LIB/CHARS/MAIN/Grinch/Model/Grinch-Model-Ok.xml'
	print xmlPath
	'''
	pathSymLink = os.readlink(source)
	# print pathSymLink
	if '/COM/' not in str(pathSymLink):
	    published = False
	
	return published


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
		    ALL_USERS.append(user)
		if CHK_SEARCH_ALL == False:
		    ALL_USERS.append(CURRENT_USER)
		    break        
    return ALL_USERS		
		
def check_Path(source):
    check = False
    if os.path.exists(source):
	check = True
    return check
    
# #########################################################################################################################
# METHOD                                                                                                                  #
# #########################################################################################################################

#====================================================================================================== Functions to thread

def searchA7(type_process,with_locked):
    
    def search_unpublished():
	for directory in INCLUDE_DIR_LOCKED:
	    #startTimeAll = datetime.now()
	    #print startTimeAll
	    directory = directory
	    #directory = 'GRI/S0015/'
	    START_DIR = START_DIR_OFF_LOCKED_A7 + '/' + directory
	    print START_DIR
	    check = check_Path(START_DIR)
	    if check == True:
		for root, dirnames, filenames in os.walk(START_DIR):
		    dirnames[:] = [d for d in dirnames if d not in exclude]
		    for dirname in dirnames:
			#print dirname
			START_DIR = START_DIR_OFF_LOCKED_A7 + '/' + directory + '/' + dirname
			args = [START_DIR,ALL_USERS,CURRENT_PROJECT_lower,START_DIR_LOCAL_LOCKED_A7,INCLUDE_DIR_LOCKED,EXCLUDE_DIR_USERS_LOCKED,INCLUDE_EXT_LOCKED,TMP_PATH_FILE_LOCKED,TMP_PATH_FILE_BROKEN,TMP_PATH_FILE_UPB,BROKENA7,CURRENT_USER,n_users_tot,startTimeAll]
			__THREAD__INSTANCE__(os.path.basename(__file__),args,type_process,with_locked)
			#print BROKENA7
			# print 'search_unpublished'
		    #break  
		    
    def search_locked_brocken():  
  	exclude = set(EXCLUDE_DIR_USERS_LOCKED)
	for directory in INCLUDE_DIR_LOCKED:

	    directory = directory
	    # directory = directory + '/PROPS/VEHICLES/'
	    START_DIR = START_DIR_OFF_LOCKED_A7 + '/' + directory
	    check = check_Path(START_DIR)
	    print START_DIR
	    
	    if check == True:
	      for root, dirnames, filenames in os.walk(START_DIR):
		  dirnames[:] = [d for d in dirnames if d not in exclude]
		  for dirname in dirnames:
		      print dirname
		      START_DIR = START_DIR_OFF_LOCKED_A7 + '/' + directory + '/' + dirname
		      args = [START_DIR,ALL_USERS,CURRENT_PROJECT_lower,START_DIR_LOCAL_LOCKED_A7,INCLUDE_DIR_LOCKED,EXCLUDE_DIR_USERS_LOCKED,INCLUDE_EXT_LOCKED,TMP_PATH_FILE,BROKENA7,CURRENT_USER,n_users_tot,startTimeAll]
		      __THREAD__INSTANCE__(os.path.basename(__file__),args,type_process,with_locked)
		  break
  
    tps = 'Locked'
    TMP_PATH_FILE = TMP_PATH_FILE_LOCKED
    if BROKENA7 == True:
	tps = 'Broken'
	TMP_PATH_FILE = TMP_PATH_FILE_BROKEN
    if BROKENA7 == 'upb':
	tps = 'unpublished a7'
	TMP_PATH_FILE = TMP_PATH_FILE_UNPUBLISHED
	
    msg = '\n----- Search '+tps+' Files, Work in Progress! Please wait ...\n'
    print msg
    print ALL_USERS
    startTimeAll = datetime.now()
    print startTimeAll
    
    exclude = set(EXCLUDE_DIR_USERS_LOCKED)
    
    if BROKENA7 == 'upb':
	search_unpublished()	
    else:
	search_locked_brocken()


def run(type_process,with_locked):
    u = 0
    for user in USERS:
	u += 1
	# print user
	ALL_USERS=[user]
	searchA7(type_process,with_locked)


# ############################################################################################################### VARS DONT TOUCH
print sys.argv
CURRENT_USER 		= os.getenv('USER')
BROKENA7		= False
if 'bck' in sys.argv or 'upb' in sys.argv:
    try:
      if str(sys.argv[1])	== 'bck':
	  CURRENT_USER 	= sys.argv[2]
	  BROKENA7 = True
    except:
	pass
    try:
	if str(sys.argv[2])	== 'bck':
	    CURRENT_USER 	= sys.argv[1]    
	    BROKENA7	= True

    except:
      pass
    try:
      if str(sys.argv[1])	== 'upb':
	  CURRENT_USER 	= sys.argv[2]
	  BROKENA7 = 'upb'
    except:
      pass
    try:
      if str(sys.argv[2])	== 'upb':
	  CURRENT_USER 	= sys.argv[1]
	  BROKENA7	= 'upb'	  
    except:
	pass

else:
    try:
	CURRENT_USER 	= sys.argv[1]
	BROKENA7 = True
    except:
	pass


print CURRENT_USER
print BROKENA7


ALL_PROJECTS	 		= {"gri": [71, 209, 71], "lun": [0, 153, 255], "dm3": [204, 51, 255], "max": [139, 0, 0], "pets2": [255, 51, 0] }		
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
START_DIR_LOCAL_LOCKED_A7 	= START_DIR_USERS+'COM/Assets'
START_DIR_OFF_LOCKED_A7 	= START_DIR_USERS+'OFF/Assets'
TMP_FILE_LOCKED			= CURRENT_PROJECT+'A7LockedBy.tmp'
TMP_FILE_BROKEN			= CURRENT_PROJECT+'A7BrokenBy.tmp'
TMP_PATH_FILE_UNPUBLISHED	= CURRENT_PROJECT+'A7unPublishedBy.tmp'
EXCLUDE_DIR_USERS_LOCKED 	= ['COM','OFF','TMP','SVN','.SVN','REFS','PLUGINS','IMAGES','THUMBNAILS','OLD','DESIGN','MAPS','GIF','PSD','GRINCH','TEMPLATES','SHARED','Vfx','Anim_Clip','Refs_Xml','.flags','mel','.mdaTrash']
EXCLUDE_DIR_USERS_LOCKED 	= []
INCLUDE_DIR_LOCKED 		= [CURRENT_PROJECT,'LIB','LIBREF','MODELING','PREVIZ','USECASE','USECASEDEV','LINUP']
INCLUDE_DIR_LOCKED 		= ['GRI']
INCLUDE_EXT_LOCKED 		= ['CSV','XML','INKGRAPH','A7']
TMP_PATH_FILE_LOCKED 		= '/u/'+os.getenv('USER')+'/Public/'+str(TMP_FILE_LOCKED)
TMP_PATH_FILE_BROKEN 		= '/u/'+os.getenv('USER')+'/Public/'+str(TMP_FILE_BROKEN)
TMP_PATH_FILE_UPB 		= '/u/'+os.getenv('USER')+'/Public/'+str(TMP_PATH_FILE_UNPUBLISHED)

CHK_SEARCH_ALL  		= False

ALL_USERS = get_AllUsers()
n_users_tot = len(ALL_USERS)

deleteContent(TMP_PATH_FILE_LOCKED)
deleteContent(TMP_PATH_FILE_BROKEN)
deleteContent(TMP_PATH_FILE_UPB)

if CURRENT_USER=='a':
  CHK_SEARCH_ALL = True
  USERS = get_AllUsers()
else:
  USERS = [CURRENT_USER]
  f = open(TMP_PATH_FILE_LOCKED,'a')
  f.write(CURRENT_USER+'\n') # python will convert \n to os.linesep
  f.close()
  f = open(TMP_PATH_FILE_BROKEN,'a')
  f.write(CURRENT_USER+'\n')
  f.close()
  f = open(TMP_PATH_FILE_UPB,'a')
  f.write(CURRENT_USER+'\n')
  f.close()


if BROKENA7 == False:
  TMP_FILE_LOCKED = TMP_PATH_FILE_LOCKED
if BROKENA7 == True:
  TMP_FILE_LOCKED = TMP_PATH_FILE_BROKEN
if BROKENA7 == 'upb':
  TMP_FILE_LOCKED = TMP_PATH_FILE_UPB


# ############################################################################################################### THREADING PROCESSES VARIABLES  

#================================================ type of sharing ressources process | optional ( default stack ) 
# type_process = 'stack' 	# thread are executed in order
type_process = 'parallel'	# thread are executed simultaneous

#================================================ lock process | optional ( default True (longer) )
with_locked = False		# lock and wait end of run threading process function

#================================================

# ############################################################################################################### RUN 


# run(type_process,with_locked)


#cmd = 'nedit '+str(TMP_FILE_LOCKED)
#os.system( cmd )

