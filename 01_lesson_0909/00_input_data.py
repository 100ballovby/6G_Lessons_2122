'''
функция input() позволяет ввести
что-то с клавиатуры и сохранить в переменную.
По умолчанию input вернет СТРОКУ
'''
age = int( input('Сколько тебе лет? ') )
# обернув input в int, я буду получать только числа
print(age + 7)
