from flask_restful import Resource
from flask import jsonify


class PlayersByClubResource(Resource):

    def get(self, encrypted_club_name):
        club = str()
        for word in encrypted_club_name.split('%'):
            club += word + ' '
        club = club.strip()
        response = {
            'players': list(),
            'statusCode': 200
        }
        for player in self.__players_data:
            if club == player['club']:
                response['players'].append(player)
        return jsonify(response)

    @classmethod
    def init_data(cls, players_data):
        cls.__players_data = players_data
        return cls
