import random

from collections import namedtuple

Transition = namedtuple("Transition",
                        ("state", "reward", "done", "action", "next_state"))


class Meomory:
    def __init__(self, capacity, batch_size):
        self.capacity = capacity
        self.batch_size = batch_size
        self.memory = []
        self.memory_counter = 0

    def sample(self):
        return random.sample(self.memory, self.batch_size)

    def add(self, *transition):
        self.memory.append(Transition(*transition))
        if len(self.memory) > self.capacity:
            self.memory.pop(0)
        assert len(self.memory) <= self.capacity
