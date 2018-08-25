import sys 
import random
import re

def GraphToGenome(pGeneGraph):
    print("Start")
    print(pGeneGraph)

    aNode=[]
    nodez=pGeneGraph.split(")")
    for e in nodez:
       matches=re.findall("\d+",e)
       if len(matches) > 0:
           matches[0]=int(matches[0])
           matches[1]=int(matches[1])
           aNode.append(matches)

    print(aNode)
    i=random.randint(0, len(aNode)-1)
    print("i is ",i)
    print("Pick ",aNode[i])
 
    BreakList=[]
    print("Loop ",len(aNode)," times.")
    for j in range(len(aNode)-1):
       if aNode[j][1]- aNode[j+1][0] == 1 or  aNode[j][1]- aNode[j+1][0] == -1:
          #print(aNode[j][1], " and ",aNode[j+1][0]," are in the same cycle")
          continue
       else:
          print("Break at: ",j," between ",aNode[j][1]," and ",aNode[j+1][0])
          BreakList.append(j)

    print("Breaks at ",BreakList)

    P=["hi"]

    return P 

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




def ChromoToList(aString):
    # Syntany blocks is a string in parens converted to a list of signed integers
    newList=[0]
    aString=aString.strip('(')
    aString=aString.strip(')')
    tList=aString.split()
    
    for x in range(len(tList)):
       newList.append(int(tList[x]))
       
    return newList

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

def CycleToChromosome(pString):

    Nodes=ChromoToList(pString)
    #Nodes=Nodes[1:]

    zSize=int(len(Nodes)/2)+1
    Chromosome=[]
    for j in range(1,zSize):
        ndx1=2*j-1
        ndx2=2*j
        if Nodes[ndx1] < (Nodes[ndx2]):
           Chromosome.insert(j,Nodes[ndx2]/2)
        else:
           Chromosome.insert(j,-Nodes[ndx1]/2)

    return Chromosome


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

intList=readData()
P=[]
Q=[]
P=CreateChrome(intList,1)
Q=CreateChrome(intList,2)
print("**  part I **")
#print("P is ",P)
print("Q is ",Q)

print("ChromosomeToCycle ",intList)

print("**  part II Create Graph**")
Edges=ColoredEdges(P)

aString=""
for e in Edges:
   aString+=str(e)+", "
geneGraph=aString[:-2]
print("Here we go: ",geneGraph)
#geneGraph="(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)"
print("**  part III Graph back to Genome**")
genome=GraphToGenome(geneGraph)
print("Genome 1",genome)


Edges=ColoredEdges(Q)

aString=""
for e in Edges:
   aString+=str(e)+", "
geneGraph=aString[:-2]
print("Here we go: ",geneGraph)
#geneGraph="(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)"
print("**  part III Graph back to Genome**")
genome=GraphToGenome(geneGraph)
print("Genome 2",genome)
