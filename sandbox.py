# -*- coding: utf-8 -*-
'''     List of Samples Functions to learn  InK UI-API  - Verbose Documentation  '''

# ##################################################################################
# MG ILLUMINATION                                                                    #
# First Crazy Debroussailleur : jDepoortere                                        #
# Author : cPOTTIER                                                                #
# Last Update : 12-04-2016                                                         #
# ##################################################################################

#================================================================================================================================== PRIMARY CLASS
import sys, ink.proto
path_modules = '/u/'+ink.io.ConnectUserInfo()[2]+'/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples'
sys.path.append(path_modules)

if '__InK__connect' in sys.modules:
    del(sys.modules["__InK__connect"])
    import __InK__connect
    from __InK__connect import * 
else:
    import __InK__connect
    from __InK__connect import *


#==================================================================================================================== Ink external useful CLASSES
__PIPEIN_GRAPH          = __InK__connect.__PIPEIN_GRAPH__(graphs.DEFAULT, None) # protograph, verbose mode
#================================================================================================================================================

#================================================================================================================================== local CLASSES

class __ORGANIZER__():   
    # print sys.modules
    def __init__(self,X_move_nask=0,Y_move_nask=-1.5,X_ecart_nask=3,ecart=2,ecartClip_Y=1):
        '''   '''
        self.X_move_nask    = X_move_nask
        self.Y_move_nask    = Y_move_nask
        self.X_ecart_nask   = X_ecart_nask
        self.ecart          = ecart
        self.ecartClip_Y    = ecartClip_Y

    def moveClipA7s(self,__PIPEIN_GRAPH,protoGraph,stream,assetClips,layout,layA7Pos_Y):
        '''   '''
        layout    = protoGraph.GetLayout()
        inc_Y     = 0
        # infos nomenclature clip_p0340sub etc -> varNomenClips = ['sub', 'trailer', 'tr', 'vi']
        for pa in assetClips:
            clipA7Pos       = __PIPEIN_GRAPH.getPosition(pa,layout)
            clipA7Pos_X     = 0
            clipA7Pos_Y     = layA7Pos_Y + inc_Y

            X_move_naskRelToLayA7 = clipA7Pos_X + ( self.ecart*2 )
            if str(stream) == 'Upstreams':
                X_move_naskRelToLayA7 = clipA7Pos_X - ( self.ecart*2 )
            Y_move_naskRelToLayA7     = clipA7Pos_Y
            layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            inc_Y = inc_Y + self.ecartClip_Y
        #========= Apply 
        protoGraph.Show()
        protoGraph.Apply()
        protoGraph.SelectAll()


    def moveEditA7s(self,__PIPEIN_GRAPH,protoGraph,assetListEdit,layA7Pos_X,layA7Pos_Y):
        '''   '''

        layout = protoGraph.GetLayout()
        protoGraph.SelectAll()
        selection = protoGraph.GetSelection()       

        for pa in selection:
            try:
                if str(assetListEdit[0]) in str(pa):
                    X_move_naskRelToLayA7 = layA7Pos_X + self.X_move_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + self.Y_move_nask
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetListEdit[1]) in str(pa):
                    X_move_naskRelToLayA7 = layA7Pos_X + self.X_move_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (self.Y_move_nask*2)
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetListEdit[2]) in str(pa) and 'NasK' in str(a):
                    X_move_naskRelToLayA7 = layA7Pos_X + self.X_ecart_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (self.Y_move_nask*3)
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetListEdit[2]) in str(pa) and 'NasK' not in str(a):
                    X_move_naskRelToLayA7 = layA7Pos_X - self.X_ecart_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (self.Y_move_nask*3)
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass


            if 'EDIT-Stereo_Session.a7' in str(pa):
                X_move_naskRelToLayA7 = layA7Pos_X - (self.X_ecart_nask)
                Y_move_naskRelToLayA7 = layA7Pos_Y + (self.Y_move_nask*3)
                layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )

            if 'EDIT-NasK_Stereo.a7' in str(pa):
                X_move_naskRelToLayA7 = layA7Pos_X + (self.X_ecart_nask)
                Y_move_naskRelToLayA7 = layA7Pos_Y + (self.Y_move_nask*3)
                layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )

    def LAYOUT_addA7s(self,__PIPEIN_GRAPH,myFilm,mySeq,mySHOT,myCat,protoGraph,layA7Pos_X,layA7Pos_Y,type_layout):
        ''' add Nask/timing,casting,stereo | Stereo/stereo_session '''

        layout = protoGraph.GetLayout()

        #======================================================================
        #========= add Nask/timing,casting,stereo | 
        #======================================================================

        assetList = []
        
        if str(type_layout) == 'Layout':
            assetList = ['Casting','Timing','Stereo']
            path = myFilm+'/'+mySeq+'/EDIT/NasK/'+myFilm+'_'+mySeq+'_EDIT-NasK_'

        if str(type_layout) == 'Anim':
            assetList = ['Casting','Timing']
            path = myFilm+'/'+mySeq+'/EDIT/NasK/'+myFilm+'_'+mySeq+'_EDIT-NasK_'

        if str(type_layout) == 'Previz':
            assetList = ['Casting','Timing','Stereo']
            path = 'PREVIZ/'+mySeq+'/EDIT/NasK/PREVIZ_'+mySeq+'_EDIT-NasK_'

        if str(type_layout) == 'Usecase':
            assetList = ['Casting','Timing']
            path = 'USECASE/'+mySeq+'/EDIT/NasK/USECASE_'+mySeq+'_EDIT-NasK_'

        #=========
        for Name in assetList:
            A7path = path+Name+'.a7'
            __PIPEIN_GRAPH.add_A7('dirPath',A7path) # _type, A7(str,list,dic), A7Select[optional], A7position[optional]

        #======================================================================
        #========= add Stereo/stereo_session
        #======================================================================
        if str(type_layout) == 'Layout':
            A7path = myFilm+'/'+mySeq+'/EDIT/Stereo/'+myFilm+'_'+mySeq+'_EDIT-Stereo_Session.a7'
            __PIPEIN_GRAPH.add_A7('dirPath',A7path)
        if str(type_layout) == 'Previz':
            A7path = 'PREVIZ/'+mySeq+'/EDIT/Stereo/PREVIZ_'+mySeq+'_EDIT-Stereo_Session.a7'
            __PIPEIN_GRAPH.add_A7('dirPath',A7path)
        # if str(type_layout) == 'Usecase':
        #     A7path = 'USECASE/'+mySeq+'/EDIT/Stereo/USECASE_'+mySeq+'_EDIT-Stereo_Session.a7'
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
                    X_move_naskRelToLayA7 = layA7Pos_X + self.X_move_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + self.Y_move_nask
                    layout.SetPos(a, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetList[1]) in str(a):
                    X_move_naskRelToLayA7 = layA7Pos_X + self.X_move_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (self.Y_move_nask*2)
                    layout.SetPos(a, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetList[2]) in str(a) and 'NasK' in str(a):
                    X_move_naskRelToLayA7 = layA7Pos_X + self.X_ecart_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (self.Y_move_nask*3)
                    layout.SetPos(a, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetList[2]) in str(a) and 'NasK' not in str(a):
                    X_move_naskRelToLayA7 = layA7Pos_X - self.X_ecart_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (self.Y_move_nask*3)
                    layout.SetPos(a, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass

        #======================================================================
        #========= Apply 
        #======================================================================
        protoGraph.Show()
        protoGraph.Apply()
        protoGraph.SelectAll()



    def retrieve_pathInfos(self,__PIPEIN_GRAPH,type_layout,a7,myFilm,mySeq,myShot,mySHOT,check_actor_ok,projectLower):
        ''' retrieve information for path if USECASE or specials cases '''
        if type_layout == 'Usecase' and check_actor_ok.upper() in str(a7).upper():       
            A7_infos      = __PIPEIN_GRAPH.getA7_infos(a7)
            a_catFamily      = A7_infos['a_catFamily']
            if str(a_catFamily) == None:
                a_catFamily = mySeq
            pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/'+a_catFamily+'/'+mySeq+'/'+mySeq+'_'+mySHOT+'.inkGraph'

        if str(myFilm) == 'MLUN' or str(myFilm) == 'SLUN':
            if type_layout == 'Layout':
                pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/RLO/'+myFilm+'/'+mySeq+'/'+mySeq+'_'+myShot+'.inkGraph'
            if type_layout == 'Anim':
                pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/'+myFilm+'/'+mySeq+'/'+mySeq+'_'+mySHOT+'.inkGraph'
        try:
            return pathGraphSave
        except:
            pass

#===========================================================================================================================  end Classes




#===========================================================================================================================  PART 1 , UI LOGICAL

  # BASICS
  # TOOLS NAME COME FROM FUNCTIONS NAME
  # IMPORTANT HACK
  # DEFAULT CATEGORIES ORDER IS ALPHABETICAL FUNCTION NAME INSIDE (IF NO Cat, 'NAME.py' IS THE NAME OF the cat)


def K01_SAMPLE_1(): 
    # Function Name give the Tool Name visible in Ink Interface
    # The description give the mouseover information in Ink Interface
    ''' LAST sandbox.py UPDATE 01-02-2016 '''
    print 'KANGOOROO' # print in Out log Result Window AND InK Konsole after Run Action
  
#=========================== UI
K01_SAMPLE_1.__position__            = 1                       # order of the tool in th category
K01_SAMPLE_1.__category__            = 'B - FIRST SAMPLES'       # comment this line to understand default category
K01_SAMPLE_1.__author__              = 'Karlova' 


def K01_SAMPLE_2():
    ''' 
    KANGOROO TOOL 

    Description : Some samples to understand InK UI logical
    '''
    print 'KANGOROO' # print KANGOROO Dialog Result Window AND in InK Konsole after Run Action
  
  
#=========================== UI
K01_SAMPLE_2.__position__            = 2                                                             # todo to understand
#K01_SAMPLE_2.__toolDesc__           = ( 002, 'kroumch', 'audioIcon.png', 'Pipe', '' )   # todo to understand
K01_SAMPLE_2.__icon__                = 'pipe/createGraphOccLight.png'
K01_SAMPLE_2.__category__            = 'B - FIRST SAMPLES'
K01_SAMPLE_2.__author__              = 'Le Baron Rouge'
K01_SAMPLE_2.__shortText__           = 'Icon Title'                                            # Text write on Icon Tool




#===========================================================================================================================  PART 2 , UI CONSTRUCTION


def K02_UI_CONSTRUCT(Action1='Var_Name', Action2=0, Action3=0, Action4=True, Action5=True, Action6=True):
    '''
    UI CONSTRUCTION SAMPLE 

    - Order of items are relative to order declaration in the function:
    def K02_UI_CONSTRUCT(Action1='Var_Name', Action2=0, Action3=0, Action4=True, Action5=True, Action6=True):
    '''
  
#=========================== UI
K02_UI_CONSTRUCT.__category__         = 'C - UI'
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



#===========================================================================================================================  QT UI external

#=========== Require FOR QT SAMPLE

import sys, ink.proto
path_modules = '/u/'+ink.io.ConnectUserInfo()[2]+'/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples'
sys.path.append(path_modules)
if 'sandboxqt' in sys.modules:
    del(sys.modules["sandboxqt"])
    import sandboxqt
else:
    import sandboxqt

#=========== 

def K03_UI_CONSTRUCT_QT():
    ''' 
    UI QT CONSTRUCTION SAMPLE 

    qt UI/script are in sandboxqt.py
    IMPORTANT : pas de majuscule dans le nom !!!!
    '''

    return None

#=========================== UI
K03_UI_CONSTRUCT_QT.__category__         = 'C - UI'
K03_UI_CONSTRUCT_QT.__author__           = 'cpottier'
K03_UI_CONSTRUCT_QT.__textColor__        = '#7cfcaa'
K03_UI_CONSTRUCT_QT.__customTool__       = 'sandboxqt'




def AA00_MYTOOLZ():
    ''' TOOLz 4 Von KARLOVA '''
    print 'T4'
    import sys, ink.proto
    path_modules = '/u/'+ink.io.ConnectUserInfo()[2]+'/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples'
    sys.path.append(path_modules)

    if '__InK__connect' in sys.modules:
        del(sys.modules["__InK__connect"])
        import __InK__connect
        from __InK__connect import * 
    else:
        import __InK__connect
        from __InK__connect import *

    if 'karlovaboardzatorMain' in sys.modules:
        del(sys.modules["karlovaboardzatorMain"])
        import karlovaboardzatorMain
    else:
        import karlovaboardzatorMain

    return None

#=========================== UI

AA00_MYTOOLZ.__category__         = 'A - A'
AA00_MYTOOLZ.__author__           = 'cpottier'
AA00_MYTOOLZ.__textColor__        = '#7cfcaa'
# AA00_MYTOOLZ.__customTool__       = 'karlovaboardzator'
AA00_MYTOOLZ.__customTool__       = 'karlovaboardzatorMain'










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
K04_GET_SELECTED_ASSETS_INFOS.__category__         = 'D - ASSET INFOS'
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
K05_UI_ADD_ASSET_FROM_PATH.__category__         = 'E - ASSET INTERACTION'
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
K06_UI_ADD_ASSET_FROM_NEWLIB.__category__         = 'E - ASSET INTERACTION'
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
K07_UI_CLONE_ASSET.__category__         = 'E - ASSET INTERACTION'
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
K08_UI_ASSETS_MOVE.__category__         = 'E - ASSET INTERACTION'
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
K09_UI_ADD_MOVE_ASSET_REL_TO_ANOTHER.__category__         = 'E - ASSET INTERACTION'
K09_UI_ADD_MOVE_ASSET_REL_TO_ANOTHER.__author__           = 'cpottier'


#===========================================================================================================================  F - SAVE GRAPH


def K10_SAVE_GRAPH():
    ''' 
    - SAVE GRAPH
        nothing todo : auto add A7 au pif, and save graph
        -> PRIVATE : sample1 with name, sample2 with path
        -> PUBLIC : use your path, see code, change code
    '''

    protoGraph     = ink.proto.Graph( graphs.DEFAULT )
    # protoGraph = ink.proto.Graph('Default')
    layout      = protoGraph.GetLayout()

    # You can't save an empty protograph

    A7auPif        = nomen.Nomen.NewLib( lib='LIB', name='A7fromNewLib', family=['MATERIALS'], types='Maps', stage='' )
    A7auPifProto   = protoGraph.Add(A7auPif)
    A7auPifProto.AddFile('mgs')  # un fichier msg minimal est a associer obligatoirement
    protoGraph.Show()
    protoGraph.Apply()

    # graph A7 to be saved need to be select ? 
    for proto in protoGraph:
        protoGraph.SetSelection([proto])
        protoGraph.Show()
        protoGraph.Apply()
    # selection again hack, todo find why
    proto = protoGraph.List()[0]
    protoGraph.SetSelection([proto])
    protoGraph.Show()
    protoGraph.Apply()

    protoGraphName = 'mySample1'
    # will save 
    # /u/'+projectLower+'/Users/myaccount/Presets/Graphs/mySample1.inkGraph 
    protoGraph.GetSelection(withLayout=True)     # withLayout est à False par defaut
    protoGraph.Write(str(protoGraphName), private=True)

    graphPath = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/'+protoGraphName+'.inkGraph'
    if os.path.isfile(graphPath):
        print 'Private mySample1 [OK]'
        print graphPath , 'Have been saved !!!'
        pass
    else :
        print graphPath + '\n\nSaving FAILED !!!'


    protoGraphName = 'mySample2'
    graphPath = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/'+protoGraphName+'.inkGraph'
    # will save 
    # /u/'+projectLower+'/Users/myaccount/Presets/Graphs/mySample1.inkGraph 
    protoGraph.GetSelection(withLayout=True)     # withLayout est à False par defaut
    protoGraph.Write(graphPath, private=True)

    if os.path.isfile(graphPath):
        print 'Private mySample2 [OK]'
        print graphPath , 'Have been saved !!!'
        pass
    else :
        print graphPath + '\n\nSaving FAILED !!!'

#=========================== UI
K10_SAVE_GRAPH.__category__         = 'F - SAVE GRAPH'
K10_SAVE_GRAPH.__author__           = 'cpottier'





def K11_SAVE_SELECTION_IN_NEW_GRAPH():
    ''' 
    - SAVE SELECTION IN NEW PRIVATE PROTOGRAPH

    You need to import and select some assets of them

    That will save an new grapg with your selected assets
    mySample3_select.inkGraph into Private Graphs

    '''

    protoGraph     = ink.proto.Graph( graphs.DEFAULT )
    layout      = protoGraph.GetLayout()
    protoGraphName = 'mySampleK11_select'
    protoGraph.GetSelection(withLayout=True)     # withLayout est à False par defaut
    protoGraph.Write(str(protoGraphName), private=True)

    graphPath = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/'+protoGraphName+'.inkGraph'
    if os.path.isfile(graphPath):
        print 'Private sample_select [OK]'
        print graphPath , 'Have been saved !!!'
        pass
    else :
        print graphPath + '\n\nSaving FAILED !!!'


#=========================== UI
K11_SAVE_SELECTION_IN_NEW_GRAPH.__category__         = 'F - SAVE GRAPH'
K11_SAVE_SELECTION_IN_NEW_GRAPH.__author__           = 'cpottier'




def K12_SAVE_SEVERAL_A7_IN_SEVERAL_GRAPH():
    ''' 
    - SAVE IN DIFERRENT PROTOGRAPH

    You need to import and select all or some assets

    That will save an new graph for each asset
    mySample_several_1(2,3...).inkGraph into Private Graphs

    '''

    type_layout = None 
    protoGraph  = ink.proto.Graph( graphs.DEFAULT )
    layout      = protoGraph.GetLayout()

    selection   = protoGraph.GetSelection()
    if not selection:
        raise Exception('Please select All a7 !')

    assetList=[]

    for pa in selection:  
        assetList.append(pa)

    protoGraph.SetSelection(assetList , selectionMode = ink.proto.SEL_DELETE, clearBeforeOp=ink.proto.SEL_CLEAR)

    n = 0
    for pa in assetList:
        n += 1
        protoGraphName = 'mySampleK12_several_'+str(n)
        graphPath = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/'+protoGraphName+'.inkGraph'

        protoGraph.SetSelection([pa])
        layout.SetPos(pa, (0,0) ) # optional
        protoGraph.Show()
        protoGraph.Apply()

        protoGraphS  = ink.proto.Graph.FromQuery('foo', [pa]) 
        l = protoGraphS.GetLayout()                           
        l.LoadGraphPos([pa])                              
        protoGraphS.Write(str(graphPath), private=True)

        if os.path.isfile(graphPath):
            print 'Private sample_select [OK]'
            print graphPath , 'Have been saved !!!'
            pass
        else :
            print graphPath + '\n\nSaving FAILED !!!'

#=========================== UI
K12_SAVE_SEVERAL_A7_IN_SEVERAL_GRAPH.__category__         = 'F - SAVE GRAPH'
K12_SAVE_SEVERAL_A7_IN_SEVERAL_GRAPH.__author__           = 'cpottier'









#===================================================================================================================================== CLASS CRUD


def K20_CLASS_CRUD(getAssetsInfos1='True',getAssetsInfos2='Wip',assetToAdd='LIB/MATERIALS/Paint/Maps/Paint-Maps.a7',addA7='True',findA7='True',XNAMEX='XNAMEX-Shading_Shots_Scout.a7', shotList='', castType='Actor', castStage='Ok', shotType='Anim', libName='LIB', familyList='CHARS,PROPS,SETS', update=True, select=True):
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
K20_CLASS_CRUD.__category__         = 'X - TOOLZ'
K20_CLASS_CRUD.__author__           = 'cpottier'
K20_CLASS_CRUD.__textColor__        = '#6699ff'
K20_CLASS_CRUD.__paramsType__        = {
    # 'XNAMEX'        :  ( 'str' , 'XNAMEX-Shading_Shots_Scout.a7')
   'getAssetsInfos1'        :  ( 'bool', 'False' , ['True', 'False']  ),
   'getAssetsInfos2'        :  ( 'bool', 'False' , ['Wip', 'Wip']  ),   
   'assetToAdd'        :  ( 'str' , 'LIB/MATERIALS/Paint/Maps/Paint-Maps.a7'),
   'addA7'            :  ( 'bool', 'False' , ['True', 'False']  ),
   'findA7'            :  ( 'bool', 'True' , ['True', 'False']  )    
   
}



#===========================================================================================================================  PART LAST , GOODIES

#===================================================================================================================================  K80_GOODIES


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

#================================================================================================================================ END  K80_GOODIES

#====================================================================================================================== K81_DATABASE_sqlLite_create

def K81_DATABASE_sqlLite_create(task,projects='Var_Name',status='Var_Name'):
    ''' 
    SQL Create Read Insert :
      - create a db file, if not exist
      - create users table, and populate it, if not exist
      - insert your task
      - read datas
    '''

    db = '/u/'+ink.io.ConnectUserInfo()[2]+'/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples/sqlite.db'
    tb = 'users'

    if not os.path.isfile(db):
        f = open(db, 'w')
        f.close()
        st = os.stat(db)
        os.chmod(db, st.st_mode | stat.S_IEXEC)

    conn = sqlite3.connect(db) # connecteur
    cursor = conn.cursor()

    # if not os.path.isfile(db):
    with conn as c : # curseur
        # creation de la table
        c.execute("""create table if not exists """ +tb+ """(login text, projet text, task text, status text)""")
        # insertion
        c.execute("""insert into """ +tb+ """ values ('GAMIN', 'gri', '86451', 'open')""")
        c.execute("""insert into """ +tb+ """ values ('GAMIN', 'lun', '86617', 'open')""")
        c.execute("""insert into """ +tb+ """ values ('KARLOVA', 'gri', '86619', 'wip')""")
        c.execute("""insert into """ +tb+ """ values ('GAMIN', 'lun', '86604', 'open')""")
        c.execute("""insert into """ +tb+ """ values ('GAMIN', 'dm3', '86624', 'locked')""")
        c.execute("""insert into """ +tb+ """ values ('GAMIN', 'dm18', '86600', 'open')""")
        c.execute("""insert into """ +tb+ """ values ('KARLOVA', 'starwars', '86602', 'open')""")

    # delete all entries > 7
    cursor.execute("""SELECT * FROM """ +tb+""" """)
    nRows = len(cursor.fetchall())
    limit = nRows-7
    # cursor.execute("""DELETE FROM """ +tb+""" WHERE users.task IN (SELECT task FROM users ORDER BY task LIMIT """+str(nRows)+""")""")
    # cursor.execute("""DELETE FROM """ +tb+""" WHERE users.task IN (SELECT task FROM users ORDER BY task LIMIT """+str(limit)+""")""")
    # cursor.execute("""DELETE FROM """ +tb+""" WHERE users.task IN (SELECT task FROM users ORDER BY task LIMIT 9,100)""")
    # cursor.execute("""SELECT * FROM """ +tb+""" """)
    # nRows = str(len(cursor.fetchall()))
    # print nRows

    # insert
    data = {"login" : str(ink.io.ConnectUserInfo()[0]), "projet" : str(projects), "task" : str(task), "status" : str(status)}
    cursor.execute("""
    INSERT INTO """ +tb+ """(login, projet, task, status) VALUES(:login, :projet, :task, :status)""", data)


    print '---- first entry ----'
    cursor.execute('SELECT * FROM '+tb)
    user1 = cursor.fetchone()
    print user1
    print '---- all entries ----', nRows
    users = cursor.fetchall()
    for user in users:
        print user


    cursor.execute("""DELETE FROM """ +tb+""" WHERE users.task IN (SELECT task FROM users ORDER BY task LIMIT  14)""")
    cursor.execute("""SELECT * FROM """ +tb+""" """)

    nRows = len(cursor.fetchall())     
    print nRows

    conn.close()


#=========================== UI
# K81_DATABASE_sqlLite_create.__position__         = 4
K81_DATABASE_sqlLite_create.__category__         = 'Z - GOODIES'
K81_DATABASE_sqlLite_create.__author__           = 'cpottier'
K81_DATABASE_sqlLite_create.__paramsType__        = {  
    'task'        :  ( 'str' , 'Give strawberries tagada for ever to Vador'), 
    'projects'       :  ( 'enum', 'gri',['gri', 'dm3', 'lun'] ),
    'status'       :  ( 'enum', 'open',['open', 'locked', 'wip'] )
}

#================================================================================================================ end  K81_DATABASE_sqlLite_create


#===================================================================================================================== K82_DATABASE_sqlLite_update

def K82_DATABASE_sqlLite_update(task,projects='Var_Name',status='Var_Name'):
    ''' 
    SQL Delete random entry, Update Task entry :
      - read datas
    '''

    db = '/u/'+ink.io.ConnectUserInfo()[2]+'/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples/sqlite.db'
    tb = 'users'

    if not os.path.isfile(db):
        f = open(db, 'w')
        f.close()
        st = os.stat(db)
        os.chmod(db, st.st_mode | stat.S_IEXEC)

    conn = sqlite3.connect(db) # connecteur
    cursor = conn.cursor()

    # if not os.path.isfile(db):
    with conn as c : # curseur
        # creation de la table
        c.execute("""create table if not exists """ +tb+ """(login text, projet text, task text, status text)""")
        # insertion
        c.execute("""insert into """ +tb+ """ values ('GAMIN', 'gri', '86451', 'open')""")
        c.execute("""insert into """ +tb+ """ values ('GAMIN', 'lun', '86617', 'open')""")
        c.execute("""insert into """ +tb+ """ values ('KARLOVA', 'gri', '86619', 'wip')""")
        c.execute("""insert into """ +tb+ """ values ('GAMIN', 'lun', '86604', 'open')""")
        c.execute("""insert into """ +tb+ """ values ('GAMIN', 'dm3', '86624', 'locked')""")
        c.execute("""insert into """ +tb+ """ values ('GAMIN', 'dm18', '86600', 'open')""")
        c.execute("""insert into """ +tb+ """ values ('KARLOVA', 'starwars', '86602', 'open')""")

    # delete all entries > 7
    cursor.execute("""SELECT * FROM """ +tb+""" """)
    nRows = len(cursor.fetchall()) 
    limit = nRows-7
    # cursor.execute("""DELETE FROM """ +tb+""" WHERE users.task IN (SELECT task FROM users ORDER BY task LIMIT """+str(nRows)+""")""")
    # cursor.execute("""DELETE FROM """ +tb+""" WHERE users.task IN (SELECT task FROM users ORDER BY task LIMIT """+str(limit)+""")""")

    # cursor.execute("""DELETE FROM """ +tb+""" WHERE users.task IN (SELECT task FROM users ORDER BY task LIMIT  9,100)""")


    # cursor.execute("""SELECT * FROM """ +tb+""" """)
    # nRows = str(len(cursor.fetchall()))
    # print nRows

    # update last entry
    cursor.execute("""SELECT max(task) FROM """ +tb+""" """)
    max_id = cursor.fetchone()[0]
    cursor.execute("""UPDATE """+tb+""" SET task = ? WHERE task = """+max_id+""" """, (task,))

    print '---- all entries ---- ', nRows
    cursor.execute('SELECT * FROM '+tb)
    users = cursor.fetchall()
    for user in users:
        print user


    cursor.execute("""DELETE FROM """ +tb+""" WHERE users.task IN (SELECT task FROM users ORDER BY task LIMIT  14)""")
    cursor.execute("""SELECT * FROM """ +tb+""" """)

    nRows = len(cursor.fetchall())     
    print nRows
    conn.close()        


#=========================== UI
# K82_DATABASE_sqlLite_update.__position__         = 4
K82_DATABASE_sqlLite_update.__category__         = 'Z - GOODIES'
K82_DATABASE_sqlLite_update.__author__           = 'cpottier'
K82_DATABASE_sqlLite_update.__paramsType__        = {  
    'task'        :  ( 'str' , 'Taskarin de Taskaron')
}

#==================================================================================================================== end  K82_DATABASE_sqlLite_update






#========================================================================================================================================  FIN GOODIES




#================================================================================================================================ AK01_GRAPH_Organizer


def AK01_GRAPH_Organizer(show_neighbours='True',organize_Upstreams='True',organize_Downstreams='True',x_ecart='2',SaveGraph='False',protoGraphM=None): 
    ''' 
    | /
    | \ Tool - Last update 24-03-2016
      ----------------------------------------------------------------------
      - Organize Context Layout for layout, anim, previz, usecase 
      -> get streams      
      -> Add Nask/timing,casting,stereo | Stereo/stereo_session
      ----------------------------------------------------------------------

      Select Anim/Layout.a7
    '''

    #========= MODIFIABLES
    # X_move_nask     = 0
    # Y_move_nask     = -1.5
    # X_ecart_nask    = 3
    # ecart           = 2
    # ecartClip_Y     = 1
    #========= MODIFIABLE , optional
    pathGraphLocal = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/_organizer_toto.inkGraph' # for debug/tests

    #==============================================================================================================
    __ORGANIZER = __ORGANIZER__() # local class for organize .a7
    # __ORGANIZER = __ORGANIZER__(X_move_nask,Y_move_nask,X_ecart_nask,ecart,ecartClip_Y) # to mof defaults choices
    #==============================================================================================================

    #=========  
    protoGraph  = ink.proto.Graph( graphs.DEFAULT )
    layout      = protoGraph.GetLayout()
    selection   = protoGraph.GetSelection()
    type_layout = None 

    if not selection:
        raise Exception('Please select All a7 !')

    #========= Retrieve Type Graph
    for pa in selection: 
        A7_infos      = __PIPEIN_GRAPH.getA7_infos(pa)
        nm_asset      = A7_infos['nm_asset']
        a_types       = A7_infos['a_types']    
        GraphName     = str(nm_asset)

        #========= retrieve graphname
        result = __PIPEIN_GRAPH.getGraph_infos(pa) 
        # return  myNomen, myFilm, mySeq, myShot
        # eg: GRI/S0025/M0010/Layout/GRI_S0025_M0010-Layout.a7 GRI S0025 M0010
        myFilm    = result[1] # 
        mySeq     = result[2]
        myShot    = result[3]
        mySHOT    = result[4]

        myCat     = 'None'
        check_actor_ok = str(mySeq)+'-Actor-Ok'

        #========= determine cases
        try:
            result = __PIPEIN_GRAPH.getTypeLayout(pa,a_types,nm_asset,projectLower,myFilm,myShot,myCat,mySeq,mySHOT,False) # verbose true false , optional
            type_layout      = result[0]
            check_clips      = result[1]
            pathGraphSave    = result[2]
            mySHOT           = result[3]

            if mySHOT == 'None':
                print 'mySHOT == None !'
        except:
            pass

    #========= Retrieve a7 Downstreams and Upstreams
        if str(show_neighbours)=='True':

            layout.SetPos(pa, (0,0) )

            protoGraph.Show()
            protoGraph.Apply()
            protoGraph.SelectAll()

            layA7Pos    = __PIPEIN_GRAPH.getPosition(pa,layout)
            layA7Pos_X  = layA7Pos[0]
            layA7Pos_Y  = layA7Pos[1]

            # FiltersDownstreams = {'family': ['.*'] , 'type': ['.*']}  
            if str(type_layout) == 'Usecase' or str(type_layout) == 'Anim':
                FiltersDownstreams = {'family': ['.*'] , 'type': ['Anim','Clip']} 
            if str(type_layout) == 'Previz' or str(type_layout) == 'Layout':
                FiltersDownstreams = {'family': ['.*'] , 'type': ['Layout','Clip']} 
            StreamProtoList = __PIPEIN_GRAPH.GetStreams('GetDownstreams',protoGraph,layout,pa,FiltersDownstreams) # typeStreams,protoGraph,layout,assetProto,Filters=None,A7pos=None,verbose=False
            FiltersUpstreams = {'family': ['.*'] , 'type': ['.*']}             
            StreamProtoList = __PIPEIN_GRAPH.GetStreams('GetUpstreams',protoGraph,layout,pa,FiltersUpstreams) # typeStreams,protoGraph,layout,assetProto,Filters=None,A7pos=None,verbose=False

    #========= select a7 Upstreams for positioning
        assetClips = []
        UpStreamProtoList = protoGraph.GetUpstreams( pa )

    #========= get infos
        for us in UpStreamProtoList:
            assetClips.append(us)
            if type_layout == 'Usecase' and 'ACTOR-OK' in str(us).upper() and str(mySeq).upper() in str(us).upper():
                A7_infos_us      = __PIPEIN_GRAPH.getA7_infos(us)
                a_catFamily      = A7_infos_us['a_catFamily']
                a_name           = A7_infos_us['a_name']   

    #========= retrieve information for path if USECASE or specials cases 
            result = __ORGANIZER.retrieve_pathInfos(__PIPEIN_GRAPH,type_layout,us,myFilm,mySeq,myShot,mySHOT,check_actor_ok,projectLower)
            if result != None:
                pathGraphSave = result                   

    #========= set position layout.a7 Upstreams
        __ORGANIZER.moveClipA7s(__PIPEIN_GRAPH,protoGraph,'Upstreams',assetClips,layout,layA7Pos_Y)

    #========= select a7 Downstreams  for positioning
    if organize_Downstreams == 'True':
        assetClips = []
        assetClipsByName = []
        niFilters = __PIPEIN_GRAPH._Filters(FiltersDownstreams)
        DownStreamProtoList = protoGraph.GetDownstreams( pa, niFilter=niFilters )
        for ds in DownStreamProtoList:
            if str(check_clips) in str(ds):
                assetClipsByName.append(ds)
        # re order list , by path Name and not InK object logical
        assetClips = sorted(assetClipsByName, reverse=True)
    #========= set position clip.a7 Downstreams
        __ORGANIZER.moveClipA7s(__PIPEIN_GRAPH,protoGraph,'Clips',assetClips,layout,layA7Pos_Y)

    #======================================================================
    #========= add, set position .a7 timing,casting,stereo, stereo_session
    #======================================================================
    __ORGANIZER.LAYOUT_addA7s(__PIPEIN_GRAPH,myFilm,mySeq,mySHOT,myCat,protoGraph,layA7Pos_X,layA7Pos_Y,type_layout)

    #======================================================================
    # SAVE LAYOUT GRAPH
    #======================================================================
    if str(SaveGraph) == 'False' :
        if 'NONE' in str(pathGraphSave).upper():
            print '\n\nERROR, bad path : ' + pathGraphSave
        else:
            print '\nAK01_GRAPH_Organizer is Happy :)\n'
            print 'You can Save ' , GraphName, 'in ', pathGraphSave
    if str(SaveGraph) == 'True' :
        if 'NONE' in str(pathGraphSave).upper():
            print '\n\nERROR, bad path : ' + pathGraphSave
        else:
            protoGraph.Write(pathGraphSave, comment='', private=False)
            if os.path.isfile(pathGraphSave):
                print '\nAK01_GRAPH_Organizer is Happy :)\n'
                print GraphName , '\nHave been saved ', 'in ', pathGraphSave, ' !!!'
            else :
                print pathGraphSave , ' saving FAILED  !!!'


#=========================== UI

AK01_GRAPH_Organizer.__category__         = 'A - PIPE-IN TOOLZ'
AK01_GRAPH_Organizer.__author__           = 'cpottier'
AK01_GRAPH_Organizer.__textColor__        = '#6699ff'
AK01_GRAPH_Organizer.__paramsType__       = {
'show_neighbours'        :  ( 'bool', 'True' , ['True', 'False']  ) ,
'organize_Upstreams'        :  ( 'bool', 'True' , ['True', 'False']  ) ,
'organize_Downstreams'     :  ( 'bool', 'True' , ['True', 'False']  ) ,
'x_ecart'                   :  ( 'enum', '2',['-6','-3','-2', '-1', '1', '2', '3', '6', '9'] ) ,
'SaveGraph'                :  ( 'bool', 'False' , ['True', 'False']  )
}


#============================================================================================================================ end AK01_GRAPH_Organizer


#=========================================================================================================================== AK01_MULTIGRAPH_Organizer


def AK01_MULTIGRAPH_Organizer(SaveGraph='False'):
    ''' 
    | /
    | \ Tool - Last update 24-03-2016
    ----------------------------------------------------------------------
      - Organize and Save Graph(s) 
      
      Select one or several anim, layout .a7
      (previz, usecase enable, slun enable)

      todo:
            -> test mlun
            -> real pathSave when Multi
    ----------------------------------------------------------------------
    '''

    #========= MODIFIABLES
    # X_move_nask     = 0
    # Y_move_nask     = -1.5
    # X_ecart_nask    = 3
    # ecart           = 2
    # ecartClip_Y     = 1
    #========= MODIFIABLE , optional
    pathGraphLocal = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/_organizer_toto.inkGraph' # for debug/tests

    #==============================================================================================================
    __ORGANIZER = __ORGANIZER__() # local class for organize .a7
    # __ORGANIZER = __ORGANIZER__(X_move_nask,Y_move_nask,X_ecart_nask,ecart,ecartClip_Y) # to mof defaults choices
    #==============================================================================================================

    #=========
    protoGraph  = ink.proto.Graph( graphs.DEFAULT )
    layout      = protoGraph.GetLayout()
    selection   = protoGraph.GetSelection()
    type_layout = None 

    if not selection:
        raise Exception('Please select All a7 !')

    assetList=[]

    for pa in selection:  
        assetList.append(pa)
        layout.SetPos(pa, (0,0) )

    protoGraph.SetSelection(assetList , selectionMode = ink.proto.SEL_DELETE, clearBeforeOp=ink.proto.SEL_CLEAR)

    n = 0
    for pa in assetList:
        n += 1
        #========= List of A7 that will be saved in new Graph
        assetList_forGraphtoSave = []

        #=========
        protoGraphName = 'GRAPHNAME_'+str(n)
        graphPathLocal = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/'+protoGraphName+'.inkGraph' # for debug

        protoGraph.SetSelection([pa])
        protoGraph.Show()
        protoGraph.Apply()

        #========= repositionning a7 ref
        layout.SetPos(pa, (0,0) )
        layA7Pos    = __PIPEIN_GRAPH.getPosition(pa,layout)
        layA7Pos_X  = layA7Pos[0]
        layA7Pos_Y  = layA7Pos[1]

        #========= populate List
        assetList_forGraphtoSave.append(pa)
       
        #========= Retrieve Type Graph
        A7_infos      = __PIPEIN_GRAPH.getA7_infos(pa)
        nm_asset      = A7_infos['nm_asset']
        a_types       = A7_infos['a_types'] 
        GraphName     = str(nm_asset)

        #========= retrieve graphname
        try:
            result = __PIPEIN_GRAPH.getGraph_infos(pa,False) # return  myNomen, myFilm, mySeq, myShot, myCat
            myFilm    = result[1] # = PROJECT in fact
            mySeq     = result[2]
            myShot    = result[3]
            mySHOT    = result[4]

            myCat     = 'None'
            check_actor_ok = str(mySeq)+'-Actor-Ok'

        except:
            __PIPEIN_GRAPH.getA7_infos(pa,True)
            __PIPEIN_GRAPH.getGraph_infos(pa,True)
            raise Exception('Error retrieving myShot mySeq mySHOT myCat infos !!!')

        #========= determine cases
        try:
            result = __PIPEIN_GRAPH.getTypeLayout(pa,a_types,nm_asset,projectLower,myFilm,myShot,myCat,mySeq,mySHOT,False) # verbose true false , optional
            type_layout      = result[0]
            check_clips      = result[1]
            pathGraphSave    = result[2]
            mySHOT           = result[3]
            if mySHOT == 'None':
                print 'myShot == None !'
        except:
            pass

        #======================================================================
        #========= Retrieve Downstreams
        #======================================================================
        if str(type_layout) == 'Usecase' or str(type_layout) == 'Anim':
            FiltersDownstreams = {'family': ['.*'] , 'type': ['Anim','Clip']} 
        if str(type_layout) == 'Previz' or str(type_layout) == 'Layout':
            FiltersDownstreams = {'family': ['.*'] , 'type': ['Layout','Clip']}  
        StreamProtoList = __PIPEIN_GRAPH.GetStreams('GetDownstreams',protoGraph,layout,pa,FiltersDownstreams) # typeStreams,protoGraph,layout,assetProto,Filters=None,A7pos=None,verbose=False
        assetList_forGraphtoSave = assetList_forGraphtoSave + StreamProtoList
        #========= select a7 Upstreams for positioning
        assetClips = []
        assetClipsByName = []
        niFilters = __PIPEIN_GRAPH._Filters(FiltersDownstreams)
        DownStreamProtoList = protoGraph.GetDownstreams( pa, niFilter=niFilters )
        for ds in DownStreamProtoList:
            if str(check_clips) in str(ds):
                assetClipsByName.append(ds)
        # re order list , by path Name and not InK object logical
        assetClips = sorted(assetClipsByName, reverse=True)
        #========= set position clip.a7 Downstreams
        # __ORGANIZER.moveClipA7s(__PIPEIN_GRAPH,protoGraph,'Clips',assetClips,layout,layA7Pos_X,layA7Pos_Y,ecart,ecartClip_Y)
        __ORGANIZER.moveClipA7s(__PIPEIN_GRAPH,protoGraph,'Clips',assetClips,layout,layA7Pos_Y)

        #======================================================================
        #========= Retrieve Upstreams
        #======================================================================
        FiltersUpstreams = {'family': ['.*'] , 'type': ['.*']}             
        StreamProtoList = __PIPEIN_GRAPH.GetStreams('GetUpstreams',protoGraph,layout,pa,FiltersUpstreams) # typeStreams,protoGraph,layout,assetProto,Filters=None,A7pos=None,verbose=False
        assetList_forGraphtoSave = assetList_forGraphtoSave + StreamProtoList
        #========= select a7 Upstreams for positioning
        assetClips = []
        UpStreamProtoList = protoGraph.GetUpstreams( pa )
        for us in UpStreamProtoList:
            assetClips.append(us)
        #========= set position layout.a7 Upstreams
        __ORGANIZER.moveClipA7s(__PIPEIN_GRAPH,protoGraph,'Upstreams',assetClips,layout,layA7Pos_Y)

        #========= get infos
        if str(type_layout) == 'Usecase':
            for a7 in assetList_forGraphtoSave:
                if type_layout == 'Usecase' and 'ACTOR-OK' in str(a7).upper() and str(mySeq).upper() in str(a7).upper():
                    A7_infos      = __PIPEIN_GRAPH.getA7_infos(a7)
                    a_catFamily      = A7_infos['a_catFamily']
                    a_name           = A7_infos['a_name']   
        #========= retrieve information for path if USECASE or specials cases 
                result = __ORGANIZER.retrieve_pathInfos(__PIPEIN_GRAPH,type_layout,a7,myFilm,mySeq,myShot,mySHOT,check_actor_ok,projectLower)
                if result != None:
                    pathGraphSave = result   

        # #======================================================================
        #========= add EDIT a7s 
        #======================================================================
        assetListEdit =  __ORGANIZER.LAYOUT_addA7s(__PIPEIN_GRAPH,myFilm,mySeq,mySHOT,myCat,protoGraph,layA7Pos_X,layA7Pos_Y,type_layout)

        #======================================================================
        #========= positionning EDIT a7s  for friendly user layout
        #======================================================================
        assetListEditPos = __ORGANIZER.moveEditA7s(__PIPEIN_GRAPH,protoGraph,assetListEdit,layA7Pos_X,layA7Pos_Y)

        #========= add EDIT a7 in assetList for Graph to Save
        protoGraph.SelectAll()
        selection = protoGraph.GetSelection()   

        if type_layout == 'Layout' or type_layout == 'Anim' or type_layout == 'Previz':
            checkString = str(mySeq) + '_EDIT-'

        if type_layout == 'Usecase':
            # checkString = str(a_name).upper() + '_EDIT-'   
            checkString = str(mySeq).upper() + '_EDIT-' 

        for pa in selection:             
            if str(checkString) in str(pa):
                assetList_forGraphtoSave.append(pa)

        #======================================================================
        #========= Apply 
        #======================================================================
        protoGraph.Show()
        protoGraph.Apply()

        #======================================================================
        # SAVE LAYOUT GRAPH
        #======================================================================
        # pathGraphSave = graphPathLocal
        if str(SaveGraph) == 'False':
            if 'NONE' in str(pathGraphSave).upper():
                print '\n\nERROR, bad path : ' + pathGraphSave
            else:
                print '\nAK01_MULTIGRAPH_Organizer is Happy :)\n'
                print pathGraphSave , 'ready to be saved ...'
        if str(SaveGraph) == 'True': 

            if 'NONE' in str(pathGraphSave).upper():
                print '\n\nERROR, bad path : ' + pathGraphSave
            else:            
                protoGraphS  = ink.proto.Graph.FromQuery(str(protoGraphName), assetList_forGraphtoSave) 
                l = protoGraphS.GetLayout()                           
                l.LoadGraphPos(assetList_forGraphtoSave)         

                protoGraphS.Write(str(pathGraphSave), private=True)

                if os.path.isfile(pathGraphSave):
                    print '\nAK01_MULTIGRAPH_Organizer is Happy :)\n'
                    print pathGraphSave , 'Have been saved !!!'
                    pass
                else :
                    print pathGraphSave + '\n\nSaving FAILED !!!'



#=========================== UI

AK01_MULTIGRAPH_Organizer.__category__          = 'A - PIPE-IN TOOLZ'
AK01_MULTIGRAPH_Organizer.__author__            = 'cpottier'
AK01_MULTIGRAPH_Organizer.__textColor__         = '#6699ff'
AK01_MULTIGRAPH_Organizer.__paramsType__        = {
'SaveGraph'                :  ( 'bool', 'False' , ['True', 'False']  )
}


# ====================================================================================================================== end  AK01_MULTIGRAPH_Organizer



#========================================================================================================================= AK02_LAYOUT_BuildCameraModel


def AK02_LAYOUT_BuildCameraModel(autoload='True',autosave='True',save_private='True',cat='MAIN',_cat=None):
    ''' 
    | /
    | \ Tool - Last update 15-03-2016
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
        params = __PIPEIN_GRAPH.get_autoEcart_X(StreamProtoList,params)

    #========= set position .a7 Downstreams
    n_streams = len(StreamProtoList)
    __PIPEIN_GRAPH.move_StreamProtoList(n_streams,StreamProtoList,layout,A7refPos,params)
    #========= apply and refresh graph
    protoGraph.Show()
    #========= save Graph
    # myGraph = myGraphLocal
    if str(save_private) == 'True':
        myGraph = myGraphLocal        
    if str(autosave) == 'True' and str(save_private) == 'True':
        # __PIPEIN_GRAPH.SaveGraph(myGraph) # to do , to debug
        protoGraph.Write(myG, private=True)
        print '[ OK ] ' + myG + ' have been saved -> ' + myGraph
    if str(autosave) == 'True' and str(save_private) == 'False':
        # __PIPEIN_GRAPH.SaveGraph(myGraph) # to do , to debug
        protoGraph.Write(str(myGraph), private=False)
        print '[ OK ] ' + myG + ' have been saved -> ' + myGraph
    if str(autosave) == 'False':
        print '[ OK ] You can save : ' + myG


# #=========================== UI

AK02_LAYOUT_BuildCameraModel.__category__           = 'A - PIPE-IN TOOLZ'
AK02_LAYOUT_BuildCameraModel.__author__             = 'cpottier'
AK02_LAYOUT_BuildCameraModel.__textColor__          = '#6699ff'
AK02_LAYOUT_BuildCameraModel.__paramsType__         = {
'autoload'                :  ( 'bool', 'True' , ['True', 'False']  ),
'autosave'                :  ( 'bool', 'True' , ['True', 'False']  ),
'save_private'            :  ( 'bool', 'True' , ['True', 'False']  ),
'cat'                     :  ( 'enum', 'MAIN',['MAIN', 'SECONDARY', 'TERTIARY'] )
}

#========================================================================================================================= AK03_LAYOUT_BuildHumanShape


def AK03_LAYOUT_BuildHumanShape(autoload='True',autosave='True',save_private='True',cat='MAIN',_cat=None):
    ''' 
    | /
    | \ Tool - Last update 15-03-2016
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
        params = __PIPEIN_GRAPH.get_autoEcart_X(StreamProtoList,params)

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
    # to do for upstreams ? 

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
    #========= save Graph
    # myGraph = myGraphLocal
    if str(save_private) == 'True':
        myGraph = myGraphLocal        
    if str(autosave) == 'True' and str(save_private) == 'True':
        # __PIPEIN_GRAPH.SaveGraph(myGraph) # to do , to debug
        protoGraph.Write(myG, private=True)
        print '[ OK ] ' + myG + ' have been saved -> ' + myGraph
    if str(autosave) == 'True' and str(save_private) == 'False':
        # __PIPEIN_GRAPH.SaveGraph(myGraph) # to do , to debug
        protoGraph.Write(str(myGraph), private=False)
        print '[ OK ] ' + myG + ' have been saved -> ' + myGraph
    if str(autosave) == 'False':
        print '[ OK ] You can save : ' + myG


# #=========================== UI

AK03_LAYOUT_BuildHumanShape.__category__          = 'A - PIPE-IN TOOLZ'
AK03_LAYOUT_BuildHumanShape.__author__            = 'cpottier'
AK03_LAYOUT_BuildHumanShape.__textColor__         = '#6699ff'
AK03_LAYOUT_BuildHumanShape.__paramsType__        = {
'autoload'                :  ( 'bool', 'True' , ['True', 'False']  ),
'autosave'                :  ( 'bool', 'True' , ['True', 'False']  ),
'save_private'            :  ( 'bool', 'True' , ['True', 'False']  ),
'cat'                     :  ( 'enum', 'MAIN',['MAIN', 'SECONDARY', 'TERTIARY'] )
}















































  
  # print '----------------------------- Get user parameters -------------------'
  # graph = ink.proto.Graph( graphs.DEFAULT )
  
  # # -- Get user parameters
  # castType        = graphs.__GetArgList( castType, separator = '_' )
  # libName         = graphs.__GetArgStr( libName )
  # castStage       = graphs.__GetArgStr( castStage )
  # familyList      = graphs.__GetArgList( familyList, separator = ',' )
  # shotType        = graphs.__GetArgList( shotType, separator = '_' )
  # sceneList       = graphs.__GetArgProtoList( graph, shotList, types=shotType, stage='', onlyExist=False, separator = ',' )
  # update          = graphs.__GetArgBool( update )
  # select          = graphs.__GetArgBool( select )
  
  # print 'castType         : '         , castType
  # print 'libName          : '         , libName
  # print 'castStage        : '         , castStage
  # print 'familyList       : '         , familyList
  # print 'shotType         : '         , shotType
  # print 'sceneList        : '         , sceneList
  # print 'update           : '         , update
  # print 'select           : '         , select

  # List_Types = 'LIT,   SHADOW_CASTERS,   BDD,CHARACTERS, SETS'
  # listTypes = graphs.__GetArgList(List_Types)
  # print listTypes

