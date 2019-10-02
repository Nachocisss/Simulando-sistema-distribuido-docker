FROM python:latest

RUN apt-get update 
RUN apt-get -y install python
COPY servidor.py /servidor/
EXPOSE 5000

# I would like to introduce something new, the 'WORKDIR' command.
# This command changes the base directory of your image.
# Here we define '/server/' as base directory (where all commands will be executed).
WORKDIR /app
#CMD python servidor.py
