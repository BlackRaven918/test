FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ltitool.py .
EXPOSE 5000
CMD [ "python","-m","flask","--app","ltitool.py","run","--host","0.0.0.0","--no-reload" ]