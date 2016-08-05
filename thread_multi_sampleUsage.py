#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 05-08-2016                                                                #
# Thread Sample Usage                                                              #
# ##################################################################################


#=========================================================================================================================== threads CLASSES
import sys,os
if '__Thread__class' in sys.modules:
    del(sys.modules["__Thread__class"])
    import __Thread__class
    from __Thread__class import * 
else:
    import __Thread__class
    from __Thread__class import *
#===========================================================================================================================================


class run_myFunction_toThread():
    def __init__(self, args):
        self.args = args

    def myFunction_toThread(self):
	'''  '''
	msg = self.args[0]
	print msg



# __Thread__class.__THREAD__INSTANCE__('test4')
__Thread__class.__THREAD__INSTANCE__('test44')
