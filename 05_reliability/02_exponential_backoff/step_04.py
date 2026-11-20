"""
Урок 5.2 "Экспоненциальная задержка", шаг 4

Посчитайте паузы перед повторами так, как это делает Celery при `retry_jitter=False`.

На вход подаётся строка из трёх значений `retry_backoff` (`True` или целое число),
`retry_backoff_max` и `max_retries`.

Множитель равен 1 для `True`, иначе числу, но не меньше 1. Пауза перед повтором с номером k (с нуля)
равна `min(retry_backoff_max, множитель * 2 ** k)`.

Выведите строки `повтор N: X с` для всех повторов (N с единицы), а затем `всего ожидания: S с`.

Ввод и вывод. Входные данные читайте функцией `input()`, результат выводите через `print()`. Перед
отправкой нажмите "Запустить код", чтобы проверить решение на своих данных.

Пример ввода:

    2 60 5

Пример вывода:

    повтор 1: 2 с
    повтор 2: 4 с
    повтор 3: 8 с
    повтор 4: 16 с
    повтор 5: 32 с
    всего ожидания: 62 с
"""

# Решение
backoff, maximum, max_retries = input().split()
factor = 1 if backoff == "True" else max(1, int(backoff))
maximum, max_retries = int(maximum), int(max_retries)

total = 0
for retries in range(max_retries):
    delay = min(maximum, factor * 2 ** retries)
    total += delay
    print(f"повтор {retries + 1}: {delay} с")
print(f"всего ожидания: {total} с")
