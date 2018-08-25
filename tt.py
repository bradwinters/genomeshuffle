import sys 
import random
import re

#################################################
####   Core SubRoutines                ##########
#################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def GraphToGenome(pGeneGraph):
    print("Start")
    print("1:",pGeneGraph)
    outP=[]
    aNode=[]

    ##  put bracked pairs into a list
    ##
    nodez=pGeneGraph.split(")")
    for e in nodez:
       matches=re.findall("\d+",e)
       if len(matches) > 0:
           matches[0]=int(matches[0])
           matches[1]=int(matches[1])
           aNode.append(matches)
    print("Only lists of pairs, all in one list")
    print("2:",aNode)

    # make the rings 
    print("Loop ",len(aNode)," times.")
    print("As long consecutive pairs connect, add them to ring")
    print("When pairs don't connect, complete the ring and start another")
    Ring=[]
    Ring.append(aNode[0])
    RingCnt=1
    for j in range(len(aNode)-1):
       if aNode[j][1]- aNode[j+1][0] == 1 or  aNode[j][1]- aNode[j+1][0] == -1:
          #print(aNode[j][1], " and ",aNode[j+1][0]," connect, same cycle")
          Ring.append(aNode[j+1])
       else:
          #print(aNode[j][1], " and ",aNode[j+1][0]," dont connect")
          print("Put current ring in final Output list by itself")
          outP.append(Ring)
          print("Start a new Ring")
          Ring=[]
          Ring.append(aNode[j+1])
          RingCnt+=1

    outP.append(Ring)
    print(RingCnt," Rings Counted, ",len(outP)," rows to process.")

    P=[]
    for e in range(len(outP)):
       GenomeGraph=outP[e]
       fGenomeG=[]
       for x in range(len(GenomeGraph)):
           print(GenomeGraph[x][0],GenomeGraph[x][1])
           fGenomeG.append(GenomeGraph[x][0])
           fGenomeG.append(GenomeGraph[x][1])
       #print(fGenomeG) 
       Chromos=CycleToChromosome(fGenomeG)
       print(Chromos) 
       P.append(Chromos)


    return P 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ColoredEdges(pP):
    CEdges=[]
    print("inside ColoredEdges")

    for element in pP:
       Chromo=ChromoToList(element)
       Nodes=ChromosomeToCycle(Chromo)
       Nodes.append(Nodes[0])
       Nodes.insert(0,0)
       print("Nodes: ",Nodes)
       for j in range(1,len(Chromo)):
           ndx1=2*j
           ndx2=ndx1+1
           CEdges.append((Nodes[ndx1],Nodes[ndx2]))

    return CEdges




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ChromosomeToCycle(pChromo):
    '''
    Creates graph where odd numbers are the head, even the tail.  
    Direction is preserved by the pairs being in order or not
    So 3,4 is clockwise, in order while 4,3 is reversed
    '''
    # convert a single chromosome into a cycle 
    # represented as a sequence of integers in Nodes
    Nodes=[]
    for j in range(1,len(pChromo)):
       i=pChromo[j]
       if i > 0:
           ndx1=2*j-1
           ndx2=2*j
           Nodes.insert(ndx1,2*i-1)
           Nodes.insert(ndx2,2*i)
       else:
           ndx1=2*j-1
           ndx2=2*j
           Nodes.insert(ndx1,-2*i)
           Nodes.insert(ndx2,-2*i-1)

    return Nodes

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def CycleToChromosome(Nodes):
    #Nodes=ChromoToList(pString)
    #Nodes=Nodes[1:]
    print("In cycle2chromo")
    print(Nodes)
    print("Size of nodes ",len(Nodes))
    #zSize=int(len(Nodes)/2)+1
    zSize=int(len(Nodes)/2)
    print("zSize of nodes ",zSize)
    Chromosome=[]
    for j in range(zSize):
        print(j)
        ndx1=2*j-1
        ndx2=2*j
        if Nodes[ndx1] < (Nodes[ndx2]):
           Chromosome.insert(j,Nodes[ndx2]/2)
        else:
           Chromosome.insert(j,-Nodes[ndx1]/2)


    C=NiceList2(Chromosome)
    
    return C





#################################################
####   Utilities                       ##########
#################################################

#  ( 1 2 4 3 6 5...) to a list of just numbers.
def ChromoToList(aString):
    # Syntany blocks is a string in parens converted to a list of signed integers
    newList=[0]
    aString=aString.strip('(')
    aString=aString.strip(')')
    tList=aString.split()
    for x in range(len(tList)):
       newList.append(int(tList[x]))
       
    return newList

def NiceList2(pList):

    OutString="("
    for e in range(len(pList)):
        if pList[e] > 0:
            OutString+="+"+str(int(pList[e]))+" " 
        else:
            OutString+=str(int(pList[e]))+" " 

    #preO=OutString[:len(OutString)-1]    
    preO=OutString[:-1]    
    preO+=")"
    return preO

