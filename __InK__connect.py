# -*- coding: utf-8 -*-
'''   Globals variables  '''

# ##################################################################################
# MG ILLUMINATION                                                           	   #
# First Crazy Debroussailleur : jDepoortere                                        #
# Author : cPOTTIER                                                                #
# Date : 2016                                                                      #
# ##################################################################################

# Required modules
import graphs
import nomen
import ink.proto
import ink.query
import nask.sdk
import nask.sdk.casting
import nask.sdk.shots as shots
import nask.sdk.hit	
import proj.pipe.ink.graphs as prodgraphs
from subprocess import Popen, PIPE

# Optionals modules
import re 
import sys
import os 
import time
import datetime

# Globals
CONNECT_USER_INFOS      = ink.io.ConnectUserInfo()
CONNECT_USER0           = CONNECT_USER_INFOS[0]
CONNECT_USER1           = CONNECT_USER_INFOS[1] # todo to ask why ?
PROJECT                 = CONNECT_USER_INFOS[2].upper()
projectLower            = PROJECT.lower()
USER                    = CONNECT_USER_INFOS[1]
MAIL_HOSTNAME           = 'HOSTNAME.illum-mg.fr'
MAIL_USER               = USER+'@illum-mg.fr'
LOCALPATH               = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/'
