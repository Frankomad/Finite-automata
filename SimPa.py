import sys

linije = []
for line in sys.stdin:
    line = line.rstrip()
    linije.append(line)
linije[0] = linije[0].split("|")
for i in range(1,7):
    linije[i] = linije[i].split(",")
##linije[0] su ulazni nizovi +KORISTIM
##linije[1] su stanja automata -
##linije[2] su simboli ulaznih nizova -
##linije[3] su simboli stoga -
##linije[4] su prihvatljiva stanja +KORISTIM
##linije[5] je pocetno stanje +KORISTIM
##linije[6] je dno stoga +KORISTIM

kljucevi = []
vrijednosti = []
for i in range(7,len(linije)):
    prijelaz = linije[i].rstrip().split("->")
    kljucevi.append(prijelaz[0])
    vrijednosti.append(prijelaz[1])

for i in range(len(linije[0])): #linije[0] su ulazni nizovi
    niz = linije[0][i].split(",")
    stanje = linije[5][0]
    stog = []
    stog.append(linije[6][0])
    ispis = stanje +"#"+stog[0]
    prihvatljivost = "0"
    van = 0
    for k in range(0,len(niz)):
        if(van !=0 or len(stog)==0):
            break
        key = stanje+","+niz[k]+","+stog[0]
        if(kljucevi.count(key) == 0):
            provjereni = []
            pom = 0
            for x in range(100):
                if(pom !=0):
                    break
                key = stanje+",$,"+stog[0]
                if(kljucevi.count(key) == 0):
                    ispis+="|fail"
                    van = 1
                    break
                else:
                    value = vrijednosti[kljucevi.index(key)].split(",")
                    stanje = value[0]
                    if(len(value[1]) >0 and value[1].count("$") == 0):
                        ispis+= "|"+value[0]+"#"
                        if(len(value[1])>1):
                           xd = ""
                           for rev in value[1]:
                                xd = rev + xd
                           if(value[1][len(value[1])-1] == stog[0]):
                               value[1] = value[1][::-1]
                               stog.reverse()
                               for simbol in range(1,len(xd)):
                                   stog.append(xd[simbol])
                               stog.reverse()
                           else:
                               stog.reverse()
                               stog.pop()
                               stog.reverse()
                               stog.reverse()
                               for simbol in range(0,len(xd)):
                                   stog.append(xd[simbol])
                               stog.reverse()
                        else:
                            ispis+=""
                        for simbol in stog:
                           ispis+= simbol
                    elif(len(value[1]) >0 and value[1].count("$") != 0):
                        if(len(stog)!=0):
                            stog.reverse()
                            stog.pop()
                            stog.reverse()
                        if(len(stog)>0):
                                ispis+="|"+stanje+"#"
                                for simbol in stog:
                                   ispis+= simbol
                        else:
                            for simbol in stog:
                                   ispis+= simbol
                            ispis += "|"+stanje+"#$|fail"
                            x = 101
                            k = len(niz)+1
                            break
                    else:
                        print("lapsus!")
                        break
                    ###iz epsilon prijelaza provjeravamo je li iduce ok
                    key = stanje+","+niz[k]+","+stog[0]
                    if(kljucevi.count(key)!=0):
                        value = vrijednosti[kljucevi.index(key)].split(",")
                        stanje=value[0]
                        if(len(value[1]) >0 and value[1].count("$") == 0):
                            ispis+= "|"+value[0]+"#"
                            xd = ""
                            for rev in value[1]:
                                xd = rev + xd
                            if(len(value[1])>1):
                               if(value[1][len(value[1])-1] == stog[0]):
                                   stog.reverse()
                                   for simbol in range(1,len(xd)):
                                       stog.append(xd[simbol])
                                   stog.reverse()
                               else:
                                   stog.reverse()
                                   stog.pop()
                                   stog.reverse()
                                   stog.reverse()
                                   for simbol in range(0,len(xd)):
                                       stog.append(xd[simbol])
                                   stog.reverse()
                            else:
                                ispis +=""
                            for simbol in stog:
                               ispis+= simbol
                        elif(len(value[1]) >0 and value[1].count("$") != 0):
                            if(len(stog)!=0):
                                stog.reverse()
                                stog.pop()
                                stog.reverse()
                            if(len(stog)>0):
                                    ispis+="|"+stanje+"#"
                                    for simbol in stog:
                                       ispis+= simbol
                            else:
                                for simbol in stog:
                                       ispis+= simbol
                                ispis += "|"+stanje+"#$|fail"
                                x = 101
                                k = len(niz)+1
                                break
                        pom = 1        
                        break
                            
                                
        else:
                    value = vrijednosti[kljucevi.index(key)].split(",")
                    stanje=value[0]
                    if(len(value[1]) >0 and value[1].count("$") == 0):
                        ispis+= "|"+value[0]+"#"
                        if(len(value[1])>1):
                           xd = ""
                           for rev in value[1]:
                               xd = rev + xd
                           if(value[1][len(value[1])-1] == stog[0]):
                               stog.reverse()
                               for simbol in range(1,len(xd)):
                                   stog.append(xd[simbol])
                               stog.reverse()
                           else:
                               stog.reverse()
                               stog.pop()
                               stog.reverse()
                               value[1] = value[1][::-1]
                               stog.reverse()
                               for simbol in range(0,len(xd)):
                                   stog.append(xd[simbol])
                               stog.reverse()
                        else:
                            ispis+=""
                        for simbol in stog:
                           ispis+= simbol
                    elif(len(value[1]) >0 and value[1].count("$") != 0):
                        if(len(stog)!=0):
                            stog.reverse()
                            stog.pop()
                            stog.reverse()
                            if(len(stog)>0):
                                ispis+="|"+stanje+"#"
                                for simbol in stog:
                                   ispis+= simbol
                        else:
                            for simbol in stog:
                                   ispis+= simbol
                            ispis += "|"+stanje+"#$|fail"
                            k = len(niz)+1
                            break
    if(stanje not in linije[4] and len(stog)>0):
        if("fail" not in ispis):
            provjereno = []
            for u in range(20):
                if(len(stog)!=0):
                    key = stanje +",$,"+stog[0]
                    provjereno.append(key)
                    if (kljucevi.count(key)!=0):
                            value = vrijednosti[kljucevi.index(key)].split(",")
                            stanje = value[0]
                            if(len(value[1]) >0 and value[1].count("$") == 0):
                                ispis+= "|"+value[0]+"#"
                                if(len(value[1])>1):
                                   xd = ""
                                   for rev in value[1]:
                                        xd = rev +xd
                                   if(value[1][len(value[1])-1] == stog[0]):
                                       stog.reverse()
                                       for simbol in range(1,len(xd)):
                                           stog.append(xd[simbol])
                                       stog.reverse()
                                   else:
                                       stog.reverse()
                                       stog.pop()
                                       stog.reverse()
                                       stog.reverse()
                                       for simbol in range(1,len(xd)):
                                           stog.append(xd[simbol])
                                       stog.reverse()
                                else:
                                    ispis+=""
                                for simbol in stog:
                                   ispis+= simbol
                            else:
                                if(len(stog)!=0):
                                    stog.reverse()
                                    stog.pop()
                                    stog.reverse()
                                if(len(stog)>0):
                                        ispis+="|"+stanje+"#"
                                        for simbol in stog:
                                           ispis+= simbol
                                else:
                                    for simbol in stog:
                                           ispis+= simbol
                                    ispis += "|"+stanje+"#$"
                                    if stanje not in linije[4]:
                                        ispis +="|fail"
                                    u = 1000
                    if stanje in linije[4]:
                        prihvatljivost = "1"
                        break
                    if(len(stog)!=0):
                        key = stanje +",$,"+stog[0]
                        if(provjereno.count(key) != 0):
                            break
                    if(len(stog)==0):
                        break
    if(stanje in linije[4] and "fail" in ispis and k==len(niz)):
        ispis = ispis.replace("|fail","")
    if(stanje in linije[4] and "fail" not in ispis):
        prihvatljivost = "1"
    print(ispis+"|"+prihvatljivost)

            
            

