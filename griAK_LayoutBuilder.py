# -*- coding: utf-8 -*-
'''                   Some Tools for Pip-In - Verbose Documentation              '''

# ##################################################################################
# MG ILLUMINATION                                                                  #
# First Crazy Debroussailleur : jDepoortere                                        #
# Author : cPOTTIER                                                                #
# Last Update : 27-06-2016                                                         #
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


# ===========================================================================================================================  AK02_LAYOUT_BuildCameraModel



def AK02_LAYOUT_BuildCameraModel(autoload='True',autosave='True',save_private='False',cat='MAIN',all_cats='True',_cat=None):
    ''' 
    | /
    | \ Tool - Last update 27-06-2016
      ----------------------------------------------------------------------
      - Organize MODEL Context Layout 

      - autosave graphs in :
            MODELING/CHARS/MODTECH/
                    -> M_MAIN.inkGraph
                    -> M_SECONDARY.inkGraph
                    -> M_TERTIARY.inkGraph   

      - Auto Execution or Select CAMERA-Actor_ModChars-Ok.a7
      ----------------------------------------------------------------------
        todo :
            - release gestion filters = None
            - r&d : check len name for ecart auto optimal
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

    #=========

    cat_array = [] 

    catFamily = [] # for external request
    if _cat != None :
      cat = _cat[0]
      for a in _catFamily:
        catFamily.append(a)
    if _cat == None :
        catFamily.append(cat)
        cat = cat

    cat_array.append(cat)

    if all_cats == 'True':
        cat_array = ['MAIN', 'SECONDARY', 'TERTIARY']

    for cat_in_Array in cat_array:

        A7R                     = 'CAMERA-Actor_ModChars-Ok.a7'
        A7RefPath               = 'LIB/CAMERAS/CAMERA/Ok/'+A7R
        myG                     = 'M_'+cat_in_Array+'.inkGraph'
        myGraph                 = 'MODELING/CHARS/MODTECH/'+myG
        myGraphLocal            = LOCALPATH+'M_'+cat_in_Array+'.inkGraph' # for debug   
        catFamily = []
        catFamily.append(cat_in_Array)

        #======================================================================
        #========= Declare protograph
        #======================================================================
        protoGraph  = ink.proto.Graph( graphs.DEFAULT )
        layout      = protoGraph.GetLayout()

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
'save_private'            :  ( 'bool', 'False' , ['True', 'False']  ),
'cat'                     :  ( 'enum', 'MAIN',['MAIN', 'SECONDARY', 'TERTIARY'] ),
'all_cats'                :  ( 'bool', 'True' , ['True', 'False']  )
}



def AK03_LAYOUT_BuildHumanShape(autoload='True',autosave='True',save_private='False',cat='MAIN',all_cats='True',_cat=None):
    ''' 
    | /
    | \ Tool - Last update 27-06-2016
      ----------------------------------------------------------------------
      - Organize FACIAL Context Layout

      - autosave graphs in :
                MODELING/CHARS/MODTECH/
                    -> F_MAIN.inkGraph
                    -> F_SECONDARY.inkGraph
                    -> F_TERTIARY.inkGraph

      - Auto Execution or Select Human-Shape_BcsTpl.a7
      ----------------------------------------------------------------------
        todo :
            - release gestion Filters = None
            - r&d : check len name for ecart auto optimal
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



    # catFamily = []
    # if _cat != None :
    #   cat = _cat[0]
    #   for a in _catFamily:
    #     catFamily.append(a)
    # if _cat == None :
    #     catFamily.append(cat)
    #     cat = cat

    # A7R                     = 'Human-Shape_BcsTpl.a7'
    # A7RefPath               = 'LIB/TEMPLATES/Human/Shape/'+A7R
    # myG                     = 'F_'+cat+'.inkGraph'
    # myGraph                 = 'MODELING/CHARS/MODTECH/'+myG
    # myGraphLocal            = LOCALPATH+'F_'+cat+'.inkGraph' # for test
    autoLoadA7ref           = False
    if autoload == 'True':
        autoLoadA7ref       = True # in 2 variables because this script can be call external  

    # Functions ###################################################################################################

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

    # End Functions ################################################################################################  

    #=========

    cat_array = []  # for external request

    catFamily = []
    if _cat != None :
      cat = _cat[0]
      for a in _catFamily:
        catFamily.append(a)
    if _cat == None :
        catFamily.append(cat)
        cat = cat

    cat_array.append(cat)

    if all_cats == 'True':
        cat_array = ['MAIN', 'SECONDARY', 'TERTIARY']

    for cat_in_Array in cat_array:

        A7R                     = 'Human-Shape_BcsTpl.a7'
        A7RefPath               = 'LIB/TEMPLATES/Human/Shape/'+A7R
        myG                     = 'F_'+cat_in_Array+'.inkGraph'
        myGraph                 = 'MODELING/CHARS/MODTECH/'+myG
        myGraphLocal            = LOCALPATH+'F_'+cat_in_Array+'.inkGraph' # for test
        catFamily = []
        catFamily.append(cat_in_Array)
        
        #======================================================================
        #========= Declare protograph
        #======================================================================
        protoGraph  = ink.proto.Graph( graphs.DEFAULT )
        layout      = protoGraph.GetLayout()

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
'save_private'            :  ( 'bool', 'False' , ['True', 'False']  ),
'cat'                     :  ( 'enum', 'MAIN',['MAIN', 'SECONDARY', 'TERTIARY'] ),
'all_cats'                :  ( 'bool', 'True' , ['True', 'False']  )
}
