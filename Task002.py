# В файле находятся названия фруктов.
# Выведите все фрукты, названия которых начинаются на
# заданную букву.
# а –> абрикос, авокадо,апельсин, айва.
data = open('Fruit.txt', encoding = 'utf-8')
data_from_file = data.readlines()
data.close()

letter = input('Введите букву:  ')
result = []
for index in range (len(data_from_file)):
    word = str(data_from_file[index])
    if word[0] == letter:
        result.append(word)
print(f'Фрукты на букву {letter}: {result}')