import pygame
import os
from System.menu.Menu import MenuScreen
from System.config.Config import Config


def check_file(path: str) -> str:
    if os.path.exists(path):
        return path
    else:
        raise FileNotFoundError(f"File '{path}' does not exist.")


def main() -> None:
    config_file = Config(check_file("System/config/game.ini"))
    config = config_file.configurate()

    running = True
    playing = True
    mode = pygame.FULLSCREEN
    resolution = config["screen_size"]

    pygame.init()
    pygame.mixer.init()
    if config["fullscreen"][0] == 1:
        resolution = (0, 0)  # * (0,0) is default resolution for fullscreen
        screen = pygame.display.set_mode(resolution, mode)
    else:
        screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()

    while running:
        # * Menus here
        MenuScreen(screen, config, clock).run()


if __name__ == "__main__":
    main()
