# api_final
Цель работы над проектом - получить навыки работы с Django REST framework.
Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения. При попытке изменить чужие данные должен возвращаться код ответа 403 Forbidden.

### Стек технологий

![](https://img.shields.io/badge/Python-3.7-blue?style=flat&logo=Python&logoColor=#3776AB)
![](https://img.shields.io/badge/Django-2.2.16-blue?style=flat&logo=Django&logoColor=red)
![](https://img.shields.io/badge/DRF-3.12.4-blue?style=flat&logo=Django&logoColor=red)


### Эндпоинты для взаимодействия с ресурсами:


* api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
* api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
* api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
* api/v1/groups/ (GET): получаем список всех групп.
* api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
* api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать. 
* api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.

В ответ на запросы POST, PUT и PATCH ваш API возвращает объект, который был добавлен или изменён.

Работа с моделью Post осуществляется через через ModelViewSet.

В проекте описана модель Follow, в ней два поля — user (кто подписан) и following (на кого подписан). Для этой модели в документации уже описан эндпоинт /follow/ и два метода:

GET — возвращает все подписки пользователя, сделавшего запрос. Возможен поиск по подпискам по параметру search
POST — подписать пользователя, сделавшего запрос на пользователя, переданного в теле запроса. При попытке подписаться на самого себя, пользователь получит информативное сообщение об ошибке. Проверка должна осуществляться на уровне API.
Анонимный пользователь на запросы к этому эндпоинту получает ответ с кодом 401 Unauthorized.

При запросе на изменение или удаление данных осуществляется проверка прав доступа.

### Как запустить проект:

##### Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:apisland/api_final_yatube.git
```

```
cd api_final_yatube
```

##### Cоздать и активировать виртуальное окружение:

```
python -m venv env
```
##### для Windows:
```
source env/Scripts/activate
```
##### для *nix:
```
source env/bin/activate
```

##### Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

##### Выполнить миграции:

```
python3 manage.py migrate
```
или
```
python manage.py migrate
```
##### Запустить проект:

```
python3 manage.py runserver
```
или
```
python manage.py runserver
```

