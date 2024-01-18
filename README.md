# compas-pro-task
Тестовое задание для компании ООО Компас ПРО

## Для клонирования проекта выполните 

### Установка

Клонируйте репозиторий с помощью следующей команды:
   ```bash
   git clone git@github.com:Abramov0Alexandr/compas-pro-task.git
   ```

Соберите образ и запустите контейнер:

   ```bash
    docker compose up --build
   ```

## Документация (swagger-ui, redoc)
    
- http://localhost:8000/api/schema/swagger-ui/ 
- http://localhost:8000/api/schema/redoc/

## Маршруты для работы с пользователями

- GET http://localhost:8000/api/users/{int}/ Для получения информации о пользователе
- POST http://localhost:8000/api/users/create/ Для добавления нового пользователя

