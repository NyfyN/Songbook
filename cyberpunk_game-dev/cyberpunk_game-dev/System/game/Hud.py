import pygame
from typing import Tuple
from .Player import Player


class Hud:
    def __init__(self, screen: pygame.Surface, config: dict,
                 health: int, current_healt: int,
                 resource: int, current_resource: int,
                 exp: int, level: int,
                 ) -> None:  # ! Add pos: Tuple[int, int] argument
        self.screen = screen
        self.config = config
        self.width = screen.get_width()
        self.height = screen.get_height()
        # self.pos = pos
        self.player_health = health // 50
        self.max_player_health = health
        self.level = Player.level
        self.max_exp = self.level * 100

        # * Skill icons (placeholders)
        self.skill_icons = [
            pygame.Surface((50, 50)),
            pygame.Surface((50, 50)),
            pygame.Surface((50, 50)),
            pygame.Surface((50, 50)),
        ]

        for icon in self.skill_icons:
            icon.fill((100, 100, 100))  # * Placeholder color for skill icons

        self.update()

    def update(self):
        self.exp = Player.exp

    def draw_resource_circle(self, type: str):
        # * Position for the health circle (bottom left corner)
        radius = 100
        center_x = radius + 10  # Adding some padding
        center_y = self.height - radius - 10  # Adding some padding
        health_ratio = self.player_health / self.max_player_health
        end_angle = int(360 * health_ratio)

        # * Draw health circle background
        if type == "health":
            pygame.draw.circle(self.screen, (255, 0, 0),
                               (center_x, center_y), radius)
        # * Draw current health as an arc
        pygame.draw.arc(self.screen, (0, 255, 0), (center_x - radius,
                        center_y - radius, 2 * radius, 2 * radius), 0, end_angle, radius)

    def draw_skill_icons(self):
        # * Position for skill icons (center bottom, above the experience bar)
        icon_size = 50
        spacing = 10
        total_width = len(self.skill_icons) * icon_size + \
            (len(self.skill_icons) - 1) * spacing
        start_x = (self.width - total_width) // 2
        y = self.height - 100  # Position above the experience bar

        for i, icon in enumerate(self.skill_icons):
            x = start_x + i * (icon_size + spacing)
            self.screen.blit(icon, (x, y))

    def draw_experience_bar(self):
        # * Position for the experience bar (center bottom)
        exp_bar_length = 400
        exp_bar_height = 20
        # exp_ratio = (self.exp / self.max_exp) / self.level
        exp_ratio = self.exp / self.max_exp
        # current_exp_length = (exp_bar_length * exp_ratio)
        # Calculate segment length based on next level experience
        segment_length = exp_bar_length / self.max_exp
        current_exp_length = exp_bar_length * exp_ratio

        x = (self.width - exp_bar_length) // 2
        y = self.height - 40  # Adding some padding from the bottom

        # Draw experience bar background
        pygame.draw.rect(self.screen, (128, 128, 128),
                         (x, y, exp_bar_length, exp_bar_height))

        # Draw current experience as segments
        for i in range(self.max_exp):
            if i < self.exp:
                segment_x = x + i * segment_length
                pygame.draw.rect(self.screen, (255, 255, 0),
                                 (segment_x, y, segment_length, exp_bar_height))
        """
        TODO: make the length of the experience bar\ 
        TODO: dependent on the level and the amount of\
        TODO: experience needed for the next level
        """
        # * Center the experience bar horizontally
        x = (self.width - exp_bar_length) // 2
        y = self.height - 40  # Adding some padding from the bottom
        # * Draw experience bar background
        pygame.draw.rect(self.screen, (128, 128, 128),
                         (x, y, exp_bar_length, exp_bar_height))
        # * Draw current experience
        pygame.draw.rect(self.screen, (255, 255, 0),
                         (x, y, current_exp_length, exp_bar_height))

    def draw(self, type: str):
        # self.draw_mana_circle()
        self.draw_experience_bar()
        self.draw_resource_circle(type)
        self.draw_skill_icons()
