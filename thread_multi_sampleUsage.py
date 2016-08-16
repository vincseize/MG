#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 16-08-2016                                                                #
# Thread Sample Usage                                                              #
# ##################################################################################


#======================================================================= threads CLASSES dont touch
import sys, os, time 
import random
from random import randint

if '__Thread__class' in sys.modules:
    del(sys.modules["__Thread__class"])
    import __Thread__class
    from __Thread__class import * 
else:
    import __Thread__class
    from __Thread__class import *
    
# locked = RLock()
# workQueue = Queue.Queue(10)
#===================================================================================================


class __FUNCTIONS__TOTHREAD__():
  
    def __init__(self, args, with_locked=True):
        self.args = args
        self.with_locked = with_locked # True forced process ending before to execute the next
        self.run()

    def run(self):
	'''Dont Touch'''
	
	# print self.args # for debug
	
        i = 0
        while i < 2:
	  if self.with_locked == True:
	    with locked: 
		self.your_function()
	    i += 1

	  else:
	    self.your_function()
	    i += 1
	    
	  

    def your_function(self):
	'''Your Code'''
	for arg in self.args:
		for lettre in arg:
		    print lettre
		    delay = 0.05
		    delay += random.randint(1, 60) / 100
		    time.sleep(delay)
		



