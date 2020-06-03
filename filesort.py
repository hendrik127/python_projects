import shutil
import os
import collections
from datetime import datetime
import tzlocal
#from pathlib import Path
#from datetime import date

allakaust = os.path.join("C:","\\","Users","Hendrik","Downloads")

väljakaust = os.path.join("C:","\\","Users","Hendrik","Desktop","sorted")

#täna = str(date.today())
sõnastik = collections.defaultdict(list)

ajatsoon = tzlocal.get_localzone()



#failisisu = fail.read()



failid= os.listdir(allakaust)

for fail in failid:
    ogpath = os.path.join(allakaust,fail)
    täna = str(datetime.fromtimestamp(os.path.getctime(ogpath),ajatsoon).strftime('%Y-%m-%d'))
    tänaneväljakaust = os.path.join(väljakaust,täna)
    if os.path.isdir(tänaneväljakaust):
        sõnastik[täna].append(fail)
        pathin = os.path.join(allakaust,fail)
        pathout = os.path.join(tänaneväljakaust,fail)
        shutil.move(pathin,pathout)
    else:
        os.makedirs(tänaneväljakaust)
        sõnastik[täna].append(fail)
        pathin = os.path.join(allakaust,fail)
        pathout = os.path.join(tänaneväljakaust,fail)
        shutil.move(pathin,pathout)
        
#print(sõnastik)


fail = open("auto.txt","a")
for võti in sõnastik:
    failid = ""
    for failinimi in sõnastik[võti]:
        failid+=failinimi+" "
        
    fail.write(võti+":"+failid+"\n")
fail.close()


fail = open("auto.txt","r")
sisu = fail.read()
sisu2 = sisu.split("\n")
sõnastik = collections.defaultdict(list)
for i in range(len(sisu2)-1):
    võtiväärtus =sisu2[i].split(":")
    väärtused = võtiväärtus[1].split(" ")
    sõnastik[võtiväärtus[0]]=sõnastik[võtiväärtus[0]]+väärtused
fail.close()   
print(sõnastik)

while True:
    sisend = input("Kas tahad leida kausta, milles fail on (vajuta ""K"") või sisesta kaust, mille sisu tahad kuvada(""S""):")
    
    if sisend == "K":
        failinimi = input("Sisesta fail, mille kausta tahad leida: ")
        if failinimi == "":
            break

        for võti in sõnastik:
            if failinimi in sõnastik[võti]:
                print("Fail asub kaustas: "+võti)
            else:
                print("Faili ei leitud!")
            
    elif sisend == "S":
        kaustanimi = input("Sisesta kaust, mille sisu tahad kuvada: ")
        print("Kausta sisu:")
        for fail in sõnastik[kaustanimi]:
            if fail == "":
                continue
            print("\t"+fail)
            
    else:
        print("Vigane sisend!")
    
    