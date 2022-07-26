###########
# BUILDER #
###########

FROM python:3.8 as builder

# set work directory
WORKDIR /usr/src/ipr

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install wheel
USER root
RUN pip wheel --no-cache-dir --wheel-dir /usr/src/ipr/wheels -r requirements.txt

#########
# FINAL #
#########
FROM python:3.8

USER root

# create directory for the app user
RUN mkdir -p /home/ipr

# create the app user
RUN groupadd ipr && useradd -g ipr -r ipr

# create the appropriate directories
ENV HOME=/home/ipr
ENV APP_HOME=/home/ipr/src
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
COPY --from=builder /usr/src/ipr/wheels /wheels
COPY --from=builder /usr/src/ipr/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY ./src/ipr $APP_HOME
# RUN rm -rf $APP_HOME/tests

# chown all the files to the app user
RUN chown -R ipr:ipr $APP_HOME

# change to the app user
USER ipr

CMD python main.py