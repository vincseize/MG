# -*- coding: utf-8 -*-
'''     List of Samples Functions to learn  InK UI-API  - Verbose Documentation  '''

# ##################################################################################
# MG ILLUMINATION                                                           	     #
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

# QT modules
from PyQt4 import QtGui
import shutil
import string
import os
import subprocess
import collections
from collections import OrderedDict
import sip
from PyQt4 import QtGui,QtCore,QtOpenGL

# Optionals modules
import re 
import sys
import os 
import time
import datetime


# Globals
# PROJECT       = ink.io.ConnectUserInfo()[2].upper()
# projectLower  = PROJECT.lower()
# LOCALPATH     = '/u/'+projectLower+'/Users/'+ink.io.ConnectUserInfo()[1]+'/Presets/Graphs/'

CONNECT_USER_INFOS      = ink.io.ConnectUserInfo()
CONNECT_USER0           = CONNECT_USER_INFOS[0]
CONNECT_USER1           = CONNECT_USER_INFOS[1] # todo to ask why ?
PROJECT                 = CONNECT_USER_INFOS[2].upper()
projectLower            = PROJECT.lower()
USER                    = CONNECT_USER_INFOS[1]
MAIL_HOSTNAME           = 'HOSTNAME.illum-mg.fr'
MAIL_USER               = USER+'@illum-mg.fr'
LOCALPATH               = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/'

# Ink useful Classes
path_modules = "/u/"+projectLower+"/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples"
sys.path.append(path_modules)
# import __InK__classes
# # from __InK__classes import *
# from __InK__classes import __PIPEIN_GRAPH__
# from __InK__classes import _SENDMAIL


############################
#append path for tools qt
try:
  if 'sandboxQt' in sys.modules:
    del(sys.modules["sandboxQt"])
    import sandboxQt 
  else:
    import sandboxQt
except:
  pass


#===========================================================================================================================  CLASSES

# ######====================================================
# ###### GREAT, CLASSES ARE NOT VISIBLE IN UI, IT S COOL
# ######==================================================== 

# class __CONNECT_USER_INFOS__():

#     def __init__(self):
#         '''   '''
#         self.CONNECT_USER_INFOS      = ink.io.ConnectUserInfo()
#         self.CONNECT_USER0           = self.CONNECT_USER_INFOS[0]
#         self.CONNECT_USER1           = self.CONNECT_USER_INFOS[1] # todo to ask why ?
#         self.PROJECT                 = self.CONNECT_USER_INFOS[2]
#         self.projectLower            = self.PROJECT.lower()
#         self.USER                    = self.CONNECT_USER_INFOS[1]

#         self.MAIL_HOSTNAME           = 'HOSTNAME.illum-mg.fr'
#         self.MAIL_USER               = self.USER+'@illum-mg.fr'
#         self.LOCALPATH               = '/u/'+self.projectLower+'/Users/'+self.USER+'/Presets/Graphs/'

#=========================================================  SEND MAIL

# class _SENDMAIL():

#     hostname = MAIL_HOSTNAME

#     def __init__(self,mailTo,mailFrom,mailSubject,mailContent):
#         self.hostname = MAIL_HOSTNAME      
#         self.mailTo = mailTo
#         self.mailFrom = mailFrom
#         self.mailSubject = mailSubject
#         self.mailContent = mailContent
        
#     def sendmail(self):
#         return self.hostname,self.mailTo,self.mailFrom,self.mailSubject,self.mailContent

#=========================================================  CREATE READ UPDATE DELETE GRAPH




