#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 16-08-2016                                                                #
# Thread Sample Usage                                                              #
# ##################################################################################

import sys, os 

if '__Thread__class' in sys.modules:
    del(sys.modules["__Thread__class"])
    import __Thread__class
    from __Thread__class import * 
else:
    import __Thread__class
    from __Thread__class import *
    
#===================================================================================================

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
		
#=================================================================================================== 

    def your_function(self):
	'''Your Code Here'''
	import random
	from random import randint
	for arg in self.args:
	    for lettre in arg:
		print lettre
		delay = 0.05
		delay += random.randint(1, 60) / 100
		time.sleep(delay)

		
# ##################################################################################
# METHOD                                                                           #                                                               #                                                            #
# ##################################################################################

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

__Thread__class.__THREAD__INSTANCE__(args,type_process,with_locked) 	
__Thread__class.__THREAD__INSTANCE__(xargs,type_process,with_locked)



