import pandas as pd
from flask_restful import Api
import numpy as np


def get_countries():
    data_frame = pd.read_csv('data.csv')
    countries = [country for country in data_frame.iloc[:, 5].unique()]
    return countries


def get_clubs():
    data_frame = pd.read_csv('data.csv')
    clubs = [club if club is not np.nan else 'No Club' for club in data_frame.iloc[:, 9].unique()]
    return sorted(clubs)


def get_players_data():
    cols_to_use = [
        'Name', 'Age', 'Photo',
        'Nationality', 'Flag',
        'Overall', 'Potential',
        'Club'
    ]
    data_frame = pd.read_csv('data.csv', usecols=cols_to_use)
    players = data_frame.to_numpy().tolist()
    # players_name = data_frame['Name'].values
    # players_age = data_frame['Age'].values
    # players_photo = data_frame['Photo'].values
    # players_nationality = data_frame['Nationality'].values
    # players_flag = data_frame['Flag'].values
    # players_overall = data_frame['Overall'].values
    # players_potential = data_frame['Potential'].values
    # players_club = data_frame['Club'].values
    #
    # players = list(zip(players_name, players_club,
    #                    players_age, players_nationality,
    #                    players_photo, players_flag,
    #                    players_overall, players_potential))
    players_data = [dict({'name': player_name, 'age': str(player_age),
                          'club': player_club if player_club is not np.nan else 'No Club',
                          'nationality': player_nationality,
                          'photoUrl': player_photo, 'flagUrl': player_flag,
                          'overall': str(player_overall), 'potential': str(player_potential)
                          }) for (player_name, player_age,
                                  player_photo, player_nationality,
                                  player_flag, player_overall,
                                  player_potential, player_club) in players]
    return players_data


def initalize_rest_api(app, routes):
    rest_api = Api(app)
    for route in routes:
        rest_api.add_resource(route['controller'], route['endpoint'])
