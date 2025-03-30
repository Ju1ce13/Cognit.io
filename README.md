# Cognit.io 🚀

**Сервис для знакомств в сообществе программистов КАИ**

[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

Cognit.io — это платформа для знакомств и нетворкинга среди студентов и выпускников КАИ, увлеченных программированием. Находите единомышленников, обменивайтесь опытом и развивайтесь вместе!

## 🌟 Возможности

- 👤 Создание персонального профиля с информацией о навыках и интересах
- 🔍 Поиск людей по технологиям, профессии и интересам
- ❤️ Система лайков и взаимных симпатий
- 💬 Встроенный чат для общения с совместимыми пользователями

## 🛠 Технологический стек

- **Backend**: Python (FastAPI)
- **Frontend**: React.js
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy + Alembic для миграций
- **Real-time**: WebSockets для чата
- **Deployment**: Docker + Docker-compose

## 🚀 Быстрый старт

### Предварительные требования

- Установленный [Docker](https://docs.docker.com/get-docker/)
- Установленный [Docker Compose](https://docs.docker.com/compose/install/)

### Запуск проекта

1. Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/cognitio.git
cd cognitio
```

2. Создайте файл `.env` в корне проекта (на основе `.env.example`):

```bash
cp .env.example .env
```

3. Запустите проект с помощью Docker Compose:

```bash
docker-compose up -d --build
```

4. После запуска сервисы будут доступны по адресам:

   - **Frontend**: http://localhost
   - **Backend API**: http://localhost:8000
   - **Adminer** (для управления БД): http://localhost:8080

5. Для остановки проекта выполните:

```bash
docker-compose down
```

## 🏗 Структура проекта

```
cognitio_app/
├── app/            # Backend сервис (FastAPI) 
│   ├── alembic/       # Миграции базы данных
│   └── Dockerfile_backend
│   └── Dockerfile_frontend
├── docker-compose.yml # Конфигурация Docker
├── frontend/          # Frontend сервис (React)
└── .env.example       # Пример переменных окружения


```

## 🔧 Дополнительные команды

### Выполнение миграций

```bash
docker-compose run --rm backend alembic upgrade head
```

### Создание новой миграции

```bash
docker-compose run --rm backend alembic revision --autogenerate -m "Описание изменений"
```

### Просмотр логов

```bash
docker-compose logs -f backend  # Логи бэкенда
docker-compose logs -f frontend # Логи фронтенда
docker-compose logs -f db       # Логи базы данных
```

## 🤝 Участие в разработке

Мы приветствуем вклад в развитие Cognit.io! Если вы хотите помочь:

1. Форкните репозиторий
2. Создайте ветку для вашей фичи (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add some amazing feature'`)
4. Запушьте в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

---

**Cognit.io** © 2025 | Разработано с ❤️ для сообщества КАИ(КАИ - ПУП ЗЕМЛИ)
