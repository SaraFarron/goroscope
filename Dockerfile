FROM python:3.11.0

RUN pip install --upgrade pip

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
