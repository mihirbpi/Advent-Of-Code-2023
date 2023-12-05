from aocd import get_data

data = get_data(year=2023, day=4)
lines = data.split("\n")

matches_dict = {}
instances_dict = {}

for i in range(len(lines)):
    line = lines[i]
    card_no = i + 1
    instances_dict[card_no] = 1
    number_lists = line.split(": ")[1]
    winning_list = number_lists.split(" | ")[0].split(" ")
    my_list = number_lists.split(" | ")[1].split(" ")
    matches = 0

    for number in my_list:

        if number in winning_list and number != "":
            matches += 1

    matches_dict[card_no] = matches

for card_no in matches_dict:

    look_ahead = matches_dict[card_no]

    for i in range(card_no + 1, card_no + look_ahead + 1):
        instances_dict[i] += instances_dict[card_no]

print(sum(list(instances_dict.values())))