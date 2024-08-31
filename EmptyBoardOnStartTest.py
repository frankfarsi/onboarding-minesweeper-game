import unittest


class EmptyBoardOnStartTest(unittest.TestCase):

    def test_board_is_empty_on_start(self):
        self.given_the_game_is_not_started()
        self.when_the_game_is_started()
        self.then_the_board_is_empty()

    def given_the_game_is_not_started(self):
        pass

    def when_the_game_is_started(self):
        pass

    def then_the_board_is_empty(self):
        pass
