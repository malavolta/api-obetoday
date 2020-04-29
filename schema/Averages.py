from marshmallow import Schema, fields


class AveragesSchema(Schema):
    localbitcoin = fields.Float()
    yadio = fields.Float()
    dolartoday_usd = fields.Float()
    dolartoday_btc = fields.Float()
