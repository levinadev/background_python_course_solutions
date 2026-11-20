"""
Урок 7.3 "Предвыборка, частота и приоритеты", шаг 4

Определите порядок, в котором воркер возьмёт сообщения из очереди Redis с
`queue_order_strategy=priority`.

До конца ввода идут сообщения в порядке отправки, имя и приоритет от 0 до 9 или `-`, если приоритет
не указан. Приоритет округляется вниз до ступени 0, 3, 6 или 9; сообщение без приоритета попадает на
ступень 0. Сначала берутся все сообщения ступени 0, потом 3, 6 и 9, внутри ступени в порядке
отправки.

Выведите имена в порядке выполнения через пробел.

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    p9a 9
    p0a 0
    p5 5
    p2 2
    p9b 9
    p0b 0
    none -

Пример вывода:

    p0a p2 p0b none p5 p9a p9b
"""

# Решение
steps = [0, 3, 6, 9]
buckets = {step: [] for step in steps}
while True:
    try:
        name, priority = input().split()
    except EOFError:
        break
    value = 0 if priority == "-" else int(priority)
    step = max(s for s in steps if s <= value)
    buckets[step].append(name)
order = [name for step in steps for name in buckets[step]]
print(" ".join(order))
