from typing import Union

from fastapi import FastAPI

service = FastAPI()


@service.get("/")
def root():
    return {"Hello": "World"}