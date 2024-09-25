FROM python:3.11

WORKDIR /code

RUN apt update
RUN apt install -y cron
COPY ml-work-cronjob /etc/cron.d/ml-work-cronjob
RUN crontab /etc/cron.d/ml-work-cronjob
RUN apt install -y vim

COPY src/mnist/main.py /code/
COPY run.sh /code/run.sh

RUN pip install --no-cache-dir --upgrade git+https://github.com/hamsunwoo/mnist.git@0.6.7
#RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["sh", "run.sh"]
