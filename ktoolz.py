# -*- coding: utf-8 -*-
'''                   Some Tools for Pip-In - Verbose Documentation              '''

# ##################################################################################
# MG ILLUMINATION                                                                  #
# First Crazy Debroussailleur : jDepoortere                                        #
# Author : cPOTTIER                                                                #
# Last Update : 24-05-2016                                                         #
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

        A7_infos         = __PIPEIN_GRAPH.getA7_infos(a7)
        a_catFamily      = A7_infos['a_catFamily']
        a_typeFamily     = A7_infos['a_typeFamily']
        a_types          = A7_infos['a_types'][0]

        check_actor_ok   = '/'+check_actor_ok
        # print check_actor_ok.upper()

        if type_layout == 'Usecase' and check_actor_ok.upper() in str(a7).upper():       
            pathGraphSave        = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/'+a_catFamily+'/'+mySeq+'/'+mySeq+'_'+mySHOT+'.inkGraph'
            # print pathGraphSave

        if str(myFilm) == 'MLUN' or str(myFilm) == 'SLUN':
            if type_layout == 'Layout':
                pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/RLO/'+myFilm+'/'+mySeq+'/'+mySeq+'_'+mySHOT+'.inkGraph'
            if type_layout == 'Anim':
                pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/'+myFilm+'/'+mySeq+'/'+mySeq+'_'+mySHOT+'.inkGraph'
        try:
            return pathGraphSave
        except:
            pass

#===========================================================================================================================  end Classes




#================================================================================================================================ AK01_GRAPH_Organizer


def AK01_GRAPH_Organizer(SaveGraph='False',show_neighbours='True',organize_Upstreams='True',organize_Downstreams='True',x_ecart='2',protoGraphM=None): 
    ''' 
    | /
    | \ Tool - Last update 12-04-2016
      ----------------------------------------------------------------------
      - Organize Context Layout for layout, anim, previz, usecase 
      -> get streams      
      -> Add Nask/timing,casting,stereo | Stereo/stereo_session
      ----------------------------------------------------------------------

      Select Anim/Layout.a7
    '''

    #==============================================================================================================
    __ORGANIZER = __ORGANIZER__() # local class for organize .a7
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
        check_actor_ok = str(mySeq)+'-Actor-Ok.a7'

        #========= determine cases
        try:
            result = __PIPEIN_GRAPH.getTypeLayout(pa,a_types,nm_asset,projectLower,myFilm,myShot,myCat,mySeq,mySHOT,False) # verbose true false , optional
            type_layout      = result[0]
            check_clips      = result[1]
            pathGraphSave    = result[2]
            mySHOT           = result[3]

            # if mySHOT == 'None':
            #     print 'mySHOT == None !'
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
        check_actor_ok = str(mySeq)+'-Actor-Ok.a7'
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
    #========= Patch special case, no cat , to do better
        if 'NONE' in str(pathGraphSave).upper() and str(type_layout) == 'Usecase':
            pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/'+mySeq+'/'+mySeq+'_'+mySHOT+'.inkGraph'


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
'SaveGraph'                :  ( 'bool', 'False' , ['True', 'False']  )
}


#============================================================================================================================ end AK01_GRAPH_Organizer


#=========================================================================================================================== AK01_MULTIGRAPH_Organizer

