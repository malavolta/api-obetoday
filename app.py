from flask import Flask, render_template
import requests
import json
import os
from apis import average

app = Flask(__name__, template_folder='templates')


@app.route('/')
def homepage():
    btc = average.BTC_IN_VES()
    yadio = average.YADIO_RATE_USD()
    dolartoday = average.DOLARTODAY_RATE()
    return render_template('movies.html', dolarbtc=btc, yadio=yadio, dolartoday=dolartoday)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 8080), debug=True)
