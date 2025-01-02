from pybaseball import batting_stats, statcast_batter, spraychart
import pandas as pd
import matplotlib.pyplot as plt


# Get all of this season's batting data so far
data = batting_stats(2024)

# Define the player names
elly_name = 'Elly De La Cruz'
jackson_name = 'Jackson Chourio'

# Filter the data for each player using their names
elly_stats = data[data['Name'] == elly_name]  # Filter for Elly
jackson_stats = data[data['Name'] == jackson_name]  # Filter for Jackson

# Define the key statistics to include in your report
key_stats = ['Name', 'G', 'AB', 'H', 'HR', 'RBI', 'SB', 'AVG', 'OBP', 'SLG', 'OPS', 'BB%', 'K%', 'wOBA', 'wRC+', 'ISO', 'HardHit%']

# Extract only the key stats for each player
elly_key_stats = elly_stats[key_stats]
jackson_key_stats = jackson_stats[key_stats]

# Print the filtered stats for both players
print("\nElly De La Cruz Key Stats for 2024:")
print(elly_key_stats)

print("\nJackson Chourio Key Stats for 2024:")
print(jackson_key_stats)

# Combine both players' key stats into a single DataFrame
combined_key_stats = pd.concat([elly_key_stats, jackson_key_stats])

# Save the combined key stats to a CSV file
combined_key_stats.to_csv('Elly&Jackson_key_stats_2024_2.csv', index=False)

print("Key player stats saved to 'Elly&Jackson_key_stats_2024.csv'.")


# Define the player MLBAM IDs
elly_id = 682829  # Elly De La Cruz's MLBAM ID
jackson_id = 694192  # Jackson Chourio's MLBAM ID

# Set the date range for the 2024 season
start_date = '2024-01-01'
end_date = '2024-12-31'

# Get Statcast data for Elly De La Cruz
elly_statcast_data = statcast_batter(start_date, end_date, elly_id)

# Get Statcast data for Jackson Chourio
jackson_statcast_data = statcast_batter(start_date, end_date, jackson_id)

# Filter necessary columns for spray chart (hit locations, event type, exit velocity, launch angle)
columns_needed = ['game_date', 'player_name', 'events', 'hc_x', 'hc_y', 'launch_speed', 'launch_angle', 'hit_distance_sc', 'bb_type']
elly_cleaned = elly_statcast_data[columns_needed]
jackson_cleaned = jackson_statcast_data[columns_needed]

# Save cleaned data to CSV for each player
elly_cleaned.to_csv('elly_de_la_cruz_statcast_2024_Gamelog.csv', index=False)
jackson_cleaned.to_csv('jackson_chourio_statcast_2024_Gamelog.csv', index=False)

print("Elly De La Cruz's Statcast data saved to 'elly_de_la_cruz_2024_Gamelog.csv'.")
print("Jackson Chourio's Statcast data saved to 'jackson_chourio_2024_Gamelog.csv'.")

# Display cleaned data for each player
print("Cleaned Data for Elly De La Cruz:")
print(elly_cleaned.head())

print("\nCleaned Data for Jackson Chourio:")
print(jackson_cleaned.head())

# Now, let's create the spray charts for both players, Spray chart for Elly De La Cruz
plt.figure(figsize=(10, 8))
spraychart(elly_cleaned, 'reds', title="Spray Chart for Elly De La Cruz (2024)")
plt.savefig('elly_de_la_cruz_spraychart_2024.png')  # Save as image
plt.show()

# Spray chart for Jackson Chourio
plt.figure(figsize=(10, 8))
spraychart(jackson_cleaned, 'brewers', title="Spray Chart for Jackson Chourio (2024)")
plt.savefig('jackson_chourio_spraychart_2024.png') #save as image
plt.show()