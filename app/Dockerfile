FROM python:latest
ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV DB_NAME=postgres
ENV DB_USER=postgres
ENV DB_PASS=postgres
ENV DB_HOST=flask_db
ENV DB_PORT=5432
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
