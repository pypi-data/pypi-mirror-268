"""Philosopher module"""

from typing import List

from .stick import Stick
class Philosopher:
    """Philosopher class for dining philosophers problem"""

    def __init__(self, idx : int, stick_1 : Stick, stick_2 : Stick) -> None:
        self.idx = idx
        self.is_eating : bool = False
        self.eating_log : List[bool] = []
        self.asking_log : List[bool] = []
        self.sticks : List[Stick] = [stick_1, stick_2]

    def stop_eating(self) -> None: 
        """Stop eating method for philosopher"""
        for stick in self.sticks:
            stick.is_taken = False
        self.is_eating = False

    def start_eating(self) -> None:
        """Start eating method for philosopher"""
        for stick in self.sticks:
            stick.is_taken = True
        self.is_eating = True

    def update_eating_log(self) -> None:
        """Update eating log method for philosopher"""
        self.eating_log.append(self.is_eating)
