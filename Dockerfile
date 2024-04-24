FROM python:3.8
Add main.py .
WORKDIR /home/ezz/Desktop/CLOUD
COPY . .
RUN pip install nltk 
CMD ["python","./main.py"]