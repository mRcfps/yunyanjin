FROM python:3.5

ENV PYTHONUNBUFFERED=1

# Move the codebase to /web in the container
RUN mkdir /web
ADD . /web/
WORKDIR /web

# Install all dependencies, make db migrations and load db fixture
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ \
    -r requirements.txt \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic \
    && python manage.py loaddata fixture.json

# Set the source code as a volume to be shared with nginx
VOLUME [ "/web" ]

EXPOSE 8000

CMD [ "gunicorn", "yunyanjin.wsgi", "-b", "0.0.0.0:8000" ]
