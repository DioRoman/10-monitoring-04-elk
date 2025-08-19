### Подробное объяснение:

- **Настройка логирования:**
  ```python
  logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s %(levelname)s %(message)s'
  )
  ```
  — Задает формат вывода логов: время (`asctime`), уровень (`levelname`), текст сообщения (`message`).
  — Уровень — `INFO`, т.е. будут выводиться все события INFO, WARNING, ERROR и выше (DEBUG — нет).[1][2]

- **Основной бесконечный цикл:**
  ```python
  while True:
      number = random.randrange(0, 4)
      ...
      time.sleep(3)
  ```
  — Каждые 3 секунды выбирается случайное "событие" из 4-х вариантов.

- **Логирование разных уровней:**
  - `logging.info('Process started successfully.')` — Информационное сообщение.
  - `logging.warning('Unexpected input received.')` — Предупреждение.
  - `logging.error('Failed to connect to the database.')` — Ошибка.
  - `logging.exception(Exception('Unhandled exception occurred.'))` — Ошибка с трассировкой стека (выглядит как реальное исключение в логах).

***

**Что делает этот скрипт?**  
Он имитирует и генерирует случайные логи разных уровней (info/warning/error/exception) для тестирования систем логирования, мониторинга или демонстрации работы ELK/Graylog и подобного стека.

**Пример вывода:**
```
2025-08-19 14:35:44,399 INFO Process started successfully.
2025-08-19 14:35:47,401 WARNING Unexpected input received.
2025-08-19 14:35:50,403 ERROR Failed to connect to the database.
2025-08-19 14:35:53,404 ERROR Unhandled exception occurred.
Traceback (most recent call last):
  ...
Exception: Unhandled exception occurred.
```

При каждой итерации появляется случайный тип сообщения — удобно для тестов и отработки автоматического парсинга логов.
