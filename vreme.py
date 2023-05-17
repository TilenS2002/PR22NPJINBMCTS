import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('baze/manjse/FaktorCest.csv')
df = df[df['StanjePrometa'] != 'NEZNANO']
df = df[df['VremenskeOkoliscine'] != 'NEZNANO']


faktor_cest = pd.read_csv('baze/manjse/FaktorCest.csv')
nesreca = pd.read_csv('baze/manjse/Nesreca.csv')
merged_data = pd.merge(faktor_cest, nesreca, on='ZaporednaStevilkaOsebeVPN')
merged_data = merged_data[merged_data['VremenskeOkoliscine'] != 'NEZNANO']
weather_counts = merged_data['VremenskeOkoliscine'].value_counts()

total_accidents = len(merged_data)
weather_percentage = weather_counts / total_accidents * 100

print(weather_percentage)




# df.fillna("unknown", inplace=True)

def plot_stacked_bar(data, x, categories, title):
    pivot_table = data.pivot_table(index=x, columns=categories, values='ZaporednaStevilkaOsebeVPN', aggfunc='count', fill_value=0)
    normalized_table = pivot_table.div(pivot_table.sum(axis=1), axis=0)
    normalized_table.plot(kind="bar", stacked=True, figsize=(10, 6))
    plt.xlabel(x)
    plt.ylabel("Normalized Frequency")
    plt.title(title)
    plt.legend(title=categories, loc="upper left", bbox_to_anchor=(1, 1))
    plt.show()


plot_stacked_bar(df, "VremenskeOkoliscine", "StanjePrometa", "Weather Conditions and Traffic Density")

# Plot the frequency of Weather Conditions
plt.figure(figsize=(10, 5))
df['VremenskeOkoliscine'].value_counts().plot(kind='bar')
plt.title('Frequency of Weather Conditions')
plt.xlabel('Weather Condition')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10,5))
df['StanjePrometa'].value_counts().plot(kind='bar')
plt.title('Frequency of Traffic Conditions')
plt.xlabel('Traffic Condition')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10,5))
df['StanjeVozisca'].value_counts().plot(kind='bar')
plt.title('Frequency of Road Situations')
plt.xlabel('Road Situation')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10,5))
df['VrstaVozisca'].value_counts().plot(kind='bar')
plt.title('Frequency of Road Types')
plt.xlabel('Road Type')
plt.ylabel('Frequency')
plt.show()


pivot_table = pd.pivot_table(df, values='ZaporednaStevilkaOsebeVPN', index='VremenskeOkoliscine', columns='StanjePrometa', aggfunc=len, fill_value=0)
normalized_table = pivot_table.div(pivot_table.sum(axis=1), axis=0)

normalized_table.plot(kind='bar', stacked=True)
plt.title("Traffic Conditions by Weather Conditions")
plt.xlabel("Weather Conditions")
plt.ylabel("Normalized Frequency")
plt.show()


pivot_table = pd.pivot_table(df, values='ZaporednaStevilkaOsebeVPN', index='VremenskeOkoliscine', columns='StanjeVozisca', aggfunc=len, fill_value=0)

normalized_table = pivot_table.div(pivot_table.sum(axis=1), axis=0)

normalized_table.plot(kind='bar', stacked=True)
plt.title("Road Situations by Weather Conditions")
plt.xlabel("Weather Conditions")
plt.ylabel("Normalized Frequency")
plt.show()

pivot_table = pd.pivot_table(df, values='ZaporednaStevilkaOsebeVPN', index='VremenskeOkoliscine', columns='VrstaVozisca', aggfunc=len, fill_value=0)

normalized_table = pivot_table.div(pivot_table.sum(axis=1), axis=0)
normalized_table.plot(kind='bar', stacked=True)
plt.title("Road Types by Weather Conditions")
plt.xlabel("Weather Conditions")
plt.ylabel("Normalized Frequency")
plt.show()







pivot_table = pd.pivot_table(df, values='VrstaVozisca', index='VremenskeOkoliscine', columns='StanjePrometa', aggfunc=len, fill_value=0)
normalized_table = pivot_table.div(pivot_table.sum(axis=1), axis=0)
normalized_table.plot(kind='bar', stacked=True)
plt.title("Traffic Conditions by Weather Conditions")
plt.xlabel("Weather Conditions")
plt.ylabel("Number of Occurrences")
plt.show()





# grouped_data = data.groupby(['VremenskeOkoliscine', 'StanjePrometa', 'StanjeVozisca', 'VrstaVozisca']).size().reset_index(name='count')

# fig, ax = plt.subplots(figsize=(12, 8))

# labels = grouped_data['VremenskeOkoliscine'].unique()
# x = range(len(labels))

# for i, (traffic_type, road_condition, road_type) in enumerate(grouped_data.groupby(['StanjePrometa', 'StanjeVozisca', 'VrstaVozisca'])): # type: ignore
#     y = [traffic_type[0] + ' ' + road_condition[0] + ' ' + road_type[0] for _, _, _, count in road_type.values]
#     values = [count for _, _, _, count in road_type.values]
#     ax.bar(x, values, bottom=[sum(values[:j]) for j in range(i)], label=traffic_type[0] + ' ' + road_condition[0] + ' ' + road_type[0])

# ax.set_title('Frequency of weather conditions by traffic type, road condition, and road type')
# ax.set_xlabel('Weather conditions')
# ax.set_ylabel('Frequency')

# ax.set_xticks(x)
# ax.set_xticklabels(labels)

# ax.legend()
# plt.savefig('stacked_bar_chart.png')
# plt.show()
