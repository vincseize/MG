#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 30-10-2016                                                                #
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

import argparse

#============================================================================================================================================== -help

parser = argparse.ArgumentParser(description='Search locked (default), unpublished or broken a7')
parser.add_argument('.....',nargs='?',help='')
parser.add_argument('login',nargs='?',help='[optional] If None, Search for current login', default=os.getenv('USER'))
parser.add_argument('login=a',nargs='?',help='Search for all users')
parser.add_argument('.....',nargs='?',help='')
parser.add_argument('lck',nargs='?',help='Search Locked a7')
parser.add_argument('upb',nargs='?',help='Search Unpublished a7')
parser.add_argument('brk',nargs='?',help='Search Broken a7')
parser.add_argument('.....',nargs='?',help='')
parser.add_argument('path',nargs='?',help='[optional] , Defaults are [CURRENT_PROJECT,LIB,LIBREF,MODELING,PREVIZ,USECASE,USECASEDEV,LINEUP,MLUN,SLUN]')
parser.add_argument('.....',nargs='?',help='')
parser.add_argument('usage sample 1 :',nargs='?',help='python searchStranges_a7.py lck')
parser.add_argument('usage sample 2 :',nargs='?',help='python searchStranges_a7.py gamin brk')
parser.add_argument('usage sample 3 :',nargs='?',help='python searchStranges_a7.py a brk /USECASEDEV/SUBFOLDER')
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
			# return_val = result.get()
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
	if self.with_locked == True:
	    with locked: 
		self.run_myFunction(self.args)
	else:
	    self.run_myFunction(self.args)
		

    # #########################################################################################################################
    # YOUR FUNCTION                                                                                                           #
    # #########################################################################################################################
    def run_myFunction(self,args):
	'''   '''
	self.source           		= args[0]
	self.USER_TO_SEARCH		= args[1] # array
	self.CURRENT_PROJECT_lower	= args[2]
	self.START_DIR_LOCAL_LOCKED_A7	= args[3]
	self.DIR_LOCKED			= args[4]
	self.EXCLUDE_DIR_USERS_LOCKED	= args[5]
	self.INCLUDE_EXT_LOCKED		= args[6]
	self.TMP_PATH_FILE		= args[7]
	self.A7_typeSearch		= args[8]
	self.CURRENT_USER               = args[9]
	self.n_users_tot		= args[10]
	self.start_time			= args[11]
	self.directory = self.splitall(self.source)[-1]

	# print threading.currentThread().getName()

	matches = []
	path = os.path.normpath(self.source)
	searchName = self.USER_TO_SEARCH[0]
	if str(self.CURRENT_USER) == 'a':
	    searchName = 'all - ' + str(self.USER_TO_SEARCH[0])
	
	
	# ------------------------------------------------------------------------------- 
	self.start_Msg(searchName,self.directory,self.A7_typeSearch)
	# -------------------------------------------------------------------------------	
	

	self.startTimeInt = datetime.now()

	for root, dirnames, filenames in os.walk(self.source, topdown=False, onerror=None, followlinks=True): # topdown=False moins efficient que True
	    dirnames[:] = [d for d in dirnames if d not in self.EXCLUDE_DIR_USERS_LOCKED]
	    if not dirnames:   #  and len(intersect) == 0
		depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
		#print depth
		for filename in filenames:
		    ext = None
		    ext = 'a7' # to do
		    filePath = os.path.join(root, filename)
		    filePath_toWrite = self.normalize_Name(os.path.join(root, filename),ext)
		    comFalse = ''
		    comTrue = ''
		    res = None
		    
		    #==========================================================================================================================================================  locked or broken a7
		    if str(self.A7_typeSearch) == 'lck' or str(self.A7_typeSearch) == 'brk' or str(self.A7_typeSearch) == 'upb':

			try:
			    
			    # /U/GRI/USERS/OFF/ASSETS/USECASE/GROOPERT/TEST111/LAYOUT/USECASE_GROOPERT_TEST111-LAYOUT_PRE_CONFIG.A7/0001/.MDA/.MDADATA
			    result_array = self.splitall(filePath)
			    
			    if self.USER_TO_SEARCH[0] in result_array and '.mdu' in result_array :
				res = self.get_LockInfos(filePath,ext)
				result = None
				result = self.get_FileInfos(filePath)	# ln link -> 
				infoWrite = result[0]
				infoOwner = result[1]
				


				if self.A7_typeSearch == 'lck': # ==============================================================================================================================  locked a7
				    if infoWrite == True and str(infoOwner) in str(self.USER_TO_SEARCH):		
					if res[3] == res[5]: 
					    # (xxx, xxx, xxx, 'login', xxx, 'login', xxx, xxx, xxx, xxx) 				=> Locked
					    if res[3] in str(self.USER_TO_SEARCH): 
						line = str(filePath_toWrite) + str(comFalse)
						matches.append(line)
						msg = '\n' + filePath_toWrite + ' [ LOCKED by '+str(self.USER_TO_SEARCH[0])+' ]'
						print msg
						break
				#================================================================================================================================================  broken a7 or broken file
				if self.A7_typeSearch == 'brk':
				    if res[6] == True or res[8] == True: 
					# (xxx, xxx, xxx, xxx, True, xxx, True, xxx, True, xxx) 					=> Broken
					line = str(filePath_toWrite) + str(comTrue)
					matches.append(line)
					msg = '\n' + filePath_toWrite + ' [ BROKEN by '+str(self.USER_TO_SEARCH[0])+'  ]'
					print msg
					break
				      
				      
				#==========================================================================================================================================================  unpublished a7
				if self.A7_typeSearch == 'upb':				      
				    if res[0] == False and res[1] == False and res[2] == False  and res[3] == 'nobody' and res[4] == False and res[5] == 'nobody' and res[6] == False and res[7] == False and res[8] == False and res[9] == False:
					# (False, False, False, 'nobody', False, 'nobody', False, False, False, False)  		=> Unpublished
					line = str(filePath_toWrite) + str(comTrue)
					matches.append(line)
					msg = '\n' + filePath_toWrite + ' [ UNPUBLISHED by '+str(self.USER_TO_SEARCH[0])+'  ]'
					print msg
					break
				      
			except:
			    # print 'error'
			    pass
			  
      #========================================================================================================== save result	    
	matches = list(set(matches))	
	if len(matches) > 0 :
	    print ' > ' + str(len(matches)) + ' a7 ' + str(self.A7_typeSearch)
	    print matches
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

	# ------------------------------------------------------------------------------- 
	self.end_Msg(self.startTimeInt,searchName,self.directory,self.A7_typeSearch)
	# -------------------------------------------------------------------------------
	
	return matches
      
      #======================================================================================================== end save result
	      
    # #########################################################################################################################
    # END RUN FUNCTION                                                                                                        #
    # #########################################################################################################################	      
		  
		
	      
	      

    def get_FileInfosQT(self,source):
	fileInfo   = QtCore.QFileInfo(source)
	infoWrite = fileInfo.isWritable()
	infoOwner = fileInfo.owner()
	return infoWrite, infoOwner

    def get_FileInfos(self,source):
	# fileInfo   = getpwuid(stat(source).st_uid).pw_name
	# st = os.stat(source)
	infoWrite = os.access(source, os.R_OK)
	infoOwner = getpwuid(stat(source).st_uid).pw_name
	#print infoWrite, infoOwner
	return infoWrite, infoOwner

    def get_SymLinks(self,source):
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

    def get_ScmInfos(self,source,project,user):
	published = True
	pathSymLink = os.readlink(source)
	# print pathSymLink
	if '/COM/' not in str(pathSymLink):
	    published = False
	return published

    def get_LockInfos(self,filePath,ext):
	filePath = self.normalize_Name(filePath,ext)
	''' Ink API Method '''
	# assetLockedByMe, filesLockedByMe, assetLocked, assetLockOwner, filesLocked, filesLockOwner, assetBroken, assetStolen, filesBroken, filesStolen <= return	
	# (xxx, xxx, xxx, 'login', xxx, 'login', xxx, xxx, xxx, xxx)					=> Locked / Grabbed
	# (xxx, xxx, xxx, xxx, True, xxx, True, xxx, True, xxx)						=> Broken
	# (False, False, False, 'nobody', False, 'nobody', False, False, False, False) 			=> unpublished + ln => off
	res = None
	ass = ink.query.Asset(nomen.Cut(filePath))
	res = ass.GetLockInfos()
	return res

    def normalize_Name(self,filePath,ext):
	# /U/GRI/USERS/OFF/ASSETS/USECASE/GROOPERT/TEST111/LAYOUT/USECASE_GROOPERT_TEST111-LAYOUT_PRE_CONFIG.A7/0001/.MDA/.MDADATA
	# normalize name for Ink API => /USECASE/CINDYLOU/EDIT/NasK/USECASE_CINDYLOU_EDIT-NasK_Casting.a7
	filePath = "/".join(filePath.split('/')[6:]) 
	tmp =  filePath.split(ext)
	filePath = str(tmp[0])+str(ext)
	return filePath

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

    def start_Msg(self,searchName,directory,A7_typeSearch):
	print ' '
	print '===================================> [ ' + str(searchName) + ' ]  ' + str(directory) + ' search a7 [' + str(A7_typeSearch) + '] in progress, please wait ...'
	print ' '

    def end_Msg(self,startTimeInt,searchName,directory,A7_typeSearch):
	endTime = datetime.now()
	totTimeInt = endTime - self.startTimeInt
	#totTime = endTime - self.start_time
	print ' '
	print '=================================================\ '
	print '=================================================|> [ ' + str(searchName) + ' ]  ' + str(directory) + ' search a7 [' + str(A7_typeSearch) + '] DONE in ' + str(totTimeInt)
	print '=================================================/ '
	print ' '

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
	    ALL_USERS.append(user)
		            
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

