from flask import Flask
from flask_restful import Resource, Api
import os
from resource.Average import Average

app = Flask(__name__)
api = Api(app)

api.add_resource(Average, "/averages")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 8080), debug=True)
