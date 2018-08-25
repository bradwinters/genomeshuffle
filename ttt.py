import sys 
import random
import re

#################################################
####   Core SubRoutines                ##########
#################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def equalTups(tup1,tup2):

    #print("Comparing ",tup1," to ",tup2)
    if tup1==tup2:
       return True

    #print("Comparing ",tup1[0]," to ",tup2[1]," and ",tup1[1]," to ",tup2[0])
    if tup1[0]==tup2[1] and tup1[1]==tup2[0]:
       return True
    return False

def TBreakonGenomeGraph(pGeneGraph,a,b,c,d):
    print(pGeneGraph)
    aNode=[]

    bp=[]    
    bp.append((a,b))
    bp.append((c,d))

    newBp=[]
    newBp.append((a,c))
    newBp.append((b,d))


    print(bp)
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
    tupZ=[]
    for i in range(len(aNode)):
        tupZ.append((aNode[i][0],aNode[i][1])) 

    print(tupZ)
    for x in range(len(tupZ)):
       if equalTups(bp[0],tupZ[x]):
          BreakPt1=x
    for x in range(len(tupZ)):
       if equalTups(bp[1],tupZ[x]):
          BreakPt2=x


    print("output ",tupZ)
    print("Change ",tupZ[BreakPt1]," and ",tupZ[BreakPt2]," to ",newBp[0]," and ",newBp[1])

    return "Done"


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
geneGraph="(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)"
#fish
geneGraph="(2, 4), (3, 8), (7, 5), (6, 1)"
print("Here we go: ",geneGraph)
bp="1, 6, 3, 8"
pts=bp.split(',')
print(pts)
a=int(pts[0])
b=int(pts[1])   
c=int(pts[2])   
d=int(pts[3])   
ans=TBreakonGenomeGraph(geneGraph,a,b,c,d)
print(ans)
exit()
print("**  part III Graph back to Genome**")
genome=GraphToGenome(geneGraph)
print("Final Answer")
ChrmoZome=""
for Chrmo in genome:    
    ChrmoZome+=Chrmo
print(ChrmoZome)

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