def searchA7(type_process,with_locked,user):
    startTimeAll = datetime.now()
    print startTimeAll
    #print type(startTimeAll)
    ALL_USERS = [user]
    CURRENT_USER = ALL_USERS[0]
    #print ALL_USERS    
    
    def search_unpublished():
	for directory in INCLUDE_DIR_LOCKED:
	    directory = directory
	    START_DIR_UPB = START_DIR_OFF_LOCKED_A7 + '/' + directory
	    check = check_Path(START_DIR_UPB)
	    if check == True:
		args = [START_DIR_UPB,ALL_USERS,CURRENT_PROJECT_lower,START_DIR_LOCAL_LOCKED_A7,INCLUDE_DIR_LOCKED,EXCLUDE_DIR_USERS_LOCKED,INCLUDE_EXT_LOCKED,TMP_PATH_FILE,A7_typeSearch,CURRENT_USER,n_users_tot,startTimeAll]	    
		__THREAD__INSTANCE__(os.path.basename(__file__),args,type_process,with_locked)
	    else:
		print 'Invalid folder:' + str(START_DIR_UPB)
		    
    def search_locked_broken(): 
  	# exclude = set(EXCLUDE_DIR_USERS_LOCKED)
	for directory in INCLUDE_DIR_LOCKED:
	    directory = directory
	    START_DIR = START_DIR_OFF_LOCKED_A7 + '/' + directory
	    check = check_Path(START_DIR)
	    if check == True:
		args = [START_DIR,ALL_USERS,CURRENT_PROJECT_lower,START_DIR_LOCAL_LOCKED_A7,INCLUDE_DIR_LOCKED,EXCLUDE_DIR_USERS_LOCKED,INCLUDE_EXT_LOCKED,TMP_PATH_FILE,A7_typeSearch,CURRENT_USER,n_users_tot,startTimeAll]	    
		__THREAD__INSTANCE__(os.path.basename(__file__),args,type_process,with_locked)
	    else:
		print 'Invalid folder:' + str(START_DIR)
	  
  
    def search_A7(): 
  	# exclude = set(EXCLUDE_DIR_USERS_LOCKED)
	for directory in INCLUDE_DIR_LOCKED:
	    directory = directory
	    START_DIR = START_DIR_OFF_LOCKED_A7 + '/' + directory
	    check = check_Path(START_DIR)
	    if check == True:
		args = [START_DIR,ALL_USERS,CURRENT_PROJECT_lower,START_DIR_LOCAL_LOCKED_A7,INCLUDE_DIR_LOCKED,EXCLUDE_DIR_USERS_LOCKED,INCLUDE_EXT_LOCKED,TMP_PATH_FILE,A7_typeSearch,CURRENT_USER,n_users_tot,startTimeAll]	    
		__THREAD__INSTANCE__(os.path.basename(__file__),args,type_process,with_locked)
	    else:
		print 'Invalid folder:' + str(START_DIR)
  
  
    tps = ''
    if A7_typeSearch == 'lck':
	tps = 'Locked a7'
	TMP_PATH_FILE = TMP_PATH_FILE_LOCKED
    if A7_typeSearch == 'brk':
	tps = 'Broken a7'
	TMP_PATH_FILE = TMP_PATH_FILE_BROKEN
    if A7_typeSearch == 'upb':
	tps = 'unPublished a7'
	TMP_PATH_FILE = TMP_PATH_FILE_UNPUBLISHED
	
    msg = '\n----- Search '+tps+' Files, Work in Progress! Please wait ...\n'
    print msg
    print CURRENT_USER
    startTimeAll = datetime.now()
    print startTimeAll
    
    # exclude = set(EXCLUDE_DIR_USERS_LOCKED)
    
    '''
    if A7_typeSearch == 'upb':
	search_unpublished()	
    else:
	search_locked_broken()
    '''
	
    search_A7()
	
	
	
