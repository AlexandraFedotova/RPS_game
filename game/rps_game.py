import random


class Game:
    """
    Class represent 'Rock-paper-scissors game'
    """
    def __init__(self):
        self._moves = ["rock", "paper", "scissors"]
        self._rules = {"paper": "rock", "rock": "scissors", "scissors": "paper"}

    @property
    def moves(self):
        return self._moves

    @property
    def rules(self):
        return self._rules

    def _get_random_move(self):
        return random.choice(self._moves)

    def check_player_move(self, player_move: str):
        return True if player_move in self._moves else False

    def play(self, player_move: str):
        bot_move = self._get_random_move()
        if player_move == bot_move:
            return f"Bot move is {bot_move}. No one win"
        for winner, loser in self._rules.items():
            if player_move == winner and bot_move == loser:
                return f"Bot move is {bot_move}. Player win"
            if bot_move == winner and player_move == loser:
                return f"Bot move is {bot_move}. Bot win"
