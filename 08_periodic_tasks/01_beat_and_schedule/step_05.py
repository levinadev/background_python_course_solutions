"""
Урок 8.1 "Celery beat и расписание", шаг 5

Определите, срабатывает ли расписание `crontab` в заданные моменты.

В первой строке через пробел три поля `minute` (0-59), `hour` (0-23) и `day_of_week` (0-6, где 0 это
воскресенье). Каждое поле это `*`, число, диапазон `a-b`, шаг `*/n` или `a-b/n` либо список таких
записей через запятую. Дальше до конца ввода идут моменты в формате `ГГГГ-ММ-ДД ЧЧ:ММ`.

Для каждого момента выведите его и через пробел `да` или `нет`. День недели даты удобно получить
через `isoweekday() % 7`. Так воскресенье станет нулём.

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    0 3 *
    2026-10-16 03:00
    2026-10-16 03:01
    2026-10-17 04:00

Пример вывода:

    2026-10-16 03:00 да
    2026-10-16 03:01 нет
    2026-10-17 04:00 нет
"""

# Решение
from datetime import datetime


def expand(field, lo, hi):
    values = set()
    for part in field.split(","):
        step = 1
        if "/" in part:
            part, step = part.split("/")
            step = int(step)
        if part == "*":
            start, end = lo, hi
        elif "-" in part:
            start, end = map(int, part.split("-"))
        else:
            start = end = int(part)
        values.update(range(start, end + 1, step))
    return values


minute, hour, day_of_week = input().split()
minutes, hours, days = expand(minute, 0, 59), expand(hour, 0, 23), expand(day_of_week, 0, 6)
while True:
    try:
        line = input()
    except EOFError:
        break
    moment = datetime.strptime(line, "%Y-%m-%d %H:%M")
    fires = moment.minute in minutes and moment.hour in hours and moment.isoweekday() % 7 in days
    print(f"{line} {'да' if fires else 'нет'}")
