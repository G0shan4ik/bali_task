from peewee import (
    TextField,
    Model,
    IntegerField,
    SqliteDatabase,
)

from pathlib import Path
from os import getcwd


path = Path(getcwd()).joinpath('carousel_ph.db')
db = SqliteDatabase(path)
print(path)


class BaseModel(Model):
    class Meta:
        database = db


class Products(BaseModel):
    unique_id = IntegerField(primary_key=True, null=False)
    name = TextField(null=False)
    price = TextField(null=False)
    image = TextField(null=False)
    url = TextField(null=False)


def init():
    Products.create_table(safe=True)