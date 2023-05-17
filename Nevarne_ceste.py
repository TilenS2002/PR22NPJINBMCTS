import pandas as pd
import matplotlib.pyplot as plt


####################################################
###     Kateri tipi ceste so najbolj nevarni     ### 
####################################################

cesta_df = pd.read_csv('baze/manjse/Cesta.csv')
nesreca_df = pd.read_csv('baze/manjse/Nesreca.csv')
osebe_df = pd.read_csv('baze/manjse/Osebe.csv')


merged_df = pd.merge(cesta_df, nesreca_df, on='ZaporednaStevilkaOsebeVPN')
merged_df = pd.merge(merged_df, osebe_df, on='ZaporednaStevilkaOsebeVPN')
accident_freq_by_road_type = merged_df['VrstaCesteNaselja'].value_counts().sort_values(ascending=False)
injury_counts = merged_df.groupby(['VrstaCesteNaselja', 'PoskodbaUdelezenca'])['ZaporednaStevilkaOsebeVPN'].count().unstack()
injury_counts = injury_counts.loc[accident_freq_by_road_type.index]

###normalizacija
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
normalized_injury_counts = scaler.fit_transform(injury_counts)
normalized_injury_counts_df = pd.DataFrame(normalized_injury_counts, columns=injury_counts.columns, index=injury_counts.index)

print("Normalized Injury Counts by Road Type:")
print(normalized_injury_counts_df)
ax = normalized_injury_counts_df.plot(kind='bar', stacked=True)

plt.xlabel('Road Type')
plt.ylabel('Accident Count')
plt.title('Distribution of Injuries by Road Type')
plt.show()





############ STATS


#Total Accident Count by Road Type:
total_accident_count = accident_freq_by_road_type.sum()
accident_proportion = accident_freq_by_road_type / total_accident_count
total_normalized_injury_counts_df = normalized_injury_counts_df.sum(axis=1)
injury_proportion = total_normalized_injury_counts_df / total_normalized_injury_counts_df.sum()
most_frequent_injury = normalized_injury_counts_df.idxmax(axis=1)


print("Total Accident Count by Road Type:")
print(accident_freq_by_road_type)
print("\nProportion of Accident Count by Road Type:")
print(accident_proportion)
print("\nTotal Injury Count by Road Type:")
print(total_normalized_injury_counts_df)
print("\nProportion of Injury Count by Road Type:")
print(injury_proportion)
print("\nMost Frequent Injury by Road Type:")
print(most_frequent_injury)

fatal_injury_proportion = normalized_injury_counts_df['SMRT'].copy()

fatal_injury_proportion /= total_normalized_injury_counts_df

fatal_injury_proportion = fatal_injury_proportion.loc[accident_freq_by_road_type.index]

fatal_injury_proportion_sorted = fatal_injury_proportion.sort_values(ascending=True)

plt.figure(figsize=(10, 5))
fatal_injury_proportion_sorted.plot(kind='bar')
plt.xlabel('Road Type')
plt.ylabel('Proportion of Fatal Injuries')
plt.title('Proportion of Fatal Injuries by Road Type (Sorted Ascending)')
plt.show()

print("Proportion of Fatal Injuries by Road Type (Sorted Ascending):")
print(fatal_injury_proportion_sorted)