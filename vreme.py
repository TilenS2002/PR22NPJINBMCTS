import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the data
df = pd.read_csv('baze/manjse/FaktorCest.csv')


# df.fillna("unknown", inplace=True)

# # Define a function to plot a stacked bar chart
# def plot_stacked_bar(data, x, y, categories, title):
#     # Create a pivot table to aggregate the data by category
#     pivot_table = data.pivot_table(index=x, columns=categories, values=y, aggfunc="count", fill_value=0)
    
#     # Create the stacked bar chart
#     pivot_table.plot(kind="bar", stacked=True)
#     plt.xlabel(x)
#     plt.ylabel("Number of Accidents")
#     plt.title(title)
#     plt.legend(title=categories, loc="upper left", bbox_to_anchor=(1, 1))
#     plt.show()


# plot_stacked_bar(df, "VremenskeOkoliscine", "StanjePrometa","StanjeVozisca", "Weather Conditions and Traffic Density")




# plt.figure(figsize=(10,5))
# df['VremenskeOkoliscine'].value_counts().plot(kind='bar')
# plt.title('Frequency of Weather Conditions')
# plt.xlabel('Weather Condition')
# plt.ylabel('Frequency')
# plt.show()

# plt.figure(figsize=(10,5))
# df['StanjePrometa'].value_counts().plot(kind='bar')
# plt.title('Frequency of Traffic Conditions')
# plt.xlabel('Traffic Condition')
# plt.ylabel('Frequency')
# plt.show()

# plt.figure(figsize=(10,5))
# df['StanjeVozisca'].value_counts().plot(kind='bar')
# plt.title('Frequency of Road Situations')
# plt.xlabel('Road Situation')
# plt.ylabel('Frequency')
# plt.show()

# plt.figure(figsize=(10,5))
# df['VrstaVozisca'].value_counts().plot(kind='bar')
# plt.title('Frequency of Road Types')
# plt.xlabel('Road Type')
# plt.ylabel('Frequency')
# plt.show()

# traffic_by_weather = pd.crosstab(df['VremenskeOkoliscine'], df['StanjePrometa'])
# traffic_by_weather.plot(kind='bar', stacked=True, figsize=(10,5))
# plt.title('Traffic by Weather Condition')
# plt.xlabel('Weather Condition')
# plt.ylabel('Frequency')
# plt.show()


# roads_by_weather = pd.crosstab(df['VremenskeOkoliscine'], df['StanjeVozisca'])
# roads_by_weather.plot(kind='bar', stacked=True, figsize=(10,5))
# plt.title('Road Situations by Weather Condition')
# plt.xlabel('Weather Condition')
# plt.ylabel('Frequency')
# plt.show()

# road_type_by_weather = pd.crosstab(df['VremenskeOkoliscine'], df['VrstaVozisca'])
# road_type_by_weather.plot(kind='bar', stacked=True, figsize=(10,5))
# plt.title('Road Types by Weather Condition')
# plt.xlabel('Weather Condition')
# plt.ylabel('Frequency')
# plt.show()







# # Create a pivot table to count the frequency of each combination of VremenskeOkoliscine and StanjePrometa
# pivot_table = pd.pivot_table(df, values='VrstaVozisca', index='VremenskeOkoliscine', columns='StanjePrometa', aggfunc=len, fill_value=0)

# # Create a stacked bar chart
# pivot_table.plot(kind='bar', stacked=True)

# # Set the title and axes labels
# plt.title("Traffic Conditions by Weather Conditions")
# plt.xlabel("Weather Conditions")
# plt.ylabel("Number of Occurrences")

# # Show the chart
# plt.show()





# Group the data by the four attributes and count the frequency of each combination
# grouped_data = data.groupby(['VremenskeOkoliscine', 'StanjePrometa', 'StanjeVozisca', 'VrstaVozisca']).size().reset_index(name='count')

# # Create a stacked bar chart
# fig, ax = plt.subplots(figsize=(12, 8))

# # Set the x-axis labels to the weather conditions
# labels = grouped_data['VremenskeOkoliscine'].unique()
# x = range(len(labels))

# # Iterate over the combinations of the other three attributes and create a stacked bar for each weather condition
# for i, (traffic_type, road_condition, road_type) in enumerate(grouped_data.groupby(['StanjePrometa', 'StanjeVozisca', 'VrstaVozisca'])): # type: ignore
#     y = [traffic_type[0] + ' ' + road_condition[0] + ' ' + road_type[0] for _, _, _, count in road_type.values]
#     values = [count for _, _, _, count in road_type.values]
#     ax.bar(x, values, bottom=[sum(values[:j]) for j in range(i)], label=traffic_type[0] + ' ' + road_condition[0] + ' ' + road_type[0])

# # Set the chart title and axis labels
# ax.set_title('Frequency of weather conditions by traffic type, road condition, and road type')
# ax.set_xlabel('Weather conditions')
# ax.set_ylabel('Frequency')

# # Set the x-axis tick labels to the weather conditions
# ax.set_xticks(x)
# ax.set_xticklabels(labels)

# # Add a legend and save the chart
# ax.legend()
# plt.savefig('stacked_bar_chart.png')
# plt.show()
