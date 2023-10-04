from re import I, X
import sys
import queue

skupStanja = []                         #p1,p2,p3,p4,p5,p6,p7


skupSimbola = []                        #c,d

skupPrihvStanja = []                    #p5,p6,p7
                                        #p1
funkcije = []                           
kraj = '\n'
brojac = 1

lijevaStr =[]

mapa = {}
pomocni = {}

try:
    for line in iter(input , kraj):
        if (brojac == 1):
            skupStanja = line.strip().split(",")
        elif (brojac == 2):
            skupSimbola = line.strip().split(",")
        elif (brojac == 3):
            skupPrihvStanja = line.split(",")
        elif (brojac == 4):
            pocStanje = line
        else:
            try:
                funkcije = line.split('->')                 #npr. s3,a -> stanje2, stanje3...   prelazi u [(s3, a), (stanje2, stanje3)]
                lijevaStr = funkcije[0].split(',')          #s3, a
                trenStanje = lijevaStr[0]                   #trenStanje = s3
                simbol = lijevaStr[1]                       #simbol = a
                sljedeceStanje = funkcije[1]                #stanje2, stanje3

                if trenStanje in mapa:                      #pomocna mapa u koju stavljama values glavne mape
                    pomocni = mapa[trenStanje]
                    pomocni[simbol] = sljedeceStanje        #dodajemo na key simbola listu iducih stanja
                    mapa[trenStanje] = pomocni
                else:
                    pomocni = ({simbol : sljedeceStanje})
                    mapa[trenStanje] = pomocni
            except IndexError:
                break;
        brojac += 1
except EOFError:
    print('', end = '')


dohvatljivaStanja = []                                      #dohvatljiva stanja
dohvatljivaStanja.append(pocStanje)

pomocna = {}


#print(mapa)
##print()
for i in dohvatljivaStanja:                                 #za svako stanje u dohvatljivim stanjima
    #print (i)
    pomocna = mapa[i]
    for key in pomocna:                                     #za svaki simbol dodajem u dohvatljiva stanja stanje uz taj simbol
        var = pomocna[key]
        if var not in dohvatljivaStanja:                    #ako se stanej ne nalazi u dohvatljivim stanjima dodati ga
            dohvatljivaStanja.append(var)

dohvatljivaStanja.sort()                                    #sortiramo dohvatljiva stanja

##print("dohvatljiva stanja")
##print(dohvatljivaStanja)
##print()
listazaizbacivanje=[]                                       #lista da znamo koja stanja izbaciti

for key in mapa:                                            #izbacujemo nedohvatljiva stanja iz mape
    if key not in dohvatljivaStanja:
        #mapa.pop(key)
        listazaizbacivanje.append(key)

for element in listazaizbacivanje:
    mapa.pop(element)

##print(dohvatljivaStanja)
##print()
##print(listazaizbacivanje)
##print("mapa nakon izbacivanja nedohvatljivih stanja")
##print(mapa)
##print()

broj = len(dohvatljivaStanja)                               #duljina liste dohvatljivih stanja
od = 0

mapaOvisnih = {}            #mapa ovisvnih parova kljuc = par value = lista parova
listakojinisu = []  #lista koji sig nisu
listaIstih = []     #lista istih stanja
listaIstihPrvo = []     #lista istih stanja

def brisi(kljuc):
    kljuc = sorted(kljuc)
    kljuc = tuple(kljuc)
    if kljuc in mapaOvisnih.keys():
        lista = mapaOvisnih[kljuc]
        del mapaOvisnih[kljuc]
        for element in lista:
            brisi(element)
    if kljuc not in listakojinisu:
        listakojinisu.append(kljuc)


for i in range (broj):                                      #za svako stanje u listi dohvatljivih stanja

    od = od + 1     

    for j in range (od, broj):                              #for petlja za sve kombinacije stanja

        Istanje = dohvatljivaStanja[i]                      #stanja
        Jstanje = dohvatljivaStanja[j]          

        ubacujemo = True

        listaOvisnih = []

        parvalue = (Istanje, Jstanje)                       #par koji ovisi
        parvalue = sorted(parvalue)
        parvalue = tuple(parvalue)

        #print(parvalue)


        if(((Istanje in skupPrihvStanja) and (Jstanje in skupPrihvStanja))                  #ako se razlikuje prihvatljivost nisu isti npr p1 je 0 a p7 je 1
        or ((Istanje not in skupPrihvStanja) and (Jstanje not in skupPrihvStanja))):

