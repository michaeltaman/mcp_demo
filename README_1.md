# MCP Debugger (Demo) User Manual

## How to Run the Program

### 1. Install Dependencies

Make sure you have Python 3.8+ installed. In your project directory, run:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install fastapi uvicorn
```

> **Note:** If you have a `requirements.txt`, you can use `pip install -r requirements.txt` instead.

### 2. Start the Backend Server

Run the following command in your project directory:

```bash
uvicorn server.main:app --reload
```

- The server will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger (API docs) will be at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 3. Open the Client

Open `client/index.html` in your web browser (double-click or use `File > Open`).

## How to Use the Program

### A. From the Client Web Page

1. **Создать сервер** — Click to create a new server. A server ID will appear.
2. **Подключиться к SSE** — (Optional) Connects to the server for real-time events.
3. **Введите имя** — Enter your name.
4. **Отправить Say Hello** — Click to send your name to the server and get a greeting.
5. **Очистить** — Clears the server response.

> **Note:** If you restart the backend server, you must create a new server from the client before using other features.

### B. Using Swagger (API Docs)

1. Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Use the `POST /api/mcp/server/create` endpoint to create a server. Copy the `server_id` from the response.
3. Use the `POST /api/mcp/tools/call/{server_id}` endpoint to call the tool. **Important:**
   - In the `server_id` field, paste the ID you got from the previous step.
   - In the request body, use this format:

```json
{
  "name": "Say Hello",
  "arguments": {
    "name": "Mike"
  }
}
```

- Do **not** use `{ "additionalProp1": {"Mike"} }` — this will not work.

## Troubleshooting

- If you see a 404 error when connecting to SSE or calling a tool, create a new server and use the new server ID.
- If the client buttons are disabled, create a new server first.

## Notes

- The backend uses in-memory storage. All data is lost when the server restarts.
- For persistent storage, a database or file-based solution is needed.

---

Enjoy using MCP Debugger (Demo)!
