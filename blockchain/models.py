from mongoengine import Document, fields
import datetime

class BlockChain(Document):
    index = fields.IntegerField(required=True)
    previous_hash = fields.StringField(required=True)
    data = fields.StringField(required=True)
    created_on = fields.DateTimeField(required=True, default=datetime.datetime.utcnow)
    modified_on = fields.DateTimeField(required=True)
