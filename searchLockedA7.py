#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 30-08-2016                                                                #
# Search Locked A7                                                                 #
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

import threading
from threading import *
import Queue
from Queue import Queue
from multiprocessing import Pool, Process, Pipe, Lock, Value, Array, Manager, TimeoutError

#======================================================================================================================================================
import argparse
parser = argparse.ArgumentParser(description='login is optional | default is current login')
parser.add_argument('login',nargs='?')
parser.add_argument('brokenA7',nargs='?')
args = parser.parse_args()
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
	self.BROKENA7			= args[6]
	self.n_users_tot		= args[7]
	self.start_time			= args[8]
	# print self.USER_TO_SEARCH
	
	#self.USER_TO_SEARCH.append('nobody')

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
		    ext = 'a7'
		    '''
		    print filename
		    try:
			ext = os.path.splitext(filename)[1][1:]
		    except:
			pass 
		    ''' 
		    try:
 
			#print ext
			#if str(ext).upper() in self.INCLUDE_EXT_LOCKED :

		      
			#print self.USER_TO_SEARCH[0]
			#print ext
			  
			  
			  
			pathA7  = os.path.join(root, filename)
			#print pathA7
		      
		      
		      
			filePath = os.path.join(root, filename)
			result_array = self.splitall(filePath)
			#print result_array
			#if self.USER_TO_SEARCH[0] in result_array:
			    #print pathA7
			'''
			if '.mdu' in result_array and 'CINDYLOU' in result_array:
			    if self.USER_TO_SEARCH[0] in result_array:
				print pathA7	
			    '''
			  
			  
			# /U/GRI/USERS/OFF/ASSETS/USECASE/GROOPERT/TEST111/LAYOUT/USECASE_GROOPERT_TEST111-LAYOUT_PRE_CONFIG.A7/0001/.MDA/.MDADATA
			# ['/', 'u', 'gri', 'Users', 'OFF', 'Assets', 'USECASE', 'GROOPERT', 'Test111', 'Anim', 'USECASE_GROOPERT_Test111-Anim_Clip.a7', '0001', '.mda', '.mdaData']
			if self.USER_TO_SEARCH[0] in result_array:		#  	   and str(ext).upper() in str(result_array).upper()
			    #print pathA7
			  
			  
			  
			  
			  
			  
			  
			  
			  
			    # if str(ext).upper() in self.INCLUDE_EXT_LOCKED:
				
				#pathA7  = os.path.join(root, filename)
				# pathA7 = '/u/gri/Users/COM/Assets/USECASE/CINDYLOU/EDIT/NasK/USECASE_CINDYLOU_EDIT-NasK_Casting.a7'
				
				
				
				
			    if '.mdu' in result_array: 
				
				# print pathA7	
				

				
				
				
				
				
				
				
				result = None
				result = self.get_fileInfo(pathA7)	# ln link -> 
				# /u/gri/Users/OFF/Assets/USECASE/CINDYLOU/EDIT/NasK/USECASE_CINDYLOU_EDIT-NasK_Casting.a7/0003/USECASE_CINDYLOU_EDIT-NasK_Casting.a7
				infoWrite = result[0]
				infoOwner = result[1]
				#print result[0]
				#print result[1]

				# GRI_S0025_P0231-L-Occ_Render.a7

				if infoWrite == True and str(infoOwner) in str(self.USER_TO_SEARCH):				
				    
				    res = None
				      
				    # /U/GRI/USERS/OFF/ASSETS/USECASE/GROOPERT/TEST111/LAYOUT/USECASE_GROOPERT_TEST111-LAYOUT_PRE_CONFIG.A7/0001/.MDA/.MDADATA
				    filePath = "/".join(pathA7.split('/')[6:]) 
				    #print filePath
				    #print ext
				    tmp =  filePath.split(ext)
				    #print tmp
				    filePath = str(tmp[0])+str(ext)
				    #print filePath
				    # normalize name for Ink API => /USECASE/CINDYLOU/EDIT/NasK/USECASE_CINDYLOU_EDIT-NasK_Casting.a7
				    
				    ass = ink.query.Asset(nomen.Cut(filePath))
				    res = ass.GetLockInfos()
				    #print res

				    # assetLockedByMe, filesLockedByMe, assetLocked, assetLockOwner, filesLocked, filesLockOwner, assetBroken, assetStolen, filesBroken, filesStolen
				    # (True, True, True,   'cpottier', True, 'cpottier', False, False, False, False) => Grabbed
				    # (False, False, True, 'gamin'   , False, 'nobody', False, False, False, False) => locked

				    


				    if self.BROKENA7 == False:
					
					if res[3]==res[5]:
					    if res[3] in str(self.USER_TO_SEARCH):    
						matches.append(filePath)
						msg = '\n' + filePath + ' [ GRABBED by '+str(res[3])+' ]'
						print msg
					if res[3] in str(self.USER_TO_SEARCH):  
					    if res[2] == True:
						matches.append(filePath)
						msg = '\n' + filePath + ' [ LOCKED by '+str(res[3])+' ]'
						print msg
						
				    if self.BROKENA7 == True:
					  if res[6] == True:
					      matches.append(filePath)
					      msg = '\n' + filePath + ' [ BROCKEN ]'
					      print msg

		    except:
			# print 'error'
			pass

	    
	matches = list(set(matches))

	endTime = datetime.now()
	totTime = endTime - self.start_time

	print ' '
	print '===================================\ '
	print '====================================|> ' + str(self.directory) + ' search DONE in ' + str(totTime)
	print '===================================/ '	
	print str(len(matches)) + ' a7 Locked'
	print matches
	print ' '
	
	#print self.CURRENT_PROJECT_lower

	curPath = os.path.abspath('.')
	
	if len(matches) > 0 :
	    
	    try:
		TMP_FILE_LOCKED = str(curPath)+'/LOCKEDA7/'+str(self.CURRENT_PROJECT_lower)+'/'+str(self.TMP_PATH_FILE_LOCKED)
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
    tps = 'Locked-UnPublished'
    if BROKENA7 == True:
	tps = 'Broken'

    msg = '\n----- Search '+tps+' Files, Work in Progress! Please wait ...\n'
    print msg
    print ALL_USERS

    for directory in INCLUDE_DIR_LOCKED:
	#print directory
	startTimeAll = datetime.now()
	print startTimeAll
	# start_time = time.time()
	START_DIR = START_DIR_OFF_LOCKED_A7 + '/' + directory # first filter
	# START_DIR = START_DIR_LOCAL_LOCKED_A7+'/' + directory # for api Ink
	args = [START_DIR,ALL_USERS,CURRENT_PROJECT_lower,INCLUDE_DIR_LOCKED,INCLUDE_EXT_LOCKED,TMP_PATH_FILE_LOCKED,BROKENA7,n_users_tot,startTimeAll]
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
BROKENA7			= False
try:
    print sys.argv[1]
    if str(sys.argv[1])	== 'brokenA7':
	BROKENA7		= True
    else:
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
#INCLUDE_DIR_LOCKED 		= ['USECASE']
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


def get_fileInfo(source):
    # fileInfo   = getpwuid(stat(source).st_uid).pw_name
    # st = os.stat(source)
    infoWrite = os.access(source, os.R_OK)
    infoOwner = getpwuid(stat(source).st_uid).pw_name
    #print infoWrite
    #print infoOwner	
    return infoWrite, infoOwner






'''

filePath = '/u/gri/Users/COM/Assets/USECASE/CINDYLOU/EDIT/NasK/USECASE_CINDYLOU_EDIT-NasK_Casting.a7'
# (False, False, True, 'gamin', False, 'nobody', False, False, False, False) => LOCKED


result = get_fileInfo(filePath)	# ln link -> 
# /u/gri/Users/OFF/Assets/USECASE/CINDYLOU/EDIT/NasK/USECASE_CINDYLOU_EDIT-NasK_Casting.a7/0003/USECASE_CINDYLOU_EDIT-NasK_Casting.a7
infoWrite = result[0]
infoOwner = result[1]

filePath = 'USECASE/CINDYLOU/EDIT/NasK/USECASE_CINDYLOU_EDIT-NasK_Casting.a7'
ass = ink.query.Asset(nomen.Cut(filePath))
res = ass.GetLockInfos()
print res
print res[3]
'''
