"""
Урок 5.1 "Повторы задач", шаг 5

Смоделируйте, чем закончится задача с `autoretry_for`.

В первой строке настройки задачи `autoretry_for=Имя1,Имя2 max_retries=N`, где N, число или `None`
(без ограничения). Во второй строке через пробел перечислены исходы запусков по порядку. `ok`
значит, задача выполнилась, иначе это имя исключения, которое она выбросила.

Если запуск успешный, задача получает `SUCCESS`. Если исключение есть в `autoretry_for` и повторов
было меньше `max_retries`, назначается повтор (`RETRY`). Иначе задача получает `FAILURE`. После
`SUCCESS` или `FAILURE` запусков больше нет, оставшиеся исходы не используются.

Для каждого запуска выведите `попытка k: исход, СОСТОЯНИЕ`. Подклассы исключений в этой задаче не
учитываются. Сравнивайте имена.

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    autoretry_for=ConnectionError,TimeoutError max_retries=2
    TimeoutError ConnectionError ok

Пример вывода:

    попытка 1: TimeoutError, RETRY
    попытка 2: ConnectionError, RETRY
    попытка 3: ok, SUCCESS
"""

# Решение
settings = dict(part.split("=") for part in input().split())
allowed = settings["autoretry_for"].split(",")
limit = None if settings["max_retries"] == "None" else int(settings["max_retries"])
outcomes = input().split()

retries = 0
for attempt, outcome in enumerate(outcomes, 1):
    if outcome == "ok":
        print(f"попытка {attempt}: ok, SUCCESS")
        break
    if outcome in allowed and (limit is None or retries < limit):
        retries += 1
        print(f"попытка {attempt}: {outcome}, RETRY")
        continue
    print(f"попытка {attempt}: {outcome}, FAILURE")
    break
