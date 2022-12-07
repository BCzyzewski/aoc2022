with open('6/input-file.txt') as file:
    string_to_parse = file.read()



for index, letter in enumerate(string_to_parse):
    if index <= 3:
        continue

    if len(set(string_to_parse[index - 4: index])) != 4:
        continue
    else:
        print(index)
        break

# Part two

for index, letter in enumerate(string_to_parse):
    if index <= 13:
        continue

    if len(set(string_to_parse[index - 14: index])) != 14:
        continue
    else:
        print(index)
        break


