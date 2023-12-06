from aocd import get_data
import re

data = get_data(year=2023, day=6)

race_durations = list(map(int, re.split('\s+', data.split("\n")[0])[1:]))
record_distances = list(map(int, re.split('\s+', data.split("\n")[1])[1:]))
answer = 1

for i in range(len(race_durations)):
    race_duration = race_durations[i]
    ways_to_win = 0

    for hold_button_time in range(race_duration + 1):
        boat_speed = hold_button_time
        time_to_move = race_duration - hold_button_time

        total_distance = boat_speed * time_to_move
        distance_record = record_distances[i]

        if (total_distance > distance_record):
            ways_to_win += 1

    answer *= ways_to_win
print(answer)
    
    
    



