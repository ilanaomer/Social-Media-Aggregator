from pprint import pprint

import requests


# r = requests.get("http://worldcup.sfg.io/matches")
# game = r.json()
# for g in game:
#     print("{} - {}: {}-{}".format(g['home_team']['country'],g['away_team']['country'],g['home_team']['goals'],g['away_team']['goals']))

# pprint(game[0])

r2 = requests.get("http://api.openweathermap.org/data/2.5/weather",{'APIID'='f579dd56dbff7a93a29822f61c87d539'})