import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cas_data = pd.read_csv("baze/manjse/Cas.csv")
cas_data['DatumPN'] = pd.to_datetime(cas_data['DatumPN'], format='%d.%m.%Y')
cas_data['Month'] = cas_data['DatumPN'].dt.month

seasons = {
    'Winter': [12, 1, 2],
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Autumn': [9, 10, 11]
}

cas_data['Season'] = cas_data['Month'].apply(lambda x: next(season for season, months in seasons.items() if x in months))
accidents_per_season = cas_data['Season'].value_counts()
accidents_percentage = (accidents_per_season / len(cas_data)) * 100

print("Accident Statistics by Season:")
for season in accidents_per_season.index:
    accident_count = accidents_per_season[season]
    accident_percentage = accidents_percentage[season]
    print(f"{season}: {accident_count} accidents ({accident_percentage:.2f}%)")


accidents_by_month = cas_data['Month'].value_counts().sort_index()
accidents_matrix = accidents_by_month.values.reshape(1, -1) # type: ignore

month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

plt.figure(figsize=(10, 4))
sns.heatmap(accidents_matrix, cmap='YlOrRd', annot=True, fmt='d', linewidths=0.5, cbar=True) # type: ignore
plt.title("Accident Heatmap by Month")
plt.xlabel("Mesec")
plt.ylabel("število nesreč")
plt.xticks(range(len(month_labels)), month_labels)
plt.yticks([])
plt.show()