def NiceList(pList):

    OutString="("
    for e in range(len(pList)):
            OutString+=str(pList[e])+" " 

    #preO=OutString[:len(OutString)-1]    
    preO=OutString[:-1]    
    preO+=")"
    return preO



def readData():
    lines = sys.stdin.read().splitlines() 
    Allines=[] 
    Cnt=0
    for i in range(len(lines)):
       Cnt+=1
       startList=[]
       endList=[]
       aline=lines[i]
       for q in range(len(aline)):
           if aline[q]=='(':
              startList.append(q) 
           elif aline[q]==')':
              endList.append(q) 

       for x in range(len(startList)): 
           Joe=aline[startList[x]:endList[x]+1]
           #print(Joe)
           Allines.append((Cnt,Joe))
       #print(Allines)
       print("-----------------------------")


    return(Allines)

def CreateChrome(tupList,C):
    Chromo=[]
    for x in range(len(tupList)): 
        if tupList[x][0]==C:
            Chromo.append(tupList[x][1])
    return Chromo

#################################################
####   Main                            ##########
#################################################
intList=readData()
P=[]
Q=[]
P=CreateChrome(intList,1)
Q=CreateChrome(intList,2)
print("**  part I **")
#print("P is ",P)
print("Q is ",Q)

print("**  Create Colored Edges from P  **")
Edges=ColoredEdges(P)

aString=""
for e in Edges:
   aString+=str(e)+", "
geneGraph=aString[:-2]
print("Here we go: ",geneGraph)
geneGraph="(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)"
#fish
geneGraph="(2, 3), (4, 6), (5, 8), (7, 9), (10, 12), (11, 13), (14, 15), (16, 17), (18, 20), (19, 22), (21, 23), (24, 26), (25, 28), (27, 30), (29, 32), (31, 34), (33, 35), (36, 37), (38, 39), (40, 41), (42, 44), (43, 1), (46, 47), (48, 50), (49, 52), (51, 53), (54, 56), (55, 58), (57, 59), (60, 62), (61, 64), (63, 66), (65, 67), (68, 70), (69, 71), (72, 74), (73, 75), (76, 78), (77, 79), (80, 82), (81, 84), (83, 85), (86, 87), (88, 89), (90, 92), (91, 45), (93, 95), (96, 98), (97, 99), (100, 102), (101, 104), (103, 105), (106, 108), (107, 110), (109, 111), (112, 113), (114, 115), (116, 118), (117, 120), (119, 122), (121, 123), (124, 125), (126, 127), (128, 129), (130, 131), (132, 133), (134, 136), (135, 137), (138, 139), (140, 141), (142, 143), (144, 146), (145, 147), (148, 94), (149, 152), (151, 154), (153, 156), (155, 158), (157, 160), (159, 161), (162, 164), (163, 166), (165, 168), (167, 169), (170, 172), (171, 174), (173, 175), (176, 178), (177, 180), (179, 182), (181, 184), (183, 186), (185, 188), (187, 190), (189, 192), (191, 194), (193, 196), (195, 198), (197, 199), (200, 202), (201, 150), (203, 206), (205, 207), (208, 209), (210, 211), (212, 214), (213, 216), (215, 218), (217, 220), (219, 221), (222, 223), (224, 225), (226, 228), (227, 229), (230, 232), (231, 234), (233, 235), (236, 238), (237, 240), (239, 241), (242, 244), (243, 245), (246, 247), (248, 204), (250, 251), (252, 254), (253, 256), (255, 258), (257, 259), (260, 262), (261, 264), (263, 266), (265, 268), (267, 269), (270, 271), (272, 274), (273, 276), (275, 277), (278, 280), (279, 282), (281, 283), (284, 286), (285, 288), (287, 289), (290, 292), (291, 293), (294, 295), (296, 297), (298, 300), (299, 301), (302, 303), (304, 249), (305, 308), (307, 310), (309, 312), (311, 313), (314, 315), (316, 317), (318, 320), (319, 322), (321, 323), (324, 325), (326, 327), (328, 330), (329, 332), (331, 334), (333, 335), (336, 338), (337, 339), (340, 342), (341, 343), (344, 345), (346, 347), (348, 350), (349, 352), (351, 354), (353, 356), (355, 357), (358, 360), (359, 306)"
print("**  part III Graph back to Genome**")
genome=GraphToGenome(geneGraph)
print("Final Answer")
ChrmoZome=""
for Chrmo in genome:    
    ChrmoZome+=Chrmo
print(ChrmoZome)

exit()
Edges=ColoredEdges(Q)

aString=""
for e in Edges:
   aString+=str(e)+", "
geneGraph=aString[:-2]
print("Here we go: ",geneGraph)
geneGraph="(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)"
print("** Separate  part III Graph back to Genome**")
genome=GraphToGenome(geneGraph)
print("Finally: ",genome)
