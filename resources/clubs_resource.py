from flask import jsonify
from flask_restful import Resource


class ClubsResource(Resource):

    def get(self):
        response = {
            'clubs': self.__clubs,
            'statusCode': 200
        }
        return jsonify(response)

    @classmethod
    def init_data(cls, clubs):
        cls.__clubs = clubs
        return cls
