from marshmallow import Schema, fields



class  AuthRequestSchema(Schema):
    username = fields.String(allow_none=False)
    password = fields.String(allow_none=False)

class TokenSchema(Schema):
    access_token = fields.Str()
