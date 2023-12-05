from aocd import get_data

data = get_data(year=2023, day=4)
lines = data.split("\n")

answer = 0

for line in lines:
    number_lists = line.split(": ")[1]
    winning_list = number_lists.split(" | ")[0].split(" ")
    my_list = number_lists.split(" | ")[1].split(" ")
    points = 0

    for number in my_list:

        if number in winning_list and number != "":

            if points == 0:
                points = 1
            else:
                points *= 2

    answer += points

print(answer)
