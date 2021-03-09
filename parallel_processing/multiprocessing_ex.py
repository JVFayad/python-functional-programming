import collections
import multiprocessing
import os
import time

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

def transform(x):
    print(f'Process {os.getpid()} working record {x.name}')
    time.sleep(1)
    result = {'name': x.name, 'age': 2021 - x.born}
    print(f'Process {os.getpid()} done working record {x.name}')
    return result

start_time = time.time()

# use multiprocessing Pool to use more CPU cores, pass as a parameter:
# - processors number: Pool(processes=2)
# - max tasks per processor: Pool(maxtasksperchild=2)
pool = multiprocessing.Pool()
results = pool.map(transform, scientists)
end_time = time.time()

print(f'\nTime to complete: {end_time - start_time:.2f}')
pprint(results)