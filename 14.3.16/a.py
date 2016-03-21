import sys

sys.stdin = open('ex.in', 'r')
sys.stdout = open('ex.out', 'w')
a, b = map(int, input().split())
d = int(input())

print(a + b, b)
print(a)
print(d)
# http://pythontutor.ru/
# справка по  языку
print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # две звёздочки означают возведение в степень
print(37 / 3)  # один слэш — это деление с ответом-дробью
print(37 // 3)  # два слэша считают частное от деления нацело
# это как операция div в других языках
print(37 % 3)  # процент считает остаток от деления нацело
# это как операция mod в других языках
print('Как вас зовут?')
name = input()  # считываем строку и кладём её в переменную name
print('Здравствуйте, ' + name + '!')

first = 5
second = 7
print(first * second)
first = '5'
second = '7'
print(first * second)

a = int(input())
b = int(input())
s = a + b
print(s)

# условия по языку
x = int(input())
if x > 0:
    print(x)
else:
    print(-x)

# if Условие:
#    Блок инструкций 1
# else:
#    Блок инструкций 2

x = int(input())
if x < 0:
    x = -x
print(x)

print(17 / 3)  # выведет 5.66666666667
print(17 // 3)  # выведет 5
print(17 % 3)  # выведет 2

x = float(input())
print(x)
"""
Некоторые из перечисленных функций (int, round, abs) являются стандартными и не требуют подключения модуля math для использования.
Функция 	Описание
Округление
int(x) 	Округляет число в сторону нуля. Это стандартная функция, для ее использования не нужно подключать модуль math.
round(x) 	Округляет число до ближайшего целого. Если дробная часть числа равна 0.5, то число округляется до ближайшего четного числа.
round(x, n) 	Округляет число x до n знаков после точки. Это стандартная функция, для ее использования не нужно подключать модуль math.
floor(x) 	Округляет число вниз («пол»), при этом floor(1.5) == 1, floor(-1.5) == -2
ceil(x) 	Округляет число вверх («потолок»), при этом ceil(1.5) == 2, ceil(-1.5) == -1
abs(x) 	Модуль (абсолютная величина). Это — стандартная функция.
Корни, логарифмы
sqrt(x) 	Квадратный корень. Использование: sqrt(x)
log(x) 	Натуральный логарифм. При вызове в виде log(x, b) возвращает логарифм по основанию b.
e 	Основание натуральных логарифмов e = 2,71828...
Тригонометрия
sin(x) 	Синус угла, задаваемого в радианах
cos(x) 	Косинус угла, задаваемого в радианах
tan(x) 	Тангенс угла, задаваемого в радианах
asin(x) 	Арксинус, возвращает значение в радианах
acos(x) 	Арккосинус, возвращает значение в радианах
atan(x) 	Арктангенс, возвращает значение в радианах
atan2(y, x) 	Полярный угол (в радианах) точки с координатами (x, y).
degrees(x) 	Преобразует угол, заданный в радианах, в градусы.
radians(x) 	Преобразует угол, заданный в градусах, в радианы.
pi 	Константа π = 3.1415...
"""
i = 1
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
    print('#', i, ' color of rainbow is ', color, sep='')
    i += 1

for i in 1, 2, 3, 'one', 'two', 'three':
    print(i)

for i in range(4):  # равносильно инструкции for i in 0, 1, 2, 3:
    # здесь можно выполнять циклические действия
    print(i)
    print(i ** 2)
# цикл закончился, поскольку закончился блок с отступом
print('Конец цикла')

sum = 0
n = 5
for i in range(1, n + 1):
    sum += i
print(sum)

s = input()
print(len(s))
t = input()
number = int(t)
u = str(number)
print(s * 3)
print(s + ' ' + u)
# строки
s = 'abcdefg'
print(s[1])
print(s[-1])
print(s[1:3])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])

# поиск с одной
S = 'Hello'
print(S.find('e'))
# вернёт 1
print(S.find('ll'))
# вернёт 2
print(S.find('L'))
# вернёт -1

# и с другой
S = 'Hello'
print(S.find('l'))
# вернёт 2
print(S.rfind('l'))
# вернёт 3

print('Hello'.replace('l', 'L'))
# вернёт 'HeLLo'

print('Abrakadabra'.replace('a', 'A', 2))
# вернёт 'AbrAkAdabra'

print('Abracadabra'.count('a'))
# вернёт 4
print(('a' * 10).count('aa'))
# вернёт 5
"""
while условие:
    блок инструкций
    """
i = 1
while i <= 10:
    print(i ** 2)
    i += 1

n = int(input())
length = 0
while n > 0:
    n //= 10  # это эквивалентно n = n // 10
    length += 1
print(length)

i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Цикл окончен, i =', i)

a = int(input())
while a != 0:
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
    a = int(input())
else:
    print('Ни одного отрицательного числа не встретилось')

n = int(input())
for i in range(n):
    a = int(input())
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
else:
    print('Ни одного отрицательного числа не встретилось')

a = []  # заводим пустой список
n = int(input())  # считываем количество элемент в списке
for i in range(n):
    new_element = int(input())  # считываем очередной элемент
    a.append(new_element)  # добавляем его в список
    # последние две строки можно было заменить одной:
    # a.append(int(input()))
print(a)

a = [0] * int(input())
for i in range(len(a)):
    a[i] = int(input())

# дано: s = 'ab12c59p7dq'
# надо: извлечь цифры в список digits,
# чтобы стало так:
# digits == [1, 2, 5, 9, 7]

s = 'ab12c59p7dq'
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)

# на вход подаётся строка
# 1 2 3
s = input()  # s == '1 2 3'
a = s.split()  # a == ['1', '2', '3']

a = [int(s) for s in input().split()]

a = ['red', 'green', 'blue']
print(' '.join(a))
# вернёт red green blue
print(''.join(a))
# вернёт redgreenblue
print('***'.join(a))
# вернёт red***green***blue

# [выражение for переменная in последовательность]

from random import randrange

n = 10
a = [randrange(1, 10) for i in range(n)]

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()

A = {1, 2, 3}
A = set('qwerty')
print(A)
# выведет {'e', 'q', 'r', 't', 'w', 'y'}.

primes = {2, 3, 5, 7, 11}
for num in primes:
    print(num)

A = {1, 2, 3}
print(1 in A, 4 not in A)
A.add(4)

"""
 A | B
A.union(B)

Возвращает множество, являющееся объединением множеств A и B.
A |= B
A.update(B)

Добавляет в множество A все элементы из множества B.
A & B
A.intersection(B)

Возвращает множество, являющееся пересечением множеств A и B.
A &= B
A.intersection_update(B)

Оставляет в множестве A только те элементы, которые есть в множестве B.
A - B
A.difference(B)

Возвращает разность множеств A и B (элементы, входящие в A, но не входящие в B).
A -= B
A.difference_update(B)

Удаляет из множества A все элементы, входящие в B.
A ^ B
A.symmetric_difference(B)

Возвращает симметрическую разность множеств A и B (элементы, входящие в A или в B, но не в оба из них одновременно).
A ^= B
A.symmetric_difference_update(B)

Записывает в A симметрическую разность множеств A и B.
A <= B
A.issubset(B)

Возвращает true, если A является подмножеством B.
A >= B
A.issuperset(B)

Возвращает true, если B является подмножеством A.
A < B

Эквивалентно A <= B and A != B
A > B

Эквивалентно A >= B and A != B

"""