##            print("------------------------------------------------")
##            print(Istanje)
##            print(Jstanje)

            ubacujemo = 1               #varijabla da vidimo jel ubacujemo ili ne
            
            for simbol in skupSimbola:                          #za svaki simbol u skupu simbola

                #print("simbol: " + simbol)

                prijelaziIstanje = mapa[Istanje]                #mapa prijelaza
                prijelaziJstanje = mapa[Jstanje]

                iduceIstanje = prijelaziIstanje[simbol]         #iduce stanje za simbol simbol iz stanaj i
                iduceJstanje = prijelaziJstanje[simbol]         #iduce stanje za simbol simbol iz stanaj j


                parkljuc = (iduceIstanje, iduceJstanje)              #par iducih stanja o kojem ovise
                #parvalue = (Istanje, Jstanje)
                parvalue = sorted(parvalue)
                parvalue = tuple(parvalue)
                parkljuc = sorted(parkljuc)
                parkljuc = tuple(parkljuc)



                if(((iduceIstanje in skupPrihvStanja) and (iduceJstanje in skupPrihvStanja)) 
                or ((iduceIstanje not in skupPrihvStanja) and (iduceJstanje not in skupPrihvStanja))): #provjeravamo jel za simbol oba prelaze u prihvatljivo ili u neprihvatljivo stanje
                    

                    if((iduceIstanje != iduceJstanje) and ((iduceIstanje != Jstanje and iduceJstanje != Istanje) #usporedujemo (A->B B->A) i (A->neki B->neki) i (A->A B->B)
                    or (iduceIstanje != Istanje and iduceJstanje != Jstanje))):
                        
                        listaOvisnih.append(parkljuc)                           #dodajemo u listu ovisnih
                        ubacujemo = 0
                                            
                else:
                    listaOvisnih = []
                    if parvalue not in listakojinisu:
                        listakojinisu.append(parvalue)
                    brisi(parkljuc)
                    ubacujemo = 0
                    break                                                       #ak se ne podudaraju izlazi van
                

                

            if (ubacujemo == 1):
                if parvalue not in listaIstihPrvo:
                    listaIstihPrvo.append(parvalue)

                    
                
            for elem in listaOvisnih:
                if elem not in mapaOvisnih:                         #ako se ne nalazi kljuc u mapi ovishnih dodajemo ga
                    mapaOvisnih[elem] = [parvalue]
                else:
                    pomocni = mapaOvisnih[elem]                     #ako se nalazi dodajemo pomocu pomocnog polja par u polje valuesa
                    if parvalue not in pomocni:
                        pomocni.append(parvalue)                        #isti nacin ko u ucitavanju prijelaza
                    mapaOvisnih[elem] = pomocni
        else:
            listaOvisnih = []
            if parvalue not in listakojinisu:
                listakojinisu.append(parvalue)
            brisi(parvalue)


##print("mapa ovisnih")           
##print(mapaOvisnih)
##print()
##print("lista onih koje treba izbrisati")

for k in listakojinisu:
    brisi(k)

print(listakojinisu)
print()

rjecnik = {}
for stanje in dohvatljivaStanja:
    rjecnik[stanje] = stanje

#obrnuta = []
#obrnuta = reversed(dohvatljivaStanja)
#obrnuta = dohvatljivaStanja.reverse()
#print(obrnuta)
for stanje in reversed(dohvatljivaStanja):
    #print(stanje)
    for zamjensko in dohvatljivaStanja:
        tup = (zamjensko, stanje)
        tup = tuple(tup)
        #print(tup)
        if(stanje <= zamjensko or tup in listakojinisu):
            continue
        else:
            #print(tup)
            if(rjecnik[zamjensko] < rjecnik[stanje]):
                rjecnik[stanje] = rjecnik[zamjensko]

##print("rjecnik")
print(rjecnik)
##print()

listaKonStanja = []

for value in rjecnik.values():
    if value not in listaKonStanja:
        listaKonStanja.append(value)

##print()
##print(listaKonStanja)
##print()



####ispis

#moguca stanja -> dohvatljiva stanja
stringstanja = ','.join(listaKonStanja)
print(stringstanja)

#simboli -> skupSimbola
stringsimboli = ','.join(skupSimbola)
print(stringsimboli)

#prihvstanja -> skupPrihvStanja
##for i in skupPrihvStanja:
##    if i not in listaKonStanja:
##        skupPrihvStanja.remove(i)
prihvatljiva = []
for i in skupPrihvStanja:
    if i in listaKonStanja:
        prihvatljiva.append(i)

stringprihvstanja = ','.join(prihvatljiva)
print(stringprihvstanja)

#pocstanje
print(rjecnik[pocStanje])

#funkcije prijelaza
for konstanje in listaKonStanja:
    pomocnirjecnik = mapa[konstanje]
    #print(pomocnirjecnik)
    for simbol in skupSimbola:
        value = pomocnirjecnik[simbol]
        if value not in listaKonStanja:
            value = rjecnik[value]
        print(konstanje + "," + simbol + "->" + value)

##print()
##print("mapa")
##print(mapa)
##print()
##print("rjecnik")
##print(rjecnik)

    
##
##print("mapa ovisnih nakon izbacivanja")
##print(mapaOvisnih)
##print()
##print(mapa)


##for key in mapaOvisnih.keys():
##    listaIstih.append(key)

##print("lista koji su isti iz mape ovisnih (ostali na kraju)")
##print(listaIstih)
##print()

##print("lista koji su isti na prolazu")
##print(listaIstihPrvo)
##print()


##listaProm = []
##
##
########################## za promijenu istih stanja
##for elem in listaIstih:
##    var = elem[1]
##    listaProm.append(var)
##
###print(listaProm)
###print()
###print(mapa)
###print()
##
##for elem in listaProm:
##    del mapa[elem]
###print(mapa)
##
##for key in mapa:
##    values = mapa[key]
##    for key2 in values:
##        value2 = values[key2]
##        #print(value2)
