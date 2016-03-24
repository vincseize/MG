# -*- coding: utf-8 -*-
'''                   Some Tools for Pip-In - Verbose Documentation              '''

# ##################################################################################
# MG ILLUMINATION                                                                  #
# First Crazy Debroussailleur : jDepoortere                                        #
# Author : cPOTTIER                                                                #
# Last Update : 23-03-2016                                                         #
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


    # def moveEditA7s(self,__PIPEIN_GRAPH,protoGraph,assetListEdit,layA7Pos_X,layA7Pos_Y,X_move_nask,Y_move_nask,X_ecart_nask):
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



#================================================================================================================================ AK01_GRAPH_Organizer


def AK01_GRAPH_Organizer(SaveGraph='False',show_neighbours='True',organize_Upstreams='True',organize_Downstreams='True',x_ecart='2',protoGraphM=None): 
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
        assetClips = []
        UpStreamProtoList = protoGraph.GetUpstreams( pa )
        for us in UpStreamProtoList:
            assetClips.append(us)
            if type_layout == 'Usecase' and 'ACTOR-OK' in str(us).upper() and str(mySeq).upper() in str(us).upper():
                A7_infos_us      = __PIPEIN_GRAPH.getA7_infos(us)
                a_catFamily      = A7_infos_us['a_catFamily']
                a_name           = A7_infos_us['a_name'] 
                pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/'+a_catFamily+'/'+mySeq+'/'+a_name+'_'+mySHOT+'.inkGraph'

            if str(myFilm) == 'MLUN' or str(myFilm) == 'SLUN':
                if type_layout == 'Layout':
                    pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/RLO/'+myFilm+'/'+mySeq+'/'+mySeq+'_'+myShot+'.inkGraph'
                if type_layout == 'Anim':
                    pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/'+myFilm+'/'+mySeq+'/'+mySeq+'_'+mySHOT+'.inkGraph'

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
    print '\nAK01_GRAPH_Organizer is Happy :)\n'
    if str(SaveGraph) == 'False' :
        print 'You can Save ' , GraphName, 'in ', pathGraphSave
    if str(SaveGraph) == 'True' :
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
            result = __PIPEIN_GRAPH.getGraph_infos(pa,True) # return  myNomen, myFilm, mySeq, myShot, myCat
            myFilm    = result[1] # = PROJECT in fact
            mySeq     = result[2]
            myShot    = result[3]
            mySHOT    = result[4]
            myCat     = 'None'
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

        #======================================================================
        ##========= retrieve information for path if USECASE
        #======================================================================
        if str(type_layout) == 'Usecase':
            for a7 in assetList_forGraphtoSave:
                if type_layout == 'Usecase' and 'ACTOR-OK' in str(a7).upper() and str(mySeq).upper() in str(a7).upper():
                    A7_infos      = __PIPEIN_GRAPH.getA7_infos(a7)
                    a_catFamily      = A7_infos['a_catFamily']
                    a_name           = A7_infos['a_name'] 
                    pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/'+a_catFamily+'/'+mySeq+'/'+a_name+'_'+mySHOT+'.inkGraph'
 
        if str(myFilm) == 'MLUN' or str(myFilm) == 'SLUN':
            if type_layout == 'Layout':
                pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/RLO/'+myFilm+'/'+mySeq+'/'+mySeq+'_'+myShot+'.inkGraph'
            if type_layout == 'Anim':
                pathGraphSave    = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/'+myFilm+'/'+mySeq+'/'+mySeq+'_'+mySHOT+'.inkGraph'

        #======================================================================
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