class __PIPEIN_GRAPH__():

    # debug_getSelected = 'getSelected'    

    def __init__(self,graphName,verbose=None):
        self.verbose 		= verbose
        self.graphName 		= graphName
        self.protoGraph		= ink.proto.Graph( self.graphName )
    

    def _IsAppQT(self):
        try:
            ink.qt.ui.app
            return True
        except (AttributeError, NameError):
            return False
        return None  

    def _GetPointOrig(self, gridUnit = None ):
        if not self._IsAppQT():
            import ink.ui.view
            gv = ink.ui.view.GetViews( "GraphView", ink.graph.CtxCurrId() )[0]
            if gv:
                if gridUnit is None:
                    gridUnit = ink.proto.Layout.GRID
                gvPivot = gv.GetDefaultShapePos()
                ox      = ( gvPivot[0] / float(gridUnit[0]) ) - ( 25.0 / float(gridUnit[0]) )
                oy      = ( gvPivot[1] / float(gridUnit[1]) ) - ( 25.0 / float(gridUnit[1]) )
                return ox, oy
        return ( 0, 0 )


    def saveGraph(self,graphPath,debug=False):
        ''' save Graph '''
        result = self.protoGraph.Write(graphPath, comment='', private=False)
        return result


    def getPosition(self,asset,layout):
        ''' get a7 position

            direction = [Medium, Bottom, Top]
        '''
        layout.LoadGraphPos([asset])
        A7Pos   = layout.GetPoint([asset], direction='M')
        return A7Pos


    def moveAsset(self,layout,sel,X,Y):
        layout.SetPos( sel, (X, Y) )
        self.protoGraph.Apply()
        result = self.protoGraph.Show(update=True)  # todo, to understand update = true
        return result


    def getSelected(self):
        result            = []
        protoGraph        = ink.proto.Graph( self.graphName )
        assetList     		= protoGraph.GetSelection( nomen.Filter().SetTypes(['.*']).SetStage('') ) # todo, to understand return Object list
        if not assetList:
            raise Exception('Class error : Please select at list one Asset !')  
        for asset in assetList:	
            assetName = asset.GetNomen() # all asset Infos
            result.append(assetName)
        # return assetList, self.verbose # todo , to understand return Objects
        return assetList, result, self.verbose


    def getA7_infos(self,pa,verbose=False):
        ''' get a7 infos 

        todo            - find all available infos
        '''

        nm_asset        = 'None' # 1
        nm_path         = 'None' # 2
        a_libname       = 'None' # 3
        a_name          = 'None' # 4
        a_family        = 'None' # 5
        a_typeFamily    = 'None' # 6 # cf SET
        a_catFamily     = 'None' # 7
        a_var           = 'None' # 8 # PROJECT cf GRINCH
        a_types         = 'None' # 9
        a_lod           = 'None' # 10
        a_version       = 'None' # 11     


        try:
            nm_asset      = pa.GetNomen() # 1
        except:
            pass
        try:
            nm_path       = pa.GetPath() # 2
        except:
            pass
        try:
            a_libname     = nm_asset.GetLib() # 3
        except:
            pass
        try:
            a_name        = nm_asset.GetName() # 4     
        except:
            pass
        try:
            a_family      = nm_asset.GetFamilies() # 5
        except:
            pass
        try:
            a_typeFamily  = nm_asset.GetFamilies()[0] # 6
        except:
            pass
        try:
            a_catFamily   = nm_asset.GetFamilies()[1] # 7
        except:
            pass
        try:
            a_var         = nm_asset.GetVar() # 8
        except:
            pass
        try:
            a_types       = nm_asset.GetTypes() # 9
        except:
            pass
        try:
            a_lod         = nm_asset.GetLod() # 10
        except:
            pass
        try:
            a_version     = nm_asset.GetVersion() # 11      
        except:
            pass

        #----------------------------------------------------------

        A7_infos = {}
        A7_infos['nm_asset']             = nm_asset         # 1
        A7_infos['nm_path']              = nm_path          # 2
        A7_infos['a_libname']            = a_libname        # 3
        A7_infos['a_name']               = a_name           # 4
        A7_infos['a_family']             = a_family         # 5
        A7_infos['a_typeFamily']         = a_typeFamily     # 6
        A7_infos['a_catFamily']          = a_catFamily      # 7
        A7_infos['a_var']                = a_var            # 8
        A7_infos['a_types']              = a_types          # 9
        A7_infos['a_lod']                = a_lod            # 10
        A7_infos['a_version']            = a_version        # 11
  
        #----------------------------------------------------------

        if verbose==True:
            print '-------------------- verbose -------------------'
            print 'pa : '             , pa
            print 'nm_asset : '       , nm_asset          # 1
            print 'nm_path : '        , nm_path           # 2
            print 'a_libname : '      , a_libname         # 3
            print 'a_name : '         , a_name            # 4
            print 'a_family : '       , a_family          # 5
            print 'a_typeFamily : '   , a_typeFamily      # 6
            print 'a_catFamily : '    , a_catFamily       # 7
            print 'a_var : '          , a_var             # 8
            print 'a_types : '        , a_types           # 9
            print 'a_lod : '          , a_lod             # 10
            print 'a_version : '      , a_version         # 11
            print '----------------------------------------------------'

        #----------------------------------------------------------

        return A7_infos


    def findA7(self,search,A7Select=False):
        '''search is a dictionnary''' 
        #search = {'families': ['CHARS', 'MAIN'], 'name': ['Grinch'], 'types': ['Shading']}
        print search      

    #######################################################################################

        def findFromList(searchList,asset):
            result = []
            for s in searchList:
                check = False
                if s in asset:
                    check = True           
                result.append(check)
            return result

    ######################################################################################

        searchName      = search.get("name")
        searchTypes     = search.get("types")
        searchFamilies  = search.get("families")

        assetList       = []
        selList         = self.protoGraph.GetSelection()

        for asset in selList:

            # proto = asset
            # print proto

            checkAll      = []     

            assetName     = asset.GetNomen().GetName() # list
            assetFamilies = asset.GetNomen().GetFamilies() # list
            assetTypes    = asset.GetNomen().GetTypes() # list
       
            checkName     =findFromList(searchName,assetName) # todo, if no searchName
            checkTypes    =findFromList(searchTypes,assetTypes) # todo, if no searchTypes        
            checkFamilies =findFromList(searchFamilies,assetFamilies) # todo, if no searchFamilies

            checkAll.append(checkName)
            checkAll.append(checkTypes)
            checkAll.append(checkFamilies)

            tmpCheck = []
            for item in checkAll:
                if True in item:
                    tmpCheck.append(True) 

            if len(tmpCheck)==len(checkAll):
                assetList.append(asset)

            if A7Select == True:
                self.protoGraph.SetSelection(assetList, selectionMode = ink.proto.SEL_ADD, clearBeforeOp = ink.proto.SEL_CLEAR)


        return assetList, self.verbose


    def add_File(self, ext='ma', suffix='', mgDir='', type='SingleFile', properties='{}' ): 
      ''' Ajoute un fichier a une selection d'assets '''

      ext         = graphs.__GetArgStr( ext )
      suffix      = graphs.__GetArgStr( suffix )
      mgDir       = graphs.__GetArgStr( mgDir )
      _type       = graphs.__GetArgMdaType( type )
      properties  = graphs.__GetArgStr( properties )
      
      g       = ink.proto.Graph('Test')
      selList = g.GetSelection()
      
      for pa in selList:
          pa.AddFile( ext, suffix=suffix, mgDir=mgDir, type=_type, properties=properties )  # un fichier msg minimal est a associer obligatoirement
      
      result  = g.Apply()
      
      return result


    def add_A7(self,_type,A7List,A7Select=False,A7position=False):
        ''' Add Asset 
        
        _type       : -dirPath- or -NewLib-
        A7          : -str- -list- or -dictionnary
        A7Select    : select .a7                        [optional] 
        A7position  : move .a7, need A7Select           [optional]

        todo : - check if not self.protograph

        '''

        result    = None
        assetList = None

        if str(_type) == 'dirPath':
        #---------------------------------------------------------
        #------ add A7 from path
        #---------------------------------------------------------

            #------ case 1 : only one A7 as string
            if type(A7List) == type(str()):
                A7      = A7List
                A7List  = []
                A7List.append(A7)
            #------ case 2 : A7 list
            if type(A7List[0]) == type(str()):
                for A7 in A7List:
                    ql  = ink.query.Dir(dirPath=A7, rootCom=True) # todo understand rootCom
                    for q in ql :
                        qa = ink.query.Asset.FromProto( self.protoGraph.Add( q.GetNomen() ) ) 
                        qa_EditAction = qa.GetEditAction()
                        qa_Downs      = qa.DownLinksInfos()
                        qa_Ups        = qa.UpLinksInfos()
                        # print qa_EditAction,qa_Downs,qa_Ups -> todo to understand
                #------ select A7
                        if A7Select == True:
                            for proto in self.protoGraph:
                                self.protoGraph.SetSelection([proto])
                #------ positionne A7, need to be selected
                            if A7position != False:
                              X = A7position[0]
                              Y = A7position[1]
                              layout = self.protoGraph.GetLayout()
                              self.moveAsset(layout,proto,X,Y)
            #------ case 3 : A7 dictionnary -> Todo
            if type(A7List[0]) == type(dict()):
                print type(A7List[0])


        if str(_type) == 'NewLib':
        #---------------------------------------------------------
        #------ add A7 from NewLib method todo
        #---------------------------------------------------------
            print 'to test wip'
            # ScoutOk  = nomen.Nomen.NewLib( lib='LIB', name='XNAMEX', family=['SET'], var='XNAMEX', types=['Shading'], stage='' )
            # ScoutOkProto  = protoGraphToClone.Add(ScoutOk)
        #---------------------------------------------------------
        #------ apply graph
        #---------------------------------------------------------
        self.protoGraph.Apply()
        self.protoGraph.Show(update=True)  # todo, to understand update = true
        result = self.protoGraph
        assetList = self.protoGraph.List()
        # self.protoGraph.SelectAll()

        #---------------------------------------------------------
        #------ return results
        #---------------------------------------------------------
        return result, assetList, self.verbose


    def _Filters(self,Filters,verbose=None):
        '''   
        Filters as dic : {'libname': ['LIB', 'LIBDEV', 'LIBREF'], 'family': ['CHARS', 'MAIN'], 'type': ['Model'] ... }

        todo            - dics XFilters cf niFilterOpt=FILTER_ONLY , to understand before
                        - dics find and add all existing Filters
        '''
        
        niFilters = nomen.Nomen.Empty()

        if Filters.get('type'):
            niFilters =  niFilters.SetTypes(Filters.get('type'))
        if Filters.get('family'):
            niFilters =  niFilters.SetFamilies(Filters.get('family'))
        if Filters.get('stage'):
            niFilters =  niFilters.SetStage(Filters.get('stage'))

        return niFilters


    def GetStreams(self,typeStreams,protoGraph,layout,assetProto,Filters=None,A7pos=None,verbose=False):
        ''' Show Streams 
        
        typeStreams    : -GetDownstreams- -GetUpstreams-
        Filters as dic : {'libname': ['LIB', 'LIBDEV', 'LIBREF'], 'family': ['CHARS', 'MAIN'], 'type': ['Model'] ... }

        '''

        niFilters = self._Filters(Filters)

        if typeStreams == 'GetDownstreams':
            StreamProtoList = protoGraph.GetDownstreams( assetProto, niFilter=niFilters)
        if typeStreams == 'GetUpstreams':
            StreamProtoList = protoGraph.GetUpstreams( assetProto, niFilter=niFilters)
        # if typeStreams == 'GetUpstreams':
        #     for pa in StreamProtoList:            
        #         if A7pos != None: # todo better
        #             X_pos = A7pos[0]-2
        #             Y_pos = A7pos[1]                    
        #             layout.SetPos(pa, (X_pos,Y_pos) )

        #---------------------------------------------------------
        #------ apply graph
        #---------------------------------------------------------
        self.protoGraph.Apply()
        self.protoGraph.Show(update=True)  # todo, to understand update = true

        for pa in StreamProtoList:
            self.getA7_infos(pa,verbose)

        return StreamProtoList


    def move_StreamProtoList(self,n_streams,StreamProtoList,layout,A7refPos,params_get):
        ''' UI stream a7 re-organisation '''

        # PARAMS MODIFIABLES ###########################################################################################

        offset_X                = 3 # relative to X origin a7 ref - can be negative
        offset_Y                = 2 # relative to Y origin a7 ref - can be negativeInK

        ecart_a7_X              = 4 # X space between streams a7  
        ecart_a7_Y              = 2 # Y space between streams a7

        n_A7_perColumn          = 6    # max n streams  vertically   - None for not Used
        n_A7_perRow             = None # max n streams horizontally  - None for not Used
        X_space_betweenColumns  = 7

        quinconce               = False # boolean, decale les a7 une fois sur 2
        quinconce_X             = 0.5 # x offset, 0.5/-0.5 left-right, min max
        quinconce_start         = 0 # switch first quinconce_X value to modulo 0.5 to -0.5

        n_col_byGroup           = 2 # n column by a7 grouped - None for not Used
        X_space_betweenGroup    = 10 # subjectif, to do better in relation with n assets, n group etc 
        n_groups_grouped        = None # todo paquet de groups  - None for not Used

        # DON T TOUCH =========================================================

        params = {}
        params['offset_X']                  = offset_X
        params['offset_Y']                  = offset_Y
        params['ecart_a7_X']                = ecart_a7_X
        params['ecart_a7_Y']                = ecart_a7_Y

        params['n_A7_perColumn']            = n_A7_perColumn
        params['n_A7_perRow']               = n_A7_perRow
        params['X_space_betweenColumns']    = X_space_betweenColumns

        params['quinconce']                 = quinconce
        params['quinconce_X']               = quinconce_X
        params['quinconce_start']           = quinconce_start # todo

        params['n_col_byGroup']             = n_col_byGroup
        params['X_space_betweenGroup']      = X_space_betweenGroup
        params['n_groups_grouped']          = n_groups_grouped

        if params_get != None :

            if 'offset_X' in params_get.keys() : 
                params['offset_X']                      = params_get['offset_X']
            if 'offset_Y' in params_get.keys() : 
                params['offset_Y']                      = params_get['offset_Y']
            if 'ecart_a7_X' in params_get.keys() : 
                params['ecart_a7_X']                    = params_get['ecart_a7_X']
            if 'ecart_a7_Y' in params_get.keys() : 
                params['ecart_a7_Y']                    = params_get['ecart_a7_Y']

            if 'n_A7_perColumn' in params_get.keys() : 
                params['n_A7_perColumn']                = params_get['n_A7_perColumn']
            if 'n_A7_perRow' in params_get.keys() : 
                params['n_A7_perRow']                   = params_get['n_A7_perRow']
            if 'X_space_betweenColumns' in params_get.keys() : 
                params['X_space_betweenColumns']        = params_get['X_space_betweenColumns']

            if 'quinconce' in params_get.keys() : 
                params['quinconce']                     = params_get['quinconce']
            if 'quinconce_X' in params_get.keys() : 
                params['quinconce_X']                   = params_get['quinconce_X']
            if 'quinconce_start' in params_get.keys() : 
                params['quinconce_start']               = params_get['quinconce_start']

            if 'n_col_byGroup' in params_get.keys() : 
                params['n_col_byGroup']                 = params_get['n_col_byGroup']
            if 'X_space_betweenGroup' in params_get.keys() : 
                params['X_space_betweenGroup']          = params_get['X_space_betweenGroup']
            if 'n_groups_grouped' in params_get.keys() : 
                params['n_groups_grouped']              = params_get['n_groups_grouped']

        ################################################################################################################

        #------------------------------------------------------------------------------------ gestion n a7 per col
        tb_n_column = []
        for i in range(n_streams): 
            tb_n_column.append(params['n_A7_perColumn']*i)
        #--------------------------------------------------------------------------------- gestion n col per group
        tb_n_group = []
        for i in range(n_streams): 
            tb_n_group.append(params['n_col_byGroup']*i)
        #------------------------------------------------------------------------------------------ init variables
        n               = 0
        inc_X           = 0
        inc_Y           = 0
        inc_n_column    = 0
        X_ecart_group   = 0
        A7refPos_X      = A7refPos[0]
        A7refPos_Y      = A7refPos[1]        
        if params['quinconce'] == False:
            quinconce_X = 0 

        # BOUCLE sur liste a7 =========================================================================================

        for pa in StreamProtoList:
            
            #------------------------------------------------------------------------ a7 pos not used at this time            
            A7Pos             = self.getPosition(pa,layout)
            A7Pos_X           = A7Pos[0]
            A7Pos_Y           = A7Pos[1]

            #------------------------------------------------------------------------------------------- quinconce
            if quinconce == True:
                q = params['quinconce_X']
                quinconce_X = q * -1

            #---------------------------------------------------------------------------------------- apply offset 
            X_move_RelToA7    = A7refPos_X + params['offset_X'] + inc_X + quinconce_X
            Y_move_RelToA7    = A7refPos_Y + params['offset_Y'] + inc_Y
            layout.SetPos(pa, (X_move_RelToA7, Y_move_RelToA7) )

            #-------------------------------------------------------------------------------------- Incrementation 
            n += 1
            inc_Y = inc_Y + params['ecart_a7_Y']

            #------------------------------------------------------------------------------------- n a7 per Column
            if n in tb_n_column :
                inc_Y = 0
                inc_X = inc_X + params['ecart_a7_X'] + params['X_space_betweenColumns'] 
                inc_n_column += 1
                #---------------------------------------------------------------------------------- gestion Groups
                if inc_n_column in tb_n_group:
                    inc_X = inc_X + params['ecart_a7_X'] + params['X_space_betweenGroup'] 

        #-------------------------------------- Apply ---------------------------------------------------------------#

        protoGraph.Show()
        protoGraph.Apply()
        protoGraph.SelectAll()










#==== End __PIPEIN_GRAPH__ =================================================================================================================================================================#


  
#==== End classes  

