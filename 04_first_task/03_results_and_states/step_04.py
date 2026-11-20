"""
Урок 4.3 "Результаты и состояния", шаг 4

Смоделируйте, какое состояние задачи покажет `AsyncResult(id).state`.

В первой строке настройка `track_started=on` или `track_started=off`. Дальше до конца ввода идут
события, по одному в строке, в формате "событие id".

Событие | Что произошло | Что записывается в хранилище
`send` | задача отправлена | ничего
`start` | воркер начал выполнение | `STARTED`, только если track_started=on
`retry` | задача упала, назначен повтор | `RETRY`
`ok`, `fail` | задача завершилась | `SUCCESS` или `FAILURE`
`revoke` | задача отменена | `REVOKED`
`expire` | истёк срок хранения результата | запись о задаче удаляется
`state` | запрос состояния | не меняется

На каждое событие `state` выведите строку `id: СОСТОЯНИЕ`. Если записи о задаче нет, состояние
`PENDING`.

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    track_started=off
    send a1
    state a1
    start a1
    state a1
    ok a1
    state a1

Пример вывода:

    a1: PENDING
    a1: PENDING
    a1: SUCCESS
"""

# Решение
track = input().split("=")[1] == "on"
stored = {}
while True:
    try:
        event, task_id = input().split()
    except EOFError:
        break
    if event == "state":
        print(f"{task_id}: {stored.get(task_id, 'PENDING')}")
    elif event == "start" and track:
        stored[task_id] = "STARTED"
    elif event in ("retry", "ok", "fail", "revoke"):
        stored[task_id] = {"retry": "RETRY", "ok": "SUCCESS", "fail": "FAILURE", "revoke": "REVOKED"}[event]
    elif event == "expire":
        stored.pop(task_id, None)
