FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app

# This is a Dockerfile for building a container image that runs a Python web application
# using the Gunicorn web server. Here's what each line does:

# FROM python:3.7: This specifies the base image to use for the container, in this
#   case the official Python 3.7 image.
# COPY . /app: This copies the contents of the current directory (where the Dockerfile is located) to
#   a new directory called /app in the container.
# WORKDIR /app: This sets the working directory for the container to /app, so that all subsequent
#   commands are run from that directory.
# RUN pip install -r requirements.txt: This installs the Python packages listed in
#   requirements.txt, which should contain all the dependencies needed by the web application.
# EXPOSE $PORT: This exposes the port specified in the $PORT environment variable, so that it can
#   be accessed from outside the container.
# CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app: This sets the default command to run
#     when the container starts. It starts Gunicorn with one worker process (--workers=1), binds it
#     to the IP address 0.0.0.0 on the port specified by $PORT (--bind 0.0.0.0:$PORT), and tells it
#     to run the WSGI application contained in the app module (app:app). This assumes that the web
#     application has a app.py or app/__init__.py file with a callable WSGI application named app.


# the gunicorn command with its various options allows the container to run the web application
# and handle incoming requests in a scalable and performant manner.