#================================================================================================================================================
# Classe de connection
# __CONNECT_USER_INFOS    = __CONNECT_USER_INFOS__()

# Classe PIPE-IN TOOZ
protoGraph              = ink.proto.Graph( graphs.DEFAULT )
__PIPEIN_GRAPH          = __PIPEIN_GRAPH__(graphs.DEFAULT, None) # protograph, verbose mode
#================================================================================================================================================











#===========================================================================================================================  PART 1 , UI LOGICAL

  # BASICS
  # TOOLS NAME COME FROM FUNCTIONS NAME
  # IMPORTANT HACK
  # DEFAULT CATEGORIES ORDER IS ALPHABETICAL FUNCTION NAME INSIDE (IF NO CATEGORY, NAME.py IS THE NAME OF CATEGORY)


def K01_SAMPLE_1(): 
  # Function Name give the Tool Name visible in Ink Interface
  # The description give the mouseover information in Ink Interface
  ''' LAST sandbox.py UPDATE 01-02-2016 '''
  print 'KANGOOROO' # print in Out log Result Window AND InK Konsole after Run Action
  
#=========================== UI
K01_SAMPLE_1.__position__            = 1                       # order of the tool in th category
K01_SAMPLE_1.__category__            = 'A_FIRST SAMPLES'       # comment this line to understand default category
K01_SAMPLE_1.__author__              = 'Karlova' 


def K01_SAMPLE_2():
  ''' 
  KANGOROO TOOL 
  
  Description : Some samples to understand InK UI logical
  '''
  print 'KANGOROO' # print KANGOROO Dialog Result Window AND in InK Konsole after Run Action
  
  
#=========================== UI
K01_SAMPLE_2.__position__            = 2							                                 # todo to understand
#K01_SAMPLE_2.__toolDesc__           = ( 002, 'kroumch', 'audioIcon.png', 'Pipe', '' )	 # todo to understand
K01_SAMPLE_2.__icon__                = 'pipe/createGraphOccLight.png'
K01_SAMPLE_2.__category__            = 'A_FIRST SAMPLES'
K01_SAMPLE_2.__author__              = 'Le Baron Rouge'
K01_SAMPLE_2.__shortText__           = 'Icon Title'					                           # Text write on Icon Tool




#===========================================================================================================================  PART 2 , UI CONSTRUCTION


def K02_UI_CONSTRUCT(Action1='Var_Name', Action2=0, Action3=0, Action4=True, Action5=True, Action6=True):
  ''' UI CONSTRUCTION SAMPLE 

      - Order of items are relative to order declaration in the function:
        def K02_UI_CONSTRUCT(Action1='Var_Name', Action2=0, Action3=0, Action4=True, Action5=True, Action6=True):
  '''
  
#=========================== UI
K02_UI_CONSTRUCT.__category__         = 'B - UI'
K02_UI_CONSTRUCT.__author__           = 'cpottier'
K02_UI_CONSTRUCT.__textColor__        = '#7cfc00'
K02_UI_CONSTRUCT.__paramsType__       = {
   'Action1'       :  ( 'enum', 'Var_Name',['Item1', 'Item2', 'Item3'] ),
   'Action2'        :  ( 'int', '0'  ),
   'Action3'        :  ( 'int' , '0' ),
   'Action4'        :  ( 'bool', 'True' , ['True4', 'False4']  ),
   'Action5'        :  ( 'bool', 'False' , ['True5', 'False5']  ),   
   'Action6'       :  ( 'bool', 'False' , ['True6', 'False6']  )
   
}


def K03_UI_CONSTRUCT_QT(Action1='Var_Name'):
  ''' UI QT CONSTRUCTION SAMPLE '''
  
  def printFromQT():
    print 'printFromQT'


#=========================== UI
K03_UI_CONSTRUCT_QT.__category__         = 'B - UI'
K03_UI_CONSTRUCT_QT.__author__           = 'cpottier'
K03_UI_CONSTRUCT_QT.__textColor__        = '#7cfcaa'
K03_UI_CONSTRUCT_QT.__customTool__       = 'sandboxQt'


#===========================================================================================================================  PART 3 , ASSETS INFOS


def K04_GET_SELECTED_ASSETS_INFOS(AllAssetInfos=True):
  ''' 
  - GET SELECTED ASSET(S) INFOS SAMPLE
  - CHECKBOX SAMPLE
  '''
  
  move_X = -16
  move_Y = -16

  protoGraph = ink.proto.Graph('K04_GET_SELECTED_ASSETS_INFOS')
  layout = protoGraph.GetLayout()
  selection  = protoGraph.GetSelection( nomen.Filter())
  assetList=[]
  # todo better , push asset infos stream in dictionnary      
      
  if not selection:
    raise Exception('Please select an asset !')  

  if selection:
    print ''
    print '=================== SELECTED ASSET(S) ==================='
    print ''
    for asset in selection:
      assetList.append(asset)
      

  for A7 in assetList: 
    assetPath     = A7.GetPath()
    assetName     = A7.GetNomen()
    # a_type        = nm_asset.GetType() # todo      
    a_libname     = assetName.GetLib()
    a_name        = assetName.GetName()      
    a_family      = assetName.GetFamilies()
    a_typeFamily  = assetName.GetFamilies()[0] # cf SET
    a_catFamily   = assetName.GetFamilies()[1] # 
    a_var         = assetName.GetVar() # PROJECT cf GRINCH
    a_types       = assetName.GetTypes()
    a_lod         = assetName.GetLod()
    a_version     = assetName.GetVersion() 

    # get position 
    layout.LoadGraphPos([assetName])
    position = layout.GetPos(assetName)

    # move position
    # layout.SetPos(A7, (move_X,move_Y))  # to move it relative to Absolute 0 0 graph origin
    # protoGraph.Show()
    # protoGraph.Apply()

    print '------------------------------------------------------------------------------------------------------------------------------------'    
    print assetName
    print '------------------------------------------------------------------------------------------------------------------------------------'

    print '-----> A7 GetPath: '                   , assetPath
    print '-----> A7 GetNomen: '                  , assetName
    # print '-----> A7 GetType: '                 , a_type
    print '-----> A7 GetLib: '                    , a_libname
    print '-----> A7 GetName: '                   , a_name
    print '-----> A7 GetFamilies: '               , a_family
    print '-----> A7 typeFamily: '                , a_typeFamily
    print '-----> A7 catFamily: '                 , a_catFamily    
    print '-----> A7 GetVar: '                    , a_var
    print '-----> A7 GetTypes: '                  , a_types
    print '-----> A7 GetLod: '                    , a_lod
    print '-----> A7 GetVersion: '                , a_version

    print '-----> A7 Graph Position: '            , position
    # get streams
    if AllAssetInfos is 'True': # Checkbox is checked
      for infos in protoGraph.GetUpstreams(A7):
        Stream     = infos.GetNomen() 
        StreamName   = Stream.GetName()
        StreamFamily = Stream.GetFamilies()
        StreamVariation = Stream.GetVar()
        StreamType = Stream.GetTypes() 

        print ''
        print assetName
        print '-----> Linked Stream(s) : '        , Stream      
        print '                                          name type : '         , StreamName 
        print '                                          family : '            , StreamFamily 
        print '                                          variation : '         , StreamVariation      
        print '                                          type : '              , StreamType


    print ''
  
  
#=========================== UI
# K04_GET_SELECTED_ASSETS_INFOS.__position__         = 4
K04_GET_SELECTED_ASSETS_INFOS.__category__         = 'C - ASSET INFOS'
K04_GET_SELECTED_ASSETS_INFOS.__author__           = 'cpottier'
K04_GET_SELECTED_ASSETS_INFOS.__paramsType__        = {  
   'AllAssetInfos'       :  ( 'bool', 'True' , ['True', 'Minimal']  )
}



def K05_UI_ADD_ASSET_FROM_PATH(selected='False'):
  ''' Open a blank Context

  - ADD Paint-Maps ASSET from path
  - 2 differents method for selection
  '''

  A7path = 'LIB/MATERIALS/Paint/Maps/Paint-Maps.a7'

  protoGraph = ink.proto.Graph('Default')

  ql  = ink.query.Dir(dirPath=A7path, rootCom=True)
  for q in ql :
    qa = ink.query.Asset.FromProto( protoGraph.Add( q.GetNomen() ) ) 
    asset = q.GetNomen()

  protoGraph.Show()
  protoGraph.Apply()

  if selected=='True':

    # selection method 1 , you have perhaps to run 2 times this solution
    # print protoGraph.List() # premiere approche entre objet InK
    # print protoGraph.List()[0] # et equivalent getNomen
    # proto = protoGraph.List()[0]
    # protoGraph.SetSelection([proto])

    # selection method 2
    for proto in protoGraph:
      protoGraph.SetSelection([proto])
      protoGraph.Show()
      protoGraph.Apply()

  # selection method 3 , selection again hack, todo find why
  proto = protoGraph.List()[0]
  protoGraph.SetSelection([proto])

  protoGraph.Show()
  protoGraph.Apply()

#=========================== UI
K05_UI_ADD_ASSET_FROM_PATH.__category__         = 'D - ASSET INTERACTION'
K05_UI_ADD_ASSET_FROM_PATH.__author__           = 'cpottier'
K05_UI_ADD_ASSET_FROM_PATH.__paramsType__        = {  
   'selected'       :  ( 'bool', 'True' , ['True', 'False']  )
}


def K06_UI_ADD_ASSET_FROM_NEWLIB():
  ''' Open a blank Context

  - ADD Paint-Maps ASSET from .NewLib Method
  '''

  protoGraph  = ink.proto.Graph('Default')

  A7lib       = nomen.Nomen.NewLib( lib='LIB', name='Paint', family=['MATERIALS'], types='Maps', stage='' )
  A7libProto  = protoGraph.Add(A7lib)
  A7libProto.AddFile('mgs')  # un fichier msg minimal est a associer obligatoirement

  print protoGraph.List()

  for proto in protoGraph:
    protoGraph.SetSelection([proto])
    protoGraph.Show()
    protoGraph.Apply()
  # selection again hack, todo find why
  proto = protoGraph.List()[0]
  protoGraph.SetSelection([proto])
  protoGraph.Show()
  protoGraph.Apply()



#=========================== UI
K06_UI_ADD_ASSET_FROM_NEWLIB.__category__         = 'D - ASSET INTERACTION'
K06_UI_ADD_ASSET_FROM_NEWLIB.__author__           = 'cpottier'



