import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Cas.csv file
cas_data = pd.read_csv("baze/manjse/Cas.csv")

# Convert the "DatumPN" column to datetime format
cas_data['DatumPN'] = pd.to_datetime(cas_data['DatumPN'], format='%d.%m.%Y')

# Extract the month from the date
cas_data['Month'] = cas_data['DatumPN'].dt.month

# Define the seasons
seasons = {
    'Winter': [12, 1, 2],
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Autumn': [9, 10, 11]
}

# Assign seasons to each month
cas_data['Season'] = cas_data['Month'].apply(lambda x: next(season for season, months in seasons.items() if x in months))

# Count the number of accidents for each season
accidents_per_season = cas_data['Season'].value_counts()

# Calculate the percentage of accidents for each season
accidents_percentage = (accidents_per_season / len(cas_data)) * 100

# Print the statistics for each season
print("Accident Statistics by Season:")
for season in accidents_per_season.index:
    accident_count = accidents_per_season[season]
    accident_percentage = accidents_percentage[season]
    print(f"{season}: {accident_count} accidents ({accident_percentage:.2f}%)")

# Count the number of accidents for each month
accidents_by_month = cas_data['Month'].value_counts().sort_index()

# Reshape the data into a matrix
accidents_matrix = accidents_by_month.values.reshape(1, -1) # type: ignore

# Create a list of month labels
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create the heatmap
plt.figure(figsize=(10, 4))
sns.heatmap(accidents_matrix, cmap='YlOrRd', annot=True, fmt='d', linewidths=0.5, cbar=True) # type: ignore

# Customize the plot
plt.title("Accident Heatmap by Month")
plt.xlabel("Month")


# Set the x-axis tick labels to display month names
plt.xticks(range(len(month_labels)), month_labels)

# Show the heatmap
plt.show()