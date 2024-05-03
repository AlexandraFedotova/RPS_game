#Dockerfile
FROM python:3.13-rc-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY game/ ./game
CMD python game/main.py
EXPOSE 5000