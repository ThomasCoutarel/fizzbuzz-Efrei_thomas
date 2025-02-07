FROM python:3.12.4

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pytest

RUN pytest --maxfail=1 --disable-warnings -q

CMD ["python", "test_fizzbuzz.py"]
