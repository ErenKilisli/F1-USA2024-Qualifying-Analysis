import fastf1 as ff1
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

ff1.Cache.enable_cache('cache')

qualy = ff1.get_session(2024, 'United States', 'Q') 
qualy.load()

laps = qualy.laps

top_drivers = ['NOR', 'VER', 'SAI', 'LEC', 'PIA', 'RUS']

sector_times = {driver: {'S1': [], 'S2': [], 'S3': []} for driver in top_drivers}

for driver in top_drivers:
    driver_laps = laps[laps['Driver'] == driver]
    
    fastest_lap = driver_laps.loc[driver_laps['LapTime'].idxmin()]
    
    sector_times[driver]['S1'].append(fastest_lap.Sector1Time.total_seconds() if fastest_lap.Sector1Time is not pd.NaT else np.nan)
    sector_times[driver]['S2'].append(fastest_lap.Sector2Time.total_seconds() if fastest_lap.Sector2Time is not pd.NaT else np.nan)
    sector_times[driver]['S3'].append(fastest_lap.Sector3Time.total_seconds() if fastest_lap.Sector3Time is not pd.NaT else np.nan)

color_map = {
    'NOR': 'orange',    
    'VER': 'darkblue',  
    'SAI': 'blue',      
    'LEC': 'red',       
    'PIA': 'yellow',    
    'RUS': 'purple'     
}

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

#for making it histogram
bar_width = 1  

positions = np.arange(len(top_drivers))

for i, sector in enumerate(['S1', 'S2', 'S3']):
    sector_times_list = [sector_times[driver][sector][0] for driver in top_drivers]  # Get fastest times for each driver
    
    bar_colors = [color_map[driver] for driver in top_drivers]
    
    axs[i].bar(positions, sector_times_list, width=bar_width, color=bar_colors, alpha=0.7, edgecolor='black')
    
    axs[i].set_title(f'Fastest {sector} Times per Driver')
    axs[i].set_xlabel('Drivers')
    axs[i].set_ylabel('Time (seconds)')
    axs[i].set_xticks(positions)  
    axs[i].set_xticklabels(top_drivers)  
    axs[i].set_ylim(bottom=0) 

plt.tight_layout()
plt.show()
