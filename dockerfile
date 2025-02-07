FROM python:3.12.4

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pytest

CMD ["pytest", "test_fizzbuzz.py", "--maxfail=1", "--disable-warnings", "-q"]
