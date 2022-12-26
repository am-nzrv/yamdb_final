![yamdb workflow](https://github.com/gomunculusigor/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## **Описание проекта API для YaMDB.**
API для проекта YaMDB - проекта соц.сети, в котором пользователи могут размещать обзоры на произведения в разных категориях (фильмы, музыка, кино) и жанрах, после чего на основании оценок формируется рейтинг произведений. 

## **Технологии (основные инструменты):**
- Python==3.7
- Django==3.2
- djangorestframework==3.12.4
- djangorestframework-simplejwt==5.1.0
- gunicorn==20.0.4
- psycopg2-binary==2.8.6 (в идеале psycopg2)
- PyJWT==2.1.0
- pytest==6.2.4
- python-dotenv==0.20.0
- Docker

### Деплой проекта с помощью Docker:
1. Необходимо установить **Docker** для дальнейшего развертывания проекта.


2. Клонируйте репозиторий:

```git clone git@github.com:gomunculusigor/infra_sp2.git```

3. Перейдите в директорию приложения /api_yamdb и запустите сборку образа проекта

```docker build -t infra_sp2 ./yamdb```

4. Перейдите в директорию инфраструктуры /infra и запустите контейнеры:

```docker-compose up```

5. Создайте и примените миграции внутри основного контейнера **web**:

```docker-compose exec web python manage.py makemigrations```

```docker-compose exec web python manage.py migrate```

6. Сформируйте статику:

```docker-compose exec web python manage.py collectstatic --no-input```

### Деплой проекта на боевой сервер с помощью образа Docker:
1. Входим на боевой сервер (ваша виртуальная машина).

2. Необходимо установить **Docker** для дальнейшего процесса размещения проекта на боевом сервере:

    ``` sudo apt install docker.io```

3. Проверьте наличие на сервере docker-compose. Если его нет, то установите его выполнив следующие команды по порядку:
   
    - Установите утилиту curl для скачивания docker-compose:
   
    ```sudo apt -y install curl```
  
    - Скачиваем docker-compose с помощью утилиты:
   
    ```sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose```

    - Добавим право исполняемости файла docker-compose:
   
    ```sudo chmod +x /usr/local/bin/docker-compose```

    - Проверьте, что docker-compose работает путем проверки отображения списка комманд при его вызове:
   
    ```docker-compose ```

    - Для загрузки данных:
   
    ```docker-compose exec web python manage.py loaddata db.json```
## **Документация к API:**
После запуска проект 
доступен по адресу  http://51.250.107.160:8000/api/v1


## **Автор:**
https://github.com/gomunculusigor

