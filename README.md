cd /mnt/c/Users/rlyst/netology/10-monitoring-04-elk/elk-docker

sudo sysctl -w vm.max_map_count=262144 - эта команда — обязательный шаг для подготовки Linux-хоста под запуск Elasticsearch, чтобы избежать проблем с памятью.

docker compose up -d