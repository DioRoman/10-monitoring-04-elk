cd /mnt/c/Users/rlyst/netology/10-monitoring-04-elk/elk-docker

sudo sysctl -w vm.max_map_count=262144 - эта команда — обязательный шаг для подготовки Linux-хоста под запуск Elasticsearch, чтобы избежать проблем с памятью.

docker compose up -d

docker compose down

Файл `docker-compose.yml`, запускает и связывает сервисы ELK-стека (Elasticsearch, Logstash, Kibana, Filebeat) и дополнительного приложения в Docker-контейнерах. Вот, что делает каждый блок:

***

### 1. Сервис `es-hot` (Elasticsearch Hot node)
- Запускает контейнер с Elasticsearch версии 8.15.3, с именем `es-hot`.
- Настроен как горячий (hot) узел с ролями: `master`, `data_content`, `data_hot`.
- Использует JVM с 1 ГБ памяти (`ES_JAVA_OPTS`).
- Открывает порт 9200 для HTTP-запросов на все интерфейсы (`http.host=0.0.0.0`).
- Отключена безопасность `xpack.security.enabled=false` для упрощения.
- Хранит данные в volume `data01`.
- Задает высокие лимиты по памяти и открытому числу дескрипторов (ulimits).
- Включен в Docker-сеть `elastic`.
- Зависит от сервиса `es-warm` (т.е. ждет его запуска).

***

### 2. Сервис `es-warm` (Elasticsearch Warm node)
- Запускает Elasticsearch версии 8.15.3 с именем `es-warm`.
- Узел с ролями `master`, `data_warm` (хранит менее горячие данные).
- Аналогичные настройки памяти, безопасности и сети.
- Данные хранятся в volume `data02`.
- Использует ту же сеть `elastic`.
- Этот узел и `es-hot` образуют кластер `es-docker-cluster`.

***

### 3. `kibana`
- Запускает Kibana 8.15.3, сервис для визуализации и интерфейса к Elasticsearch.
- Пробрасывает порт 5601 наружу.
- Подключается к Elasticsearch по адресам `es-hot:9200` и `es-warm:9200`.
- Выполняется после запуска Elasticsearch узлов.

***

### 4. `logstash`
- Контейнер с Logstash 8.15.3, сервис для обработки и трансформации логов.
- JVM с 512 МБ памяти.
- Порты 5044 и 5046 проброшены (обычно для приема логов от Beats и других источников).
- Монтирует локальные конфиги Logstash (`logstash.conf`, `logstash.yml`).
- Часть сети `elastic`.
- Зависит от Elasticsearch (ждет их запуска).

***

### 5. `filebeat`
- Контейнер Filebeat 8.15.3 — агент для сбора и отправки логов.
- Запущен с привилегиями (`privileged: true`) и от пользователя root.
- Выполняет команду `filebeat -e -strict.perms=false`.
- Монтирует конфигурационный файл `filebeat.yml` и директории Docker для сбора контейнерных логов.
- Подключен к сети `elastic`.
- Ждет запуска Logstash.

***

### 6. `some_application`
- Дополнительное приложение на Python 3.10 Alpine.
- Монтирует локальную директорию `./pinger/` в контейнер.
- Запускает скрипт `/opt/run.py`.

***

### 7. Volumes
- Объявлены три локальных volume (`data01`, `data02`, `data03`) для хранения данных Elasticsearch.

***

### 8. Networks
- Создана сеть `elastic` с драйвером `bridge`, для связи всех контейнеров.

***

## Итог:
Данный файл поднимает кластер Elasticsearch с двумя типами нод (hot и warm), визуализацию Kibana, сбор и обработку логов через Logstash и Filebeat, а также запускает пользовательское Python-приложение. Все сервисы связаны в одну сеть и настроены для совместной работы в ELK-стеке.