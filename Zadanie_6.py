# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,

# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
#

from itertools import count

for el in count(10):
    if el > 25:
        break
    else:
        print(el)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import cycle

i = 0
for el in cycle("123354567"):
    if i > 50:
        break
    print(el)
    i += 1
