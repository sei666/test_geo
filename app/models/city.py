import datetime

from .db import db
import mongoengine_goodjson as gj

class City(gj.Document):
    city = db.StringField(required=True, unique=True)
    pointLocation = db.PointField()

