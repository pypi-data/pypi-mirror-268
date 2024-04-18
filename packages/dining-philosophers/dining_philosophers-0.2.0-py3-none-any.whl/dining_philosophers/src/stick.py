"""Stick (or fork) representation for the dining philosophers problem module"""

class Stick:
    """Stick class for the dining philosophers problem"""

    def __init__(self, idx : int) -> None:
        self.idx = idx
        self.is_taken : bool = False
