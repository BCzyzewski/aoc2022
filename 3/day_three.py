import string


with open('input_next.csv') as file:
    system = file.read()

new_list = system.split("\n")[:-1]

all_common = []

score = dict(zip(list(string.ascii_lowercase), range(1,27)))
score.update(dict(zip(list(string.ascii_uppercase), range(27,53))))

for element in new_list:
    new_list_a, new_list_b = element[:len(element) // 2], element[len(element) // 2:]
    common = list(set([x for x in new_list_a if x in new_list_b]))
    all_common.append(score[common[0]])


print(sum(all_common))


# Part two

parts_of_three = []

all_common = []

for i in range(len(new_list) // 3):
    parts_of_three.append(new_list[i * 3: (i + 1) * 3])

    common = list(set.intersection(*map(set, parts_of_three[i])))

    all_common.append(score[common[0]])

print(sum(all_common))