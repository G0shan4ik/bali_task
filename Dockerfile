FROM chetan1111/botasaurus:latest

WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN apt update -y && apt install gcc -y


COPY pyproject.toml .

RUN rm -rf build
RUN poetry install


ENTRYPOINT ["poetry", "run", "dev"]
#CMD ["python", "main.py"]