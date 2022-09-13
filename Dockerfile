# syntax=docker/dockerfile:1

FROM python:3.10-buster
WORKDIR /prog
RUN pip install "poetry"
COPY pyproject.toml .
RUN poetry install
ADD src ./src
CMD [ "poetry", "run", "python3", "src/main.py" ]
