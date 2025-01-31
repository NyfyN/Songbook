import pygame


class Player:
    level = 1
    health = 100
    exp = 10
    max_exp = level * 100
    resources = [
        "mana",
        "fury",
        "nature",
        "light",
        "focus"
        # TODO: Thinking about self refill of resources
    ]

    # * Add parameter about resources when Player is creating
    def __init__(self, screen: pygame.Surface):
        self.resource = "mana"  # * Default resource

    @classmethod
    def set_max_exp(cls):
        cls.max_exp = cls.level * 100

    @classmethod
    def add_exp(cls):
        if cls.exp <= (cls.max_exp - 10):
            cls.exp += 10
        else:
            cls.level_up()
        return cls.exp

    @classmethod
    def level_up(cls):
        cls.level += 1
        cls.set_max_exp()
        cls.health += 10
        cls.exp = 0

    # @classmethod
    # # def level(cls):
    # #     return cls.level
