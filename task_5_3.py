
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def gen_of_school(names, name_class):
    """Генератор кортежей вида (<tutor>, <klass>)"""
    counter_klass = 0
    counter_name = 0
    while counter_klass < len(name_class):
        if counter_klass >= len(names):
            yield None, name_class[counter_klass]
            counter_klass += 1
            counter_name += 1
            break
        else:
            yield names[counter_name], name_class[counter_klass]
            counter_klass += 1
            counter_name += 1


for gen in gen_of_school(tutors, klasses):
    print(gen, type(gen))
