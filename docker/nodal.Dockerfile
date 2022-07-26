###########
# BUILDER #
###########

FROM python:3.8 as builder

# set work directory
WORKDIR /usr/src/nodal

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install wheel
USER root
RUN pip wheel --no-cache-dir --wheel-dir /usr/src/nodal/wheels -r requirements.txt

#########
# FINAL #
#########
FROM python:3.8

USER root

# create directory for the app user
RUN mkdir -p /home/nodal

# create the app user
RUN groupadd nodal && useradd -g nodal -r nodal

# create the appropriate directories
ENV HOME=/home/nodal
ENV APP_HOME=/home/nodal/src
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
COPY --from=builder /usr/src/nodal/wheels /wheels
COPY --from=builder /usr/src/nodal/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY ./src/nodal $APP_HOME
# RUN rm -rf $APP_HOME/tests

# chown all the files to the app user
RUN chown -R nodal:nodal $APP_HOME

# change to the app user
USER nodal

CMD python main.py