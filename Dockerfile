FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install -r app-requirements.txt

ENV FLASK_APP=calculator.py
ENV FLASK_DEBUG=True

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]