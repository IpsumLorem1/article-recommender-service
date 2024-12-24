# Сервис для рекомендации статей на основе введённого запроса

## Описание проекта

Этот проект представляет собой веб-приложение для поиска статей, которое использует эмбеддинги и библиотеку Faiss для быстрого поиска наиболее релевантных результатов. Оно включает:
- **Backend** на FastAPI для обработки запросов и взаимодействия с Faiss.
- **Frontend** на Vue.js для интерфейса пользователя.

## Структура проекта


### Backend

- Используемые технологии: `Python`, `FastAPI`, `Uvicorn`, `Poetry`
- Основные функции:
  - Обработка запросов на поиск статей
  - Управление Faiss-индексом для быстрого поиска
- Зависимости описаны в файле `pyproject.toml`.

#### Установка backend:

1. Перейдите в папку `backend`:
  ```bash
   cd backend
   poetry install
   poetry run uvicorn main:app
   ```


### Frontend

- Используемые технологии: `Vue.js`, `Vite`, `axios`, `npm`
- Основные функции:
  - Интуитивно понятный пользовательский интерфейс для поиска статей
  - Работа с API, предоставляемым backend
- Зависимости описаны в файле `package.json`.

#### Установка frontend:

1. Перейдите в папку `frontend`:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```