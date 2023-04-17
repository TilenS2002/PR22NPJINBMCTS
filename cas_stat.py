import pandas as pd

# pomen kode: koda, ki ločuje nesreče po jutru, popoldnevu in večeru
# izpiše: število nesreč procentualno

# deklariranje časov dneva
morning_start = pd.to_datetime('00.00', format='%H.%M').time()
morning_end = pd.to_datetime('12.00', format='%H.%M').time()
afternoon_start = pd.to_datetime('12.00', format='%H.%M').time()
afternoon_end = pd.to_datetime('18.00', format='%H.%M').time()
evening_start = pd.to_datetime('18.00', format='%H.%M').time()
evening_end = pd.to_datetime('23.59', format='%H.%M').time()
cas_df=pd.read_csv("baze/manjse/Cas.csv")

#popravek ure
cas_df['UraPN'] = pd.to_datetime(cas_df['UraPN'].astype(str).apply(lambda x: x + '.00' if len(x) == 2 else x), format='%H.%M').dt.time

#ustvarjenje tabel
morning_df = cas_df[(cas_df['UraPN'] >= morning_start) & (cas_df['UraPN'] <= morning_end)]
afternoon_df = cas_df[(cas_df['UraPN'] >= afternoon_start) & (cas_df['UraPN'] <= afternoon_end)]
evening_df = cas_df[(cas_df['UraPN'] >= evening_start) & (cas_df['UraPN'] <= evening_end)]

#izpis
skupaj= len(cas_df)
print(f"zjutraj: {len(morning_df)/ skupaj * 100:.2f}%")
print(f"popoldne: {len(afternoon_df)/ skupaj * 100:.2f}%")
print(f"zvečer: {len(evening_df)/ skupaj * 100:.2f}%")

