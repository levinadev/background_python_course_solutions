"""
Урок 3.1 "Знакомство с Redis", шаг 5

Реализуйте упрощённую консоль Redis для строк и счётчиков. В первой строке число команд, дальше по
одной команде.

Команда | Ответ
`SET key value` | записать строку, ответ `OK`
`GET key` | значение в кавычках, например `"42"`, или `(nil)`
`INCR key`, `DECR key` | изменить число на +1 или -1, ответ `(integer) N`
`INCRBY key n` | изменить число на n (n может быть отрицательным), ответ `(integer) N`
`DEL key [key ...]` | удалить ключи, ответ `(integer) N`, сколько из них существовало

Отсутствующий ключ в `INCR`, `DECR` и `INCRBY` считается нулём. Если в ключе лежит не целое число,
выведите `(error) ERR value is not an integer or out of range` и не меняйте значение. Значения и
ключи не содержат пробелов.

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    4
    SET visits 10
    INCRBY visits 5
    GET visits
    DEL visits nothing

Пример вывода:

    OK
    (integer) 15
    "15"
    (integer) 1
"""

# Решение
store = {}


def as_int(value):
    try:
        return int(value)
    except ValueError:
        return None


for _ in range(int(input())):
    cmd, key, *rest = input().split()
    if cmd == "SET":
        store[key] = rest[0]
        print("OK")
    elif cmd == "GET":
        print(f'"{store[key]}"' if key in store else "(nil)")
    elif cmd == "DEL":
        keys = [key] + rest
        removed = sum(1 for k in keys if store.pop(k, None) is not None)
        print(f"(integer) {removed}")
    else:
        step = {"INCR": 1, "DECR": -1}.get(cmd) or int(rest[0])
        current = as_int(store.get(key, "0"))
        if current is None:
            print("(error) ERR value is not an integer or out of range")
        else:
            store[key] = str(current + step)
            print(f"(integer) {current + step}")