def AK01_MULTIGRAPH_Organizer(SaveGraph='False'):
    ''' 
    | /
    | \ Tool - Last update 12-04-2016
    ----------------------------------------------------------------------
      - Organize and Save Graph(s) 
      
      Select one or several anim, layout .a7
      (previz, usecase enable, slun enable)

    ----------------------------------------------------------------------
    '''

    #==============================================================================================================
    __ORGANIZER = __ORGANIZER__() # local class for organize .a7
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
            check_actor_ok = str(mySeq)+'-Actor-Ok.a7'

            # print myFilm, mySeq, mySeq, myShot, mySHOT

        except:
            __PIPEIN_GRAPH.getA7_infos(pa,True)
            __PIPEIN_GRAPH.getGraph_infos(pa,True)
            raise Exception('Error retrieving myShot mySeq mySHOT myCat infos !!!')
            # /u/dm3/Users/COM/Presets/Graphs/ANIM/USECASE/UVWXYZ/MACLEO/MACLEO_Test101.inkGraph ready to be saved ...
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
        
        # print myFilm, mySeq, mySeq, myShot, mySHOT
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
        __ORGANIZER.moveClipA7s(__PIPEIN_GRAPH,protoGraph,'Clips',assetClips,layout,layA7Pos_Y)
        # print myFilm, mySeq, mySeq, myShot, mySHOT
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
        # print myFilm, mySeq, mySeq, myShot, mySHOT
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
        #========= Patch special case, no cat , to do better
            if 'NONE' in str(pathGraphSave).upper():
                pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/'+mySeq+'/'+mySeq+'_'+mySHOT+'.inkGraph'
                                    # /u/dm3/Users/COM/Presets/Graphs/ANIM/USECASE/UVWXYZ/MACLEO/MACLEO_Test101.inkGraph ready to be saved ...
        #======================================================================
        #========= add EDIT a7s 
        #======================================================================
        assetListEdit =  __ORGANIZER.LAYOUT_addA7s(__PIPEIN_GRAPH,myFilm,mySeq,mySHOT,myCat,protoGraph,layA7Pos_X,layA7Pos_Y,type_layout)
        print myFilm, mySeq, mySeq, myShot, mySHOT
        #======================================================================
        #========= positionning EDIT a7s  for friendly user layout
        #======================================================================
        assetListEditPos = __ORGANIZER.moveEditA7s(__PIPEIN_GRAPH,protoGraph,assetListEdit,layA7Pos_X,layA7Pos_Y)

        #========= add EDIT a7 in assetList for Graph to Save
        protoGraph.SelectAll()
        selection = protoGraph.GetSelection()   


        checkString = str(mySeq) + '_EDIT-'

        # if type_layout == 'Layout' or type_layout == 'Anim' or type_layout == 'Previz':
        #     checkString = str(mySeq) + '_EDIT-'

        # if type_layout == 'Usecase':
        #     checkString = str(a_name).upper() + '_EDIT-'   

        for pa2 in selection:             
            if str(checkString) in str(pa2):
                assetList_forGraphtoSave.append(pa2)

        #======================================================================
        #========= Apply 
        #======================================================================
        protoGraph.Show()
        protoGraph.Apply()

        #======================================================================
        # SAVE LAYOUT GRAPH
        #======================================================================
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



# ========================================================================================================================== end  AK01_MULTIGRAPH_Organizer

# ===========================================================================================================================  AK0X_LAYOUT_Builder

if PROJECT == 'GRI':
    if USER == 'cpottier' or USER == 'gamin' or USER == 'gamin'  or USER == 'kroumch':
        import griAK_LayoutBuilder
        from griAK_LayoutBuilder import *





#================================================================================================================================ AK04_CHAR_MOD





