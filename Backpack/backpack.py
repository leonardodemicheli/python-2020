backpacks = ['backpack1', 'backpack2', 'backpack3', 'backpack4']

class Backpack:
    players = []
    def __init__(self):

        def add(self):
            backpacks.append('backi')
    def init_players(self):
        self.players = [{'name' : '', 'score' : 0, 'backpack' : []},
                   {'name' : '', 'score' : 0, 'backpack' : []}]
        return self.players

    def set_name(self, player, name):
        self.players[player].update({'name' : name})

    def get_name(self, player):
        return self.players[player]['name']

    def get_info(self):
        return self.players

    def add_backpack(self, player, item):
        self.players[player]['backpack'].append(item)

    def remove_backpack(self, player, item):
        self.players[player]['backpack'].remove(item)
