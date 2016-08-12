#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 12-08-2016                                                                #
# Thread Sample Usage                                                              #
# ##################################################################################


#=================================================================================== threads CLASSES
import sys, os, time 
import random
from random import randint

import sys,os
if '__Thread__class' in sys.modules:
    del(sys.modules["__Thread__class"])
    import __Thread__class
    from __Thread__class import * 
else:
    import __Thread__class
    from __Thread__class import *
#===================================================================================================


class __FUNCTIONS__TOTHREAD__():
  
    def __init__(self, args):
        self.args = args
        self.run()

    def run(self):
	'''Your Code'''
	
	print self.args[0]
	print self.args[1]
	
        i = 0
        while i < 2:
	    for arg in self.args:
		for lettre in arg:
		    # sys.stdout.write(lettre)
		    # sys.stdout.flush()
		    print lettre
		    attente = 0.2
		    attente += random.randint(1, 60) / 100
		    time.sleep(attente)
		i += 1