def AK04_CHAR_MOD(Chars ='LIB/CHARS/MAIN/SECONDARY/TERTIARY/GENERIC',Costume = 'Casual', Hairs='Casual', HairsBranch=False, Actor=False, SaveGraph=False):
    ''' 
    | /
    | \ Tool - Last update 13-05-2016
    ----------------------------------------------------------------------
    Creer les a7 de modeling de perso
    Indiquer le nom de la famille et celui du perso ainsi que le costume si besoin
    Ou selectionner le Model-ok (sans variation) pour une mise a jour du graphe

    Ex : LIB/CHARS/MAIN/Kroumch

    ----------------------------------------------------------------------
    '''

    #==============================================================================================================
    __ORGANIZER = __ORGANIZER__() # local class for organize .a7
    #==============================================================================================================

    if SaveGraph==True:
        writeGraph = True

    writeGraph = False # secu


    def Add_Hairs(protoGraph,_name,costume='Casual'):
        ''' Add Hairs   '''
        if costume=='Casual':
            HairsOk     =  nomen.Nomen.NewLib( lib='LIB', name=_name, family=['CHARS', 'TERTIARY'], types=['Hairs'], stage='Ok' )
            # LIB/CHARS/TERTIARY/BabyFreedoA/Ok/BabyFreedoA-Hairs-Ok.a7 
            HairsProto  =  protoGraph.Add(HairsOk)
            protoGraphTmp.Apply()
            protoGraphTmp.Show(update=True)
            # print HairsProto

    #====================================================================== end Functions


    protoGraphTmp = ink.proto.Graph('Tmp')
    selection     = protoGraphTmp.GetSelection( nomen.Filter().SetTypes(['Model']).SetStage('Ok') )

    if selection:
        nmChars    = selection[0].GetNomen()
    else:
        nmChars    = graphs.__GetArgNomen( Chars, types=['Model'], stage='Ok', onlyExist=False )

        
    if not nmChars:
        raise Exception( 'Enter valid Chars parameter' )






    # Chars = 'LIB/CHARS/TERTIARY/BabyFreedoA'

    # if Chars is 'LIB/CHARS/MAIN/SECONDARY/TERTIARY/GENERIC':
    #     raise Exception( 'Enter valid Chars parameter or select Model-Ok.a7' )



    libName      = nmChars.GetLib()
    name         = nmChars.GetName()
    families     = nmChars.GetFamilies()

    mainFamily   = families[0]
    subFamily    = families[1]
    lineUpFamily = subFamily.capitalize()






    print ''
    print '################################################'
    print '### Graphe de modeling de perso'
    print '################################################'
    print '### Lib          :',libName
    print '### Famille    :',  '/'.join(families)
    print '### Nom        :',name
    print '### Costume :',Costume
    print '################################################'
    print ''

    #==========================================================================
    # Logs and debug Params
    #==========================================================================

    publicGraph= True
    logPath    = None
    printOnly  = False
    verbose    = 0

    if False and os.environ.get('USER') in [ 'ick', 'alec' ]:
        print "--------------TEST DEBUG--------------------"
        publicGraph = True
        logPath     = '/tmp/pipe.Model_Char.log'
        printOnly   = False
        verbose     = 0

    #==========================================================================
    #  Graphe de Reference et graphe a ecrire
    #==========================================================================

    grRef       = 'LIBREF/CHARS_MODELING'
    grDest      = 'MODELING/CHARS' + '/'+subFamily+ '/' +name

    #=================================================================================
    #  Filtre et regle de clone pour les a7 de LIBREF avec name XNAMEX et XCOSTUMEX
    #=================================================================================

    mainFilter    = nomen.Filter().SetLib('LIBREF')
    mainModifier  = nomen.Filter().SetLib( libName ).SetFamilies( families ).SetName( name ).SetVar(Costume)
    mainRules     = {
                      'niModifier' : mainModifier,
                    }

    #==========================================================================
    #  Filtre et regle de clone pour l a7 de lineup
    #==========================================================================

    lineUpFilter    = nomen.Filter().SetLib('LIB').SetFamilies( ['CHARS'] ).SetName( 'SHARED' ).SetTypes(['Model', 'Lineup'])
    lineUpModifier  = nomen.Filter().SetTypes(['Model', 'Lineup', lineUpFamily])
    lineUpRules     = {
                        'niModifier' : lineUpModifier,
                      }

    #===============================================

    showFilter  = nomen.Filter().SetLib( 'LIBREF' )
    showMask    = nomen.FILTER_WITHOUT
    clearBefore = True 

    showRules   = ( showFilter, showMask, clearBefore )

    #=============================================== > VOIR ALEC POUR CETTE PARTIE DU CODE

    def PostApply( graph ):

        def SortAssetPath( a, b ):
            if a.GetNomen().GetVar() == 'Casual':
                return cmp( 0, 1 )
            if b.GetNomen().GetVar() == 'Casual':
                return cmp( 1, 0 )
            return cmp( a.GetPath(), b.GetPath() )

        # get all -Var-Model-Ok and -Var-Model_Turn assets created same Var types
        modelOkList     = graph.Find( nomen.Filter().SetVar('\w.*').SetTypes(['Model']).SetStage('Ok') )
        modelTurnList   = graph.Find( nomen.Filter().SetVar('\w.*').SetTypes(['Model', 'Turn']).SetStage('') )

        if not modelOkList or not modelTurnList:
            return
        modelOk         = modelOkList[0]
        modelTurn       = modelTurnList[0]
        
        modelOkFilter   = modelOk.GetNomen().Copy().SetVar('\w.*')
        modelTurnFilter = modelTurn.GetNomen().Copy().SetVar('\w.*')
        modelOkDir      = os.path.dirname( modelOk.GetPath() )
        modelTurnDir    = os.path.dirname( modelTurn.GetPath() )
        
        # recup de tous les assets tries par nom, mais les Casual en 1er
        modelOkList   = ink.query.Search( dirPath=modelOkDir, niFilter=modelOkFilter, niFilterOpt=ink.proto.FILTER_ONLY, sortCmp=SortAssetPath, rootType=ink.query.SEARCH_BOTH )
        modelTurnList = ink.query.Search( dirPath=modelTurnDir, niFilter=modelTurnFilter, niFilterOpt=ink.proto.FILTER_ONLY, sortCmp=SortAssetPath, rootType=ink.query.SEARCH_BOTH )
        
        # Ajout dans le graph des assets trouves
        modelOkList   = graph.AddAssets( modelOkList )
        modelTurnList = graph.AddAssets( modelTurnList )
        
        # get initials datas (after apply func)
        layout        = graph.GetLayout()
        initPoint     = layout.GetPoint( [ modelOk, modelTurn ] )

        # update layout with new assets
        for idx, modelGroup in enumerate( zip( modelOkList, modelTurnList ) ):
            layout.Horizontal( modelGroup, 2 )
            layout.Move( modelGroup, ( 0, -idx ), magnetPoint=initPoint )

    ######################################################################################################################################
    #------------------------------------------------------------------------------------------------------------------------------------
    #------ Selection du LINEUP de famille
    #------ S'il n existe pas on le cree
    #------ Dans le cas d'un costume different de casual cette connexion n'est pas necessaire car elle est faite a partir du Model-Ok 
    #------------------------------------------------------------------------------------------------------------------------------------
    ######################################################################################################################################

    if Costume == 'Casual':

        #==========================================================================
        #  Test pour savoir si l'A7 de Lineup existe et si il  est locke ou grabbe  
        #==========================================================================

        LineUpNomen  = nomen.Nomen.NewLib( lib=libName, name='SHARED', family=['CHARS'], var='', types=[ 'Model', 'Lineup', lineUpFamily ], stage='' )

        if ink.proto.Exist(LineUpNomen):
            protoGraph   = ink.proto.Graph('ShowLineup')

            if HairsBranch == True:
            #==========================================================================
            #  Add Casual Hairs-Ok 
            #==========================================================================
                HairsOkProto = Add_Hairs(protoGraph,name,Costume)

            LineUpNomenProto  = protoGraph.Add( LineUpNomen )

            IsLock            = ink.query.Asset(LineUpNomen).GetLockInfos()[0]
            HaveBeenPublished = ink.query.Asset(LineUpNomen).GetScmInfos()[0]

            if not IsLock and HaveBeenPublished :
                protoGraph.SetSelection(protoGraph.List() , clearBeforeOp=ink.proto.SEL_CLEAR)
                protoGraph.Apply()
                protoGraph.SelectAll()

                print '############################################################################'
                print '## GRAB OR LOCK A7 Selected (Hairs and LineUp)'
                print '############################################################################'
                # raise Exception( 'GRABBER OU LOCKER l A7 Hairs-Ok ( a7 selectionne) et recommencer la creation!!!!!!!!!!!' )

        #==========================================================================================================
        #  Filtre de selection apres apply general : selectFilter=None, selectMode=None pour ne rien selectionner
        #  En l'occurance ce filtre ne selectionne que les a7 clones a partir des a7 de ref ayant  XNAMEX 
        #==========================================================================================================

        selectFilter = nomen.Filter().SetLib( libName ).SetFamilies( families ).SetName( name )
        selectMask   = nomen.FILTER_ONLY
        selectMode   = ink.proto.SEL_ADD
        selectBefore = ink.proto.SEL_CLEAR

    ####################################################################################
    #-----------------------------------------------------------------------------------
    #------ Creation des a7  dans le cas d'un costume autre que casual
    #------ On cree une branche supplementaire  a partir des a7 casual
    #-----------------------------------------------------------------------------------
    ####################################################################################

    if Costume != 'Casual':

        #==============================================================================================================
        #  Filtre de selection apres apply general : selectFilter=None, selectMode=None pour ne rien selectionner
        #  En l'occurance ce filtre ne selectionne que les a7 clones a partir des a7 de ref ayant  XNAMEX et XOSCTUMEX
        #==============================================================================================================

        selectFilter = nomen.Filter().SetLib( libName ).SetFamilies( families ).SetName( name ).SetVar( Costume )
        selectMask   = nomen.FILTER_ONLY
        selectMode   = ink.proto.SEL_ADD
        selectBefore = ink.proto.SEL_CLEAR

    #===============================================================
    #  Fusion de tous les filtres et de toutes les regles de clone 
    #===============================================================

    cloneRules   = ( 
                     ( lineUpFilter , lineUpRules ),
                     ( mainFilter   , mainRules   ),
                   )
    
    #====================================================================================
    #  Execution de la macro de clone 
    #====================================================================================

    return graphs._ExtraClone( grRef, grDest, cloneRules, PostApply, showFilter, showMask, clearBefore, selectFilter, selectMask, selectMode, selectBefore, publicGraph, writeGraph, printOnly, logPath, verbose )




#=========================== UI

AK04_CHAR_MOD.__category__         = 'A - PIPE-IN TOOLZ'
AK04_CHAR_MOD.__author__           = 'cpottier'
AK04_CHAR_MOD.__textColor__        = '#6699ff'
AK04_CHAR_MOD.__paramsType__       = {
# 'Chars'        :  ( 'str', 'LIB/CHARS/MAIN/SECONDARY/TERTIARY/GENERIC'  ),
'Chars'        :  ( 'str', 'LIB/CHARS/TERTIARY/BabyFreedoA'  ),
'Costume'      :  ( 'str', 'Casual'  ),
'Hairs'        :  ( 'str', 'Casual'  ),
'HairsBranch' :  ( 'bool', 'False' , ['True', 'False']  ),  
'Actor'        :  ( 'bool', 'False' , ['True', 'False']  ),  
'SaveGraph'    :  ( 'bool', 'False' , ['True', 'False']  )
}
