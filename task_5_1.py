
def numbers_gen(right_num):
    """Функция-генератор нечетных чисел от 1 до right_num"""
    for num in range(1, right_num + 1, 2):
        yield num


in_number = int(input('Введите число - правую границу генератора: '))
odd_num_gen = numbers_gen(in_number)
for i in range(1, in_number + 1, 2):
    print(next(odd_num_gen))
