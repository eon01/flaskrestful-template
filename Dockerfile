FROM python:3.4
WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD app.conf .
ADD . .
EXPOSE 5000
ENTRYPOINT python app.py
