#Dockerfile
FROM python:3.12-rc
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py game.py ./
CMD python main.py
EXPOSE 5000