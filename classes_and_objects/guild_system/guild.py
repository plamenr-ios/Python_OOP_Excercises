from project.player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player not in self.players and player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif not player.guild == "Unaffiliated" and player not in self.players:
            return f"Player {player.name} is in another guild."
        else:
            return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name):
        for i in self.players:
            if player_name == i.name:
                i.guild = "Unaffiliated"
                self.players.remove(i)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        nl = '\n'
        return f"Guild: {self.name}\n" \
               f"{nl.join(x.player_info() for x in self.players)}"



