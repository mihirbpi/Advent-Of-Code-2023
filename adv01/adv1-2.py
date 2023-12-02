from aocd import get_data
data = get_data(year=2023, day=1)
inputs = data.split("\n")

nums_dict = {"one" : "1", "two": "2", "three": "3", 
             "four" : "4", "five": "5", "six": "6", 
             "seven": "7", "eight": "8", "nine": "9", 
             "1": "1", "2": "2", "3": "3", 
             "4": "4", "5": "5", "6": "6", 
             "7": "7", "8": "8", "9": "9"} 

answer = 0

for input in inputs:
    nums_in_input = []

    for num in list(nums_dict.keys()):

        if (num in input):
            nums_in_input.append((num, input.index(num)))
            nums_in_input.append((num, len(input)-"".join(reversed(input)).index("".join(reversed(num)))))

    num1 = nums_dict[min(nums_in_input, key=lambda x : x[1])[0]]
    num2 = nums_dict[max(nums_in_input, key=lambda x : x[1])[0]]
    answer += int(num1 + num2)
    
print(answer)
