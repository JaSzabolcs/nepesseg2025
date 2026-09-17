import os
telepulesek=[]
with open('lakossag_2025.csv','r',encoding='utf-8') as forras:
    forras.readline()
    for f in forras:
        adatok=f.strip().split(';')
        szotar={
            'megyekod':adatok[0],
            'telepules':adatok[1],
            'tipus':adatok[2],
            'ferfi':int(adatok[3].replace(' ','')),
            'no':int(adatok[4].replace(' ',''))
        }
        telepulesek.append(szotar)


def megye_adatai():
    megyekod=input('Írd be a megye kódját: ')
    telepulesek_szama=0
    lakossag=0
    varoslakok=0
    for i in telepulesek: 
        if i['megyekod']==megyekod:
            telepulesek_szama+=1
            lakossag+=i['ferfi']+i['no']
            if i['tipus'] in ['fővárosi kerület','vármegye székhely','vármegyei jogú város','város']:
                varoslakok+=i['ferfi']+i['no']

    print(f'Települések száma a megyében: {telepulesek_szama}')
    print(f'A megyében {lakossag} lakos él')
    print(f'A városokban (beleértve a megyei jogú várost és megyeszékhelyet is) {varoslakok} élnek')

def telepules_tipusai():
    tipuslista=[]
    for i in telepulesek:
        if i['tipus'] not in tipuslista:
            tipuslista.append(i['tipus'])
    abc='abcdefghijkl'
    index=0
    tipusok={}
    for i in tipuslista:
        tipusok[abc[index]]=i
        index+=1
    for kulcs in tipusok:
        print(f'[{kulcs}] {tipusok[kulcs]}')
    valasztott_tipus=input('Mi a választott típus: ')
    if valasztott_tipus not in tipusok:
        print('Nincs ilyen típus')
        return
    valasztott_tipus=tipusok[valasztott_tipus]
    print(valasztott_tipus)
    
    db=0
    sorok=os.get_terminal_size().lines
    megjelenitettdbszam=sorok-1
    for i in [x for x in telepulesek if x['tipus']==valasztott_tipus ]:
        print(f'{i['telepules']}, lakosok száma: {i['ferfi']+i['no']}')
        db+=1
        if db %megjelenitettdbszam==0:
            input('')
            os.system('cls')
while True:
    print('[1] Megye adatai')
    print('[2] Település típusai')
    print('[x] Kilépés')
    menupont=input('Válassz funkciót: ')
    if menupont.lower()=='x':
        break
    elif menupont=='1':
        megye_adatai() 
    elif menupont=='2':
        telepules_tipusai()


