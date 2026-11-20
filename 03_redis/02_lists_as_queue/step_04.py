"""
Урок 3.2 "Списки как очередь", шаг 4

Реализуйте списки Redis. В первой строке число команд, дальше по одной команде.

Команда | Ответ
`LPUSH key v1 v2 ...` | добавить значения по одному в начало списка, ответ `(integer) N`, это новая
длина
`RPUSH key v1 v2 ...` | добавить значения в конец, ответ это новая длина
`LPOP key`, `RPOP key` | забрать элемент из начала или конца и вывести его в кавычках; `(nil)`, если
список пуст
`LLEN key` | `(integer) N`
`LRANGE key start stop` | элементы с позиции start по stop включительно, каждый строкой `i)
"значение"` с нумерацией от 1; `(empty array)`, если элементов нет

Индексы в `LRANGE` считаются от 0. Отрицательный индекс отсчитывается с конца, -1 это последний
элемент. Если start меньше начала списка, он считается равным 0; если stop больше последнего
индекса, равным последнему индексу.

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    4
    LPUSH tasks a b c
    LRANGE tasks 0 -1
    RPOP tasks
    LLEN tasks

Пример вывода:

    (integer) 3
    1) "c"
    2) "b"
    3) "a"
    "a"
    (integer) 2
"""

# Решение
lists = {}
for _ in range(int(input())):
    cmd, key, *args = input().split()
    items = lists.setdefault(key, [])
    if cmd == "LPUSH":
        for value in args:
            items.insert(0, value)
        print(f"(integer) {len(items)}")
    elif cmd == "RPUSH":
        items.extend(args)
        print(f"(integer) {len(items)}")
    elif cmd in ("LPOP", "RPOP"):
        if not items:
            print("(nil)")
        else:
            print(f'"{items.pop(0) if cmd == "LPOP" else items.pop()}"')
    elif cmd == "LLEN":
        print(f"(integer) {len(items)}")
    else:
        n = len(items)
        start, stop = int(args[0]), int(args[1])
        if start < 0:
            start = max(n + start, 0)
        if stop < 0:
            stop = n + stop
        part = items[start:stop + 1] if stop >= start else []
        if not part:
            print("(empty array)")
        for i, value in enumerate(part, 1):
            print(f'{i}) "{value}"')
