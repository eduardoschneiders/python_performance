FROM python:3.6-slim

WORKDIR /app

ADD ./requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 5000

ENV FLASK_DEBUG 1

CMD ["python", "app.py" ]
