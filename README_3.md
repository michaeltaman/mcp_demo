# MCP Debugger (Demo) – README_3.md

## 📦 Описание проекта

Это демонстрационное приложение, состоящее из:

- Backend на FastAPI с подключением к PostgreSQL
- Frontend (HTML + JS + CSS)
- Полностью готовый для запуска локально и в Docker

---

## 🚀 Быстрый старт

### 🔧 Запуск ЛОКАЛЬНО (Standalone)

1️⃣ Перейдите в директорию `server`:

```
cd server
```

2️⃣ Создайте и активируйте виртуальное окружение:

```
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3️⃣ Установите зависимости:

```
pip install -r ../requirements.txt
```

4️⃣ Запустите сервер FastAPI:

```
cd ../
C:\Users\mictr\MyProjects\mcp_demo>uvicorn server.main:app --reload
```

5️⃣ Откройте `client/index.html` в браузере, подключение будет к `localhost:8000`

---

### 🐳 Запуск в Docker

1️⃣ Остановите старые контейнеры (если нужно):

```
docker-compose down
```

2️⃣ Соберите образы и запустите контейнеры:

```
docker-compose up --build
```

3️⃣ Убедитесь, что контейнеры работают:

- Backend доступен на `localhost:8000`
- Frontend доступен на `localhost:80`
- БД PostgreSQL на `localhost:5432`

4️⃣ Проброс порта через ngrok для фронтенда:

```
ngrok http 80
```

5️⃣ Перейдите по ссылке, предоставленной ngrok, и увидьте MCP Debugger (Demo)

---

## 📚 Состав проекта

```
/mcp-demo/
├── client/              # Frontend
│   ├── index.html
│   ├── app.js
│   └── style.css
├── server/              # Backend
│   ├── main.py
│   ├── tools.py
│   ├── utils.py
│   └── initdb/init.sql
├── docker-compose.yml   # Docker Compose
├── Dockerfile           # Dockerfile для backend
└── requirements.txt     # Зависимости для Python
```

---

## 📌 Полезные команды

- Проверка работы БД (PostgreSQL):

```
docker exec -it <db_container_name> psql -U postgres -d mcp_db
```

- Тест API:

```
curl http://localhost:8000/api/mcp/dbtest
```

---

Удачи! 🚀
