FROM python:3.8-slim-buster

WORKDIR /pss_app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN pip3 install -e .

ENV FLASK_APP pss_app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]