def check_threads():
    # print 'check_threads'
    try:
	while threading.activeCount() > 2:
	    # time.sleep(1)
	    n = threading.activeCount()
	    #print n

    except:
	print 'error'
	pass

def run(type_process,with_locked):
  
    deleteContent(TMP_PATH_FILE_LOCKED)
    deleteContent(TMP_PATH_FILE_BROKEN)
    deleteContent(TMP_PATH_FILE_UNPUBLISHED)
  
  
  
  
  
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
      f = open(TMP_PATH_FILE_UNPUBLISHED,'a')
      f.write(CURRENT_USER+'\n')
      f.close()


    if A7_typeSearch == 'lck':
      TMP_FILE_LOCKED = TMP_PATH_FILE_LOCKED
    if A7_typeSearch == 'brk':
      TMP_FILE_LOCKED = TMP_PATH_FILE_BROKEN
    if A7_typeSearch == 'upb':
      TMP_FILE_LOCKED = TMP_PATH_FILE_UNPUBLISHED  
    
  
  
  
  
  
  
    #print A7_typeSearch
    startTime = datetime.now()
  
    u = 0
    for user in USERS:
	#print user
	#ALL_USERS=[]
	#ALL_USERS=[user]
	searchA7(type_process,with_locked,user)
    check_threads()
    
    #endTime = datetime.now()
    #totTime = endTime - startTime
    #time.sleep(10)
    # print '###################################### DONE in ' + str(totTime)


