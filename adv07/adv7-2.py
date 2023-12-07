from aocd import get_data
import re
from collections import Counter

data = get_data(year=2023, day=7)

hands_and_bids = [tuple(re.split("\s+", line)) for line in data.split("\n")]

label_to_val = {str(i) : i for i in range(2, 10)}
faces = ["T", "Q", "K", "A"]
label_to_val["J"] = 1

for i in range(len(faces)):
    label_to_val[faces[i]] = 10 + i 

numeric_type = {0: "high_card", 1: "one pair", 
                2: "two pair", 3: "three of a kind", 
                4: "full house", 5: "four of a kind", 
                6: "five of a kind"}

def hand_to_type(hand):
    modified_hand = ""
    hand_without_jokers = ""
   
    for c in hand:

        if (c != "J"):
            hand_without_jokers += c
    hand_dict = Counter(hand_without_jokers)

    for c in hand:

        if (c == "J"):

            if(len(hand_without_jokers) > 0):
                modified_hand += sorted(list(hand_dict.keys()), key=lambda c: hand_dict[c])[-1]
            else:
                modified_hand += "A"
        else:
            modified_hand += c

    hand_dict = Counter(modified_hand)

    amounts = [ [1, 1, 1, 1, 1], [1, 1, 1, 2], 
                [1, 2, 2], [1, 1, 3],
                [2, 3], [1, 4], [5] ]
    
    for i in range(len(amounts)):
        
        if(sorted(list(hand_dict.values())) == amounts[i]):
            return i, hand_dict

def convert_to_compare_same_type(h):
    res = ""

    for c in h:
        res += chr(ord('a') + label_to_val[c])
    return res

sorted_hands = []

for type in range(0, 7):
    hands_with_type = [hb for hb in hands_and_bids if hand_to_type(hb[0])[0] == type]
    hands_with_type.sort(key=lambda h: convert_to_compare_same_type(h[0]))
    sorted_hands += hands_with_type

answer = 0

for i in range(len(sorted_hands)):
    answer += int(sorted_hands[i][1]) * (i + 1)

print(answer)