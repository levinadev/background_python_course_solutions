"""
Урок 9.2 "Django и транзакции", шаг 4

Смоделируйте, найдёт ли задача запись в базе. Воркер в модели берёт задачу мгновенно, а запись видна
ему, только если зафиксирована.

До конца ввода идут команды.

Команда | Что происходит
`begin` | начинается транзакция
`insert N` | создаётся запись N, в транзакции до фиксации невидимая для воркера, вне транзакции
сразу зафиксированная
`delay N` | задача для записи N отправляется сразу и сразу выполняется
`on_commit N` | в транзакции задача откладывается до фиксации, вне транзакции отправляется сразу
`commit` | записи транзакции фиксируются, затем по порядку выполняются отложенные задачи
`rollback` | записи и отложенные задачи транзакции отбрасываются

Для каждой выполненной задачи выведите `задача N: запись найдена` или `задача N: запись не найдена`,
а для каждой отброшенной при откате `задача N: не отправлена`.

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    begin
    insert 1
    delay 1
    commit
    delay 1

Пример вывода:

    задача 1: запись не найдена
    задача 1: запись найдена
"""

# Решение
committed = set()
pending_rows = []
pending_tasks = []
in_transaction = False


def run(task_id):
    print(f"задача {task_id}: {'запись найдена' if task_id in committed else 'запись не найдена'}")


while True:
    try:
        command, *arg = input().split()
    except EOFError:
        break
    if command == "begin":
        in_transaction = True
    elif command == "insert":
        if in_transaction:
            pending_rows.append(int(arg[0]))
        else:
            committed.add(int(arg[0]))
    elif command == "delay":
        run(int(arg[0]))
    elif command == "on_commit":
        if in_transaction:
            pending_tasks.append(int(arg[0]))
        else:
            run(int(arg[0]))
    elif command == "commit":
        committed.update(pending_rows)
        for task_id in pending_tasks:
            run(task_id)
        pending_rows, pending_tasks, in_transaction = [], [], False
    elif command == "rollback":
        for task_id in pending_tasks:
            print(f"задача {task_id}: не отправлена")
        pending_rows, pending_tasks, in_transaction = [], [], False
