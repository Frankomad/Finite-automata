import sys

ulNizovi = []                           # a,pnp,a|pnp,lab2|pnp,a|pnp,lab2,utr,utr
skupStanja = []                         #p5,s3,s4,st6,stanje1,stanje2
skupSimbola = []                        #a,lab2,pnp,utr
skupPrihvStanja = []                    #p5
                                        #stanje1
funkcije = []                           
kraj = ''
brojac = 1

sljedecaStanja = []

lijevaStr =[]

mapa = {}
mapaUnutar = {}

pomocni = {}

try:
    for line in iter(input, kraj):
        if (brojac == 1):
            ulNizovi = line.strip().split("|")
        elif (brojac == 2):
            skupStanja = line.strip().split(",")
        elif (brojac == 3):
            skupSimbola = line.strip().split(",")
        elif (brojac == 4):
            skupPrihvStanja = line.strip().split(",")
        elif (brojac == 5):
            pocStanje = line
        else:
            funkcije = line.split('->')                 #npr. s3,a -> stanje2, stanje3...   prelazi u [(s3, a), (stanje2, stanje3)]
            lijevaStr = funkcije[0].split(',')          #s3, a
            trenStanje = lijevaStr[0]                   #trenStanje = s3
            simbol = lijevaStr[1]                       #simbol = a
            sljedecaStanja = funkcije[1].split(',')     #stanje2, stanje3

            if trenStanje in mapa:                      #pomocna mapa u koju stavljama values glavne mape
                pomocni = mapa[trenStanje]
                pomocni[simbol] = sljedecaStanja        #dodajemo na key simbola listu iducih stanja
                mapa[trenStanje] = pomocni
            else:
                pomocni = ({simbol : sljedecaStanja})
                mapa[trenStanje] = pomocni

        brojac += 1
except EOFError:
    print('')

            
#print(mapa)

        

        
izlaz = ""

for ulNiz in ulNizovi:                                  # a,pnp,a|pnp,lab2|pnp,a|pnp,lab2,utr,utr

    listaStanja = []                                    #lista stanja u kojima se nalazimo

    listaStanja.append(pocStanje)                       #sadasnjaStanja -> [stanje1]

    listaSljedStanja = []                               #lista sljedecih stanja

    niz = []                
    
    niz = ulNiz.split(",")                              #[a, pnp, a]

    
    for znak in niz:                                    #a    pnp    a
    

        #EPSILON- nalazimo listu trenutnih stanja
        for stanje in listaStanja:                                  #listaStanja = [pocStanje, ...]

            if stanje in mapa:                                      #ako se stanje nalazi u mapi

                mapa2 = mapa[stanje]                                #mapa:   s3(key):[a(key): stanje2, stanje3]  ->  mapa2:  a(key): stanje2, stanje3

                if '$' in mapa2:                                    #ako stanje sadrži prijelaz '$'

                    values = mapa2['$']                             #values = [stanje2, stanje3]

                    for value in values:                            #stanje2,  stanje3

                        if (value != '#'):                          #ako je prazno satnje preskoci

                            if value not in listaStanja:            #provjerit jel se nalazi vec unutra
                    
                                listaStanja.append(value)           #dodat u listu listaStanja
            


        #provjeravao simbol prijelaza i stavljamo u listuSljedStanja
        for stanje in listaStanja:

            if stanje in mapa:

                mapa3 = mapa[stanje]                                #mapa:   s3(key):[a(key): stanje2, stanje3]  ->  mapa2:  a(key): stanje2, stanje3

                if znak in mapa3:                                   #ako se znak nalazi u mapi s prijelazima za to stanje  ako je znak a i ako S3 ima prijelaz sa znakom a

                    values = mapa3[znak]                            #values je lista sa stanjima u koje trenutno stanje prelazi za dobiveni znak

                    for value in values:                            #za svako stanje u listi iducih staanje

                        if (value != '#'):                          #ako je prazno satnje preskoci

                            if value not in listaSljedStanja:       #provjeri ak se ne nalazi u listi sljed stanja

                                listaSljedStanja.append(value)      #onda dodaj


        #ispisati trenutna stanja, i iduca stanja postaviti kao trenutna

                            
        #print("Sljed stanja: ", listaSljedStanja)
        #print("tren stanje: ", listaStanja)
                                

        listaStanja.sort()                                      #sortiramo listu
        if (len(listaStanja) == 0):                             #ako je prazna lista na izlaz dodajemo #
            izlaz = izlaz + '#'
        else:
            izlaz = izlaz + ','.join(listaStanja)               #inace na izlaz listu
        izlaz = izlaz + '|'
                            
        listaStanja = listaSljedStanja                          #zamjenimo da iduca postaju sadasnja
 
        listaSljedStanja = []                                   #vratimo listu sadasnjih stanja na praznu
            
    #u vanjskom foru

    #EPSILON- zadnja provjera u kojoj nalazimo epsilon u listu trenutnih stanja (nakon petlje za zadnji niz)
    for stanje in listaStanja:                                  #listaStanja = [pocStanje, ...]

        if stanje in mapa:                                      #ako se stanje nalazi u mapi

            mapa2 = mapa[stanje]                                #mapa:   s3(key):[a(key): stanje2, stanje3]  ->  mapa2:  a(key): stanje2, stanje3

            if '$' in mapa2:                                    #ako stanje sadrži prijelaz '$'

                values = mapa2['$']                             #values = [stanje2, stanje3]

                for value in values:                            #stanje2,  stanje3

                    if (value != '#'):                          #ako je prazno satnje preskoci

                        if value not in listaStanja:            #provjerit jel se nalazi vec unutra
                    
                            listaStanja.append(value)           #dodat u listu listaStanja

                            

    listaStanja.sort()                                      #sortiramo listu
    #print("tren stanje: ", listaStanja)
    if (len(listaStanja) == 0):                             #ispis
            izlaz = izlaz + '#'
    else:
        izlaz = izlaz + ','.join(listaStanja)

    print(izlaz)
    #print()
                        
    listaStanja = []
    izlaz = ''
        
    

    
