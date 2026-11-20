# Решения задач курса [Celery и Redis. Фоновые задачи в Python и запросы к ИИ (2026)](https://stepik.org/a/296990) на Stepik

В репозитории собраны все 27 задач курса. Это модели механизмов Celery и Redis на чистом Python, потому что в песочнице Stepik нет ни Redis, ни Celery. В файле задачи есть условие, пример из тестов и решение, которое проходит проверку на Stepik. Репозиторий нужен, чтобы после решения задачи можно было сравнить свой код с вариантом автора курса.

## Как пользоваться

1. Сначала решите задачу сами и отправьте решение на Stepik. Решение автора в курсе откроется только после этого.
2. Найдите файл задачи. Он лежит в папке модуля, внутри неё в папке урока и называется `step_NN.py`, где `NN` означает номер шага в уроке. Ссылки на все файлы есть в содержании ниже.
3. Сравните своё решение с решением из файла. Оно стоит после комментария `# Решение`.

Если задача не получается, не открывайте решение сразу. Перечитайте теорию урока, откройте подсказку под условием на Stepik, запустите программу на своих данных и выведите через `print()` переменные, в которых сомневаетесь. Подсмотренное решение почти ничему не учит.

## Как запустить решение

Нужен Python 3.10 или новее, сторонние библиотеки не нужны. Решения читают входные данные через `input()`, как на Stepik. Например, так запускается первая задача.

```bash
python 02_background_tasks/03_queue_by_hand/step_02.py
```

После запуска введите данные с клавиатуры и нажмите Enter, как описано в условии в начале файла.

## Содержание

Номер модуля в названии папки совпадает с номером модуля в курсе, а номер урока с номером урока внутри модуля.

### 2. Зачем нужны фоновые задачи

| Урок | Шаг | Файл |
|---|---|---|
| 2.3 Очередь своими руками | 2 | [`02_background_tasks/03_queue_by_hand/step_02.py`](02_background_tasks/03_queue_by_hand/step_02.py) |
| 2.3 Очередь своими руками | 3 | [`02_background_tasks/03_queue_by_hand/step_03.py`](02_background_tasks/03_queue_by_hand/step_03.py) |

### 3. Redis для работы с Celery

| Урок | Шаг | Файл |
|---|---|---|
| 3.1 Знакомство с Redis | 5 | [`03_redis/01_redis_basics/step_05.py`](03_redis/01_redis_basics/step_05.py) |
| 3.2 Списки как очередь | 4 | [`03_redis/02_lists_as_queue/step_04.py`](03_redis/02_lists_as_queue/step_04.py) |

### 4. Первая задача

| Урок | Шаг | Файл |
|---|---|---|
| 4.3 Результаты и состояния | 4 | [`04_first_task/03_results_and_states/step_04.py`](04_first_task/03_results_and_states/step_04.py) |
| 4.4 Что можно передавать в задачу | 4 | [`04_first_task/04_task_arguments/step_04.py`](04_first_task/04_task_arguments/step_04.py) |

### 5. Ошибки, повторы и надёжность

| Урок | Шаг | Файл |
|---|---|---|
| 5.1 Повторы задач | 5 | [`05_reliability/01_retries/step_05.py`](05_reliability/01_retries/step_05.py) |
| 5.2 Экспоненциальная задержка | 4 | [`05_reliability/02_exponential_backoff/step_04.py`](05_reliability/02_exponential_backoff/step_04.py) |
| 5.3 Идемпотентность | 4 | [`05_reliability/03_idempotency/step_04.py`](05_reliability/03_idempotency/step_04.py) |
| 5.4 Подтверждение и потеря задач | 4 | [`05_reliability/04_acks_and_lost_tasks/step_04.py`](05_reliability/04_acks_and_lost_tasks/step_04.py) |

### 6. Цепочки и группы задач

