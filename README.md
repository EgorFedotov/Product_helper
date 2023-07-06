![example workflow](https://github.com/EgorFedotov/foodgram-project-react/actions/workflows/foodgram-project-react.yml/badge.svg)

## Product helper сайт с рецептами, продуктовый помощник

Product helper - это сайт, на котором можно размещать свои рецепты, смотреть рецепты других авторов, подписываться на интересующего автора, а также формировать список покупок для выбранных рецептов.

## Стек

- Python

- Djando

- Docker

- DRF

- API

- git

- Postgres

- Nginx



## Запуск проекта

Клонируем репозиторий

```bash
  git clone git@github.com:EgorFedotov/Product_helper.git
```

На удаленном сервере устанавливаем Docker и Docker сompose:

```bash
  sudo apt install curl
  curl -fsSL https://get.docker.com -o get-docker.sh
  sh get-docker.sh 
  sudo apt-get install docker-compose-plugin
```

С локальной машины копируем docker-compose.yml, nginx.conf на сервер, находясь в папке infra выполняем команду:

```bash
  scp docker-compose.yml nginx.conf <username>@<IP сервера>:/home/<username>/
```

- Для работы с GitHub Actions необходимо в репозитории в разделе Secrets > Actions создать переменные окружения:

```
SECRET_KEY              # секретный ключ Django проекта
DOCKER_USERNAME         # логин Docker Hub
DOCKER_PASSWORD         # пароль от Docker Hub
HOST                    # публичный IP сервера
USER                    # имя пользователя на сервере
PASSPHRASE              # *если ssh-ключ защищен паролем
SSH_KEY                 # приватный ssh-ключ
TELEGRAM_TO             # ID телеграм-аккаунта для посылки сообщения
TELEGRAM_TOKEN          # токен бота, посылающего сообщение

DB_ENGINE               # django.db.backends.postgresql
POSTGRES_DB             # postgres
POSTGRES_USER           # postgres
POSTGRES_PASSWORD       # postgres
DB_HOST                 # db
DB_PORT                 # 5432 (порт по умолчанию)
DEBUG                   # False (режим отладки)
ALLOWED_HOSTS           # ['*'] (порты)
```

Чтобы на сервере запустить контейнеры, выполните команду 

```bash
  sudo docker compose up -d
```

Выполнеям миграции:

```bash
  sudo sudo docker compose exec web python manage.py makemigrations
  sudo sudo docker compose exec web python manage.py migrate
```

Создаем суперпользователя и собираем статику :

```bash
  sudo docker compose exec web python manage.py createsuperuser
  sudo docker compose exec web python manage.py collectstatic --noinput
```

Наполняем БД из файла ingredients.json:

```bash
  sudo docker compose exec web python manage.py load_ingredients
```

Для остановки контейнеров Docker

```
  sudo docker compose down -v      # с их удалением
  sudo docker compose stop         # без удаления
```



# Для запуска проета локально в корне дерриктории infa создайте файл .env и добавьте туда:
  - SECRET_KEY
  - DB_ENGINE
  - POSTGRES_DB
  - POSTGRES_USER
  - POSTGRES_PASSWORD
  - DB_HOST
  - DB_PORT
  - DEBUG
  - ALLOWED_HOSTS
