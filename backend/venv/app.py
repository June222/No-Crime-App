from flask import Flask
import flask_restful as flask_restful
from flask_restful import Api
from crime import District, Population, Place, PredictCrime

app = Flask(__name__)
api = Api(app)

api.add_resource(District, '/district/')
api.add_resource(Population, '/population/')
api.add_resource(Place,'/place/')
api.add_resource(PredictCrime,'/predict/')

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)