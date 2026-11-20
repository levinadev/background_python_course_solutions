"""
Урок 7.1 "Очереди и маршрутизация", шаг 4

Определите, в какую очередь Celery отправит каждую задачу.

В первой строке очередь по умолчанию. Во второй число правил, дальше правила по одному в строке,
шаблон и очередь. Шаблон без `*` это точное имя задачи, со `*` это маска, где `*` означает любую
последовательность символов, в том числе пустую и с точками. После правил до конца ввода идут имена
задач.

Точные имена проверяются первыми, затем маски в порядке записи, иначе очередь по умолчанию. Для
каждой задачи выведите `имя: очередь`. Подойдёт `fnmatch.fnmatchcase`.

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    celery
    2
    shop.* shop
    shop.tasks.send_email mail
    shop.tasks.send_email
    shop.tasks.charge
    billing.tasks.charge

Пример вывода:

    shop.tasks.send_email: mail
    shop.tasks.charge: shop
    billing.tasks.charge: celery
"""

# Решение
from fnmatch import fnmatchcase

default = input()
exact, patterns = {}, []
for _ in range(int(input())):
    rule, queue = input().split()
    if "*" in rule:
        patterns.append((rule, queue))
    else:
        exact[rule] = queue

while True:
    try:
        name = input()
    except EOFError:
        break
    queue = exact.get(name)
    if queue is None:
        queue = next((q for rule, q in patterns if fnmatchcase(name, rule)), default)
    print(f"{name}: {queue}")
