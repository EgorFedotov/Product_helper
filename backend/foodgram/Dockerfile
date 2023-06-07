FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]