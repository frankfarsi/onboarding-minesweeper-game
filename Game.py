from Board import Board


class Game:
    def __init__(self):
        self.board :Board= Board()
        self.isRunning:bool = False

    def start(self):
        self.isRunning = True

