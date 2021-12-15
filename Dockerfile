#Deriving the latest base image
FROM python:latest

# 
WORKDIR /app/src/main

# copy the dependencies file to the working directory
ADD requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

RUN mkdir -p ../../data/

#to COPY the remote file at working directory in container
ADD ./src/main/main.py ./
ADD ./src/main/queries.py ./

#Now it looks like this 'app/src/main/main.py'

ADD ./data/result.csv ../../data/
ADD ./data/consoles.csv ../../data/

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python3", "./main.py"]
