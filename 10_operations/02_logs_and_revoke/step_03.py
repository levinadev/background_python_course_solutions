"""
Урок 10.2 "Логи и отмена задач", шаг 3

Соберите сводку по логу воркера Celery.

До конца ввода идут строки лога. Нужны строки трёх видов (остальные пропускаются).

- `Task имя[id] succeeded in 0.0026s: результат`, задача выполнена за указанное время;
- `Task имя[id] retry: ...`, назначен повтор;
- `Task имя[id] raised unexpected: ...`, задача упала.

Для каждого имени задачи в алфавитном порядке выведите `имя: успешно N, повторов N, ошибок N,
среднее время T с`, где T это среднее время успешных выполнений с тремя знаками после запятой. Если
успешных выполнений не было, вместо `T с` выведите `-`.

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    [2026-10-16 00:12:16,637: INFO/MainProcess] Task reports.tasks.notify[8afbea2e] received
    [2026-10-16 00:12:16,641: INFO/ForkPoolWorker-4] Task reports.tasks.notify[8afbea2e] succeeded in 0.0026s: 'sent'
    [2026-10-16 00:12:51,005: INFO/ForkPoolWorker-4] Task reports.tasks.fetch_rates[1c2d3e4f] retry: Retry in 3s: RatesUnavailable('сервис курсов валют не ответил')
    [2026-10-16 00:12:59,005: INFO/ForkPoolWorker-1] Task reports.tasks.fetch_rates[1c2d3e4f] succeeded in 0.5s: {'RUB': 1.0}
    [2026-10-16 00:13:10,000: ERROR/ForkPoolWorker-2] Task reports.tasks.build_report[77aa0011] raised unexpected: KeyError('USD')

Пример вывода:

    reports.tasks.build_report: успешно 0, повторов 0, ошибок 1, среднее время -
    reports.tasks.fetch_rates: успешно 1, повторов 1, ошибок 0, среднее время 0.500 с
    reports.tasks.notify: успешно 1, повторов 0, ошибок 0, среднее время 0.003 с
"""

# Решение
import re

pattern = re.compile(r"Task (\S+)\[[^\]]+\] (succeeded in ([\d.]+)s|retry:|raised unexpected:)")
stats = {}
while True:
    try:
        line = input()
    except EOFError:
        break
    match = pattern.search(line)
    if not match:
        continue
    name, event, runtime = match.groups()
    item = stats.setdefault(name, {"ok": 0, "retry": 0, "fail": 0, "time": 0.0})
    if runtime is not None:
        item["ok"] += 1
        item["time"] += float(runtime)
    elif event == "retry:":
        item["retry"] += 1
    else:
        item["fail"] += 1

for name in sorted(stats):
    item = stats[name]
    average = f"{item['time'] / item['ok']:.3f} с" if item["ok"] else "-"
    print(f"{name}: успешно {item['ok']}, повторов {item['retry']}, ошибок {item['fail']}, среднее время {average}")
