## Деплой

- `docker network create stickertagbotNetwork`
- `docker-compose up --build`
- Ctrl+c
- `docker network connect stickertagbotNetwork telegram-redis`
- `docker network connect stickertagbotNetwork stickertagbot`

- Копируем ip `docker network inspect -f '{{range.IPAM.Config}}{{.Gateway}}{{end}}' stickertagbotNetwork`
- Вставляем в .env: `REDIS_HOST=скопированный айпи`
- `docker-compose up --build`