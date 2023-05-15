import pandas as pd
import matplotlib.pyplot as plt


####################################################
###     Kateri tipi ceste so najbolj nevarni     ### 
####################################################


# Load the databases
cesta_df = pd.read_csv('baze/manjse/Cesta.csv')
nesreca_df = pd.read_csv('baze/manjse/Nesreca.csv')
osebe_df = pd.read_csv('baze/manjse/Osebe.csv')

# Merge the relevant columns
merged_df = pd.merge(cesta_df, nesreca_df, on='ZaporednaStevilkaOsebeVPN')
merged_df = pd.merge(merged_df, osebe_df, on='ZaporednaStevilkaOsebeVPN')

# Calculate accident frequencies by road type
accident_freq_by_road_type = merged_df['VrstaCesteNaselja'].value_counts().sort_values(ascending=False)

# Group the data by road type and injury, and count the occurrences
injury_counts = merged_df.groupby(['VrstaCesteNaselja', 'PoskodbaUdelezenca'])['ZaporednaStevilkaOsebeVPN'].count().unstack()

# Sort the injury counts by the order of accident frequency
injury_counts = injury_counts.loc[accident_freq_by_road_type.index]

###normalizacija
from sklearn.preprocessing import MinMaxScaler

# Apply Min-Max normalization to injury counts
scaler = MinMaxScaler()
normalized_injury_counts = scaler.fit_transform(injury_counts)

# Create a DataFrame with the normalized values
normalized_injury_counts_df = pd.DataFrame(normalized_injury_counts, columns=injury_counts.columns, index=injury_counts.index)

# Print the normalized injury counts
print("Normalized Injury Counts by Road Type:")
print(normalized_injury_counts_df)

# Plot the stacked bar chart of injuries by road type
ax = normalized_injury_counts_df.plot(kind='bar', stacked=True)

plt.xlabel('Road Type')
plt.ylabel('Accident Count')
plt.title('Distribution of Injuries by Road Type')
plt.show()


############ STATS


#Total Accident Count by Road Type:
total_accident_count = accident_freq_by_road_type.sum()

#Proportion of Accident Count by Road Type:
accident_proportion = accident_freq_by_road_type / total_accident_count

#Total Injury Count by Road Type:
total_normalized_injury_counts_df = normalized_injury_counts_df.sum(axis=1)

#Proportion of Injury Count by Road Type:
injury_proportion = total_normalized_injury_counts_df / total_normalized_injury_counts_df.sum()

#Most Frequent Injury by Road Type:
most_frequent_injury = normalized_injury_counts_df.idxmax(axis=1)

# Print the statistics
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