import fastf1 as ff1
import matplotlib.pyplot as plt
import pandas as pd

ff1.Cache.enable_cache('cache')

qualy = ff1.get_session(2024, 'United States', 'Q') 
qualy.load()

laps = qualy.laps

top_drivers = ['NOR', 'VER', 'SAI', 'LEC', 'PIA', 'RUS']
filtered_laps = laps[laps['Driver'].isin(top_drivers)]

pole_position_time = filtered_laps['LapTime'].min()

#Calculating time gaps and distances for each driver
time_gaps = {}
distances = {}
time_to_distance_conversion_factor = 100 / 2.4  

for driver in top_drivers:
    driver_best_time = filtered_laps[filtered_laps['Driver'] == driver]['LapTime'].min()
    time_gap = (driver_best_time - pole_position_time).total_seconds()  
    distance = time_gap * time_to_distance_conversion_factor  
    time_gaps[driver] = time_gap
    distances[driver] = distance

results_df = pd.DataFrame({
    'Time Gap to Pole (s)': time_gaps,
    'Distance from Pole (m)': distances
})

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
results_df.sort_values('Time Gap to Pole (s)', ascending=True)['Time Gap to Pole (s)'].plot(kind='barh', color='skyblue', legend=False)
plt.title('Time Gap to Pole Position - 2024 USA GP Qualifying', fontsize=16)
plt.xlabel('Time Gap to Pole (seconds)', fontsize=14)
plt.ylabel('Drivers', fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.subplot(2, 1, 2)
results_df.sort_values('Distance from Pole (m)', ascending=True)['Distance from Pole (m)'].plot(kind='barh', color='lightcoral', legend=False)
plt.title('Distance from Pole Position - 2024 USA GP Qualifying', fontsize=16)
plt.xlabel('Distance from Pole (meters)', fontsize=14)
plt.ylabel('Drivers', fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()
