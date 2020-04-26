# https://pypi.org/project/nba-api/

from pandas import *
import matplotlib.pyplot as plt
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder


def one_dict(list_dict):  # create dictionary
    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict


# create Dictionary
dict_ = {'a': [11, 21, 31], 'b': [12, 22, 32]}

# creat instance of Dataframe
df = DataFrame(dict_)
print(type(df))
print('\ndataframe head:', df.head())
print('\ndataframe mean:', df.mean())
print('============================================')

# https://pypi.org/project/nba-api/

nba_teams = teams.get_teams()
print('\nfirst 3 teams from  teams List\n', nba_teams[0:3])

# to make it easer we create a dictionary ( by function one:dict)
# then convert the dict to dataframe
dict_nba_team = one_dict(nba_teams)
df_teams = DataFrame(dict_nba_team)
print('\nConvert the Dict to Table:\n', df_teams.head())

#
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print(df_warriors)

id_warriors = df_warriors[['id']].values[0][0]
# we now have an integer that can be used   to request the Warriors information
print('Warriors unique id:', id_warriors)
print('=============================================================')
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
print('\nJSON file:\n', gamefinder.get_json())
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
games = gamefinder.get_data_frames()[0]
print('All the games the Warriors played \n:', games.head())
