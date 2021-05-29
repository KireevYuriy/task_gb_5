import sys
from time import perf_counter


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = perf_counter()
num_count = [el for el in src if src.count(el) == 1]
print(f'{num_count}\n{perf_counter() - start} - время обработки count\n{sys.getsizeof(num_count)} - выделяемая память')

start = perf_counter()
num_set = set()
tmp = set()
for el in src:
    if el not in tmp:
        num_set.add(el)
    else:
        num_set.discard(el)
    tmp.add(el)
num_sequence = [el for el in src if el in num_set]
print(f'\n{num_sequence}\n{perf_counter() - start} - время обработки set\n{sys.getsizeof(num_sequence)}'
      f' - выделяемая память')
