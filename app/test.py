from schematics.models import Model
from schematics.types import StringType


class Person(Model):
    name = StringType()


p = Person()
p.name = 'Fiona Apple'
p.hug = '1'
p.validate()
