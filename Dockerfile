FROM python:3.6
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
CMD ["python", "Length_conv.py"]