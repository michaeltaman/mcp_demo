from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from typing import Dict, Any
import asyncio
import logging
import time
from server.tools import SayHelloTool  # Исправленный импорт
from server.utils import generate_server_id  # Исправленный импорт

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

app = FastAPI()


# Middleware for logging requests and responses
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    # Log request
    logger.info(f"Request: {request.method} {request.url.path}")

    # Get response
    response = await call_next(request)

    # Calculate processing time
    process_time = time.time() - start_time

    # Log response
    logger.info(f"Response: {response.status_code} - Processed in {process_time:.3f}s")

    return response


# Разрешаем CORS для клиента
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

# Хранилище серверов по их ID
servers = {}


@app.post("/api/mcp/server/create")
async def create_server():
    server_id = generate_server_id()
    servers[server_id] = {"id": server_id, "tool": SayHelloTool()}
    return {"server_id": server_id}


@app.get("/api/mcp/sse/{server_id}")
async def stream_events(request: Request, server_id: str):
    if server_id not in servers:
        raise HTTPException(status_code=404, detail="Server not found")

    async def event_generator():
        while True:
            if await request.is_disconnected():
                break
            await asyncio.sleep(1)  # Пустой пинг каждую секунду
            yield f"event: ping\ndata: keepalive\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.post("/api/mcp/tools/call/{server_id}")
async def call_tool(server_id: str, payload: Dict[str, Any]):
    if server_id not in servers:
        raise HTTPException(status_code=404, detail="Server not found")
    tool = servers[server_id]["tool"]
    name = payload.get("name")
    if name != tool.name:
        return JSONResponse(status_code=400, content={"error": "Tool not found"})
    arguments = payload.get("arguments", {})
    result = tool.execute(arguments)
    return {"status": "success", "result": result}
