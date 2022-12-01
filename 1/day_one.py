# AOC Day 1

with open('input.txt') as file:
    values = file.read()

data = values[:-1].split("\n\n")

data_new = [x.split("\n") for x in data]

data_next = [list(map(int, x)) for x in data_new]

all_calories = []

for calories in data_next:
    all_calories.append(sum(calories))

# Part One response
print(max(all_calories))


# Part Two

print(sum(sorted(all_calories, reverse=True)[:3]))

