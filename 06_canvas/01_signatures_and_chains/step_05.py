"""
Урок 6.1 "Сигнатуры и цепочки", шаг 5

Смоделируйте выполнение цепочки задач.

Доступные задачи `add(x, y)` это сумма, `mul(x, y)` это произведение, `sub(x, y)` это разность `x -
y`, `neg(x)` это смена знака, `div(x, y)` это целочисленное деление `x // y`.

В первой строке первая задача и все её аргументы, например `add 2 3`. Дальше до конца ввода идут
сигнатуры `s имя аргументы` (результат предыдущей задачи встаёт первым аргументом) или `si имя
аргументы` (результат игнорируется). У `s neg` аргументов нет.

Для каждой выполненной задачи выведите `шаг k: имя(аргументы) = результат`, где аргументы записаны
как кортеж Python, например `sub(5, 10)`, а для одного аргумента `neg(5,)`. Если задача делит на
ноль, выведите `шаг k: имя(аргументы), ZeroDivisionError` и остановитесь. Если вся цепочка
выполнилась, в конце выведите `результат цепочки: R`.

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    add 2 3
    s mul 10
    s sub 8

Пример вывода:

    шаг 1: add(2, 3) = 5
    шаг 2: mul(5, 10) = 50
    шаг 3: sub(50, 8) = 42
    результат цепочки: 42
"""

# Решение
OPS = {
    "add": lambda x, y: x + y,
    "mul": lambda x, y: x * y,
    "sub": lambda x, y: x - y,
    "neg": lambda x: -x,
    "div": lambda x, y: x // y,
}


def call(step, name, args):
    try:
        value = OPS[name](*args)
    except ZeroDivisionError:
        print(f"шаг {step}: {name}{tuple(args)}, ZeroDivisionError")
        return None
    print(f"шаг {step}: {name}{tuple(args)} = {value}")
    return value


name, *args = input().split()
result = call(1, name, [int(a) for a in args])
step = 1
while result is not None:
    try:
        kind, name, *args = input().split()
    except EOFError:
        print(f"результат цепочки: {result}")
        break
    step += 1
    args = [int(a) for a in args]
    if kind == "s":
        args = [result] + args
    result = call(step, name, args)
