from aocd import get_data
data = get_data(year=2023, day=1)
inputs = data.split("\n")

answer = 0

for input in inputs:
    number = ""

    for i in range(len(input)):

        if(input[i] in "0123456789"):
            number += input[i]
            break

    for i in range(len(input)-1,-1,-1):

        if(input[i] in "0123456789"):
            number += input[i]
            break

    answer += int(number)

print(answer)
