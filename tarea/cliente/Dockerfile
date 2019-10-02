# Same thing than the 'server' Dockerfile.
FROM python:latest

# Same thing than the 'server' Dockerfile.
# We import 'client.py' in '/client/' folder.
ADD cliente.py /cliente/

# I would like to introduce something new, the 'WORKDIR' command.
# This command changes the base directory of your image.
# Here we define '/cliente/' as base directory.
WORKDIR /cliente/
EXPOSE 5000
CMD python cliente.py
