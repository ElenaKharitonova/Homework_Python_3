# Создайте скрипт бота, который находит ответы
# на фразы по ключу в словаре. Бот должен, как минимум,
# отвечать на фразы «привет», «как тебя зовут». Если фраза
# ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

def bot(ph):
    dictionary = {'привет': 'добрый день', 'как тебя зовут': 'меня зовут Анатолий'}
    if phrase not in dictionary:
        print ('Я Вас не понимаю')
    else: 
        print (dictionary[phrase])

phrase = input (f'Напишите боту "привет" или "как тебя зовут"=> ')
bot(phrase)