FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /crypto

COPY requirements.txt /crypto/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /crypto/

EXPOSE 8000

CMD ["gunicorn", "cryptocurrency.wsgi:application", "--bind", "0.0.0.0:8000"]