def K07_UI_CLONE_ASSET():
  ''' Add an A7 ['SHADING'] and Clone it '''

  protoGraph          = ink.proto.Graph('Default')
  protoGraphToClone   = protoGraph

  layout = protoGraph.GetLayout()

  A7libToClone        = nomen.Nomen.NewLib( lib='LIB', name='A7fromNewLib', family=['MATERIALS'], types='Maps', stage='' )
  A7libToCloneProto   = protoGraph.Add(A7libToClone)
  A7libToCloneProto.AddFile('mgs')  # un fichier msg minimal est a associer obligatoirement
  
  for proto in protoGraph:
    protoGraph.SetSelection([proto])
    protoGraph.Show()
    protoGraph.Apply()
  # selection again hack, todo find why
  proto = protoGraph.List()[0]
  protoGraph.SetSelection([proto])
  protoGraph.Show()
  protoGraph.Apply()

  # A7 need to be selected
  selection  = protoGraphToClone.GetSelection( nomen.Filter())
  assetList=[]
  assetList.append(selection)
  # todo better , push asset infos stream in dictionnary      

  if not selection:
    raise Exception('Please select an .a7 !')  

  for proto in selection: 

    ###############################################################################
    #------------------------------------------------------------------------------
    #------ Creation graphe dans lequel on met le resultat du clone
    #------------------------------------------------------------------------------
    ###############################################################################
    protoGraphResultClone = ink.proto.Graph('protoGraph Result du Clone') # les noms de graphes peuvent comporter des espaces

    assetPath     = proto.GetPath() # no path etc, because asset is created from scratch
    assetName     = proto.GetNomen()    
    a_libname     = assetName.GetLib()
    a_name        = assetName.GetName()      
    # a_family      = assetName.GetFamilies() # no family etc, because asset is created from scratch
    # a_typeFamily  = assetName.GetFamilies()[0] # cf SET
    # a_catFamily   = assetName.GetFamilies()[1] # 
    # a_var         = assetName.GetVar() # PROJECT cf GRINCH
    # a_types       = assetName.GetTypes()
    # a_lod         = assetName.GetLod()
    # a_version     = assetName.GetVersion()

    clone_name = 'MY_CLONE_'+a_name # todo, with my Name


    mycloneparam = nomen.Filter()
    mycloneparam.SetLib('LIB')
    mycloneparam.SetName(a_name)
    mycloneparam.SetFamilies(['SHADING'])

    protoGraphResultClone.Clone(protoGraphToClone, mycloneparam, substInFile=False, forceCopy=False, copyUBLinks=True)

    # move cloned A7 position
    layout = protoGraphResultClone.GetLayout()
    layout.SetPos( protoGraphResultClone.List()[0], (0, -2) )

    protoGraphResultClone.Apply()
    protoGraphResultClone.SelectAll()


  protoGraph.Show()
  protoGraph.Apply()

#=========================== UI
K07_UI_CLONE_ASSET.__category__         = 'D - ASSET INTERACTION'
K07_UI_CLONE_ASSET.__author__           = 'cpottier'




def K08_UI_ASSETS_MOVE():
  ''' 
  - MOVE SELECTED ASSET(S)
  '''

  move_X = -16
  move_Y = -16

  protoGraph = ink.proto.Graph('Default')
  layout = protoGraph.GetLayout()
  selection  = protoGraph.GetSelection( nomen.Filter())
  assetList=[]
  # todo better , push asset infos stream in dictionnary      
      
  if not selection:
    raise Exception('Please select an asset !')  

  if selection:
    print ''
    print '=================== SELECTED ASSET(S) ==================='
    print ''
    for asset in selection:
      assetList.append(asset)
      

  for A7 in assetList: 
    assetPath     = A7.GetPath()
    assetName     = A7.GetNomen()
    print assetName

    # get position 
    # layout.LoadGraphPos([assetName])
    # position = layout.GetPos(assetName)

    # move position
    layout.SetPos(A7, (move_X,move_Y))  # to move it relative to Absolute 0 0 graph origin
    protoGraph.Show()
    protoGraph.Apply()

#=========================== UI
K08_UI_ASSETS_MOVE.__category__         = 'D - ASSET INTERACTION'
K08_UI_ASSETS_MOVE.__author__           = 'cpottier'


def K09_UI_ADD_MOVE_ASSET_REL_TO_ANOTHER():
  ''' 
  - MOVE ASSET RELATIVE TO SELECTED ASSET
  '''

  move_X = 0
  move_Y = -2

  protoGraph = ink.proto.Graph('Default')
  layout = protoGraph.GetLayout()
  selection  = protoGraph.GetSelection( nomen.Filter())
        
  if not selection:
    raise Exception('Please select an asset !')  

  if selection:
    for pa in selection:
      nmChar = pa.GetNomen()
      myname    = nmChar.GetName()
      myfamily  = nmChar.GetFamilies()
      myVar     = nmChar.GetVar()
      myTypes   = nmChar.GetTypes()
      myVersion = nmChar.GetVersion()

      A7toMove        = nomen.Nomen.NewLib( lib='LIB', name='A7toMoveRelative', family=['MATERIALS'], types='Maps', stage='' )
      A7toMoveProto   = protoGraph.Add(A7toMove)
      A7toMoveProto.AddFile('mgs')  # un fichier msg minimal est a associer obligatoirement

      # get ref a7 position
      layout.LoadGraphPos([pa])
      selPos = layout.GetPoint([selection[0]], direction='M') # todo, to understand M, B, T options
      sel_X = selPos[0]
      sel_Y = selPos[1]

      # move position
      # layout.SetPos(A7toMoveProto, (move_X+sel_X,move_Y+sel_Y))  # to move it relative to Absolute 0 0 graph origin
      protoGraph.Show()
      protoGraph.Apply()

  protoGraph.Show()
  protoGraph.Apply()


#=========================== UI
K09_UI_ADD_MOVE_ASSET_REL_TO_ANOTHER.__category__         = 'D - ASSET INTERACTION'
K09_UI_ADD_MOVE_ASSET_REL_TO_ANOTHER.__author__           = 'cpottier'

#===========================================================================================================================  CLASS CRUD


def K10_CLASS_CRUD(getAssetsInfos1='True',getAssetsInfos2='Wip',assetToAdd='LIB/MATERIALS/Paint/Maps/Paint-Maps.a7',addA7='True',findA7='True',XNAMEX='XNAMEX-Shading_Shots_Scout.a7', shotList='', castType='Actor', castStage='Ok', shotType='Anim', libName='LIB', familyList='CHARS,PROPS,SETS', update=True, select=True):
  ''' 
  CLASS GENERIC - LAST UPDATE 21-01-2016
      - CRUD () CREATE READ UPDATE DELETE ) WIP
      - Some generics functions in One Class
  '''  
  
  if addA7 is 'True': # checkbox is checked
    print '------------------------------------------------ _Class add A7 from List'  
    ######====================================================
    ###### ADD A7 [List] From Class
    ######==================================================== 
    
    A7List = ['LIB/MATERIALS/Paint/Maps/Paint-Maps.a7']
    __PIPEIN_GRAPH = __PIPEIN_GRAPH__('K10_CLASS_CRUD')
    result = __PIPEIN_GRAPH.add_A7('dirPath',A7List,True) # _type, A7(str,list,dic), A7Select[optional], A7position[optional]
    AssetList = result[0] # return infos, not usable
    inkProtoAssetList = result[1] # return object list
    verbose = result[2] # result[2] is verbose
  
  
  if getAssetsInfos1 is 'True': # checkbox is checked
    print '------------------------------------------------ _Class Get all selections infos'  
    ######====================================================
    ###### Get all selections infos From Class
    ######==================================================== 
    
    # __PIPEIN_GRAPH = __PIPEIN_GRAPH__('K10_CLASS_CRUD','getSelected') #  graphName, verbose for debug
    __PIPEIN_GRAPH = __PIPEIN_GRAPH__('K10_CLASS_CRUD')
    result = __PIPEIN_GRAPH.getSelected()
    inkProtoAssetList = result[0] # return object list
    AssetList = result[1] # return Name List
    verbose = result[2] # result[2] is verbose
    for asset in AssetList: 
      print asset


  if findA7 is 'True': # checkbox is checked
    print '------------------------------------------------ _Class find A7 ' 
    ######====================================================
    ###### Find A7 From Class
    ######==================================================== 
    search = {}
    search["name"] = ["Grinch"]
    search["families"] = ["CHARS","MAIN"]
    # search["types"] = ["Shading","Wide","Model","Hairs","Actor"]    
    search["types"] = ["Model"]    
    # __PIPEIN_GRAPH = __PIPEIN_GRAPH__('K10_CLASS_CRUD','findA7') #  graphName, verbose for debug
    __PIPEIN_GRAPH = __PIPEIN_GRAPH__('K10_CLASS_CRUD')
    result = __PIPEIN_GRAPH.findA7(search,True) # # true for selected for selected

    AssetList = result[0] # return object list
    verbose = result[1] # result[2] is verbose  
    for asset in AssetList: 
      print asset


#=========================== UI
K10_CLASS_CRUD.__category__         = 'X - TOOLZ'
K10_CLASS_CRUD.__author__           = 'cpottier'
K10_CLASS_CRUD.__textColor__        = '#6699ff'
K10_CLASS_CRUD.__paramsType__        = {
    # 'XNAMEX'        :  ( 'str' , 'XNAMEX-Shading_Shots_Scout.a7')
   'getAssetsInfos1'        :  ( 'bool', 'False' , ['True', 'False']  ),
   'getAssetsInfos2'        :  ( 'bool', 'False' , ['Wip', 'Wip']  ),   
   'assetToAdd'        :  ( 'str' , 'LIB/MATERIALS/Paint/Maps/Paint-Maps.a7'),
   'addA7'            :  ( 'bool', 'False' , ['True', 'False']  ),
   'findA7'            :  ( 'bool', 'True' , ['True', 'False']  )    
   
}


