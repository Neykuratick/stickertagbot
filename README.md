## Описание
Это мой личный сделанный на коленке телеграм бот для поиска стикеров по тегу. Над кодом особо не заморачивался, т.к не собираюсь над ним дальше работать

## Деплой

- `docker network create stickertagbotNetwork`
- `docker-compose up --build`
- Ctrl+c
- `docker network connect stickertagbotNetwork telegram-redis`
- `docker network connect stickertagbotNetwork stickertagbot`

- Копируем ip `docker network inspect -f '{{range.IPAM.Config}}{{.Gateway}}{{end}}' stickertagbotNetwork`
- Вставляем в .env: `REDIS_HOST=скопированный айпи`
- `docker-compose up --build`
