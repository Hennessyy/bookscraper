FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]

#Removed since transition to gunicorn
# ENTRYPOINT ["python"]

# CMD ["app.py"]
