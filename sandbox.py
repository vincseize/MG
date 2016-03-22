# -*- coding: utf-8 -*-
'''     List of Samples Functions to learn  InK UI-API  - Verbose Documentation  '''

# ##################################################################################
# MG ILLUMINATION                                                           	     #
# First Crazy Debroussailleur : jDepoortere                                        #
# Author : cPOTTIER                                                                #
# Last Update : 21-03-2016                                                         #
# ##################################################################################

import sys, ink.proto
path_modules = '/u/'+ink.io.ConnectUserInfo()[2]+'/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples'
sys.path.append(path_modules)
import __InK__connect
from __InK__connect import *

#============================================================================================================================= Ink useful CLASSES
# dev classes
import __InK__classes_forDev
from __InK__classes_forDev import __PIPEIN_GRAPH__

# prod classes
# import __InK__classes
# from __InK__classes import __PIPEIN_GRAPH__
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
K01_SAMPLE_1.__category__            = 'B - FIRST SAMPLES'       # comment this line to understand default category
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
K01_SAMPLE_2.__category__            = 'B - FIRST SAMPLES'
K01_SAMPLE_2.__author__              = 'Le Baron Rouge'
K01_SAMPLE_2.__shortText__           = 'Icon Title'					                           # Text write on Icon Tool




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


def K03_UI_CONSTRUCT_QT(Action1='Var_Name'):
    ''' 
    UI QT CONSTRUCTION SAMPLE 

    qt scripts are in sandboxQt.py
    '''


#=========================== append path for tools qt
try:
    if 'sandboxQt' in sys.modules:
        del(sys.modules["sandboxQt"])
        import sandboxQt 
    else:
        import sandboxQt
except:
    pass
#=========================== UI
K03_UI_CONSTRUCT_QT.__category__         = 'C - UI'
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

#================================================================================================================ end  K82_DATABASE_sqlLite_update











































#################################################################################################################################### FIN GOODIE








# def AK00_FOR_OCC_VON_KROUMCH(save_after='False'): 
#     '''
  
#     Creer la branche de rendu Occ2 pour l oeil droit.
  
#     Selectionner l'a7 Occ_2_Render.

#     '''
    

#     def save_graph(protoGraphResult):
#         '''   '''

#         assetList = []
   
#         protoGraphResult.SelectAll()
#         selection = protoGraphResult.GetSelection()
#         for pa in selection:
#             a_name        = pa.GetNomen()
#             tmp           = str(pa).split('_')[2] # todo better with filter
#             SHOT      = tmp.split('-')[0]
#             FILM          = str(pa).split('_')[1]
#             if '-L-Occ_2_Render' not in str(a_name): # to do better with filter
#                 assetList.append(pa)

#         graphPath='/u/'+projectLower+'/Users/COM/Presets/Graphs/OCC/USECASE/'+FILM+'/'+FILM+'_'+SHOT+'.inkGraph'
#         graphPathLocal='/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/occ_USECASE_'+SHOT+'.inkGraph' # debug

#         grL = ink.proto.Graph( graphPath, load=True, private=False )
#         grL.SelectAll()
#         selection = grL.GetSelection()
#         for pa in selection:
#             assetList.append(pa)

#         # graphPath = graphPathLocal  # debug
#         protoGraphS  = ink.proto.Graph.FromQuery('foo', assetList) 
#         l = protoGraphS.GetLayout()                           
#         l.LoadGraphPos(assetList) 


#     ##----------------------save graph 
#         if save_after=='False' and 'None' not in str(graphPath):
#             print graphPath , 'is ready to be saved !!!'

#         if save_after=='True' and 'None' not in str(graphPath):                         
#             protoGraphS.Write(str(graphPath), private=False)
#             if os.path.isfile(graphPath):                
#                 print graphPath , 'Have been saved !!!'
#                 pass
#             else :
#                 print graphPath + '\n\nSaving FAILED !!!'

#         if 'None' in str(graphPath): 
#           print graphPath + '\n\nSaving FAILED !!!'
#           print '\n\n BAD PATH !!!'



#     ##---------------------------------------------------------------------------------------------------------------- end defs


