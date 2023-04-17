import pandas as pd

# preberemo celotno tabelo podatkov
df = pd.read_csv('baze\pn2022.csv', delimiter=';')

# koordinate tabela
new_df = df[['ZaporednaStevilkaOsebeVPN', 'GeoKoordinataX', 'GeoKoordinataY']]
new_df = new_df.drop(new_df[(new_df['GeoKoordinataX'] == 0) & (new_df['GeoKoordinataY'] == 0)].index)
new_df.to_csv('baze/manjse/Koordinate.csv', index=False)

# čas
month_dict={'jan':'01', 'feb':'02', 'mar':'03', 'apr':'04', 'maj':'05', 'jun':'06', 'jul':'07', 'avg':'08', 'sep':'09', 'okt':'10', 'nov':'11', 'dec':'12'}

for key in month_dict.keys():
    df['UraPN'] = df['UraPN'].str.replace(f'{key}.', f'{month_dict[key]}.')
    df['UraPN'] = df['UraPN'].str.replace(f'.{key}', f'.{month_dict[key]}')

time_df=df[['ZaporednaStevilkaOsebeVPN','DatumPN','UraPN']]
time_df.to_csv('baze/manjse/Cas.csv', index=False)

# kraj
kraj_df=df[['ZaporednaStevilkaOsebeVPN','UpravnaEnotaStoritve','VNaselju','Lokacija','OpisKraja']]
kraj_df.to_csv('baze/manjse/Kraj.csv', index=False)

# nesreča
nesreca_df= df[['ZaporednaStevilkaOsebeVPN', 'VzrokNesrece', 'TipNesrece']]
nesreca_df.to_csv('baze/manjse/Nesreca.csv', index=False)

# cesta
cesta_df= df[['ZaporednaStevilkaOsebeVPN', 'VrstaCesteNaselja']]
cesta_df.to_csv('baze/manjse/Cesta.csv', index=False)

# faktorji cestisca
faktorji_df= df[['ZaporednaStevilkaOsebeVPN', 'VremenskeOkoliscine', 'StanjePrometa', 'StanjeVozisca', 'VrstaVozisca']]
faktorji_df.to_csv('baze/manjse/FaktorCest.csv', index=False)

# faktorji osebe

osebniF_df= df[['ZaporednaStevilkaOsebeVPN', 'UporabaVarnostnegaPasu', 'VrednostAlkotesta', 'VrednostStrokovnegaPregleda']]
osebniF_df['VrednostAlkotesta'] = osebniF_df['VrednostAlkotesta'].str.replace(",",".")
osebniF_df['VrednostStrokovnegaPregleda'] = osebniF_df['VrednostStrokovnegaPregleda'].str.replace(",",".")

osebniF_df['VrednostAlkotesta'] = osebniF_df['VrednostAlkotesta'].astype(float)
osebniF_df['VrednostStrokovnegaPregleda'] = osebniF_df['VrednostStrokovnegaPregleda'].astype(float)
osebniF_df.to_csv('baze/manjse/FaktorOseb.csv', index=False)

# o osebi
df['MeseciIzpita'] = (df['VozniskiStazVLetih'] * 12) + df['VozniskiStazVMesecih']
osebe_df= df[['ZaporednaStevilkaOsebeVPN', 'Povzrocitelj', 'Starost', 'Spol', 'Drzavljanstvo', 'VrstaUdelezenca', 'PoskodbaUdelezenca', 'MeseciIzpita']]
osebe_df.to_csv('baze/manjse/Osebe.csv', index=False)

#na splošno
splosno_df=df[['ZaporednaStevilkaOsebeVPN', 'KlasifikacijaNesrece']]
splosno_df.to_csv('baze/manjse/Splosno.csv', index=False)


