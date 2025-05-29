import uuid


def generate_server_id():
    """Генерация уникального идентификатора сервера."""
    return str(uuid.uuid4())
