# Django REST API
# TaskTracker

Backend для упрощенной системы управления задачами, которая позволяет пользователям создавать и управлять проектами и задачами,
назначать исполнителей и отслеживать статус заполнения.

## Содержание

- [Требования](#требования)
- [Установка](#установка)
- [Использование](#использование)
- [Разработка](#разработка)
- [Тестирование](#тестирование)
- [Развертывание](#развертывание)

## Требования

Для запуска этого проекта вам понадобятся следующие зависимости:

- Python 3.13
- Django 4.2.16
- Django REST Framework 3.15.2
- PostgreSQL (или другая база данных, если настроено иное)
- Другие зависимости, перечисленные в `requirements.txt`

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   
2. Создайте виртуальное окружение и активируйте его
    ```sh
    python -m venv venv
    .venv/Scripts/activate
   
3. Установите зависимости
    ```sh
    pip install -r requirements.txt

4. Настройте базу данных в файле settings.py:
    ```sh
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Примените миграции:
    ```sh
    python manage.py migrate

6. Создайте суперпользователя:
    ```sh
    python manage.py createsuperuser

7. Запустите сервер разработки:
    ```sh
    python manage.py runserver

## Использование

После запуска сервера, вы можете получить доступ к API через браузер или Postman.

## Вот данные запросы:
```
    http://127.0.0.1:8000/admin/
    http://127.0.0.1:8000/api/v1/drf-auth/
    http://127.0.0.1:8000/api/v1/tasklist/
    http://127.0.0.1:8000/api/v1/task/<int:pk>/
    http://127.0.0.1:8000/api/v1/taskdelete/<int:pk>/
    http://127.0.0.1:8000/api/v1/projectlist/
    http://127.0.0.1:8000/api/v1/project/<int:pk>/
    http://127.0.0.1:8000/api/v1/projectdelete/<int:pk>/
    http://127.0.0.1:8000/api/v1/profilecreate/
    http://127.0.0.1:8000/api/v1/profile/<int:pk>/
    http://127.0.0.1:8000/api/v1/profiledelete/<int:pk>/
    http://127.0.0.1:8000/api/v1/participantlist/
    http://127.0.0.1:8000/api/v1/participant/<int:pk>/
    http://127.0.0.1:8000/api/v1/participantdelete/<int:pk>/
    http://127.0.0.1:8000/token/
    http://127.0.0.1:8000/token/refresh/
    http://127.0.0.1:8000/token/verify/
    http://127.0.0.1:8000/auth/users/
    http://127.0.0.1:8000/auth/token/login/
    http://127.0.0.1:8000/api/v1/commentlist/<int:pk>/
    http://127.0.0.1:8000/api/v1/comment/<int:pk>/
    http://127.0.0.1:8000/api/v1/commentdelete/<int:pk>/
```
# Разработка

1. Создание миграций:
    ```sh
    python manage.py makemigrations

2. Применение их:
    ```sh
   python manage.py migrate

## Тестирование
```sh
    python manage.py test
```

# Развертывание

## Dockerfile
```
    FROM python:3.13-slim
    WORKDIR /tasktracker
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    COPY . .
    EXPOSE 8000
    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## docker-compose.yml
```
services:
  db:
    image: postgres:14
    environment:
      POSTGRES_DB: tasktracker
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: parol0988
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/tasktracker
    ports:
      - "8000:8000"
    depends_on:
      - db

volumes:
  postgres_data:
```

# Контакты

Если у вас есть вопросы или предложения, свяжитесь с нами по адресу email@example.com





