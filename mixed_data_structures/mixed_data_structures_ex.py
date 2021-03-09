import collections

Scientist = collections.namedtuple(
    'Scientist',
    [
        'name',
        'field',
        'born',
        'nobel'
    ]
)

scientists = [
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False)
]

# can't do this
scientists[0].name = 'any'

# but can do this
del scientists[0]