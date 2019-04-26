from flask import jsonify, Response
from flask_restful import Resource


class PlayerByNameResource(Resource):

    def get(self, name):
        response = {
            'player': 'Not Found',
            'statusCode': 200
        }
        for player in self.__players_data:
            if name.lower() in player['name'].lower():
                response['player'] = player
                break
        return jsonify(response)

    @classmethod
    def init_data(cls, players_data):
        cls.__players_data = players_data
        return cls
