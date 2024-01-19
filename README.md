# compas-pro-task
Тестовое задание для компании ООО Компас ПРО

### Установка

Клонируйте репозиторий с помощью следующей команды:
   ```bash
   git clone git@github.com:Abramov0Alexandr/compas-pro-task.git
   ```

Создайте .env файл и заполните его в соответствии с .env.sample
   ```bash
    touch compas-pro-task/.env
   ```

Соберите образ и запустите контейнер:

   ```bash
    docker compose up --build
   ```

В случае, если вы планируете запустить локальный сервер проекта, а не контейнер, 
установите необходимый флаг в настройках базы данных.
```python
RUN_AS_DOCKER_CONTAINER = False
```

## Документация (swagger-ui, redoc)

- http://localhost:8000/api/schema/swagger-ui/
- http://localhost:8000/api/schema/redoc/

## Маршруты для работы с пользователями

- GET http://localhost:8000/api/users/{int}/ Для получения информации о пользователе
- POST http://localhost:8000/api/users/create/ Для добавления нового пользователя
