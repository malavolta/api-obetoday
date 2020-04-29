from flask_restful import Resource
from libs.getAverage import YADIO_RATE_USD, BTC_IN_VES, DOLARTODAY_RATE
from models.Averages import Averages
from schema.Averages import AveragesSchema


class Average(Resource):
    def get(self):
        dolartoday = DOLARTODAY_RATE()
        localbitcoin = BTC_IN_VES()
        yadio = YADIO_RATE_USD()
        averages = Averages(localbitcoin, yadio, dolartoday['dolartoday'], dolartoday['bitcoin_ref'])
        schema = AveragesSchema()
        return schema.dump(averages), 200
