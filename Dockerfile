FROM python:3.11-buster
#
RUN pip install poetry==1.4.2
#
WORKDIR /app
COPY pyproject.toml poetry.lock .   /
COPY src/. ./
# 
RUN poetry install --without dev
 
EXPOSE 5000
CMD ["poetry","run","python","cli.py", "run"]