#     protoGraphToMaj     = ink.proto.Graph('protoGraphToMaj')
#     protoGraphToConnect = ink.proto.Graph('Clean')                    
#     selection           = protoGraphToMaj.GetSelection( nomen.Filter().SetTypes(['Occ', '2', 'Render']).SetEye('L'))
#     layout              = protoGraphToMaj.GetLayout()



#     if not selection:
#         raise Exception("Please Selectionner l'a7 d'Export_Anim  !")

#     for proto in selection:
#         nmShot      = proto.GetNomen()
#         myfilm      = nmShot.GetFilm()
#         myseq       = nmShot.GetSeq()
#         myshot      = nmShot.GetShot()

#     ##----------------------get ref a7 position, and movie downstream position
#         layout.LoadGraphPos([proto])
#         selPos = layout.GetPoint([proto], direction='M')
#         Xref = selPos[0]
#         Yref = selPos[1]
#         niFilters = nomen.Nomen.Empty().SetTypes(['Occ', 'Movie']).SetEye('L').SetVar('V2')
#         StreamProtoList = protoGraphToConnect.GetDownstreams(proto, niFilter=niFilters)
#         for ds in StreamProtoList:
#             layout.LoadGraphPos([ds])
#             selPos = layout.GetPoint([ds], direction='M')
#             Xmovie = selPos[0]
#             Ymovie = selPos[1]

#     ##----------------------LIBREF/Seq/Shot/Occ/LIBREF_Seq_Shot-R-Occ_2_Render.a7----------------------
#         Occ2Render       = nomen.Nomen.NewFilm( film='LIBREF', seq='Seq', shot='Shot', var='', types=['Occ','2', 'Render'], stage='',eye ='R' )
#         Occ2RenderProto  = protoGraphToMaj.Add(Occ2Render)
      
      
#     ##----------------------Occ2Movie----------------------
#         Occ2RMovie       = nomen.Nomen.NewFilm( film='LIBREF', seq='Seq', shot='Shot', var='V2', types=['Occ','Movie'], stage='',eye ='R' )
#         Occ2RMovieProto  = protoGraphToMaj.Add(Occ2RMovie)


#         protoGraphResult = ink.proto.Graph('result')

#         mycloneparam = nomen.Filter()
#         mycloneparam.SetFilm(myfilm)
#         mycloneparam.SetSeq(myseq)
#         mycloneparam.SetShot(myshot)

#         protoGraphResult.Clone(protoGraphToMaj, mycloneparam, substInFile=True, forceCopy=True, copyUBLinks=False)
    
#         result = protoGraphResult.Apply()

#     #======================================================================
#     #========= Branchements
#     #======================================================================
  
#         OccRenderR       = nmShot.SetTypes(['Occ', '2', 'Render']).SetEye('R')
#         OccRenderRProto  = protoGraphToConnect.Add(OccRenderR)
    
#         ExptLighting = nmShot.SetTypes(['Export', 'Lighting']).SetEye('')
#         ExptLightingProto  = protoGraphToConnect.Add(ExptLighting)    
        
#         OccRender = nmShot.SetTypes(['Occ', 'Render']).SetEye('L')
#         OccRenderProto  = protoGraphToConnect.Add(OccRender)      
    
#         OccRenderL       = nmShot.SetTypes(['Occ', 'Render']).SetEye('L')
#         OccRenderLProto  = protoGraphToConnect.Add(OccRenderL)    
    

#         protoGraphToConnect.AddLink(ExptLightingProto, OccRenderRProto, ink.proto.LINK_REF)
#         protoGraphToConnect.AddLink(OccRenderProto, OccRenderRProto, ink.proto.LINK_REF)  
#         protoGraphToConnect.AddLink( OccRenderLProto, OccRenderRProto, ink.proto.LINK_DEP, )    

#         addLinks = protoGraphToConnect.Apply()

