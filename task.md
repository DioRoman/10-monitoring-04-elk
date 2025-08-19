# Домашнее задание к занятию 15 «Система сбора логов Elastic Stack»

## Задание 1

Вам необходимо поднять в докере и связать между собой:

- elasticsearch (hot и warm ноды);
- logstash;
- kibana;
- filebeat.

Logstash следует сконфигурировать для приёма по tcp json-сообщений.

Filebeat следует сконфигурировать для отправки логов docker вашей системы в logstash.

Результатом выполнения задания должны быть:

- скриншот `docker ps` через 5 минут после старта всех контейнеров (их должно быть 5);

<img width="1910" height="356" alt="Снимок экрана 2025-08-19 164814" src="https://github.com/user-attachments/assets/6f1911f7-03ba-4ed0-971c-7beda6a15ca2" />

 - скриншот интерфейса kibana;

<img width="1859" height="947" alt="Снимок экрана 2025-08-19 173236" src="https://github.com/user-attachments/assets/19c47eeb-8cd3-41af-b2df-ab6f8373d0a0" />
  
- docker-compose манифест (если вы не использовали директорию help);

https://github.com/DioRoman/10-monitoring-04-elk/blob/main/elk-docker/docker-compose.yml
 
- ваши yml-конфигурации для стека (если вы не использовали директорию help).

https://github.com/DioRoman/10-monitoring-04-elk/blob/main/elk-docker/configs/filebeat.yml

https://github.com/DioRoman/10-monitoring-04-elk/blob/main/elk-docker/configs/logstash.conf

## Задание 2

Перейдите в меню [создания index-patterns  в kibana](http://localhost:5601/app/management/kibana/indexPatterns/create) и создайте несколько index-patterns из имеющихся.

Перейдите в меню просмотра логов в kibana (Discover) и самостоятельно изучите, как отображаются логи и как производить поиск по логам.

В манифесте директории help также приведенно dummy-приложение, которое генерирует рандомные события в stdout-контейнера.
Эти логи должны порождать индекс logstash-* в elasticsearch. Если этого индекса нет — воспользуйтесь советами и источниками из раздела «Дополнительные ссылки» этого задания.

Создание Data Views:

<img width="1375" height="689" alt="Снимок экрана 2025-08-19 170815" src="https://github.com/user-attachments/assets/5d39c733-18a6-4c43-b8e4-25d19cab6d91" />

Отображение логов. 

<img width="1847" height="915" alt="Снимок экрана 2025-08-19 171048" src="https://github.com/user-attachments/assets/ecde1512-aa59-4087-a4ed-5442c70a0682" />

 

 
