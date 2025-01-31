import pygame
import sys
from .World import World
from System.utils.utils import debug
from System.utils.Camera import Camera
from .Hud import Hud
from .Player import Player


class Game:
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, config_dict: dict):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.config_dict = config_dict
        self.tile_size = float(self.config_dict["tile_size"][0])
        self.info_activate = False

        # * Initialize the world
        self.world = World(100, 100, self.width, self.height, self.config_dict)

        # * Initialize the camera
        self.camera = Camera(self.screen)

        self.player = Player(self.screen)
        self.hud = Hud(self.screen, self.config_dict,
                       self.player.health, 100,
                       self.player.resource, 100,
                       self.player.exp, self.player.level)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.event_handler()
            self.update()
            self.draw_game()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_F1:
                    self.info_trigger()
                if event.key == pygame.K_F2:
                    Player.add_exp()
                    self.hud.update()
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    print("LOREM")
                    self.camera.zoom()

    def update(self):
        self.camera.update()

    def info_trigger(self):
        self.info_activate = not self.info_activate

    def draw_game(self):

        self.screen.fill(self.config_dict["color_black"])
        self.screen.blit(self.world.dirt_tiles,
                         (self.camera.scroll.x, self.camera.scroll.y))

        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_x):

                # * Render the assets
                render_position = self.world.world[x][y]["render_pos"]

                # * Render the additional tiles
                tile = self.world.world[x][y]["tile"]
                if tile != "":
                    self.screen.blit(self.world.tiles[tile],
                                     ((render_position[0] + self.world.dirt_tiles.get_width()/2 + 10 + self.camera.scroll.x,
                                       render_position[1] - self.tile_size + 10 + self.camera.scroll.y)))

        if self.info_activate:
            debug(self.screen, self.config_dict, self.clock)
        self.hud.draw("health")
        pygame.display.flip()
