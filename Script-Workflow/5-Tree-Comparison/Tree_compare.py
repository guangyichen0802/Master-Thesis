from ete3 import Tree

t1 = Tree('(GCF_007989405.1,((GCF_900101905.1,(GCF_013116865.1,((((GCF_013372585.1,GCF_013372605.1),(GCF_010894475.1,GCF_013372615.1)),((GCA_000219105.1,GCF_002305895.1),(GCF_000280925.3,(((GCF_010894405.1,GCF_010894435.1),(GCF_012933655.1,GCF_013155555.1)),(GCF_000331735.1,(((GCF_010894455.1,GCF_013372595.1),(GCF_006636215.1,(GCF_013336625.1,(GCF_013336645.1,(GCF_013336715.1,(GCF_013336705.1,GCF_013336725.1)))))),(GCA_000988565.1,(GCF_006518215.1,(GCF_007991095.1,GCF_900111765.1))))))))),(GCF_006400955.1,(GCF_006401215.1,(GCF_006402015.1,GCF_006402735.1)))))),(GCF_006547355.1,GCF_006547365.1)),(GCF_000278585.1,(GCF_006401635.1,(GCF_006518195.1,(GCF_000012685.1,(GCF_013116825.1,(GCF_010998655.1,(GCF_006547325.1,(GCF_010998615.1,(GCF_900106535.1,(GCF_013116835.1,(GCF_006547345.1,(GCF_006518205.1,(GCF_013116805.1,(GCF_000340515.1,(GCF_006402415.1,GCF_010279825.1))))))))))))))));')

t2 = Tree('(GCF_000340515.1,GCF_006400955.1,GCF_006402415.1,GCF_006518195.1,GCF_006518205.1,GCF_006547325.1,GCF_006547345.1,GCF_007989405.1,GCF_010279825.1,GCF_010894475.1,GCF_010998655.1,GCF_013116805.1,GCF_013116825.1,GCF_013116835.1,GCF_013116865.1,GCF_013372605.1,GCF_900106535.1,(GCA_000219105.1,GCF_002305895.1),(GCF_012933655.1,GCF_013155555.1),(GCF_000280925.3,GCF_013372585.1),(GCF_010894405.1,GCF_010894435.1),(GCF_013336625.1,(GCF_013336645.1,GCF_013336705.1,GCF_013336715.1)),(GCF_013372615.1,(GCF_006401215.1,GCF_006547365.1,GCF_900101905.1)),(GCF_006402015.1,GCF_006402735.1),(GCF_006547355.1,(GCF_007991095.1,(GCA_000988565.1,(GCF_006518215.1,GCF_900111765.1)))),(GCF_000331735.1,(GCF_010894455.1,GCF_013372595.1)),(GCF_000012685.1,GCF_000278585.1,GCF_006401635.1,GCF_010998615.1),(GCF_006636215.1,GCF_013336725.1));')

af_ref = Tree('((((D1Sd197,(CB9615,(Sakai,EDL933))),(((((SSSs046,(B18BS512,B4Sb227)),(E24377A,(IAI1,SE11)))),(F5b8401,(F2a2457T,F2a301))),((ATCC8739,HS),((BW2952,DH10B),(MG1655,W3110))))),UMN026),((IAI39,SMS35),(E234869,(536,((S88,(APEC01,UTI89)),(ED1a,CFT073))))));') 

protspam_af = Tree('(((UMN026:0.0086,(E234869:0.0064,(ED1a:0.0062,(536:0.0042,(CFT073:0.0035,(UTI89:0.0010,(APEC01:0.0008,S88:0.0005):0.0007):0.0033):0.0002):0.0006):0.0022):0.0021):0.0003,(IAI39:0.0060,SMS35:0.0058):0.0029):0.0020,(D1Sd197:0.0076,(CB9615:0.0020,(EDL933:0.0008,Sakai:0.0001):0.0020):0.0064):0.0009,(((E24377A:0.0035,(IAI1:0.0025,SE11:0.0031):0.0003):0.0022,(SSSs046:0.0052,((B18BS512:0.0026,B4Sb227:0.0021):0.0037,(F5b8401:0.0012,(F2a2457T:0.0001,F2a301:0.0003):0.0012):0.0061):0.0003):0.0004):0.0004,((ATCC8739:0.0033,HS:0.0029):0.0007,((DH10B:0.0003,MG1655:0.0001):0.0001,(BW2952:0.0002,W3110:0.0000):0.0000):0.0034):0.0014):0.0014);') 

sans_af = Tree('((F5b8401:29180.614798,(F2a2457T:4430.593414,F2a301:6888.624826):24092.521516):100966.471955,((D1Sd197:200611.403457,(CB9615:24882.538576,(EDL933:9907.551463,Sakai:3335.287694):34894.282970):116847.957209):42041.657865,(UMN026:191498.590277,((E234869:125278.224365,(ED1a:87122.036277,((UTI89:8900.999775,(APEC01:10718.413502,S88:7168.123185):2952.426121):43432.612493,(536:66645.167567,CFT073:57792.759668):13511.839364):11340.971916):37885.382141):113371.559873,(IAI39:122388.605581,SMS35:121640.268069):67917.529335):41485.441687):41285.097057):17542.080977,((SSSs046:82180.000487,(B18BS512:59672.331981,B4Sb227:45185.587935):55275.209887):11552.905695,(((BW2952:4172.059324,(DH10B:10807.981726,(MG1655:85.463442,W3110:218.382692):1303.944784):845.126026):44308.542201,(ATCC8739:36570.825996,HS:37655.260668):15335.152885):20654.819583,(IAI1:29375.279403,(E24377A:48206.963190,SE11:37468.888748):11880.756794):10463.463098):5669.824071):6854.975565):0.000000;') 

#print(t1)
#print(t2)

print(sans_af.robinson_foulds(protspam_af, unrooted_trees = True))

#print(t1.robinson_foulds(t2, unrooted_trees = True))

#print(t1.compare(t2, unrooted_trees = True))

#rf, max_rf, common_leaves, parts_t1, parts_t2 = t1.robinson_foulds(t2, unrooted_tree = True)

#print(rf)
#print(max_rf)

#print "RF distance is: "+ %(rf, max_rf)
#print "Partitions in tree2 that were not found in tree1:", parts_t1 - parts_t2
#print "Partitions in tree1 that were not found in tree2:", parts_t2 - parts_t1