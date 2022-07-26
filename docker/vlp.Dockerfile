###########
# BUILDER #
###########

FROM python:3.8 as builder

# set work directory
WORKDIR /usr/src/vlp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install wheel
USER root
RUN pip wheel --no-cache-dir --wheel-dir /usr/src/vlp/wheels -r requirements.txt

#########
# FINAL #
#########
FROM python:3.8

USER root

# create directory for the app user
RUN mkdir -p /home/vlp

# create the app user
RUN groupadd vlp && useradd -g vlp -r vlp

# create the appropriate directories
ENV HOME=/home/vlp
ENV APP_HOME=/home/vlp/src
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
COPY --from=builder /usr/src/vlp/wheels /wheels
COPY --from=builder /usr/src/vlp/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY ./src/vlp $APP_HOME
# RUN rm -rf $APP_HOME/tests

# chown all the files to the app user
RUN chown -R vlp:vlp $APP_HOME

# change to the app user
USER vlp

CMD python main.py