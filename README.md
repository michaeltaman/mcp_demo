cd server
python -m venv venv # создание виртуального окружения (опционально)
source venv/bin/activate # активация окружения (Linux/Mac)
venv\Scripts\activate # активация окружения (Windows)
pip install -r requirements.txt # установка зависимостей
cd ../
uvicorn main:app --reload
Запускаем ngrok на порт 80: ngrok http 80
docker-compose up --build
