import collections

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
    Scientist(name='Vera Rubin', field='chemistry', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False)
)

# filter scientists who have nobel
fs = filter(lambda x: x.nobel is True, scientists)

# filter scientists who have nobel and field is math
fs = filter(lambda x: x.nobel is True and x.field == 'math', scientists)

# iter through results (for Python 3)
next(fs)

# storing the results
results = tuple(filter(lambda x: x.nobel is True, scientists))

# declaring a function to work with the filter()
def nobel_filter(x):
    return x.nobel is True

results = tuple(filter(nobel_filter, scientists))

# what about a more pythonic way?
[x for x in scientists if x.nobel is True]

# even as a tuple
pprint(tuple(x for x in scientists if x.nobel is True))