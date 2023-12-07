from aocd import get_data
import re
from collections import Counter

data = get_data(year=2023, day=7)

hands_and_bids = [tuple(re.split("\s+", line)) for line in data.split("\n")]

label_to_val = {str(i) : i for i in range(2, 10)}
faces = ["T", "J", "Q", "K", "A"]

for i in range(len(faces)):
    label_to_val[faces[i]] = 10 + i 

numeric_type = {0: "high_card", 1: "one pair", 2 : "two pair", 3 : "three of a kind", 4: "full house", 5: "four of a kind", 6: "five of a kind"}

def hand_to_type(hand):
    hand_dict = Counter(hand)

    if(sorted(list(hand_dict.values())) == [5]):
        return 6, hand_dict
    elif(sorted(list(hand_dict.values())) == [1, 4]):
        return 5, hand_dict
    elif(sorted(list(hand_dict.values())) == [2, 3]):
        return 4, hand_dict
    elif(sorted(list(hand_dict.values())) == [1, 1 ,3]):  
        return 3, hand_dict
    elif(sorted(list(hand_dict.values())) == [1, 2 ,2]):
        return 2, hand_dict
    elif(sorted(list(hand_dict.values())) == [1, 1, 1, 2]):
        return 1, hand_dict
    else:
        return 0, hand_dict

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