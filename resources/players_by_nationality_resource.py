from flask_restful import Resource
from flask import jsonify


class PlayersByNationalityResource(Resource):

    def get(self, encrypted_nationality_name):
        nationality = str()
        for word in encrypted_nationality_name.split('%'):
            nationality += word + ' '
        nationality = nationality.strip()
        print(nationality)
        response = {
            'players': list(),
            'statusCode': 200
        }
        for player in self.__players_data:
            if nationality == player['nationality']:
                response['players'].append(player)
        return jsonify(response)

    @classmethod
    def init_data(cls, players_data):
        cls.__players_data = players_data
        return cls
