# Моё FastAPI приложение

Это простое FastAPI-приложение с двумя эндпоинтами.
Инструкция ниже поможет вам запустить проект.

## Установка
1. Склонируйте репозиторий:
    git clone https://github.com/MorozGH/docker1.git

2. Перейдите в папку проекта:
   cd docker1

## Запуск локально

1. Создайте виртуальное окружение:
    python3 -m venv .venv

2. Войдите в виртуальное окружение:
    source .venv/bin/activate

3. Загрузите зависимости:
    pip install -r requirements.txt

4. Запустите приложение:
    uvicorn app.main:app --reload

Приложение будет доступно по адресу: http://localhost:8000
Доступ ко всем эндпоинтам: http://localhost:8000/docs

## Запуск через Docker
1. Соберите образ:
    docker build -t docker1 .

2. Запустите контейнер на основе образа:
    docker run -d --name docker1 -p 8000:8000 docker1

3. Остановите контейнер, при необходимости:
    docker stop docker1 && docker rm docker1

Приложение будет доступно по адресу: http://localhost:8000
Доступ ко всем эндпоинтам: http://localhost:8000/docs