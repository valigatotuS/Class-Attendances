# init a base image
FROM python:3.8-alpine
# define the present working directory 
WORKDIR /test
# copy contents inside the working directory 
COPY . .
# install dependencies of our flask app
RUN pip install -r requirements.txt
# defining commands to start our container
CMD ["python", "app.py"]