import pandas as pd
import itertools


tasks = pd.read_csv('4/input_tasks.csv', header=None, names = ['one', 'two'])


def split_columns(row):
    return [list(map(int, [row.one.split("-")[0], row.one.split("-")[1]])), list(map(int, [row.two.split("-")[0], row.two.split("-")[1]]))]

def check_if_contains(row):
    first_value, second_value, third_value, forth_value = list(itertools.chain(*split_columns(row)))

    if first_value >= third_value and second_value <= forth_value: 
        return True
    elif third_value >= first_value and forth_value <= second_value:
        return True     
    else:
        return False

print(tasks.apply(check_if_contains, axis = 1).sum())

# Part Two

def check_if_contains(row):
    first_value, second_value, third_value, forth_value = list(itertools.chain(*split_columns(row)))

    first_range = set(range(first_value, second_value + 1))

    second_range = set(range(third_value, forth_value + 1))

    interlude = first_range.intersection(second_range)

    return True if interlude else False

print(tasks.apply(check_if_contains, axis = 1).sum())