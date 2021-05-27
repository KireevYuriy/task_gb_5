

def numbers_gen(right_num):
    for num in range(1, right_num + 1, 2):
        yield num


in_number = int(input('Введите число - правую границу генератора: '))
odd_num_gen = numbers_gen(in_number)
if in_number // 2 == 0:
    for i in range(in_number // 2):
        print(next(odd_num_gen))
else:
    for i in range(in_number // 2 + 1):
        print(next(odd_num_gen))