def K90_SETS_AddScout(save_after='True'): 
    ''' 
    | /
    | \ Tool - Last update 05-02-2016
      ----------------------------------------------------------------------
      AJOUTE 'Scout.a7' AU DECOR
      ----------------------------------------------------------------------

      - please GRAB Shading.a7
    '''

    # Classe de connection
    # __CONNECT_USER_INFOS    = __CONNECT_USER_INFOS__()

    # CONNECT_USER_INFOS = ink.io.ConnectUserInfo()
    # CONNECT_USER0 = CONNECT_USER_INFOS[0]
    # CONNECT_USER1 = CONNECT_USER_INFOS[1] # todo to ask why ?
    # PROJECT = CONNECT_USER_INFOS[2]
    # MAIL_HOSTNAME = 'HOSTNAME.illum-mg.fr'
    # MAIL_USER = CONNECT_USER1+'@illum-mg.fr'


    # absolute
    X_move_naskAbs = -21 
    Y_move_naskAbs = -7

    # relative with Paint-map
    X_move_nask = 0
    Y_move_nask = -3

    error0 = 'GRABBER OU LOCKER L\'A7  and run again !!!'

    paintMaps = 'LIB/MATERIALS/Paint/Maps/Paint-Maps.a7'

    #======================================================================
    #========= Add XNAMEX-Shading.a7 -> XXX-Shading_Shots_Scout.a7
    #======================================================================

    graph = ink.proto.Graph( graphs.DEFAULT )
    layout = graph.GetLayout()
    selection     = graph.GetSelection( nomen.Filter().SetTypes(['Shading']).SetStage('') )
    if not selection:
        raise Exception('Please select at least XNAMEX-Shading.a7 asset !')

    for pa in selection: # pa is the original selected asset Shading
        # Get info Optional
        nm_path       = pa.GetPath()
        nm_asset      = pa.GetNomen()     
        a_libname     = nm_asset.GetLib()
        a_name        = nm_asset.GetName()      
        a_family      = nm_asset.GetFamilies()
        a_typeFamily  = nm_asset.GetFamilies()[0] # cf SET
        a_catFamily   = nm_asset.GetFamilies()[1] # 
        a_var         = nm_asset.GetVar() # PROJECT cf GRINCH
        a_types       = nm_asset.GetTypes()
        a_lod         = nm_asset.GetLod()
        a_version     = nm_asset.GetVersion() 
        # print '----- a7 in first selection'
        # print pa
        # print nm_path,nm_asset
        # print a_libname,a_name,a_family,a_typeFamily,a_catFamily,a_var,a_types,a_lod,a_version

    #======================================================================
    #========= get shading pos for Offset between or grap and loaded graph # a test
    #======================================================================

        # layout.LoadGraphPos([pa])
        # shadingOrPos = layout.GetPoint([pa], direction='M') # todo, to understand M, B, T options
        # print shadingOrPos
  
    #======================================================================
    #========= get .ink path and create new protograph
    #======================================================================

        pathGraphLocal = '/u/'+PROJECT+'/Users/'+CONNECT_USER1+'/Presets/Graphs/'+a_name+'.inkGraph'
        pathGraph = '/u/'+PROJECT+'/Users/COM/Presets/Graphs/SHADING/'+a_typeFamily+'/'+a_catFamily+'/'+a_name+'.inkGraph'
        protoGraph = ink.proto.Graph( pathGraph, load=True, private=False )
        layout = protoGraph.GetLayout()

    #======================================================================
    #========= check if selection locked
    #======================================================================

        A7IsLock = ink.query.Asset(nm_asset).GetLockInfos()[0]
        if A7IsLock is False :
            print '############################################################################'
            print error0
            print '############################################################################'
            raise Exception( error0 )

    #======================================================================
    #========= a_name-Shading.a7-> a_name-Shading_Shots_Scout.a7
    #======================================================================
      
        Scout = nomen.Nomen.NewLib( lib='LIB', name=a_name, family=a_family, types=['Shading','Shots','Scout'], stage='' )
        ScoutProto = protoGraph.Add(Scout, execAction='', editAction='View/ViewShotsOfAsset')
        ScoutProto.AddFile('csv') # un fichier msg minimal est a associer obligatoirement
        ScoutProto.AddFile('rv')

        protoGraph.Apply()
        protoGraph.Show()

        gg = protoGraph.List()
        XNAMEX_shading = None
        check = 'LIB/SETS/'+a_catFamily+'/'+a_name+'/Shading/'+a_name+'-Shading.a7';

        for g in gg:
            ref = g
            if str(g) == check:
                XNAMEX_shading = g
    #======================================================================
    #========= add link and set Include attribute to NO
    #======================================================================
                protoGraph.AddLink( ScoutProto, XNAMEX_shading, ink.proto.LINK_DEP , ctxParams={ 'Include':'No' })
    #======================================================================
    #========= get Paint-Maps a7 position
    #======================================================================
            if str(g) == paintMaps:
                ref = g
                layout.LoadGraphPos([g])
                paintMapsPos = layout.GetPoint([g], direction='M') # todo, to understand M, B, T options
                paintMaps_X = paintMapsPos[0]
                paintMaps_Y = paintMapsPos[1]
                # print 'Paint-Maps.a7 position :' , paintMapsPos
    #======================================================================
    #========= move for friendly user layout
    #======================================================================
    # layout.SetPos(ScoutProto, (X_move_naskAbs, Y_move_naskAbs) )
    layout.SetPos(ScoutProto, (paintMaps_X+X_move_nask, paintMaps_Y+Y_move_nask) )
    #======================================================================
    #========= Apply Clean and save Graph
    #======================================================================

    protoGraph.Show()
    protoGraph.Apply()
    protoGraph.SelectAll()

    print 'SCOUT ADDED'
    if save_after == 'True':
        # protoGraph.Write(pathGraphLocal, comment='', private=False)
        print 'GRAPH SAVED !'
    else :
        print 'YOU CAN SAVE THIS GRAPH NOW !!!'     


#=========================== UI

K90_SETS_AddScout.__author__           = 'cpottier'
K90_SETS_AddScout.__textColor__        = '#6699ff'
K90_SETS_AddScout.__paramsType__        = {
'save_after'            :  ( 'bool', 'True' , ['True', 'False']  )    

}



