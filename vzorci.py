import pandas as pd

cas_df = pd.read_csv('baze/manjse/Cas.csv')
nesreca_df = pd.read_csv('baze/manjse/Nesreca.csv')
merged_df = pd.merge(cas_df, nesreca_df, on='ZaporednaStevilkaOsebeVPN')
merged_df['DatumPN'] = pd.to_datetime(merged_df['DatumPN'])
merged_df['UraPN'] = pd.to_datetime(merged_df['UraPN']).dt.time
accidents_by_month = merged_df.groupby(merged_df['DatumPN'].dt.month)['ZaporednaStevilkaOsebeVPN'].count()

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
accidents_by_month.plot(kind='line')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.title('Accident Occurrences by Month')
plt.grid(True)
plt.show()

from statsmodels.tsa.seasonal import seasonal_decompose

merged_df['DatumPN'] = pd.to_datetime(merged_df['DatumPN'], format='%d/%m/%Y')
merged_df.set_index('DatumPN', inplace=True)
accidents_by_month = merged_df.resample('M').size()

result = seasonal_decompose(accidents_by_month, model='additive')

plt.figure(figsize=(10, 8))
result.plot()
plt.show()

