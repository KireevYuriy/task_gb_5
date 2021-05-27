from itertools import islice


right_num = int(input('Введите число - правую границу генератора: '))
odd_numbers = (num for num in range(1, right_num + 1, 2))
print(*islice(odd_numbers, right_num // 2 + 1))
