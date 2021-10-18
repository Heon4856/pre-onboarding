from marshmallow import Schema, fields



class  SignupRequestSchema(Schema):
    username = fields.String(allow_none=False)
    password = fields.String(allow_none=False)