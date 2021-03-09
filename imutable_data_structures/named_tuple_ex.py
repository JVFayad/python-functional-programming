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

ada = Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False)

# can't do this
ada.name = 'any'