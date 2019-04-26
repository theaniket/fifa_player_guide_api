from flask import jsonify
from flask_restful import Resource


class NationalityResource(Resource):

    def get(self):
        response = {
            'nationalities': self.__countries,
            'statusCode': 200
        }
        return jsonify(response)

    @classmethod
    def init_data(cls, countries):
        cls.__countries = countries
        return cls