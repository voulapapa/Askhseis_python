times= {
    "jean": 25,
    "t-shirt":19,
    "hat":10,
    "earrings": 17,
    "shoes": 50,
    "socks": 7
}

kostos = 0
foros = 0
def telikokostos(rouxa):
    sunolo = 0
    for i in rouxa:
        i = lista(times[key])
        sunolo += i
    return sunolo

def Kostosmeforo (kostos):
        foros = kostos * 24 / 100
        
        sunkostos = foros + kostos
        return sunkostos
        
lista = []
while len(lista) != "":
    i = input ("Enter your clothes to the list(one per time):")
    if i == '':
         break
    else :
        try:
            lista.append(i)
            kostos = sum([times[s] for s in lista ])
            Kostosmeforo(kostos)
        except KeyError:
             print("This doesn't exist in the list")
             lista = lista[:-1]

print(round( Kostosmeforo (kostos), 2) , "€" )