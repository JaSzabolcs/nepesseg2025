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



while True:
    print('[1] Megye adatai')
    print('[2] Település típusai')
    print('[x] Kilépés')
    menupont=input('Válassz funkciót: ')
    if menupont.lower()=='x':
        break
    elif menupont=='1':
        megye_adatai() 


