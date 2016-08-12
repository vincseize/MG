#!/usr/bin/env python

# ##################################################################################
# MG ILLUMINATION                                                                  #
# Author : cPOTTIER                                                                #
# Date : 12-08-2016                                                                #
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

#========== type of threading process
type_process = 'parallel'

#========== var(s) for threading process 1
var0 = 'grinch'
var1 = 'PETS'
args = [var0,var1]

#========== var(s) for threading process 2
xvar0 = 'lorax'
xvar1 = 'DM3'
xargs = [xvar0,xvar1]

#========== don t touch ==============================================

__Thread__class.__THREAD__INSTANCE__(type_process, args)
__Thread__class.__THREAD__INSTANCE__(type_process, xargs)
