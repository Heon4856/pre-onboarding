from marshmallow import Schema, fields
from model.models import Post


class PostSchema(Schema):
    class Meta:
        model = Post

    id = fields.Integer()
    subject = fields.String(allow_none=False)
    content = fields.String(allow_none=False)
    create_date = fields.DateTime(allow_none=False)
    modify_date = fields.DateTime(allow_none=True)


class CreatePostRequestSchema(Schema):
    subject = fields.String(allow_none=False)
    content = fields.String(allow_none=False)