| Урок | Шаг | Файл |
|---|---|---|
| 6.1 Сигнатуры и цепочки | 5 | [`06_canvas/01_signatures_and_chains/step_05.py`](06_canvas/01_signatures_and_chains/step_05.py) |
| 6.2 group и chord | 5 | [`06_canvas/02_group_and_chord/step_05.py`](06_canvas/02_group_and_chord/step_05.py) |

### 7. Воркеры, очереди и масштабирование

| Урок | Шаг | Файл |
|---|---|---|
| 7.1 Очереди и маршрутизация | 4 | [`07_workers_and_queues/01_queues_and_routing/step_04.py`](07_workers_and_queues/01_queues_and_routing/step_04.py) |
| 7.3 Предвыборка, частота и приоритеты | 4 | [`07_workers_and_queues/03_prefetch_rate_priority/step_04.py`](07_workers_and_queues/03_prefetch_rate_priority/step_04.py) |
| 7.3 Предвыборка, частота и приоритеты | 5 | [`07_workers_and_queues/03_prefetch_rate_priority/step_05.py`](07_workers_and_queues/03_prefetch_rate_priority/step_05.py) |

### 8. Периодические задачи

| Урок | Шаг | Файл |
|---|---|---|
| 8.1 Celery beat и расписание | 5 | [`08_periodic_tasks/01_beat_and_schedule/step_05.py`](08_periodic_tasks/01_beat_and_schedule/step_05.py) |
| 8.2 Один beat и блокировки | 4 | [`08_periodic_tasks/02_single_beat_and_locks/step_04.py`](08_periodic_tasks/02_single_beat_and_locks/step_04.py) |

### 9. Celery в веб-приложении и тесты

| Урок | Шаг | Файл |
|---|---|---|
| 9.2 Django и транзакции | 4 | [`09_web_and_tests/02_django_and_transactions/step_04.py`](09_web_and_tests/02_django_and_transactions/step_04.py) |

### 10. Мониторинг и эксплуатация

| Урок | Шаг | Файл |
|---|---|---|
| 10.2 Логи и отмена задач | 3 | [`10_operations/02_logs_and_revoke/step_03.py`](10_operations/02_logs_and_revoke/step_03.py) |
| 10.3 Остановка воркеров и продакшен | 3 | [`10_operations/03_worker_shutdown/step_03.py`](10_operations/03_worker_shutdown/step_03.py) |

### 11. Redis или RabbitMQ

| Урок | Шаг | Файл |
|---|---|---|
| 11.1 Чем RabbitMQ отличается от Redis | 5 | [`11_redis_or_rabbitmq/01_rabbitmq_vs_redis/step_05.py`](11_redis_or_rabbitmq/01_rabbitmq_vs_redis/step_05.py) |

### 12. Нейросети в фоновых задачах

| Урок | Шаг | Файл |
|---|---|---|
| 12.1 Запрос к нейросети как фоновая задача | 4 | [`12_ai_tasks/01_ai_request_as_task/step_04.py`](12_ai_tasks/01_ai_request_as_task/step_04.py) |
| 12.2 Лимиты, повторы и стоимость | 5 | [`12_ai_tasks/02_limits_retries_cost/step_05.py`](12_ai_tasks/02_limits_retries_cost/step_05.py) |
| 12.2 Лимиты, повторы и стоимость | 6 | [`12_ai_tasks/02_limits_retries_cost/step_06.py`](12_ai_tasks/02_limits_retries_cost/step_06.py) |
| 12.2 Лимиты, повторы и стоимость | 7 | [`12_ai_tasks/02_limits_retries_cost/step_07.py`](12_ai_tasks/02_limits_retries_cost/step_07.py) |
| 12.3 Длинный текст по частям | 4 | [`12_ai_tasks/03_long_text_in_parts/step_04.py`](12_ai_tasks/03_long_text_in_parts/step_04.py) |
| 12.3 Длинный текст по частям | 5 | [`12_ai_tasks/03_long_text_in_parts/step_05.py`](12_ai_tasks/03_long_text_in_parts/step_05.py) |
