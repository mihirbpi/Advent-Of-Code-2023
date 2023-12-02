from aocd import get_data
data = get_data(year=2023, day=1)
inputs = data.split("\n")

num_words = {"one" : "1", "two": "2", "three": "3", "four" : "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

answer = 0

for input in inputs:
    number = ""
    nums_in_input = []

    for num in (list(num_words.keys()) + list(num_words.values())):

        if (num in input):
            nums_in_input.append((num, input.index(num)))
            nums_in_input.append((num, len(input)-"".join(reversed(input)).index("".join(reversed(num)))))

    num1 = min(nums_in_input, key=lambda x : x[1])[0]
    num2 = max(nums_in_input, key=lambda x : x[1])[0]

    if (num1 in num_words):
        num1 = num_words[num1]
    
    if (num2 in num_words):
        num2 = num_words[num2]

    answer += int(num1 + num2)
    
print(answer)
