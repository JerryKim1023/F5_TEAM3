FROM python:3.9-slim AS builder

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

FROM python:3.9-slim-buster
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

WORKDIR /usr/src/app

COPY . .

WORKDIR ./team3Challenge

#ADD templates templates
#
#ADD app.py .
#
#ADD utils.py .

CMD ["python3", "manage.py", "runserver", "0:8000"]
# 아래처럼 할건데 CMD를 여러개 적어주면 되나?
#      - run: pip install -r requirements.txt
#      - run: python manage.py makemigrations
#      - run: python manage.py migrate
#      - run: python manage.py test



EXPOSE 8000