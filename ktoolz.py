# -*- coding: utf-8 -*-
'''                   Some Tools for Pip-In - Verbose Documentation              '''

# ##################################################################################
# MG ILLUMINATION                                                                  #
# First Crazy Debroussailleur : jDepoortere                                        #
# Author : cPOTTIER                                                                #
# Last Update : 16-03-2016                                                         #
# ##################################################################################

import sys, ink.proto
path_modules = "/u/"+ink.io.ConnectUserInfo()[2]+"/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples"
sys.path.append(path_modules)
import __InK__connect
from __InK__connect import *

#==============================================================================================================================Ink useful CLASSES
import __InK__classes
from __InK__classes import __PIPEIN_GRAPH__
protoGraph              = ink.proto.Graph( graphs.DEFAULT )
__PIPEIN_GRAPH          = __PIPEIN_GRAPH__(graphs.DEFAULT, None) # protograph, verbose mode
#================================================================================================================================================

# ===========================================================================================================================  AK00_SETS_AddScout


def AK00_SETS_AddScout(save_after='True'): 
    ''' 
    | /
    | \ Tool - Last update 05-02-2016
      ----------------------------------------------------------------------
      AJOUTE 'Scout.a7' AU DECOR
      ----------------------------------------------------------------------

      - please GRAB Shading.a7
    '''

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
    pathGraphLocal = '/u/gri/Users/cpottier/Presets/Graphs/toto.inkGraph'

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
    # check_clips = None
    # pathGraphSave = None
    # FiltersUpstreams = {'family': ['.*'] , 'type': ['.*']}
    # FiltersDownstreams = {'family': ['.*'] , 'type': ['.*']}

    if not selection:
        raise Exception('Please select All a7 !')

    for pa in selection: 
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


# ================================================================================================================================= end  AK00_SETS_AddScout

# =============================================================================================================================== AK01_MULTIGRAPH_Organizer


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
    pathGraphLocal = '/u/'+projectLower+'/Users/cpottier/Presets/Graphs/toto.inkGraph'

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



    def moveEditA7s(protoGraph):
        '''   '''
        protoGraph.SelectAll()
        selection = protoGraph.GetSelection()       

        for pa in selection:
            try:
                if str(assetListEdit[0]) in str(pa):
                    X_move_naskRelToLayA7 = layA7Pos_X + X_move_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + Y_move_nask
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetListEdit[1]) in str(pa):
                    X_move_naskRelToLayA7 = layA7Pos_X + X_move_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (Y_move_nask*2)
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetListEdit[2]) in str(pa) and 'NasK' in str(a):
                    X_move_naskRelToLayA7 = layA7Pos_X + ecart_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (Y_move_nask*3)
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass
            try:
                if str(assetListEdit[2]) in str(pa) and 'NasK' not in str(a):
                    X_move_naskRelToLayA7 = layA7Pos_X - ecart_nask
                    Y_move_naskRelToLayA7 = layA7Pos_Y + (Y_move_nask*3)
                    layout.SetPos(pa, (X_move_naskRelToLayA7, Y_move_naskRelToLayA7) )
            except:
                pass


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

        protoGraphName = 'GRAPHNAME_'+str(n)
        graphPathLocal = '/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/'+protoGraphName+'.inkGraph'

        protoGraph.SetSelection([pa])
        protoGraph.Show()
        protoGraph.Apply()

        #========= repositionning a7 ref
        layout.SetPos(pa, (0,0) )

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

        #========= Retrieve a7 Downstreams and Upstreams

        layA7Pos    = __PIPEIN_GRAPH.getPosition(pa,layout)
        layA7Pos_X  = layA7Pos[0]
        layA7Pos_Y  = layA7Pos[1]

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

        assetListEditPos = moveEditA7s(protoGraph)

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

        #======================================================================
        # SAVE LAYOUT GRAPH
        #======================================================================
        # pathGraphSave = graphPathLocal
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



# ========================================================================================================================== end  AK01_MULTIGRAPH_Organizer


# ===========================================================================================================================  AK02_LAYOUT_BuildCameraModel



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

