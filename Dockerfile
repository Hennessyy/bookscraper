FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "src.app:app", "-b", "0.0.0.0:5000"]
