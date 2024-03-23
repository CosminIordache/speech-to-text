FROM python:3.10

WORKDIR /app

COPY speech_to_text.py /app/
COPY requirements.txt /app/
COPY models/ /app/models/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "speech_to_text.py"]