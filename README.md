# Effective Mobile — Junior DevOps | Тестовое

Простое веб-приложение, доступное через nginx как reverse proxy, развёрнутое в Docker-контейнерах.

## Технологии

- Python 3.12 (http.server) — backend
- Nginx 1.25 (alpine) — reverse proxy
- Docker + Docker Compose — контейнеризация и оркестрация

## Структура проекта

```
.
├── backend/                  # Директория исходного кода бэкенд-приложения
│   ├── Dockerfile            # Сборка образа em-backend
│   └── app.py                # Логика приложения
├── nginx/                    # Настройки веб-сервера
│   └── nginx.conf            # Конфигурация proxy_pass и изоляция сети
├── .env.example              # Шаблон окружения (скопировать в .env)
├── docker-compose.yml        # Оркестрация контейнеров
└── README.md                 # Документация проекта
```

## Запуск

1. Клонировать репозиторий:
```bash
git clone https://github.com/v1tharr/effective-mobile-devops-test.git
cd effective-mobile-devops-test
```

2. Создать файл окружения:
```bash
cp .env.example .env
```

3. Запустить:
```bash
docker compose up -d
```

4. Проверить:
```bash
curl http://localhost
```

Ожидаемый ответ: Hello from Effective Mobile!

## Остановка

```bash
docker compose down
```

## Архитектура

```
[ Пользователь ]
              │
              │ HTTP (Публичный порт :80)
              ▼
┌──────────────────────────────────────────────┐
│ Docker-сеть: app-network                     │
│                                              │
│  ┌────────────────────────┐                  │
│  │ Контейнер: em-nginx    │                  │
│  │ На базе Nginx (port 80)│                  │
│  └───────────┬────────────┘                  │
│              │                               │
│              │ proxy_pass http://backend:8080│
│              ▼                               │
│  ┌────────────────────────┐                  │
│  │ Контейнер: em-backend  │                  │
│  │ Порт 8080              │                  │
│  │ (не опубликован наружу)│                  │
│  └────────────────────────┘                  │
└──────────────────────────────────────────────┘
```

Запрос от пользователя приходит на nginx (порт 80), nginx проксирует его на веб-сервис backend по имени сервиса внутри изолированной docker-сети. Сервис backend возвращает ответ, nginx отдаёт его пользователю.