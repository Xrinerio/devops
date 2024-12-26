FROM python:3.12-slim
RUN python3 -m venv /opt/venv

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 3000

CMD ["python", "app.py"]