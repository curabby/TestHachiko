# **TestHachiko**

TestHachiko — это проект по тестовому заданию Компании "Хатико-техника", выполненный для демонстрации навыков разработки приложений.
Проект объединяет Telegram-бота и бекенд приложения на базе Django Rest Framework. Проект позволяет взаимодействовать с пользователями через Telegram, регистрировать их данные и обрабатывать команды, такие как проверка IMEI через сторонний сервис.

## **Функционал**

- Telegram-бот для взаимодействия с пользователями.
- Регистрация пользователей.
- Обращение к бекенду только зарегистрированными пользователями
- Взаимодействие с сервером через REST API.
- Хранение данных в PostgreSQL.
- Развертывание проекта осуществляется с использованием Docker, что упрощает настройку и управление зависимостями.

---

## **Установка**

### **1. Клонирование репозитория**

```bash
git clone https://github.com/curabby/TestHachiko.git
cd TestHachiko
```

### **2. Настройка окружения**

Создайте файл `.env` в корне проекта и заполните его:

```env
DEBUG=0
SECRET_KEY='YOUR_SECRET_DJANGO_KEY'
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_DB='YOUR_POSTGRES_DB'
POSTGRES_USER='YOUR_POSTGRES_USER'
POSTGRES_PASSWORD='YOUR_POSTGRES_PASSWORD'
POSTGRES_HOST=db
POSTGRES_PORT=5432
API_KEY='YOUR_TELEGRAM_API_KEY'
TOK_SALT="SALTEXAMPLE2025"
API_URL='http://drf:8000'
API_CHECK_KEY='Токен API Sandbox'
```


### **3. Запуск с помощью Docker**

Убедитесь, что Docker установлен на вашем компьютере, затем выполните:

```bash
docker-compose up --build
```

---

## **Использование**

### **Telegram-бот**

1. Запустите вашего Telegram-бота.
2. Используйте команду `/start` для начала взаимодействия.

### **API**

Примеры доступных эндпоинтов:

- **GET /api/v1/user-exist<telegram_id>**: Проверка существования пользователя.
- **POST /api/v1/register**: Регистрация нового пользователя.
- **POST /api/v1/check-imei**: Проверка IMEI

### **Документация API**

Документация доступна по адресу:

```
http://localhost:8000/swagger/
```

---

## **Технологии**

- **Python**
- **Django Rest Framework**
- **PostgreSQL**
- **Docker & Docker Compose**
- **aiogram**
- **aiohttp**
- **asyncio**

---
