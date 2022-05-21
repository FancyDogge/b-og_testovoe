FROM python:alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

EXPOSE 8000

COPY . .

RUN pip install -r requirements.txt

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]