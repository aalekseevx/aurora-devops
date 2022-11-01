FROM python:3.8-alpine as base
# Common deps
RUN apk --no-cache add \
    bash \
    openssl \
    postgresql-dev

 # # # # # #
 # Builder #
 # # # # # #

FROM base as builder

ENV PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.4

# System deps:
RUN apk --no-cache add \
    build-base \
#    curl \
    gcc \
#    gettext \
#    git \
    libffi-dev \
    linux-headers \
    openssl-dev \
    musl-dev

# Use pip to ensure a consistent poetry version
RUN pip install -U poetry
# Disable virtualenvs - docker is isolated enough
RUN poetry config virtualenvs.create false

# Copy the lock files first to cache dependencies
WORKDIR /install
COPY poetry.lock pyproject.toml /install/
RUN poetry install --no-interaction --no-ansi $(test "$AURORA_ENV" == production && echo "--no-dev")
# TODO(?): Separate wheel build in order not to recompile a whole lot of binaries each time


 # # # # # #
 #   App   #
 # # # # # #


FROM base as app
LABEL version="0.1"
LABEL maintainer="alekseev2002@inbox.ru"

# Set the environment - development or production
ARG AURORA_ENV

ENV AURORA_ENV=${AURORA_ENV} \
  PYTHONIOENCODING=UTF-8 \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random

# Copy prebuilt libs
COPY --from=builder /usr/local /usr/local

ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PATH "/app/scripts:${PATH}"

EXPOSE 80
WORKDIR /app
ADD . /app/
RUN chmod +x scripts/* && \
    pybabel compile -d locales -D bot

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["run-webhook"]
