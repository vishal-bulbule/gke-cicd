FROM python:3.8

EXPOSE 8081
WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

CMD ["python", "app.py"]