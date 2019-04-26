from flask import Flask
from resources import PlayerByNameResource, PlayersByClubResource, PlayersByNationalityResource, NationalityResource, \
    ClubsResource
from utilities import get_players_data, initalize_rest_api, get_countries, get_clubs

players_data = get_players_data()
countries = get_countries()
clubs = get_clubs()

routes = [
    {'controller': PlayerByNameResource.init_data(players_data),
     'endpoint': '/player/name/<string:name>'},
    {'controller': NationalityResource.init_data(countries),
     'endpoint': '/nationalities'},
    {'controller': ClubsResource.init_data(clubs),
     'endpoint': '/clubs'},
    {'controller': PlayersByNationalityResource.init_data(players_data),
     'endpoint': '/player/nationality/<string:encrypted_nationality_name>'},
    {'controller': PlayersByClubResource.init_data(players_data),
     'endpoint': '/player/club/<string:encrypted_club_name>'},
]

app = Flask(__name__)
initalize_rest_api(app, routes)

if __name__ == '__main__':
    app.run(debug=True)
