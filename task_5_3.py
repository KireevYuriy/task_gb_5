
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Евгений', 'Игорь']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) > len(klasses):
    for i in range(len(tutors) - len(klasses)):
        klasses.append(None)
school_list = ((name, klass) for name, klass in zip(tutors, klasses))
print(*school_list, '\n', type(school_list))