# ############################################################################################################### VARS DONT TOUCH

CURRENT_USER = os.getenv('USER')

# ##################################################################### type search
A7_typeSearch	= 'lck'
if 'brk' in sys.argv or 'upb' in sys.argv or 'lck' in sys.argv:
    #============================== brk search
    try:
      if str(sys.argv[1])	== 'brk':
	  #CURRENT_USER 	= sys.argv[2]
	  A7_typeSearch = 'brk'
    except:
	pass
    try:
	if str(sys.argv[2])	== 'brk':
	    CURRENT_USER 	= sys.argv[1]    
	    A7_typeSearch	= 'brk'
    
    except:
	pass
    #============================== upb search
    try:
      if str(sys.argv[1])	== 'upb':
	  #CURRENT_USER 	= sys.argv[2]
	  A7_typeSearch = 'upb'
    except:
	pass
    try:
	if str(sys.argv[2])	== 'upb':
	    CURRENT_USER 	= sys.argv[1]
	    A7_typeSearch	= 'upb'	  
    except:
	pass
    #============================== lck search
    try:
      if str(sys.argv[1])	== 'lck':
	  #CURRENT_USER 	= sys.argv[2]
	  A7_typeSearch = 'lck'
    except:
	pass
    try:
	if str(sys.argv[2])	== 'lck':
	    CURRENT_USER 	= sys.argv[1]
	    A7_typeSearch	= 'lck'	  
    except:
	pass

