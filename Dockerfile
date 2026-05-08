# 1. Base image: Python 3.10 slim version use kar rahe hain taaki image size chota rahe
FROM python:3.10-slim-buster

# 2. Working directory set karein
WORKDIR /app

# 3. System dependencies install karein (Tgcrypto aur network tools ke liye zaroori hain)
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. requirements.txt copy karein aur install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Baaki saara code copy karein
COPY . .

# 6. Port expose karein (Render ka default 8080 hai)
EXPOSE 8080

# 7. Bot ko run karne ki command
CMD ["python3", "bot.py"]
