import collections
import itertools

from functools import reduce
from pprint import pprint


Scientist = collections.namedtuple(
    'Scientist',
    [
        'name',
        'field',
        'born',
        'nobel'
    ]
)

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie ', field='math', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='physics', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False)
)

names_and_ages = tuple(
    {'name': x.name, 'age': 2021 - x.born}
    for x in scientists
)

# use reduce function to accumulate the value of a sum of numbers
total_age = reduce(
    lambda acc, val: acc + val['age'],
    names_and_ages,
    0
)

print(total_age)

# what about a more pythonic way?
print(sum([x['age'] for x in names_and_ages]))

# Reuniting scientists from each field using reduce
def reducer(acc, val):
    acc[val.field].append(val.name)
    
    return acc

scientists_by_field = reduce(
    reducer,
    scientists,
    {'math': [], 'physics': [], 'chemistry': [], 'astronomy': []}
)

print('\n')
pprint(scientists_by_field)

# Doing it another way with collections defaultdict
scientists_by_field = reduce(
    reducer,
    scientists,
    collections.defaultdict(list)
)

print('\n')
pprint(scientists_by_field)

# Doing it another way with itertools groupby
scientists_by_field = {
    item[0]: list(item[1])
    for item in itertools.groupby(scientists, lambda x: x.field)
}

print('\n')
pprint(scientists_by_field)