from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
import os
from resource.Average import Average

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/averages": {"origins": "http://localhost"}})
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

api.add_resource(Average, "/averages")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 8080), debug=True)