FROM python:3.6-alpine

WORKDIR /usr/app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

ENTRYPOINT ["python"]

CMD ["app.py"]