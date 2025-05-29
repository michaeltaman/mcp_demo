let serverId = null;
let eventSource = null;

document.getElementById('create-server').addEventListener('click', async () => {
  const response = await fetch('http://127.0.0.1:8000/api/mcp/server/create', {
    method: 'POST',
  });
  if (!response.ok) {
    alert('Ошибка при создании сервера');
    return;
  }
  const data = await response.json();
  serverId = data.server_id;
  document.getElementById('server-id').textContent = serverId;
  document.getElementById('connect-sse').disabled = false;
  document.getElementById('send-hello').disabled = false;
});

document.getElementById('connect-sse').addEventListener('click', () => {
  if (!serverId) return;
  eventSource = new EventSource(
    `http://127.0.0.1:8000/api/mcp/sse/${serverId}`
  );
  eventSource.onopen = () => {
    document.getElementById('status').textContent = 'Connected';
    document.getElementById('status').classList.remove('disconnected');
    document.getElementById('status').classList.add('connected');
    document.getElementById('send-hello').disabled = false;
  };
  eventSource.onmessage = (event) => {
    console.log('Received message:', event.data);
  };
  eventSource.onerror = () => {
    document.getElementById('status').textContent = 'Disconnected';
    document.getElementById('status').classList.remove('connected');
    document.getElementById('status').classList.add('disconnected');
  };
});

// 🔥 Добавляем обработчик для кнопки "Отправить Say Hello"
document.getElementById('send-hello').addEventListener('click', async () => {
  const name = document.getElementById('name').value;
  if (!serverId) {
    alert('Сначала создайте сервер');
    return;
  }
  const response = await fetch(
    `http://127.0.0.1:8000/api/mcp/tools/call/${serverId}`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: 'Say Hello',
        arguments: { name: name || 'Guest' },
      }),
    }
  );
  if (!response.ok) {
    alert('Ошибка при отправке запроса');
    return;
  }
  const data = await response.json();
  document.getElementById('response').textContent = JSON.stringify(
    data,
    null,
    2
  );
  updateClearButtonVisibility();
});

// Add clear response button functionality
document.getElementById('clear-response').addEventListener('click', () => {
  document.getElementById('response').textContent = '';
  document.getElementById('clear-response').style.display = 'none';
});

// Function to update clear button visibility
function updateClearButtonVisibility() {
  const response = document.getElementById('response');
  const clearButton = document.getElementById('clear-response');
  clearButton.style.display = response.textContent.trim() ? 'block' : 'none';
}

// Initialize clear button visibility
updateClearButtonVisibility();
