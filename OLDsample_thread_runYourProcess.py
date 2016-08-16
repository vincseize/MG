#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 16-08-2016                                                                #
# Thread Sample Usage                                                              #
# ##################################################################################


#============================================================================= threads CLASSES
import sys,os
if '__Thread__class' in sys.modules:
    del(sys.modules["__Thread__class"])
    import __Thread__class
    from __Thread__class import * 
else:
    import __Thread__class
    from __Thread__class import *
#=============================================================================================

#========================================================== type of sharing ressources process
# type_process = 'stack' 	# thread are executed in order
type_process = 'parallel'	# thread are executed simultaneous

#==================================================== lock process | optional ( default True )
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

#========== methode to run several functions =================================================

__Thread__class.__THREAD__INSTANCE__(args,type_process,with_locked) 	
__Thread__class.__THREAD__INSTANCE__(xargs,type_process,with_locked)

