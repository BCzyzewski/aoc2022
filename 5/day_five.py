import pandas as pd

df = pd.read_fwf('5/containers.txt', header = None).iloc[:-1,:]
df.columns = list(range(1,10))


all_dict = {}

for column in df.columns:

    selected_column = list(df[column])
    filtered_column = list(filter(lambda a: str(a) != 'nan', selected_column))
    all_dict[column] = filtered_column


def parse_instructions(instruction: str):
    v1, amount, from_str, from_cont, to_str, to_cont =  instruction.split(" ")
    return int(amount), int(from_cont), int(to_cont)

def move_container(values: dict, amount: int, from_cont: int, to_cont: int):
   for container in range(1, amount + 1):
        to_insert = values[from_cont].pop(0)
        values[to_cont].insert(0, to_insert)


with open('5//instructions.txt') as file:
    inst = file.read().split('\n')

for ins in inst:
    amount, from_cont, to_cont = parse_instructions(ins)

    move_container(all_dict, amount, from_cont, to_cont)

# Part Two

all_dict = {}

for column in df.columns:

    selected_column = list(df[column])
    filtered_column = list(filter(lambda a: str(a) != 'nan', selected_column))
    all_dict[column] = filtered_column


def move_container(values: dict, amount: int, from_cont: int, to_cont: int):
    to_insert = values[from_cont][0:amount]
    del values[from_cont][0:amount]
    to_insert.extend(values[to_cont])
    values[to_cont] = to_insert


for ins in inst:
    amount, from_cont, to_cont = parse_instructions(ins)

    move_container(all_dict, amount, from_cont, to_cont)

print(all_dict)