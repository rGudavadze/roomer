FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY requirements.txt /opt/app/

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . /opt/app/
RUN mkdir -p /opt/app/static

RUN useradd -ms /bin/bash roomer
RUN chown -R roomer:roomer /opt/app

ADD scripts/docker-entrypoint.sh /home/roomer/docker-entrypoint.sh
ADD scripts/check_service.py /home/roomer/check_service.py

RUN chmod +x /home/roomer/docker-entrypoint.sh
USER roomer

ENTRYPOINT ["/home/roomer/docker-entrypoint.sh"]
