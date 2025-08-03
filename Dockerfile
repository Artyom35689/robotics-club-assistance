FROM python:3.11-slim-bullseye

# Установка системных зависимостей
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/ws

# Обновляем pip и устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install python-telegram-bot

# Оставляем установку зависимостей на runtime (из volume)
CMD ["bash"]
