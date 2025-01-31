import pygame
from typing import Tuple
from System.game.Player import Player


def draw_text(screen: pygame.Surface, text: str, size: int,
              color: Tuple[int, int, int], pos: Tuple[int, int]) -> None:

    font = pygame.font.SysFont(None, size)
    lines = text.split('\n')
    x, y = pos
    for line in lines:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(topleft=(x, y))
        screen.blit(text_surface, text_rect)
        y += text_surface.get_height()


def debug(screen: pygame.Surface, config: dict, clock: pygame.time.Clock):
    # TODO: turn it into good debug function
    draw_text(screen,
              'fps={}\nmouse_pos.x={}\nmouse_pos.y={}\nlevel={}\
              \ncurrent_exp={}\nmax_exp={}'.format(round(clock.get_fps()),
                                                   pygame.mouse.get_pos()[
                  0],
                  pygame.mouse.get_pos()[1],
                  Player.level,
                  Player.exp,
                  Player.max_exp),
              30,
              config["color_white"],
              (10, 10))
