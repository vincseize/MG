
def AK00_FOR_OCC_VON_KROUMCH(save_after='False'): 
    '''
  
    Creer la branche de rendu Occ2 pour l oeil droit.
  
    Selectionner l'a7 Occ_2_Render.

    '''
    

    def save_graph(protoGraphResult,myfilm,myseq,myshot):
        '''   '''

        assetList = []

        graphPath='/u/'+projectLower+'/Users/COM/Presets/Graphs/OCC/USECASE/'+myfilm+'/'+myfilm+'_'+myseq+'_'+myshot+'.inkGraph'
        graphPathLocal='/u/'+projectLower+'/Users/'+USER+'/Presets/Graphs/occ2_'+myfilm+'_'+myseq+'_'+myshot+'.inkGraph'
        # print graphPath, graphPathLocal
        # retrieving the added Occ2 .a7
        protoGraphResult.SelectAll()
        selection = protoGraphResult.GetSelection()
        for pa in selection:
            a_name = pa.GetNomen()
            if '-L-Occ_2_Render' not in str(a_name): # to do better with filter
                assetList.append(pa)

        # retrieving the originals .a7
        grL = ink.proto.Graph( graphPath, load=True, private=False )
        grL.SelectAll()
        selection = grL.GetSelection()
        for pa in selection:
            assetList.append(pa)

        graphPath = graphPathLocal # for debug
        protoGraphS  = ink.proto.Graph.FromQuery('foo', assetList) 
        l = protoGraphS.GetLayout()                           
        l.LoadGraphPos(assetList) 

        if save_after=='False' and 'None' not in str(graphPath):
            print graphPath , 'is ready to be saved !!!'

        if save_after=='True' and 'None' not in str(graphPath):                         
            protoGraphS.Write(str(graphPath), private=False)
            if os.path.isfile(graphPath):                
                print graphPath , 'Have been saved !!!'
                pass
            else :
                print graphPath + '\n\nSaving FAILED !!!'

        if 'None' in str(graphPath): 
          print graphPath + '\n\nSaving FAILED !!!'
          print '\n\n BAD PATH !!!'


    ##---------------------------------------------------------------------------------------------------------------- end defs



    protoGraphToMaj     = ink.proto.Graph('protoGraphToMaj')
    protoGraphToConnect = ink.proto.Graph('Clean')                    
    selection           = protoGraphToMaj.GetSelection( nomen.Filter().SetTypes(['Occ', '2', 'Render']).SetEye('L'))
    layout              = protoGraphToMaj.GetLayout()



    if not selection:
        raise Exception("Please Selectionner l'a7 Occ_2_Render Left  !")

    for proto in selection:
        nmShot      = proto.GetNomen()
        myfilm      = nmShot.GetFilm()
        myseq       = nmShot.GetSeq()
        myshot      = nmShot.GetShot()

    ##----------------------get ref a7 position, and movie downstream position
        layout.LoadGraphPos([proto])
        selPos = layout.GetPoint([proto], direction='M')
        Xref = selPos[0]
        Yref = selPos[1]
        niFilters = nomen.Nomen.Empty().SetTypes(['Occ', 'Movie']).SetEye('L').SetVar('V2')
        StreamProtoList = protoGraphToConnect.GetDownstreams(proto, niFilter=niFilters)
        for ds in StreamProtoList:
            layout.LoadGraphPos([ds])
            selPos = layout.GetPoint([ds], direction='M')
            Xmovie = selPos[0]
            Ymovie = selPos[1]

    ##----------------------LIBREF/Seq/Shot/Occ/LIBREF_Seq_Shot-R-Occ_2_Render.a7----------------------
        Occ2Render       = nomen.Nomen.NewFilm( film='LIBREF', seq='Seq', shot='Shot', var='', types=['Occ','2', 'Render'], stage='',eye ='R' )
        Occ2RenderProto  = protoGraphToMaj.Add(Occ2Render)
      
      
    ##----------------------Occ2Movie----------------------
        Occ2RMovie       = nomen.Nomen.NewFilm( film='LIBREF', seq='Seq', shot='Shot', var='V2', types=['Occ','Movie'], stage='',eye ='R' )
        Occ2RMovieProto  = protoGraphToMaj.Add(Occ2RMovie)

    ##----------------------Clone----------------------
        protoGraphResult = ink.proto.Graph('result')

        mycloneparam = nomen.Filter()
        mycloneparam.SetFilm(myfilm)
        mycloneparam.SetSeq(myseq)
        mycloneparam.SetShot(myshot)

        protoGraphResult.Clone(protoGraphToMaj, mycloneparam, substInFile=True, forceCopy=True, copyUBLinks=False)
    
        result = protoGraphResult.Apply()

    #======================================================================
    #========= Branchements
    #======================================================================
  
        OccRenderR       = nmShot.SetTypes(['Occ', '2', 'Render']).SetEye('R')
        OccRenderRProto  = protoGraphToConnect.Add(OccRenderR)
    
        ExptLighting = nmShot.SetTypes(['Export', 'Lighting']).SetEye('')
        ExptLightingProto  = protoGraphToConnect.Add(ExptLighting)    
        
        OccRender = nmShot.SetTypes(['Occ', 'Render']).SetEye('L')
        OccRenderProto  = protoGraphToConnect.Add(OccRender)      
    
        OccRenderL       = nmShot.SetTypes(['Occ', 'Render']).SetEye('L')
        OccRenderLProto  = protoGraphToConnect.Add(OccRenderL)    
    

        protoGraphToConnect.AddLink(ExptLightingProto, OccRenderRProto, ink.proto.LINK_REF)
        protoGraphToConnect.AddLink(OccRenderProto, OccRenderRProto, ink.proto.LINK_REF)  
        protoGraphToConnect.AddLink( OccRenderLProto, OccRenderRProto, ink.proto.LINK_DEP, )    

        addLinks = protoGraphToConnect.Apply()

    #======================================================================
    #========= positionnement
    #======================================================================
        offset_Y = 1.5
        layout = protoGraphToConnect.GetLayout()
        layout.SetPos(OccRenderRProto, (Xref, Yref-offset_Y) ) # XXX-R-Occ_2_Render.a7
        niFilters = nomen.Nomen.Empty().SetTypes(['Occ', 'Movie']).SetEye('R').SetVar('V2')
        StreamProtoList = protoGraphToConnect.GetDownstreams( OccRenderRProto, niFilter=niFilters)
        for ds in StreamProtoList:
            layout.SetPos(ds, (Xmovie, Ymovie-offset_Y) ) # XXX-V2-R-Occ_Movie.a7
        protoGraphToConnect.Show()

    #======================================================================
    #========= save graph
    #======================================================================   
        save_graph(protoGraphResult,myfilm,myseq,myshot)


#=========================== UI

AK00_FOR_OCC_VON_KROUMCH.__category__          = 'A - PIPE-IN TOOLZ'
AK00_FOR_OCC_VON_KROUMCH.__author__            = 'cpottier'
AK00_FOR_OCC_VON_KROUMCH.__textColor__         = '#6699ff'
AK00_FOR_OCC_VON_KROUMCH.__paramsType__        = {
'save_after'            :  ( 'bool', 'False' , ['True', 'False']  )    

}




