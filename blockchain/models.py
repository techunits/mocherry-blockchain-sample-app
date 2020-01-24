from mongoengine import Document, fields
import datetime

class Article(Document):
    title = fields.StringField(required=True, max_length=255)
    description = fields.StringField(required=False)
    tags = fields.ListField(required=False)
    created_on = fields.DateTimeField(required=True, default=datetime.datetime.utcnow)
    modified_on = fields.DateTimeField(required=True)
