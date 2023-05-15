import pandas as pd

# Load the databases
cas_df = pd.read_csv('baze/manjse/Cas.csv')
nesreca_df = pd.read_csv('baze/manjse/Nesreca.csv')

# Merge the relevant columns
merged_df = pd.merge(cas_df, nesreca_df, on='ZaporednaStevilkaOsebeVPN')

# Convert the date and time columns to DateTime format
merged_df['DatumPN'] = pd.to_datetime(merged_df['DatumPN'])
merged_df['UraPN'] = pd.to_datetime(merged_df['UraPN']).dt.time

# Group accidents by month and calculate the count
accidents_by_month = merged_df.groupby(merged_df['DatumPN'].dt.month)['ZaporednaStevilkaOsebeVPN'].count()

import matplotlib.pyplot as plt

# Plot the accidents by month
plt.figure(figsize=(10, 6))
accidents_by_month.plot(kind='line')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.title('Accident Occurrences by Month')
plt.grid(True)
plt.show()

from statsmodels.tsa.seasonal import seasonal_decompose

# Convert the date column with proper formatting
merged_df['DatumPN'] = pd.to_datetime(merged_df['DatumPN'], format='%d/%m/%Y')

# Set the accident date as the DataFrame index
merged_df.set_index('DatumPN', inplace=True)

# Resample the data to a monthly frequency
accidents_by_month = merged_df.resample('M').size()

# Perform seasonal decomposition
result = seasonal_decompose(accidents_by_month, model='additive')

# Plot the decomposition components
plt.figure(figsize=(10, 8))
result.plot()
plt.show()

