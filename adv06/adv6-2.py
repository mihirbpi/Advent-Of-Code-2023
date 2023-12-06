from aocd import get_data
import numpy as np
import re

data = get_data(year=2023, day=6)

race_duration = int("".join(re.split('\s+', data.split("\n")[0])[1:]))
record_distance = int("".join(re.split('\s+', data.split("\n")[1])[1:]))

time_min = np.floor((-race_duration -  np.sqrt(race_duration**2 - 4*record_distance)) / 2 + 1)

time_max = np.floor((-race_duration + np.sqrt(race_duration**2 - 4*record_distance)) / 2)

ways_to_win = int(time_max - time_min + 1)

print(ways_to_win)
    
    
    



