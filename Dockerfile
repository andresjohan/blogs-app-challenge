FROM python:3.9

WORKDIR /app

COPY requirements.txt .

COPY app .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

#RUN python manage.py makemigrations
#RUN python manage.py migrate


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]












