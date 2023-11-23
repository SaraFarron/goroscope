# Бот для самых точных гороскопов на сегодня

## Депенденсис
```shell
python3
pypi discord.py requests
```

.env
```
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
VK_URL=https://api.vk.ru/method/wall.get?access_token=YOUR_VK_APP_SERVICE_TOKEN&v=5.199&owner_id=-193489972

```

## Запуск

```shell
docker build . -t goroscope
docker run --env-file .env goroscope
```
или

```shell
pipenv run python main.py
```
Если не хотите pipenv и докер, то добавьте переменные из `.env` и
```shell
python main.py
```
