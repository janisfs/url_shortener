FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY url_shortener.py .

CMD ["uvicorn", "url_shortener:app", "--host", "0.0.0.0", "--port", "8000"]
