# В файле находятся названия фруктов.
# Выведите все фрукты, названия которых начинаются на
# заданную букву.
# а –> абрикос, авокадо,апельсин, айва.

def printLettersFruit(let, numbers):
    result = []
    for index in range (len(numbers)):
        word = str(numbers[index])
        if word[0] == let:
            result.append(word)
    print(f'Фрукты на букву {let}: {result}')  

data = open('Fruit.txt', encoding = 'utf-8')
data_from_file = data.readlines()
data.close()

letter = input('Введите букву:  ')
printLettersFruit(letter, data_from_file)