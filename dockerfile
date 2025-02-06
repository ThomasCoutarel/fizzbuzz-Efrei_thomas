FROM python:3.12.4
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir pytest

RUN pytest main.py

CMD ["python", "main.py"]
