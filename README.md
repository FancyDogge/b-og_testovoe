# blog_testovoe
Тестовое задание

## Инструкция
Для начала нужно клонировать данный репозиторий

```
git clone https://github.com/FancyDogge/blog_testovoe.git
```

Вас уже будет ждать готовый docker-compose.yml

Убедитесь, что вы работаете в директории с docker-compose.yml и введите следующую команду для сборки образа:

```
docker-compose build
```

Должна начаться сборка образа и установка зависимостей из Dockerfile

Далее, чтобы создать контейнеры и в следствии запустить приложение с сервером, введите

```
docker-compose up

если хотите, чтобы процесс запустился в бэкграунде:

docker-compose up -d
```

Все готово!
Теперь приложение api запущено на порте 8000 и доступно по адресу localhost

Нужно сделать миграции в базу данных postgres, для этого в директории с docker-compose.yml следует ввести:
```
docker-compose exec api python manage.py makemigration
docker-compose exec api python manage.py migrate
```

И создать superuser

```
docker-compose exec api python manage.py createsuperuser
```
После этого, с помощью админки можно заполнить базу данных юзерами и постами от них, на указанные в профилях почты должен приходить список постов юзеров, на которых подписаны пользователи
