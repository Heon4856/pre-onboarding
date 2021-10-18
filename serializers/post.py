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


class PostListSchema(Schema):
    post_list = fields.List(fields.Nested(PostSchema))


class CreatePostRequestSchema(Schema):
    subject = fields.String(allow_none=False)
    content = fields.String(allow_none=False)