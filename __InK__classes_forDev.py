# -*- coding: utf-8 -*-
'''     List of Samples Functions to learn  InK UI-API  - Verbose Documentation  '''

# ##################################################################################
# MG ILLUMINATION                                                                  #
# First Crazy Debroussailleur : jDepoortere                                        #
# Author : cPOTTIER                                                                #
# Last Update : 22-03-2016                                                         #
# ##################################################################################

#================================================================================================================================== PRIMARY CLASS
import sys, ink.proto
path_modules = "/u/"+ink.io.ConnectUserInfo()[2]+"/Users/COM/InK/Scripts/Python/proj/pipe/ink/exemples"
sys.path.append(path_modules)
import __InK__connect
from __InK__connect import *
#=======================================================================================================================  CLASS __PIPEIN_GRAPH__


class __PIPEIN_GRAPH__():
    

    def __init__(self,graphName,verbose=None):
        self.verbose    = verbose
        self.graphName    = graphName
        self.protoGraph   = ink.proto.Graph( self.graphName )
    

    def _IsAppQT(self):
        try:
            ink.qt.ui.app
            return True
        except (AttributeError, NameError):
            return False
        return None  


    #-------------------------- Graph


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


    def saveGraph(self,graphPath,verbose=False):
        ''' save Graph with path 
            -> control if really graphPath isfile 
        '''

        # self.protoGraph.GetSelection(withLayout=True)     # withLayout est à False par defaut
        # self.protoGraphM.Write(str(protoGraphName), private=True)

        self.protoGraph.GetSelection()
        self.protoGraph.Apply()
        result = self.protoGraph.Write(graphPath, comment='', private=False)



        if os.path.isfile(graphPath):
            print graphPath , 'Have been saved !!!'
            pass
        else :
            print graphPath + '\n\nSaving FAILED !!!'

        return result


    def getGraph_infos(self,pa,verbose=False):
        ''' 
            for GraphBuilder 
            todo : new class only for Builder toolz
        '''

        myNomen     = pa.GetNomen()
        myFilm      = myNomen.GetFilm()
        mySeq       = myNomen.GetSeq()
        myShot      = myNomen.GetShot()
        mySHOT      = 'None' # for specials cases as previz or usecase

        # retreive shot if specials cases, as previz, usecase 
        try:
            checkShot = str(pa).split('_P')[1] # todo better with filter
            mySHOT = 'P'+checkShot[0:4]
        except:
            pass
        try:
            checkShot = str(pa).split('_Z')[1] # todo better with filter
            mySHOT = 'Z'+checkShot[0:4]
        except:
            pass

        if verbose == True:
            print myNomen, myFilm, mySeq, myShot, mySHOT

        return  myNomen, myFilm, mySeq, myShot, mySHOT # eg: GRI/S0025/M0010/Layout/GRI_S0025_M0010-Layout.a7 GRI S0025 M0010



    #------------------------- Layout

                          # pa,a_types,nm_asset,projectLower,PROJECT,myShot,myCat,mySeq,SHOT,True
    def getTypeLayout(self,pa,a_types,nm_asset,projectLower,PROJECT,myShot,myCat,mySeq,SHOT,verbose=False):
        ''' 
            for GraphBuilder 
            todo : new class only for Builder toolz
        '''
        
        # case Layout
        if len(a_types) == 1 and a_types[0] == 'Layout' and 'PREVIZ' not in str(nm_asset):
            type_layout = 'Layout'
            check_clips = '-Layout_Clip'
            pathGraphSave = '/u/'+projectLower+'/Users/COM/Presets/Graphs/RLO/'+mySeq+'/'+mySeq+'_'+myShot+'.inkGraph'

        # case Previz
        if len(a_types) == 1 and a_types[0] == 'Layout' and 'PREVIZ' in str(nm_asset):
            type_layout = 'Previz'
            check_clips = '-Layout_Clip'
            pathGraphSave = '/u/'+projectLower+'/Users/COM/Presets/Graphs/PREVIZ/'+mySeq+'/'+mySeq+'_'+myShot+'.inkGraph'

        # case Anim 
        if len(a_types) == 1 and a_types[0] == 'Anim' and 'USECASE' not in str(nm_asset):
            type_layout = 'Anim'
            check_clips = '-Anim_Clip'
            pathGraphSave = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/'+PROJECT+'/'+mySeq+'/'+mySeq+'_'+SHOT+'.inkGraph'

        # case Usecase
        if len(a_types) == 1 and a_types[0] == 'Anim' and 'USECASE' in str(nm_asset):
            type_layout = 'Usecase'
            check_clips = '-Anim_Clip'
            tmp = str(pa).split('USECASE_')[1] # todo better with filter
            mySeq = tmp.split('_')[0]
            tmp2 = tmp.split('_')[1]
            SHOT = tmp2.split('-')[0]

            # Prov, premiere pass to do better
            pathGraphSave = '/u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/'+myCat+'/'+mySeq+'/'+mySeq+'_'+SHOT+'.inkGraph' 

            # Assets # sample 1
            # USECASE/MANI/Test101/Anim/USECASE_MANI_Test101-Anim.a7 
            # Assets # sample 2
            # USECASE/LOOKDEV/BathroomOffset/Anim/USECASE_LOOKDEV_BathroomOffset-Anim.a7 

            # Graphs # sample 1
            # /u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/TERTIARY/MANI/ManI_Test101.inkGraph # private 
            # Graphs # sample 2
            # /u/'+projectLower+'/Users/COM/Presets/Graphs/ANIM/USECASE/LOOKDEV/BathroomOffset.inkGraph 

        if verbose==True:
            print 'type_layout : ' + type_layout
            print 'check_clips : ' + check_clips
            print 'pathGraphSave : ' + pathGraphSave
            print 'SHOT : ' + SHOT

        return type_layout, check_clips, pathGraphSave, SHOT



    #------------------------ A7




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
        self.protoGraph        = ink.proto.Graph( self.graphName )
        assetList         = self.protoGraph.GetSelection( nomen.Filter().SetTypes(['.*']).SetStage('') ) # todo, to understand return Object list
        if not assetList:
            raise Exception('Class error : Please select at list one Asset !')  
        for asset in assetList: 
            assetName = asset.GetNomen() # all asset Infos
            result.append(assetName)
        # return assetList, self.verbose # todo , to understand return Objects
        return assetList, result, self.verbose


    def getA7_infos(self,pa,verbose=False):
        ''' get a7 infos 

            - todo: find more, or all available infos
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
        self.protoGraph.Show()
        self.protoGraph.Apply()
        self.protoGraph.SelectAll()


    def get_autoEcart_X(self,StreamProtoList,params):
        ''' Get Auto Ecart X '''

        longest = []
        longestName = []
        for pa in StreamProtoList:
            A7_infos = self.getA7_infos(pa,False)  # True False optional for verbose Mode
            a_name   = A7_infos['a_name'] 
            l = len(str(a_name))
            longestName.append(l)
        try:
            longestName = max(longestName)
        except:
            pass
        longest.append(longestName)
        nLetters = float(max(longest))
        autoEcart_X = ( nLetters / 10. ) * 3.  
        params['ecart_a7_X'] = autoEcart_X
        params['X_space_betweenGroup'] = autoEcart_X*1.1 

        return params

#======================================================================================================================= End class __PIPEIN_GRAPH__ 







#==============================================================================================================================  CLASS __SENDMAIL__

# class __SENDMAIL__():

#     hostname = MAIL_HOSTNAME

#     def __init__(self,mailTo,mailFrom,mailSubject,mailContent):
#         self.hostname = MAIL_HOSTNAME      
#         self.mailTo = mailTo
#         self.mailFrom = mailFrom
#         self.mailSubject = mailSubject
#         self.mailContent = mailContent
        
#     def sendmail(self):
#         return self.hostname,self.mailTo,self.mailFrom,self.mailSubject,self.mailContent

#========================================================================================================================== end  CLASS __SENDMAIL__

