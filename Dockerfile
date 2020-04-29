FROM python:3.8
COPY . /app
RUN pip install -r /app/requirements.txt
CMD ["'python", "/app/src/app.py"]
