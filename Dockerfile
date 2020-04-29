FROM python:3.8
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r /app/requirements.txt
COPY . .
CMD ["python", "/app/src/app.py"]