# ##################################################################### path search optional
path_search = 'Default'
try:
    if '/' in  str(sys.argv[-1]):
	path_search = str(sys.argv[-1])[1:]
except:
    pass


# ##################################################################### other var

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
if CURRENT_PROJECT 		== 'PETS2':
  HOME_COLOR = ALL_PROJECTS['pets2']
  
START_DIR_USERS 		= '/u/'+CURRENT_PROJECT_lower+'/Users/'	    
START_DIR_PUBLIC 		= START_DIR_USERS+'COM/Presets/Graphs/'
START_DIR_LOCAL_LOCKED_A7 	= START_DIR_USERS+'COM/Assets'
START_DIR_OFF_LOCKED_A7 	= START_DIR_USERS+'OFF/Assets'

TMP_FILE_LOCKED			= 'A7_'+CURRENT_PROJECT+'_lockedBy.tmp'
TMP_FILE_BROKEN			= 'A7_'+CURRENT_PROJECT+'_brokenBy.tmp'
TMP_FILE_UPB			= 'A7_'+CURRENT_PROJECT+'_unPublishedBy.tmp'
EXCLUDE_DIR_USERS_LOCKED 	= ['COM','OFF','TMP','SVN','.SVN','REFS','PLUGINS','IMAGES','THUMBNAILS','OLD','DESIGN','MAPS','GIF','PSD','GRINCH','TEMPLATES','SHARED','CFX','Anim_Clip','REFS_XML','.FLAGS','MAL','.MDATRASH','MATTE','TOOLS']
#EXCLUDE_DIR_USERS_LOCKED 	= []
INCLUDE_DIR_LOCKED 		= [CURRENT_PROJECT,'LIB','LIBREF','MODELING','PREVIZ','USECASE','USECASEDEV','LINEUP','MLUN','SLUN']
if str(A7_typeSearch) == 'brk':
    INCLUDE_DIR_LOCKED 		= ['LIBREF']
if str(path_search) != 'Default':
    INCLUDE_DIR_LOCKED = [str(path_search)]

INCLUDE_EXT_LOCKED 		= ['CSV','XML','INKGRAPH','A7']
TMP_PATH_FILE_LOCKED 		= '/u/'+os.getenv('USER')+'/Public/'+str(TMP_FILE_LOCKED)
TMP_PATH_FILE_BROKEN 		= '/u/'+os.getenv('USER')+'/Public/'+str(TMP_FILE_BROKEN)
TMP_PATH_FILE_UNPUBLISHED 	= '/u/'+os.getenv('USER')+'/Public/'+str(TMP_FILE_UPB)

CHK_SEARCH_ALL  		= False

ALL_USERS = get_AllUsers()
n_users_tot = len(ALL_USERS)
#print ALL_USERS


'''
deleteContent(TMP_PATH_FILE_LOCKED)
deleteContent(TMP_PATH_FILE_BROKEN)
deleteContent(TMP_PATH_FILE_UNPUBLISHED)


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
  f = open(TMP_PATH_FILE_UNPUBLISHED,'a')
  f.write(CURRENT_USER+'\n')
  f.close()


if A7_typeSearch == 'lck':
  TMP_FILE_LOCKED = TMP_PATH_FILE_LOCKED
if A7_typeSearch == 'brk':
  TMP_FILE_LOCKED = TMP_PATH_FILE_BROKEN
if A7_typeSearch == 'upb':
  TMP_FILE_LOCKED = TMP_PATH_FILE_UNPUBLISHED
'''

# ############################################################################################################### VARIABLES  

#================================================ type of sharing ressources process | optional ( default stack ) 
# type_process = 'stack' 	# thread are executed in order
type_process = 'parallel'	# thread are executed simultaneous

#================================================ lock process | optional ( default True (longer) )
with_locked = False		# lock and wait end of run threading process function

#================================================



# ############################################################################################################### RUN 



run(type_process,with_locked)











