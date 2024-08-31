from State import State


class Cell:
    def __init__(self, state):
        self.state:State = State.EMPTY

    def __eq__(self, other):
        return self.state == other.state
