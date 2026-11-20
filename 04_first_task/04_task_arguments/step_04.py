"""
Урок 4.4 "Что можно передавать в задачу", шаг 4

Смоделируйте, что получит задача, если передать ей значение через JSON-сериализатор Celery.

На вход подаётся одна строка, значение в записи Python. В нём числа, строки, `True`, `False`,
`None`, `bytes`, списки, кортежи, словари и множества, в том числе вложенные. Прочитать его можно
функцией `ast.literal_eval`.

Правила преобразования.

- кортеж становится списком;
- ключи словаря становятся строками. Число становится своей записью (`1` даёт `'1'`), `True` даёт
`'true'`, `False` даёт `'false'`, `None` даёт `'null'`;
- множество не сериализуется;
- остальное, включая `bytes`, передаётся без изменений.

Если в значении есть множество, выведите `EncodeError`. Если задача получит ровно то же самое,
выведите `без изменений`. Иначе выведите `задача получит: ` и результат в записи Python (`repr`).

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    (1, 2)

Пример вывода:

    задача получит: [1, 2]
"""

# Решение
import ast


class NotSerializable(Exception):
    pass


def key(k):
    if isinstance(k, str):
        return k
    if k is True:
        return "true"
    if k is False:
        return "false"
    if k is None:
        return "null"
    if isinstance(k, (int, float)):
        return repr(k)
    raise NotSerializable


def convert(value):
    if isinstance(value, (set, frozenset)):
        raise NotSerializable
    if isinstance(value, (list, tuple)):
        return [convert(v) for v in value]
    if isinstance(value, dict):
        return {key(k): convert(v) for k, v in value.items()}
    return value


original = ast.literal_eval(input())
try:
    received = convert(original)
except NotSerializable:
    print("EncodeError")
else:
    if repr(received) == repr(original):
        print("без изменений")
    else:
        print(f"задача получит: {received!r}")
