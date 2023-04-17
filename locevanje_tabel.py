import pandas as pd

#Koda je narejena v namen ločevanja velike baze pn2022.csv na manjše odtabele v namen boljšega razumevanja, optimizacije in lažjega pristopanja do analize in pregled podatkov.
# za ključ je uporabljena 'ZaporednaStevilkaOsebeVPN', ki preko vseh baz predstavlja enako nesrečo.

#preberemo celotno tabelo podatkov
df = pd.read_csv('baze\pn2022.csv', delimiter=';')

#      KOORDINATE NESREČ      #
#   Nova tabela vsebuje koordinato x in y kraja nesreče, za takšen pristop smo se odločili predvsem zarai vizualizacije, kjer lahko nesreče predstavimo na mapi slovenije.
new_df = df[['ZaporednaStevilkaOsebeVPN', 'GeoKoordinataX', 'GeoKoordinataY']]
new_df = new_df.drop(new_df[(new_df['GeoKoordinataX'] == 0) & (new_df['GeoKoordinataY'] == 0)].index)
new_df.to_csv('baze/manjse/Koordinate.csv', index=False)

#      KRAJ NESREČ      #
kraj_df=df[['ZaporednaStevilkaOsebeVPN','UpravnaEnotaStoritve','VNaselju','Lokacija','OpisKraja']]
kraj_df.to_csv('baze/manjse/Kraj.csv', index=False)

#      ČAS NESREČ      #
# reformatiranje ur, zaradi napačnega izvoza, kjer je bila ura spremenjena v datum
month_dict={'jan':'01', 'feb':'02', 'mar':'03', 'apr':'04', 'maj':'05', 'jun':'06', 'jul':'07', 'avg':'08', 'sep':'09', 'okt':'10', 'nov':'11', 'dec':'12'}
for key in month_dict.keys():
    df['UraPN'] = df['UraPN'].str.replace(f'{key}.', f'{month_dict[key]}.')
    df['UraPN'] = df['UraPN'].str.replace(f'.{key}', f'.{month_dict[key]}')
   
df['UraPN'] = pd.to_datetime(df['UraPN'], format='%H.%M', errors='coerce')
try:
    df['UraPN'] = pd.to_datetime(df['UraPN'], format='%H.%M').dt.strftime('%H.%M')
except ValueError:
    df['UraPN'] = '00.00'

time_df=df[['ZaporednaStevilkaOsebeVPN','DatumPN','UraPN']]
time_df.to_csv('baze/manjse/Cas.csv', index=False)

#      NESREČA      #
nesreca_df= df[['ZaporednaStevilkaOsebeVPN', 'VzrokNesrece', 'TipNesrece']]
nesreca_df.to_csv('baze/manjse/Nesreca.csv', index=False)

#      CESTA NESREČE      #
cesta_df= df[['ZaporednaStevilkaOsebeVPN', 'VrstaCesteNaselja']]
cesta_df.to_csv('baze/manjse/Cesta.csv', index=False)

#      FAKTORJI CESTIŠČA      #
faktorji_df= df[['ZaporednaStevilkaOsebeVPN', 'VremenskeOkoliscine', 'StanjePrometa', 'StanjeVozisca', 'VrstaVozisca']]
faktorji_df.to_csv('baze/manjse/FaktorCest.csv', index=False)

#      FAKTORJI OSEBE      #
osebniF_df= df[['ZaporednaStevilkaOsebeVPN', 'UporabaVarnostnegaPasu', 'VrednostAlkotesta', 'VrednostStrokovnegaPregleda']]

# popravek vrednosti iz String v float za nadalno statistiko
osebniF_df['VrednostAlkotesta'] = osebniF_df['VrednostAlkotesta'].str.replace(",",".")
osebniF_df['VrednostStrokovnegaPregleda'] = osebniF_df['VrednostStrokovnegaPregleda'].str.replace(",",".")
osebniF_df['VrednostAlkotesta'] = osebniF_df['VrednostAlkotesta'].astype(float)
osebniF_df['VrednostStrokovnegaPregleda'] = osebniF_df['VrednostStrokovnegaPregleda'].astype(float)

osebniF_df.to_csv('baze/manjse/FaktorOseb.csv', index=False)

#      O OSEBI      #
# vozniski izpit poracunan v mesecih
df['MeseciIzpita'] = (df['VozniskiStazVLetih'] * 12) + df['VozniskiStazVMesecih']

osebe_df= df[['ZaporednaStevilkaOsebeVPN', 'Povzrocitelj', 'Starost', 'Spol', 'Drzavljanstvo', 'VrstaUdelezenca', 'PoskodbaUdelezenca', 'MeseciIzpita']]
osebe_df.to_csv('baze/manjse/Osebe.csv', index=False)

#      SPLOŠNO      #
splosno_df=df[['ZaporednaStevilkaOsebeVPN', 'KlasifikacijaNesrece']]
splosno_df.to_csv('baze/manjse/Splosno.csv', index=False)