#     #======================================================================
#     #========= positionnement
#     #======================================================================
#         offset_Y = 1.5
#         layout = protoGraphToConnect.GetLayout()
#         layout.SetPos(OccRenderRProto, (Xref, Yref-offset_Y) ) # XXX-R-Occ_2_Render.a7
#         niFilters = nomen.Nomen.Empty().SetTypes(['Occ', 'Movie']).SetEye('R').SetVar('V2')
#         StreamProtoList = protoGraphToConnect.GetDownstreams( OccRenderRProto, niFilter=niFilters)
#         for ds in StreamProtoList:
#             layout.SetPos(ds, (Xmovie, Ymovie-offset_Y) ) # XXX-V2-R-Occ_Movie.a7
#         protoGraphToConnect.Show()

#     #======================================================================
#     #========= save graph
#     #======================================================================  
#         save_graph(protoGraphResult)


# #=========================== UI

# AK00_FOR_OCC_VON_KROUMCH.__category__          = 'A - PIPE-IN TOOLZ'
# AK00_FOR_OCC_VON_KROUMCH.__author__            = 'cpottier'
# AK00_FOR_OCC_VON_KROUMCH.__textColor__         = '#6699ff'
# AK00_FOR_OCC_VON_KROUMCH.__paramsType__        = {
# 'save_after'            :  ( 'bool', 'False' , ['True', 'False']  )    

# }


































#=================================================================================================================================  PIPE IN TOOLZ

def AK00_SETS_AddScout(save_after='True'): 
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

        pathGraphLocal = '/u/'+projectLower+'/Users/'+CONNECT_USER1+'/Presets/Graphs/'+a_name+'.inkGraph'
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

AK00_SETS_AddScout.__category__          = 'A - PIPE-IN TOOLZ'
AK00_SETS_AddScout.__author__            = 'cpottier'
AK00_SETS_AddScout.__textColor__         = '#6699ff'
AK00_SETS_AddScout.__paramsType__        = {
'save_after'            :  ( 'bool', 'True' , ['True', 'False']  )    

}



