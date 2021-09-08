FROM python:3.6
COPY requirements.txt /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "Test.py"]