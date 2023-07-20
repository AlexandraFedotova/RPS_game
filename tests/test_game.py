from game import rps_game


class TestGame:
    def setup_method(self):
        self.test_game = rps_game

    def test_rules(self):
        right_rules = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
        assert right_rules == self.test_game.rules

    def test_moves(self):
        right_moves = ["rock", "paper", "scissors"]
        assert right_moves == self.test_game.moves

    def test_check_player_move(self):
        valid_move = "paper"
        invalid_move = "water"
        assert True == self.test_game.check_player_move(valid_move)
        assert False == self.test_game.check_player_move(invalid_move)