def AK01_GRAPH_Organizer(show_neighbours='True',organize_Upstreams='True',organize_Downstreams='True',x_ecart='2',SaveGraph='False',protoGraphM=None): 
    ''' 
    | /
    | \ Tool - Last update 10-03-2016
      ----------------------------------------------------------------------
      - Organize Context Layout for layout, anim, previz, usecase 
      -> get streams      
      -> Add Nask/timing,casting,stereo | Stereo/stereo_session

      - todo
              switch to auto save usecase
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
    pathGraphLocal = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/toto.inkGraph'

    # DONT TOUCH #########################################################
    MASTER              = None
    SEQUENCE            = None

    layA7Pos_X          = None
    layA7Pos_Y          = None
    # ecart               = int(graphs.__GetArgStr(int(x_ecart)))
    ecart               =  2
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
            path = 'USECASE/'+SEQUENCE+'/EDIT/NasK/USECASE_'+SEQUENCE+'_EDIT-NasK_'

        # USECASE/PIGA/EDIT/NasK/USECASE_PIGA_EDIT-NasK_Casting.a7 
        # print path

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

    # if protoGraphM != None:
    #     protoGraph = protoGraphM 
    # else:
    #     protoGraph  = ink.proto.Graph( graphs.DEFAULT )        


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
        try:

            result = __PIPEIN_GRAPH.getGraph_infos(pa)
            MASTER       = result[0]
            SEQUENCE     = result[1]
            SHOT         = result[2]
            CATEGORY     = result[3]

            #========= get a7 position
            # layA7Pos    = __PIPEIN_GRAPH.getPosition(pa,layout)
            # layA7Pos_X = layA7Pos[0]
            # layA7Pos_Y = layA7Pos[1]


        except:
            __PIPEIN_GRAPH.getA7_infos(pa,True)
            raise Exception('Error retrieving MASTER SEQUENCE SHOT CATEGORY infos !!!')

        #========= determine cases
        try:

            result = __PIPEIN_GRAPH.getTypeLayout(pa,a_types,nm_asset,projectLower,PROJECT,MASTER,CATEGORY,SEQUENCE,SHOT)

            type_layout      = result[0]
            check_clips      = result[1]
            pathGraphSave    = result[2]
            SHOT             = result[3]

            if SHOT == 'None':
                print 'Shot == None !'
                
        except:
            # result = __PIPEIN_GRAPH.getTypeLayout(pa,a_types,nm_asset,projectLower,PROJECT,MASTER,CATEGORY,SEQUENCE,SHOT,True)
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
        for us in UpStreamProtoList:
            assetClips.append(us)
            if type_layout == 'Usecase' and 'ACTOR-OK' in str(us).upper() and str(SEQUENCE).upper() in str(us).upper():
                A7_infos_us      = __PIPEIN_GRAPH.getA7_infos(us)
                a_catFamily      = A7_infos_us['a_catFamily']
                a_name           = A7_infos_us['a_name'] 
                pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/'+a_catFamily+'/'+SEQUENCE+'/'+a_name+'_'+SHOT+'.inkGraph'

    #========= set position layout.a7 Upstreams
        moveClipA7s(protoGraph,'Upstreams',assetClips,layout,layA7Pos_X,layA7Pos_Y)
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
        moveClipA7s(protoGraph,'Clips',assetClips,layout,layA7Pos_X,layA7Pos_Y)

    #======================================================================
    #========= add, set position .a7 timing,casting,stereo, stereo_session
    #======================================================================
    LAYOUT_addA7s(PROJECT,SEQUENCE,SHOT,CATEGORY,protoGraph,layA7Pos_X,layA7Pos_Y,X_move_nask,Y_move_nask,ecart,type_layout)

    #======================================================================
    # SAVE LAYOUT GRAPH
    #======================================================================
    print '\nAK01_GRAPH_Organizer is Happy :)\n'
    if str(SaveGraph) == 'False' :
        print 'You can Save ' , GraphName, 'in ', pathGraphSave
    if str(SaveGraph) == 'True' :
        # todo to understand
        # __PIPEIN_GRAPH.SaveGraph(pathGraphSave)
        # print GraphName , 'Have been saved ', 'in ', pathGraphSave, ' !!!'



        protoGraph.Write(pathGraphSave, comment='', private=False)
        if os.path.isfile(pathGraphSave):
            print GraphName , '\nHave been saved ', 'in ', pathGraphSave, ' !!!'
        else :
            print pathGraphSave , ' saving FAILED  !!!'


#=========================== UI

AK01_GRAPH_Organizer.__category__         = 'A - PIPE-IN TOOLZ'
AK01_GRAPH_Organizer.__author__           = 'cpottier'
AK01_GRAPH_Organizer.__textColor__        = '#6699ff'
AK01_GRAPH_Organizer.__paramsType__       = {
# 'sep'                       :  ('') ,
# 'master_layout'             :  ( 'bool', 'True' , ['True', 'False']  ) ,  # todo switch layout/anim
# 'master_anim'               :  ( 'bool', 'False' , ['True', 'False']  ) , # todo switch layout/anim
'show_neighbours'        :  ( 'bool', 'True' , ['True', 'False']  ) ,
'organize_Upstreams'        :  ( 'bool', 'True' , ['True', 'False']  ) ,
'organize_Downstreams'     :  ( 'bool', 'True' , ['True', 'False']  ) ,
'x_ecart'                   :  ( 'enum', '2',['-6','-3','-2', '-1', '1', '2', '3', '6', '9'] ) ,
'SaveGraph'                :  ( 'bool', 'False' , ['True', 'False']  )
}


#=========================================================================================================================== AK01_MULTIGRAPH_Organizer


def AK01_MULTIGRAPH_Organizer(SaveGraph='False'):
    ''' 
    | /
    | \ Tool - Last update 16-03-2016
    ----------------------------------------------------------------------
      - Organize and Save Graph(s) 
      - Multi select and auto batch mode enable
      
      Select one or several anim, layout .a7
      (previz, usecase enabled)

    ----------------------------------------------------------------------
    '''

    # MODIFIABLE #########################################################
    # Nask relative with Layout.a7
    X_move_nask         =  0
    Y_move_nask         = -1.5
    ecart_nask          =  3
    # for debug or tests
    pathGraphLocal = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/toto.inkGraph'

    # DONT TOUCH #########################################################
    MASTER              = None
    SEQUENCE            = None

    layA7Pos_X          = None
    layA7Pos_Y          = None
    # ecart               = int(graphs.__GetArgStr(int(x_ecart)))
    ecart               = 2
    ecartClip_Y         = 1

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
            X_move_naskRelToLayA7 = ecart*2
            if str(stream) == 'Upstreams':
                X_move_naskRelToLayA7 = -abs(X_move_naskRelToLayA7)
            Y_move_naskRelToLayA7     = clipA7Pos_Y
            layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            inc_Y = inc_Y + ecartClip_Y
        #========= Apply 
        protoGraph.Show()
        protoGraph.Apply()
        protoGraph.SelectAll()



    def moveEditA7s(protoGraph,assetListEdit,layA7Pos_X,layA7Pos_Y,X_move_nask,Y_move_nask):
        '''   '''

        layout = protoGraph.GetLayout()
        protoGraph.SelectAll()
        selection = protoGraph.GetSelection()       

        for pa in selection:
            # print pa
            try:
                if str(assetListEdit[0]) in str(pa):
                    print pa
                    X_move_naskRelToLayA7 = layA7Pos_X + X_move_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + Y_move_nask
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetListEdit[1]) in str(pa):
                    print pa
                    X_move_naskRelToLayA7 = layA7Pos_X + X_move_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (Y_move_nask*2)
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetListEdit[2]) in str(pa) and 'NasK' in str(a):
                    print pa
                    X_move_naskRelToLayA7 = layA7Pos_X + ecart_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (Y_move_nask*3)
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetListEdit[2]) in str(pa) and 'NasK' not in str(a):
                    print pa
                    X_move_naskRelToLayA7 = layA7Pos_X - ecart_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (Y_move_nask*3)
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass


            if 'EDIT-Stereo_Session.a7' in str(pa):
                X_move_naskRelToLayA7 = layA7Pos_X - (ecart_nask)
                Y_move_naskRelToLayA7 = layA7Pos_Y + (Y_move_nask*3)
                layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )

            if 'EDIT-NasK_Stereo.a7' in str(pa):
                X_move_naskRelToLayA7 = layA7Pos_X + (ecart_nask)
                Y_move_naskRelToLayA7 = layA7Pos_Y + (Y_move_nask*3)
                layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )



    def LAYOUT_addA7s(PROJECT,SEQUENCE,SHOT,CATEGORY,protoGraph,type_layout):
        ''' add Nask/timing,casting,stereo | Stereo/stereo_session '''

        assetListEdit = []
        
        #========= add timing/casting/stereo

        if str(type_layout) == 'Layout':
            assetListEdit = ['Casting','Timing','Stereo']
            path = PROJECT+'/'+SEQUENCE+'/EDIT/NasK/'+PROJECT+'_'+SEQUENCE+'_EDIT-NasK_'

        if str(type_layout) == 'Anim':
            assetListEdit = ['Casting','Timing']
            path = PROJECT+'/'+SEQUENCE+'/EDIT/NasK/'+PROJECT+'_'+SEQUENCE+'_EDIT-NasK_'

        if str(type_layout) == 'Previz':
            assetListEdit = ['Casting','Timing','Stereo']
            path = 'PREVIZ/'+SEQUENCE+'/EDIT/NasK/PREVIZ_'+SEQUENCE+'_EDIT-NasK_'

        if str(type_layout) == 'Usecase':
            assetListEdit = ['Casting','Timing']
            path = 'USECASE/'+SEQUENCE+'/EDIT/NasK/USECASE_'+SEQUENCE+'_EDIT-NasK_'

        #=========
        for Name in assetListEdit:
            A7path = path+Name+'.a7'
            __PIPEIN_GRAPH.add_A7('dirPath',A7path,True) # _type, A7(str,list,dic), A7Select[optional], A7position[optional]

        #========= add Stereo/stereo_session

        if str(type_layout) == 'Layout':
            A7path = PROJECT+'/'+SEQUENCE+'/EDIT/Stereo/'+PROJECT+'_'+SEQUENCE+'_EDIT-Stereo_Session.a7'
            __PIPEIN_GRAPH.add_A7('dirPath',A7path)
        if str(type_layout) == 'Previz':
            A7path = 'PREVIZ/'+SEQUENCE+'/EDIT/Stereo/PREVIZ_'+SEQUENCE+'_EDIT-Stereo_Session.a7'
            __PIPEIN_GRAPH.add_A7('dirPath',A7path)
        # if str(type_layout) == 'Usecase':
        #     A7path = 'USECASE/'+SEQUENCE+'/EDIT/Stereo/USECASE_'+SEQUENCE+'_EDIT-Stereo_Session.a7'
        #     __PIPEIN_GRAPH.add_A7('dirPath',A7path)

        #========= Apply VERY IMPORTANT
        protoGraph.Show()
        protoGraph.Apply()

        return assetListEdit


    #============================================================================================================== end functions

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

            result = __PIPEIN_GRAPH.getGraph_infos(pa)
            MASTER       = result[0]
            SEQUENCE     = result[1]
            SHOT         = result[2]
            CATEGORY     = result[3]
        except:
            __PIPEIN_GRAPH.getA7_infos(pa,True)
            __PIPEIN_GRAPH.getGraph_infos(pa,True)
            raise Exception('Error retrieving MASTER SEQUENCE SHOT CATEGORY infos !!!')

        #========= determine cases
        try:

          result = __PIPEIN_GRAPH.getTypeLayout(pa,a_types,nm_asset,projectLower,PROJECT,MASTER,CATEGORY,SEQUENCE,SHOT)
          type_layout      = result[0]
          check_clips      = result[1]
          pathGraphSave    = result[2]
          SHOT             = result[3]

          if SHOT == 'None':
              print 'Shot == None !'

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
        moveClipA7s(protoGraph,'Clips',assetClips,layout,layA7Pos_X,layA7Pos_Y)

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
        moveClipA7s(protoGraph,'Upstreams',assetClips,layout,layA7Pos_X,layA7Pos_Y)

        #======================================================================
        ##========= retrieve information for path if USECASE
        #======================================================================
        if str(type_layout) == 'Usecase':
            for a7 in assetList_forGraphtoSave:
                if type_layout == 'Usecase' and 'ACTOR-OK' in str(a7).upper() and str(SEQUENCE).upper() in str(a7).upper():
                    A7_infos      = __PIPEIN_GRAPH.getA7_infos(a7)
                    a_catFamily      = A7_infos['a_catFamily']
                    a_name           = A7_infos['a_name'] 
                    pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/'+a_catFamily+'/'+SEQUENCE+'/'+a_name+'_'+SHOT+'.inkGraph'
 
        #======================================================================
        #========= add EDIT a7s 
        #======================================================================

        assetListEdit = LAYOUT_addA7s(PROJECT,SEQUENCE,SHOT,CATEGORY,protoGraph,type_layout)

        #======================================================================
        #========= positionning EDIT a7s  for friendly user layout
        #======================================================================

        assetListEditPos = moveEditA7s(protoGraph,assetListEdit,layA7Pos_X,layA7Pos_Y,X_move_nask,Y_move_nask)

        #========= add EDIT a7 in assetList for Graph to Save
        protoGraph.SelectAll()
        selection = protoGraph.GetSelection()   

        if type_layout == 'Layout' or type_layout == 'Anim' or type_layout == 'Previz':
            checkString = str(SEQUENCE) + '_EDIT-'

        if type_layout == 'Usecase':
            checkString = str(a_name).upper() + '_EDIT-'   

        for pa in selection:             
            if str(checkString) in str(pa):
                assetList_forGraphtoSave.append(pa)

        #======================================================================
        #========= Apply 
        #======================================================================
        protoGraph.Show()
        protoGraph.Apply()
        # protoGraph.SelectAll()

        #======================================================================
        # SAVE LAYOUT GRAPH
        #======================================================================
        pathGraphSave = graphPathLocal
        if str(SaveGraph) == 'False':
            print pathGraphSave , 'ready to be saved ...'
        if str(SaveGraph) == 'True': 
            protoGraphS  = ink.proto.Graph.FromQuery(str(protoGraphName), assetList_forGraphtoSave) 
            l = protoGraphS.GetLayout()                           
            l.LoadGraphPos(assetList_forGraphtoSave)         

            protoGraphS.Write(str(pathGraphSave), private=True)

            if os.path.isfile(pathGraphSave):
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

