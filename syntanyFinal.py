def RevComp(inString):
    newS=""
    fred=inString[::-1]
    for l in fred:
      newS+=Comp(l)
    return newS, fred

def Comp(NA):
    if NA=='C':
      return 'G'
    if NA=='G':
      return 'C'
    if NA=='A':
      return 'T'
    if NA=='T':
      return 'A'

myfile = open("test.dat")
#myfile = open("sy.dat")
#myfile = open("syextra.dat")
#myfile = open("q4.dat")
rowcnt=0
fcnt=0
for line in myfile:
    row=line.strip()
    if rowcnt==0:
       kMer=int(row)
    elif rowcnt==1:
       source=row
    elif rowcnt==2:
       target=row
    rowcnt+=1
print("KMer:",kMer)    
print("Source:",source)
print("Target:",target)
RevC, Rev =RevComp(target)
print("Reversed     ",Rev)
print("Reversed Comp",RevC)
print("Size of Source: ",len(source))
print("Size of Target: ",len(target))
print("Size of Revers: ",len(Rev))
print("Size of RCompl: ",len(RevC))
Rsize=len(target)
EndS=kMer-1 


###############################################################################
###  Create a dict of the source strings of the kmers
###  In case of collidions, store positions of kmers as int lists
###  First, unload old list, del old hash, add new addr and redo hash
###    with the new add on to the list.  Undo this at lookup time.
###############################################################################
FBlock={}
address=0
for i in range(len(source)-EndS):
   kkey=source[i:i+kMer]
   if kkey in FBlock.keys():
       #print("Loop ",i," ",kkey,"is already here:",FBlock[kkey])
       tList=FBlock[kkey]
       tList.append(address)
       del FBlock[kkey]
       FBlock[kkey]=tList 
       #print("Redflag ",FBlock[kkey])
   else:
       tList=[]
       tList.append(address)
       FBlock[kkey]=tList
   address+=1

#print(FBlock)
###  Hash cnd overflow created


#print("Start the loop")
for j in range(len(target)-EndS):
    Tkey=target[j:j+kMer]
    mAtch=FBlock.get(Tkey)
    if mAtch !=None:
        for jj in range(len(mAtch)):
            fcnt+=1
            Ostring="("+str(mAtch[jj])+", "+str(j)+")"
            print(Ostring)

    Rkey=RevC[j:j+kMer]
    mAtch=FBlock.get(Rkey)
    if mAtch !=None:
        for jj in range(len(mAtch)):
            fcnt+=1
            Ostring="("+str(mAtch[jj])+", "+str(Rsize-j-kMer)+")"
            print(Ostring)

myfile.close()
