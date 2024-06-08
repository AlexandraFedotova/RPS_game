#Dockerfile
FROM python:3.12-rc
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY game/ ./game
CMD python game/main.py
EXPOSE 80