
# 2. Напишите программу, которая получает целое число 
# и возвращает его шестнадцатеричное строковое представление. Функцию 
# hex используйте для проверки своего результата.
# HEX: int = 16
# number = int(input('Введите число:= '))
# print(f'Проверка через хекс:= {hex(number)}')

# if number == 0:
#     result = 'Мне кажется ты вводишь ноль'
# else:
#     result: str = ''
#     while number > 0:
#         result = '0123456789ABCDEF'[number % HEX] + result
#         number //= HEX
# print(f' Результат = {result}')

# 3. Напишите программу, которая принимает две строки вида “a/b” 
# - дробь с числителем и знаменателем. Программа должна 
# возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions

import fractions

drob_a_1 = str
drob_a_2 = str
drob_b_1 = str
drob_b_2 = str
drob_input_1 = input('Введите первую дробь в виде a/b допустим 5/6:= ')
drob_input_2 = input('Введите вторую дробь в виде a/b допустим 3/8:= ')
drob_a_1 = int(drob_input_1[0])
drob_a_2 = drob_a_2_2 = int(drob_input_1[2])
drob_b_1 = int(drob_input_2[0])
drob_b_2 = int(drob_input_2[2])
if drob_a_2 != drob_b_2:
    drob_a_1 *= drob_b_2
    drob_a_2 *= drob_b_2
    drob_b_1 *= drob_a_2_2
    drob_b_2 *= drob_a_2_2
    print("Сумма дробей равна: ", drob_a_1 + drob_b_1,"/", drob_a_2)
else:
    print("Сумма дробей равна: ", drob_a_1 + drob_b_1,"/", drob_a_2)
print("Произведение дробей равно: ", drob_a_1 * drob_b_1,"/", drob_a_2 * drob_b_2)
drob_input_1 = fractions.Fraction(drob_a_1, drob_a_2)
drob_input_2 = fractions.Fraction(drob_b_1, drob_b_2)
print("Произведение дробей равно: ", drob_input_1 * drob_input_2)
print("Cумма дробей равна: ", drob_input_1 + drob_input_2)
