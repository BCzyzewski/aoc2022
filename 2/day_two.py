# Part one

'''
A - Rock
B - Paper
C - Scissors

X - Rock
Y - Paper
Z - Scissors

0 - Loss
3 - Draw
6 - Win
'''

import pandas as pd

usersDf = pd.read_csv('input2.csv', sep=' ' , engine='python', header=None, names = ['First', 'Second'])

def points(row):
    if row.First == 'A' and row.Second == 'X':
        return 4
    elif row.First == 'A' and row.Second == 'Y':
        return 8
    elif row.First == 'A' and row.Second == 'Z':
        return 3
    elif row.First == 'B' and row.Second == 'X':
        return 1
    elif row.First == 'B' and row.Second == 'Y':
        return 5
    elif row.First == 'B' and row.Second == 'Z':
        return 9
    elif row.First == 'C' and row.Second == 'X':
        return 7
    elif row.First == 'C' and row.Second == 'Y':
        return 2
    elif row.First == 'C' and row.Second == 'Z':
        return 6                         
    else:
        None

usersDf['Result'] = usersDf.apply(points, axis = 1)

print(usersDf['Result'].sum())


# Part two

'''
A - Rock
B - Paper
C - Scissors

X - Lose
Y - Draw
Z - Win

0 - Loss
3 - Draw
6 - Win
'''
strategy  = {
    'X' : {
        'A' : 'C',
        'B' : 'A',
        'C' : 'B'
    },
    'Y' : {
        'A' : 'A',
        'B' : 'B',
        'C' : 'C'
    },
    'Z' : {
        'A' : 'B',
        'B' : 'C',
        'C' : 'A'
    }
}

point = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}

together = {
    'X' : 0,
    'Y' : 3,
    'Z' : 6
}


def points(row):
    return point[strategy[row.Second][row.First]] + together[row.Second]



usersDf['Result'] = usersDf.apply(points, axis = 1)


print(usersDf['Result'].sum())



