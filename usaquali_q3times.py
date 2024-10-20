import fastf1 as ff1
import matplotlib.pyplot as plt
import pandas as pd

ff1.Cache.enable_cache('cache')

qualy = ff1.get_session(2024, 'United States', 'Q') 
qualy.load()

laps = qualy.laps

top_drivers = ['NOR', 'VER', 'SAI', 'LEC', 'PIA', 'RUS']
filtered_laps = laps[laps['Driver'].isin(top_drivers)]

print("Filtered laps columns:")
print(filtered_laps.columns)

plt.figure(figsize=(14, 8))

color_map = {
    'NOR': 'orange',   
    'VER': 'darkblue',  
    'SAI': 'blue',      
    'LEC': 'red',      
    'PIA': 'yellow',    
    'RUS': 'purple'     
}

#only Q3 laps
q3_laps = filtered_laps[filtered_laps['LapNumber'] <= 12]  

lap_times_q3 = {
    'Lap': [],
    'Driver': [],
    'LapTime': []
}

for lap_number in range(1, 13):  
    for driver in top_drivers:
        driver_lap = q3_laps[(q3_laps['Driver'] == driver) & (q3_laps['LapNumber'] == lap_number)]
        if not driver_lap.empty:
            lap_times_q3['Lap'].append(lap_number)
            lap_times_q3['Driver'].append(driver)
            lap_times_q3['LapTime'].append(driver_lap['LapTime'].dt.total_seconds().min())  


lap_df_q3 = pd.DataFrame(lap_times_q3)


if lap_df_q3.empty:
    print("No lap times collected for Q3.")
else:
    lap_df_pivot = lap_df_q3.pivot(index='Lap', columns='Driver', values='LapTime')


    lap_df_pivot.plot(kind='bar', figsize=(14, 8), color=[color_map[driver] for driver in lap_df_pivot.columns], width=0.8)

    plt.title('Qualifying Time - Q3 - 2024 USA GP', fontsize=16)
    plt.xlabel('Laps', fontsize=14)
    plt.ylabel('Lap Time (seconds)', fontsize=14)
    plt.xticks(rotation=0)  # Keep the x labels horizontal

    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines
    plt.tight_layout()

    plt.show()
