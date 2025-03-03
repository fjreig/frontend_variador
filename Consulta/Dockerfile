#Using python
FROM python:3.11

#Copy files to your container
WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

#Running your APP
CMD [ "python", "./app.py"]