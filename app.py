#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, traceback, configparser, os
from flask import Flask
from flask_restful import Resource, Api, reqparse

# app information
app = Flask(__name__)

# api configuration
api = Api(app)
api.prefix = "/v1"


# start configuration parser
parser = configparser.ConfigParser()
parser.read("app.conf")

# reading variables
logger_level = parser.get('logging', 'logger_level', raw = True)
handler_level = parser.get('logging', 'handler_level', raw = True)
log_format = parser.get('logging', 'log_format', raw = True)
log_file = parser.get('logging', 'log_file')

# set logger logging level
logger = logging.getLogger(__name__)
logger.setLevel(eval(logger_level))

# set handler logging level
handler = logging.FileHandler(log_file)
handler.setLevel(eval(handler_level))

# create a logging format
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


# prepare the parser
parser = reqparse.RequestParser()

parser.add_argument('arg', type=str, help='an argument')




class HelloWorld(Resource):
    def post(self, parameter):
        # parse args
        args = parser.parse_args()
        
        arg = args['arg']
        return {'parameter': parameter, 'arg': arg }
        

api.add_resource(HelloWorld, '/<string:parameter>')



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # To test this, run flask app and ``` curl  http://0.0.0.0:5000/v1/myparameter -d "arg=myarg" -X POST ```
    
    
    
