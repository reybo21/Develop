players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, 
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, 
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

class Player:

    new_team = []

    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.age, self.position, self.team)

    @classmethod
    def get_team(cls, team_list):
        for player in team_list:
            cls.new_team.append(Player(player))
        return cls.new_team


new_team = Player.get_team(players)

print(new_team)
for player in new_team:
    print(player)