def K91_GRAPH_Organizer(show_neighbours='True',organize_Upstreams='True',organize_Downstreams='True',x_ecart='2',SaveGraph='False'): 
    ''' 
    | /
    | \ Tool - Last update 02-03-2016
      ----------------------------------------------------------------------
      - Organize Context Layout for layout, anim, previz, usecase 
      -> get streams      
      -> Add Nask/timing,casting,stereo | Stereo/stereo_session

      - todo
              auto save usecase
              choice for real tool name
      ----------------------------------------------------------------------

      Select All .a7 or Layout.a7

    '''

    # MODIFIABLE #########################################################
    # Nask relative with Layout.a7
    X_move_nask         =  0
    Y_move_nask         = -1.5
    ecart_nask          =  3
    # for debug or tests
    pathGraphLocal = '/u/gri/Users/cpottier/Presets/Graphs/toto.inkGraph'

    # DONT TOUCH #########################################################
    MASTER              = None
    SEQUENCE            = None

    layA7Pos_X          = None
    layA7Pos_Y          = None
    ecart               = int(graphs.__GetArgStr(int(x_ecart)))
    ecartClip_Y         =  1

    ######################################################################



    def moveClipA7s(protoGraph,stream,assetClips,layout,layA7Pos_X,layA7Pos_Y):
        '''   '''
        layout    = protoGraph.GetLayout()
        inc_Y     = 0
        # infos nomenclature clip_p0340sub etc -> varNomenClips = ['sub', 'trailer', 'tr', 'vi']
        for pa in assetClips:
            clipA7Pos    = __PIPEIN_GRAPH.getPosition(pa,layout)
            clipA7Pos_X           = clipA7Pos[0]
            clipA7Pos_Y           = layA7Pos_Y + inc_Y
            X_move_naskRelToLayA7 = clipA7Pos_X + ( ecart*2 )
            if str(stream) == 'Upstreams':
                X_move_naskRelToLayA7 = clipA7Pos_X - ( ecart*2 )
            Y_move_naskRelToLayA7     = clipA7Pos_Y
            layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            inc_Y = inc_Y + ecartClip_Y
        #========= Apply 
        protoGraph.Show()
        protoGraph.Apply()
        protoGraph.SelectAll()

    def LAYOUT_addA7s(PROJECT,SEQUENCE,SHOT,CATEGORY,protoGraph,X,Y,X_move_nask,Y_move_nask,ecart,type_layout):
        ''' add Nask/timing,casting,stereo | Stereo/stereo_session '''

        layout = protoGraph.GetLayout()

        #======================================================================
        #========= add Nask/timing,casting,stereo | 
        #======================================================================

        assetList = []
        
        if str(type_layout) == 'Layout':
            assetList = ['Casting','Timing','Stereo']
            path = PROJECT+'/'+SEQUENCE+'/EDIT/NasK/'+PROJECT+'_'+SEQUENCE+'_EDIT-NasK_'

        if str(type_layout) == 'Anim':
            assetList = ['Casting','Timing']
            path = PROJECT+'/'+SEQUENCE+'/EDIT/NasK/'+PROJECT+'_'+SEQUENCE+'_EDIT-NasK_'

        if str(type_layout) == 'Previz':
            assetList = ['Casting','Timing','Stereo']
            path = 'PREVIZ/'+SEQUENCE+'/EDIT/NasK/PREVIZ_'+SEQUENCE+'_EDIT-NasK_'

        if str(type_layout) == 'Usecase':
            assetList = ['Casting','Timing']
            path = 'USECASE/'+CATEGORY+'/'+SEQUENCE+'/EDIT/NasK/'+PROJECT+'_'+SEQUENCE+'_EDIT-NasK_'

        #=========
        for Name in assetList:
            A7path = path+Name+'.a7'
            __PIPEIN_GRAPH.add_A7('dirPath',A7path) # _type, A7(str,list,dic), A7Select[optional], A7position[optional]

        #======================================================================
        #========= add Stereo/stereo_session
        #======================================================================
        if str(type_layout) == 'Layout':
            A7path = PROJECT+'/'+SEQUENCE+'/EDIT/Stereo/'+PROJECT+'_'+SEQUENCE+'_EDIT-Stereo_Session.a7'
            __PIPEIN_GRAPH.add_A7('dirPath',A7path)
        if str(type_layout) == 'Previz':
            A7path = 'PREVIZ/'+SEQUENCE+'/EDIT/Stereo/PREVIZ_'+SEQUENCE+'_EDIT-Stereo_Session.a7'
            __PIPEIN_GRAPH.add_A7('dirPath',A7path)
        # if str(type_layout) == 'Usecase':
        #     A7path = 'USECASE/'+SEQUENCE+'/EDIT/Stereo/USECASE_'+SEQUENCE+'_EDIT-Stereo_Session.a7'
        #     __PIPEIN_GRAPH.add_A7('dirPath',A7path)
        #========= Apply 
        protoGraph.Show()
        protoGraph.Apply()
        protoGraph.SelectAll()

        #======================================================================
        #========= move for friendly user layout
        #======================================================================
        A7add = protoGraph.List()
        for a in A7add:
            try:
                if str(assetList[0]) in str(a):
                    X_move_naskRelToLayA7 = X + X_move_nask
                    Y_move_naskRelToLayA7 = Y + Y_move_nask
                    layout.SetPos(a, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetList[1]) in str(a):
                    X_move_naskRelToLayA7 = X + X_move_nask
                    Y_move_naskRelToLayA7 = Y + (Y_move_nask*2)
                    layout.SetPos(a, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetList[2]) in str(a) and 'NasK' in str(a):
                    X_move_naskRelToLayA7 = X + ecart_nask
                    Y_move_naskRelToLayA7 = Y + (Y_move_nask*3)
                    layout.SetPos(a, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetList[2]) in str(a) and 'NasK' not in str(a):
                    X_move_naskRelToLayA7 = X - ecart_nask
                    Y_move_naskRelToLayA7 = Y + (Y_move_nask*3)
                    layout.SetPos(a, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass

        #======================================================================
        #========= Apply 
        #======================================================================
        protoGraph.Show()
        protoGraph.Apply()
        protoGraph.SelectAll()


    #============================================================================================================== end functions

    protoGraph  = ink.proto.Graph( graphs.DEFAULT )
    layout      = protoGraph.GetLayout()
    selection   = protoGraph.GetSelection()
    type_layout = None 

    if not selection:
        raise Exception('Please select All a7 !')

    #========= Retrieve Type Graph
    for pa in selection: 
        A7_infos = __PIPEIN_GRAPH.getA7_infos(pa)
        nm_asset      = A7_infos['nm_asset']
        a_types       = A7_infos['a_types']

        #========= retrieve graphname
        try:
            check = str(pa).split('_')[2] # todo better with filter
            MASTER      = check.split('-')[0]
            SEQUENCE    = str(pa).split('_')[1]
            SHOT        = 'None'
            CATEGORY    = 'None'

            try:
                checkShot = str(pa).split('_P')[1] # todo better with filter
                SHOT = 'P'+checkShot[0:4]
            except:
                pass
            try:
                checkShot = str(pa).split('_Z')[1] # todo better with filter
                SHOT = 'Z'+checkShot[0:4]
            except:
                pass

            GraphName = str(nm_asset)  

            #========= get a7 position
            layA7Pos    = __PIPEIN_GRAPH.getPosition(pa,layout)
            layA7Pos_X = layA7Pos[0]
            layA7Pos_Y = layA7Pos[1]

            #========= retrieve protoA7
            ProtoA7 = pa

        except:
            pass

        #========= determine cases
        try:
            # case Layout
            if len(a_types) == 1 and a_types[0] == 'Layout' and 'PREVIZ' not in str(nm_asset):
                type_layout = 'Layout'
                check_clips = '-Layout_Clip'
                pathGraphSave = '/u/'+projectLower+'/Users/COM/Presets/Graphs/RLO/'+SEQUENCE+'/'+SEQUENCE+'_'+MASTER+'.inkGraph'

            # case Previz
            if len(a_types) == 1 and a_types[0] == 'Layout' and 'PREVIZ' in str(nm_asset):
                type_layout = 'Previz'
                check_clips = '-Layout_Clip'
                pathGraphSave = '/u/'+projectLower+'/Users/COM/Presets/Graphs/PREVIZ/'+SEQUENCE+'/'+SEQUENCE+'_'+MASTER+'.inkGraph'

            # case Anim 
            if len(a_types) == 1 and a_types[0] == 'Anim' and 'USECASE' not in str(nm_asset):
                type_layout = 'Anim'
                check_clips = '-Anim_Clip'
                pathGraphSave = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/'+PROJECT+'/'+SEQUENCE+'/'+SEQUENCE+'_'+SHOT+'.inkGraph'

            # case Usecase
            if len(a_types) == 1 and a_types[0] == 'Anim' and 'USECASE' in str(nm_asset):
                type_layout = 'Usecase'
                check_clips = '-Anim_Clip'
                tmp = str(pa).split('USECASE_')[1] # todo better with filter
                SEQUENCE = tmp.split('_')[0]
                tmp2 = tmp.split('_')[1]
                SHOT = tmp2.split('-')[0]

                # Prov, premiere pass to do better
                pathGraphSave = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/'+CATEGORY+'/'+SEQUENCE+'/'+SEQUENCE+'_'+SHOT+'.inkGraph' 

                # Assets # sample 1
                # USECASE/MANI/Test101/Anim/USECASE_MANI_Test101-Anim.a7 
                # Assets # sample 2
                # USECASE/LOOKDEV/BathroomOffset/Anim/USECASE_LOOKDEV_BathroomOffset-Anim.a7 

                # Graphs # sample 1
                # /u/gri/Users/COM/Presets/Graphs/ANIM/USECASE/TERTIARY/MANI/ManI_Test101.inkGraph # private 
                # Graphs # sample 2
                # /u/gri/Users/COM/Presets/Graphs/ANIM/USECASE/LOOKDEV/BathroomOffset.inkGraph 

            if SHOT == 'None':
                print pathGraphSave
                raise Exception('Shot == None !')


        except:
            pass

    #========= Retrieve a7 Downstreams and Upstreams

        if str(show_neighbours)=='True':

            layout.SetPos(ProtoA7, (0,0) )

            protoGraph.Show()
            protoGraph.Apply()
            protoGraph.SelectAll()

            layA7Pos    = __PIPEIN_GRAPH.getPosition(ProtoA7,layout)
            layA7Pos_X  = layA7Pos[0]
            layA7Pos_Y  = layA7Pos[1]

            Filters = {'family': ['.*'] , 'type': ['.*']}  
            StreamProtoList = __PIPEIN_GRAPH.GetStreams('GetDownstreams',protoGraph,layout,ProtoA7,Filters)
            StreamProtoList = __PIPEIN_GRAPH.GetStreams('GetUpstreams',protoGraph,layout,ProtoA7,Filters)

    #========= select a7 Upstreams for positioning
        assetClips = []
        UpStreamProtoList = protoGraph.GetUpstreams( ProtoA7 )
        for us in UpStreamProtoList:
            assetClips.append(us)
            if type_layout == 'Usecase' and 'ACTOR-OK' in str(us).upper() and str(SEQUENCE).upper() in str(us).upper():
                A7_infos_us      = __PIPEIN_GRAPH.getA7_infos(us)
                a_catFamily      = A7_infos_us['a_catFamily']
                pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/'+a_catFamily+'/'+SEQUENCE+'/'+SEQUENCE+'_'+SHOT+'.inkGraph'

    #========= set position layout.a7 Upstreams
        moveClipA7s(protoGraph,'Upstreams',assetClips,layout,layA7Pos_X,layA7Pos_Y)
    #========= select a7 Downstreams  for positioning
    if organize_Downstreams == 'True':
        assetClips = []
        assetClipsByName = []
        DownStreamProtoList = protoGraph.GetDownstreams( ProtoA7 )
        for ds in DownStreamProtoList:
            # if '-Layout_Clip' in str(ds): # to do better, with filter 'Clip'
            if str(check_clips) in str(ds): # to do better, with filter 'Clip'
                assetClipsByName.append(ds)
        # re order list , by path Name and not InK object logical
        assetClips = sorted(assetClipsByName, reverse=True)
    #========= set position clip.a7 Downstreams
        moveClipA7s(protoGraph,'Clips',assetClips,layout,layA7Pos_X,layA7Pos_Y)

    #======================================================================
    #========= add, set position .a7 timing,casting,stereo, stereo_session
    #======================================================================
    LAYOUT_addA7s(PROJECT,SEQUENCE,SHOT,CATEGORY,protoGraph,layA7Pos_X,layA7Pos_Y,X_move_nask,Y_move_nask,ecart,type_layout)

    #======================================================================
    # SAVE LAYOUT GRAPH
    #======================================================================
    print '\nK91_GRAPH_Organizer is Happy :)\n'
    if str(SaveGraph) == 'False' :
        print 'You can Save ' , GraphName, 'in ', pathGraphSave
    if str(SaveGraph) == 'True' :
        __PIPEIN_GRAPH.saveGraph(pathGraphSave)
        print GraphName , 'Have been saved ', 'in ', pathGraphSave, ' !!!'



#=========================== UI

K91_GRAPH_Organizer.__author__           = 'cpottier'
K91_GRAPH_Organizer.__textColor__        = '#6699ff'
K91_GRAPH_Organizer.__paramsType__        = {
# 'sep'                       :  ('') ,
# 'master_layout'             :  ( 'bool', 'True' , ['True', 'False']  ) ,  # todo switch layout/anim
# 'master_anim'               :  ( 'bool', 'False' , ['True', 'False']  ) , # todo switch layout/anim
'show_neighbours'        :  ( 'bool', 'True' , ['True', 'False']  ) ,
'organize_Upstreams'        :  ( 'bool', 'True' , ['True', 'False']  ) ,
'organize_Downstreams'     :  ( 'bool', 'True' , ['True', 'False']  ) ,
'x_ecart'                   :  ( 'enum', '2',['-6','-3','-2', '-1', '1', '2', '3', '6', '9'] ) ,
'SaveGraph'                :  ( 'bool', 'False' , ['True', 'False']  )
}




def K92_LAYOUT_BuildCameraModelZator(autoload='True',autosave='True',save_private='True',cat='MAIN',_cat=None):
    ''' 
    | /
    | \ Tool - Last update 01-03-2016
      ----------------------------------------------------------------------
      - Organize MODEL Context Layout 
      - autosave graphs in :
            MODELING/CHARS/MODTECH/
                    -> M_MAIN.inkGraph
                    -> M_SECONDARY.inkGraph
                    -> M_TERTIARY.inkGraph      
      - todo :
            - release gestion filters = None
            - r&d : check len name for ecart auto optimal
      ----------------------------------------------------------------------

      Auto Execution or Select CAMERA-Actor_ModChars-Ok.a7

    '''

    # PARAMS MODIFIABLES ############################################################################################

    A7refPos_X              = None #  X origin a7 ref - None for not Used
    A7refPos_Y              = None #  Y origin a7 ref - None for not Used
    offset_X                = 6    #  4 # relative to X origin a7 ref - can be negative
    offset_Y                = 3    #  0 # relative to Y origin a7 ref - can be negative
    ecart_a7_X              = 'Auto' #  3 # X space between streams a7  , if = 'Auto', space depends of A7 name longer
    ecart_a7_Y              = None #  2 # Y space between streams a7

    n_A7_perColumn          = None #  6 # max n streams vertically 
    n_A7_perRow             = None #  6 # max n streams horizontally - None for not Used
    X_space_betweenColumns  = 2

    quinconce               = None #  True False # boolean, decale les a7 une fois sur 2
    quinconce_X             = None #  0.5 # x offset, 0.5/-0.5 left-right, min max
    quinconce_start         = None #  0 # switch first quinconce_X value to modulo 0.5 to -0.5

    n_col_byGroup           = None #  2 # n column by a7 grouped
    X_space_betweenGroup    = 2    #  ecart_a7_X*2 # subjectif, to do better in relation with n assets, n group etc 
    n_groups_grouded        = None # todo paquet de groups  - None for not Used

    # DONT TOUCH ###################################################################################################

    params = {}
    
    if A7refPos_X != None :
        params['A7refPos_X']                    = A7refPos_X
    if A7refPos_Y != None :
        params['A7refPos_Y']                    = A7refPos_Y
    if offset_X != None :
        params['offset_X']                      = offset_X
    if offset_Y != None :
        params['offset_Y']                      = offset_Y
    if ecart_a7_X != None :
        params['ecart_a7_X']                    = ecart_a7_X
    if ecart_a7_Y != None :
        params['ecart_a7_Y']                    = ecart_a7_Y

    if n_A7_perColumn != None :
        params['n_A7_perColumn']                = n_A7_perColumn
    if n_A7_perRow != None :
        params['n_A7_perRow']                   = n_A7_perRow
    if X_space_betweenColumns != None :
        params['X_space_betweenColumns']        = X_space_betweenColumns

    if quinconce != None :
        params['quinconce']                     = quinconce
    if quinconce_X != None :
        params['quinconce_X']                   = quinconce_X
    if quinconce_start != None :
        params['quinconce_start']               = quinconce_start

    if n_col_byGroup != None :
        params['n_col_byGroup']                 = n_col_byGroup
    if X_space_betweenGroup != None :
        params['X_space_betweenGroup']          = X_space_betweenGroup
    if n_groups_grouded != None :
        params['n_groups_grouded']              = n_groups_grouded

    #=========

    catFamily = []
    if _cat != None :
      cat = _cat[0]
      for a in _catFamily:
        catFamily.append(a)
    if _cat == None :
        catFamily.append(cat)
        cat = cat

    A7R                     = 'CAMERA-Actor_ModChars-Ok.a7'
    A7RefPath               = 'LIB/CAMERAS/CAMERA/Ok/'+A7R
    myG                     = 'M_'+cat+'.inkGraph'
    myGraph                 = 'MODELING/CHARS/MODTECH/'+myG
    myGraphLocal            = LOCALPATH+'M_'+cat+'.inkGraph' # for debug   

    autoLoadA7ref           = False
    if autoload == 'True':
        autoLoadA7ref       = True # in 2 variables because this script can be call external  

    _Longest = [0]

    # Functions ###################################################################################################

    def showStream(protoGraph,assetProto,typeStreams,catFamily,A7posRef=None):
        ''' show a7 streams '''
        A7pos = None
        Filters = {'type': ['Model']}                  
        family = ['CHARS']
        family.append(catFamily[0])
        Filters['family'] = family
        # Filters = {'family': ['CHARS', 'MAIN'] , 'type': ['Model']} #  Ordre Important pour family filters 1-CHARS 2-MAIN etc
        StreamProtoList = __PIPEIN_GRAPH.GetStreams(typeStreams,protoGraph,layout,assetProto,Filters)

        return StreamProtoList
    
    # End Functions ################################################################################################  

    #======================================================================
    #========= Add Get Ref A7
    #======================================================================
    if autoLoadA7ref == True:
        __PIPEIN_GRAPH.add_A7('dirPath',A7RefPath,True) # _type, A7(str,list,dic), A7Select[optional], A7position[optional]
        protoGraph.Show()
        protoGraph.Apply()
        protoGraph.SelectAll()

    if autoLoadA7ref == False:
        layout      = protoGraph.GetLayout()
        selection   = protoGraph.GetSelection()
        if not selection:
            raise Exception('Please select '+A7R+' !')
    #======================================================================
    #========= Get Selection and move to center graph
    #======================================================================
    layout      = protoGraph.GetLayout()
    selection   = protoGraph.GetSelection()
    layout.SetPos(A7RefPath, (0,0) )
    protoGraph.Show()
    protoGraph.Apply()
    protoGraph.SelectAll()
    #======================================================================
    #========= Retrieve ref.a7 Pos
    #======================================================================
    for pa in selection: 
        A7_infos = __PIPEIN_GRAPH.getA7_infos(pa)
        nm_asset      = A7_infos['nm_asset']
        a_types       = A7_infos['a_types']    
        if str(pa) == str(A7RefPath):
            ProtoA7 = pa
    #======================================================================
    #========= get  Refa7 position
    #======================================================================
            A7refPos    = __PIPEIN_GRAPH.getPosition(pa,layout)
    #======================================================================
    #========= show a7 Downstreams
    #======================================================================  
            StreamProtoList      = showStream(protoGraph,ProtoA7,'GetDownstreams',catFamily)
    #========= apply and refresh graph
            protoGraph.Show()
            protoGraph.Apply()
            protoGraph.SelectAll()
    #======================================================================
    #========= set position .a7 Downstreams
    #======================================================================

    #========= R&D for auto-ecart, check longest name for ecart optimal
    if str(ecart_a7_X).upper() == 'AUTO':         
        longestName = []
        for pa in StreamProtoList:
            A7_infos = __PIPEIN_GRAPH.getA7_infos(pa,False)  # True False optional for verbose Mode
            a_name   = A7_infos['a_name'] 
            l = len(str(a_name))
            longestName.append(l)
        try:
            longestName = max(longestName)
        except:
            pass
        _Longest.append(longestName)
        nLetters = int(max(_Longest))
        autoEcart_X = (nLetters/10)*2
        params['ecart_a7_X'] = autoEcart_X
        params['X_space_betweenGroup'] = autoEcart_X

    #========= set position .a7 Downstreams
    n_streams = len(StreamProtoList)
    __PIPEIN_GRAPH.move_StreamProtoList(n_streams,StreamProtoList,layout,A7refPos,params)
    #========= apply and refresh graph
    protoGraph.Show()
    #========= save Graph
    # myGraph = myGraphLocal
    if str(save_private) == 'True':
        myGraph = myGraphLocal        
    if str(autosave) == 'True':
        __PIPEIN_GRAPH.saveGraph(myGraph)
        print myGraph + ' SAVED !!!'
    if str(autosave) == 'False':
        print '[ OK ] You can save : ' + myG


# #=========================== UI

K92_LAYOUT_BuildCameraModelZator.__author__             = 'cpottier'
K92_LAYOUT_BuildCameraModelZator.__textColor__          = '#6699ff'
K92_LAYOUT_BuildCameraModelZator.__paramsType__         = {
'autoload'                :  ( 'bool', 'True' , ['True', 'False']  ),
'autosave'                :  ( 'bool', 'True' , ['True', 'False']  ),
'save_private'            :  ( 'bool', 'True' , ['True', 'False']  ),
'cat'                     :  ( 'enum', 'MAIN',['MAIN', 'SECONDARY', 'TERTIARY'] )
}



def K93_LAYOUT_BuildHumanShapeZator(autoload='True',autosave='True',save_private='True',cat='MAIN',_cat=None):
    ''' 
    | /
    | \ Tool - Last update 01-03-2016
      ----------------------------------------------------------------------
      - Organize FACIAL Context Layout 
      - autosave graphs in :
                MODELING/CHARS/MODTECH/
                    -> F_MAIN.inkGraph
                    -> F_SECONDARY.inkGraph
                    -> F_TERTIARY.inkGraph

      - todo :
            - release gestion Filters = None
            - r&d : check len name for ecart auto optimal
      ----------------------------------------------------------------------

      Auto Execution or Select Human-Shape_BcsTpl.a7

    '''

    # PARAMS MODIFIABLES ############################################################################################

    A7refPos_X              = None # X origin a7 ref - None for not Used
    A7refPos_Y              = None # Y origin a7 ref - None for not Used
    offset_X                = 8 # 4 # relative to X origin a7 ref - can be negative
    offset_Y                = 3 #  0 # relative to Y origin a7 ref - can be negative
    ecart_a7_X              = 'Auto' #  3 # X space between streams a7  , if = 'Auto', space depends of A7 name longer 
    ecart_a7_Y              = None #  2 # Y space between streams a7

    n_A7_perColumn          = None #  6 # max n streams vertically 
    n_A7_perRow             = None #  6 # max n streams horizontally - None for not Used
    X_space_betweenColumns  = 3

    quinconce               = None #  True False # boolean, decale les a7 une fois sur 2
    quinconce_X             = None #  0.5 # x offset, 0.5/-0.5 left-right, min max
    quinconce_start         = None #  0 # switch first quinconce_X value to modulo 0.5 to -0.5

    n_col_byGroup           = None #  2 # n column by a7 grouped
    X_space_betweenGroup    = 3    #  ecart_a7_X*2 # subjectif, to do better in relation with n assets, n group etc 
    n_groups_grouded        = None # todo paquet de groups  - None for not Used

    # DONT TOUCH ###################################################################################################

    params = {}
    
    if A7refPos_X != None :
        params['A7refPos_X']                = A7refPos_X
    if A7refPos_Y != None :
        params['A7refPos_Y']                = A7refPos_Y
    if offset_X != None :
        params['offset_X']                  = offset_X
    if offset_Y != None :
        params['offset_Y']                  = offset_Y
    if ecart_a7_X != None :
        params['ecart_a7_X']                = ecart_a7_X
    if ecart_a7_Y != None :
        params['ecart_a7_Y']                = ecart_a7_Y

    if n_A7_perColumn != None :
        params['n_A7_perColumn']            = n_A7_perColumn
    if n_A7_perRow != None :
        params['n_A7_perRow']               = n_A7_perRow
    if X_space_betweenColumns != None :
        params['X_space_betweenColumns']    = X_space_betweenColumns

    if quinconce != None :
        params['quinconce']                 = quinconce
    if quinconce_X != None :
        params['quinconce_X']               = quinconce_X
    if quinconce_start != None :
        params['quinconce_start']           = quinconce_start

    if n_col_byGroup != None :
        params['n_col_byGroup']             = n_col_byGroup
    if X_space_betweenGroup != None :
        params['X_space_betweenGroup']      = X_space_betweenGroup
    if n_groups_grouded != None :
        params['n_groups_grouded']          = n_groups_grouded

    #=========

    catFamily = []
    if _cat != None :
      cat = _cat[0]
      for a in _catFamily:
        catFamily.append(a)
    if _cat == None :
        catFamily.append(cat)
        cat = cat

    A7R                     = 'Human-Shape_BcsTpl.a7'
    A7RefPath               = 'LIB/TEMPLATES/Human/Shape/'+A7R
    myG                     = 'F_'+cat+'.inkGraph'
    myGraph                 = 'MODELING/CHARS/MODTECH/'+myG
    myGraphLocal            = LOCALPATH+'F_'+cat+'.inkGraph' # for test
    autoLoadA7ref           = False
    if autoload == 'True':
        autoLoadA7ref       = True # in 2 variables because this script can be call external  

    _Longest = [0]

    def showStream(protoGraph,assetProto,typeStreams,catFamily,A7posRef=None):
        ''' show a7 streams '''

        A7pos = None
        layout      = protoGraph.GetLayout()

        if typeStreams == 'GetDownstreams':
            Filters = {'type': ['.*']}                
            family = ['CHARS']
            family.append(catFamily[0])
            Filters['family'] = family  #  Ordre Important pour family filters 1-CHARS 2-MAIN etc
            StreamProtoList = __PIPEIN_GRAPH.GetStreams(typeStreams,protoGraph,layout,assetProto,Filters)

        if typeStreams == 'GetUpstreams':
            Filters = {'type': ['Actor','Skin']}
            if A7posRef != None:
                X_posRef = A7posRef[0] - 0.1
                Y_posRef = A7posRef[1] + 0.6
                A7pos = []    
                A7pos.append(X_posRef) 
                A7pos.append(Y_posRef) 
            StreamProtoList = __PIPEIN_GRAPH.GetStreams(typeStreams,protoGraph,layout,assetProto,Filters,A7pos)      

        # move upstream, to do better
        for pa in StreamProtoList:            
            if A7pos != None: # todo better
                # X_pos = A7pos[0]-2
                X_pos = A7pos[0]-(2+1.2)
                Y_pos = A7pos[1]+0.2                    
                layout.SetPos(pa, (X_pos,Y_pos) )



        return StreamProtoList

    #============================================================================================================== end functions


    #======================================================================
    #========= Add Get Ref A7
    #======================================================================
    if autoLoadA7ref == True:
        __PIPEIN_GRAPH.add_A7('dirPath',A7RefPath,True) # _type, A7(str,list,dic), A7Select[optional], A7position[optional]
        protoGraph.Show()
        protoGraph.Apply()
        protoGraph.SelectAll()

    if autoLoadA7ref == False:
        layout      = protoGraph.GetLayout()
        selection   = protoGraph.GetSelection()
        if not selection:
            raise Exception('Please select '+A7R+' !')
    #======================================================================
    #========= Get Selection and move to center graph
    #======================================================================
    layout      = protoGraph.GetLayout()
    selection   = protoGraph.GetSelection()
    layout.SetPos(A7RefPath, (0,0) )
    protoGraph.Show()
    protoGraph.Apply()
    protoGraph.SelectAll()
    #======================================================================
    #========= Retrieve a7 Pos
    #======================================================================
    for pa in selection: 
        A7_infos      = __PIPEIN_GRAPH.getA7_infos(pa)
        nm_asset      = A7_infos['nm_asset']
        a_types       = A7_infos['a_types']   
        if str(pa) == str(A7RefPath):
            ProtoA7 = pa
    #======================================================================
    #========= get  Refa7 position
    #======================================================================
            A7refPos = __PIPEIN_GRAPH.getPosition(pa,layout)
    #======================================================================
    #========= show .a7 Downstreams
    #======================================================================  
            StreamProtoList = showStream(protoGraph,ProtoA7,'GetDownstreams',catFamily)
    #========= apply and refresh graph
            protoGraph.Show()
            protoGraph.Apply()
            protoGraph.SelectAll()
    #======================================================================
    #========= set position .a7 Downstreams
    #======================================================================

    #========= R&D for auto-ecart, check longest name for ecart optimal
    if str(ecart_a7_X).upper() == 'AUTO':         
        longestName = []
        for pa in StreamProtoList:
            A7_infos = __PIPEIN_GRAPH.getA7_infos(pa,False)  # True False optional for verbose Mode
            a_name   = A7_infos['a_name'] 
            l = len(str(a_name))
            longestName.append(l)
        try:
            longestName = max(longestName)
        except:
            pass
        _Longest.append(longestName)
        nLetters = int(max(_Longest))
        autoEcart_X = (nLetters/10)*2
        params['ecart_a7_X'] = autoEcart_X
        params['X_space_betweenGroup'] = autoEcart_X
    #========= set position .a7 Downstreams   
    n_streams = len(StreamProtoList)
    __PIPEIN_GRAPH.move_StreamProtoList(n_streams,StreamProtoList,layout,A7refPos,params)
    #========= apply and refresh graph
    protoGraph.Show()
    protoGraph.Apply()
    protoGraph.SelectAll()
    #======================================================================
    #========= show childrens Skin Upstreams
    #====================================================================== 
    longestName = []  
    selection   = protoGraph.GetSelection()

    #========= R&D for auto-ecart, check longest name for ecart optimal
    for pa in StreamProtoList:
        l = len(str(pa))
        longestName.append(l)
    try:
        longestName = max(longestName)
    except:
        pass
    _Longest.append(longestName)
    nLetters = int(max(_Longest))

    for pa in selection: 
        A7_infos      = __PIPEIN_GRAPH.getA7_infos(pa)
        nm_asset      = A7_infos['nm_asset']
        nm_path       = A7_infos['nm_path']
        A7posRef      = []
        position      = __PIPEIN_GRAPH.getPosition(pa,layout)
        A7posRef.append(position[0])
        A7posRef.append(position[1])
        if str(nm_asset) != str(A7RefPath):
            result = showStream(protoGraph,pa,'GetUpstreams',catFamily,A7posRef)  # protoGraph,assetProto,typeStreams,catFamily,A7posRef=None

    # to do better
    # for pa in StreamProtoList:   
    #     A7pos         = __PIPEIN_GRAPH.getPosition(pa,layout)         
    #     X_pos         = A7pos[0]-2
    #     Y_pos         = A7pos[1]                    
    #     layout.SetPos(pa, (X_pos,Y_pos) )


    #========= apply and refresh graph
    protoGraph.Show()
    protoGraph.Apply()
    #======================================================================
    #========= save Graph
    #======================================================================
    # myGraph = myGraphLocal
    if str(save_private) == 'True':
        myGraph = myGraphLocal  
    if str(autosave) == 'True':
        __PIPEIN_GRAPH.saveGraph(myGraph)
        print myGraph + ' SAVED !!!'
    if str(autosave) == 'False':
        print '[ OK ] You can save : ' + myG


# #=========================== UI

K93_LAYOUT_BuildHumanShapeZator.__author__            = 'cpottier'
K93_LAYOUT_BuildHumanShapeZator.__textColor__         = '#6699ff'
K93_LAYOUT_BuildHumanShapeZator.__paramsType__        = {
'autoload'                :  ( 'bool', 'True' , ['True', 'False']  ),
'autosave'                :  ( 'bool', 'True' , ['True', 'False']  ),
'save_private'            :  ( 'bool', 'True' , ['True', 'False']  ),
'cat'                     :  ( 'enum', 'MAIN',['MAIN', 'SECONDARY', 'TERTIARY'] )
}








# #===========================================================================================================================  PART LAST , GOODIES

def K80_GOODIES(UserConnected0,UserConnected1,Projet,sendMail_wip='False'):
    ''' 
    run action will print :
    - USER INFOS
    
    - SEND MAIL TO YOURSELF WIP
    - SHOW HIDE UI ELEMENT WIP
    - ENABLE DISABLED ELEMENT UI WIP

    - Bug : 

      # todo ask dev dpt , bug plantage thread pyqt

      # send-mail: warning: valid_hostname: misplaced delimiter: .macguff.fr                                                                   
      # send-mail: fatal: file /etc/postfix/main.cf: parameter myhostname: bad parameter value: .macguff.fr                                    
      # QObject::connect: Cannot queue arguments of type 'QTextCursor'                                                                               
      # (Make sure 'QTextCursor' is registered using qRegisterMetaType().)                                                                           
      # QObject::connect: Cannot queue arguments of type 'QTextBlock'                                                                                 
      # (Make sure 'QTextBlock' is registered using qRegisterMetaType().)                                                                               
      # QObject::setParent: Cannot set parent, new parent is in a different thread
      # QPixmap: It is not safe to use pixmaps outside the GUI thread

    '''


    # Classe de connection
    CONNECT_USER_INFOS = _CONNECT_USER_INFOS()
    
    
    ######====================================================
    ###### SEND MAIL FROM CLASS SAMPLE
    ######==================================================== 


    # todo , external lib

    mail_from = MAIL_USER
    mail_to = MAIL_USER
    mail_subject = 'Hello Happy taxes payers!'
    mail_content = []
    mail_content.append('You know what i m happy ...')
    mail_content.append('Droopy, Cordially')

    SENDMAIL = _SENDMAIL(mail_from,mail_to,mail_subject,'mailContent : You know what i m happy ...')
    result = SENDMAIL.sendmail()
    print result



    if sendMail_wip is 'TrueX': # Checkbox is checked 
        MyLog = open('/tmp/tmpMail', 'w')
        for line in mail_content :
            MyLog.write(line)
            MyLog.close()

        # todo , bug plantage thread pyqt

        # send-mail: warning: valid_hostname: misplaced delimiter: .macguff.fr                                                                   
        # send-mail: fatal: file /etc/postfix/main.cf: parameter myhostname: bad parameter value: .macguff.fr                                    
        # QObject::connect: Cannot queue arguments of type 'QTextCursor'                                                                               
        # (Make sure 'QTextCursor' is registered using qRegisterMetaType().)                                                                           
        # QObject::connect: Cannot queue arguments of type 'QTextBlock'                                                                                 
        # (Make sure 'QTextBlock' is registered using qRegisterMetaType().)                                                                               
        # QObject::setParent: Cannot set parent, new parent is in a different thread
        # QPixmap: It is not safe to use pixmaps outside the GUI thread

        cmd = 'mail '+mail_to+' -s "'+mail_subject+'" < /tmp/tmpMail';
        os.system(cmd)

  

#=========================== UI
# K80_GOODIES.__position__         = 4
K80_GOODIES.__category__         = 'Z - GOODIES'
K80_GOODIES.__author__           = 'cpottier'
K80_GOODIES.__paramsType__        = {  
    'UserConnected0'        :  ( 'str' , ink.io.ConnectUserInfo()[0]),
    'UserConnected1'        :  ( 'str' , ink.io.ConnectUserInfo()[1]),
    'Projet'        :  ( 'str' , ink.io.ConnectUserInfo()[2]),
    'sendMail_wip'       :  ( 'bool', 'False' , ['True', 'False']  )
}













# ###################################################################################################### FIN GOODIES


  
#   # print '----------------------------- Get user parameters -------------------'
#   # graph = ink.proto.Graph( graphs.DEFAULT )
  
#   # # -- Get user parameters
#   # castType        = graphs.__GetArgList( castType, separator = '_' )
#   # libName         = graphs.__GetArgStr( libName )
#   # castStage       = graphs.__GetArgStr( castStage )
#   # familyList      = graphs.__GetArgList( familyList, separator = ',' )
#   # shotType        = graphs.__GetArgList( shotType, separator = '_' )
#   # sceneList       = graphs.__GetArgProtoList( graph, shotList, types=shotType, stage='', onlyExist=False, separator = ',' )
#   # update          = graphs.__GetArgBool( update )
#   # select          = graphs.__GetArgBool( select )
  
#   # print 'castType         : '         , castType
#   # print 'libName          : '         , libName
#   # print 'castStage        : '         , castStage
#   # print 'familyList       : '         , familyList
#   # print 'shotType         : '         , shotType
#   # print 'sceneList        : '         , sceneList
#   # print 'update           : '         , update
#   # print 'select           : '         , select

#   # List_Types = 'LIT,   SHADOW_CASTERS,   BDD,CHARACTERS, SETS'
#   # listTypes = graphs.__GetArgList(List_Types)
#   # print listTypes

