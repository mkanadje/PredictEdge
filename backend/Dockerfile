FROM python:3.11-slim

WORKDIR /backend

COPY backend/ ./backend/
COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]