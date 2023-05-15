import pandas as pd
from sklearn.preprocessing import MinMaxScaler

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


## vizualizacija iz katere vidimo da je največ nesreč popovdne, izstopa pa petek popoldne
import matplotlib.pyplot as plt
import seaborn as sns

cas_df['time_range'] = pd.cut(cas_df['UraPN'].apply(lambda x: x.hour*60 + x.minute),
                              bins=[0, morning_end.hour*60 + morning_end.minute, 
                                    afternoon_end.hour*60 + afternoon_end.minute, 
                                    1440],
                              labels=['morning', 'afternoon', 'evening'],
                              right=False)

cas_df['day'] = pd.to_datetime(cas_df['DatumPN'], format='%d.%m.%Y').dt.day_name()


heatmap_df = cas_df.pivot_table(index='time_range', columns='day', values='UraPN', aggfunc=len)
heatmap_df = heatmap_df.reindex(['morning', 'afternoon', 'evening'], axis=0)
heatmap_df = heatmap_df.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], axis=1)

sns.set(font_scale=1.2)
fig, ax = plt.subplots(figsize=(10,7))
sns.heatmap(heatmap_df, cmap='Oranges', annot=True, fmt='d', cbar=False, ax=ax)
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_title('Število nesreč v razmerju časa dneva in dneva v tednu', fontsize=16, pad=20)
plt.tight_layout()
plt.show()