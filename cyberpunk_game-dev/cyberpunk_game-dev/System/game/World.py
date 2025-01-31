import pygame
import random
import noise

class World:
    def __init__(self, grid_length_x: int, grid_length_y: int, width: int, height: int, config_dict: dict) -> None:
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height
        self.tile_size = config_dict["tile_size"][0]
        self.perlin_scale = grid_length_x / 2
        self.tiles = self.load_images("Data/assets")
        self.dirt_tiles = pygame.Surface((grid_length_x * config_dict["tile_size"][0] * 2, 
                                          grid_length_y * config_dict["tile_size"][0] + 2 * config_dict["tile_size"][0])).convert_alpha()
        self.world = self.create_world()

    
    def create_world(self) -> list:
        world = []

        for grid_x in range(self.grid_length_x):
            world.append([])
            for grid_y in range(self.grid_length_y):
                world_tile = self.grid_to_world(grid_x, grid_y)
                world[grid_x].append(world_tile)

                render_position = world_tile["render_pos"]
                self.dirt_tiles.blit(self.tiles["block"], (render_position[0] + self.dirt_tiles.get_width()/2,
                                                           render_position[1]))

        return world
    
    def grid_to_world(self, grid_x: int, grid_y: int) -> dict:
        #* Calculating the coordinates of a rectangle in the Cartesian coordinate system
        rect = [
            (grid_x * self.tile_size, grid_y * self.tile_size),
            (grid_x * self.tile_size + self.tile_size, grid_y * self.tile_size),
            (grid_x * self.tile_size + self.tile_size, grid_y * self.tile_size + self.tile_size),
            (grid_x * self.tile_size, grid_y * self.tile_size + self.tile_size)
        ]
        #* Convert a rectangle to an isometric polygon
        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        #* Finding the minimum X and Y coordinates in an isometric polygon
        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])
        
        seed = random.randint(1, 100)
        perlin = 100 * noise.pnoise2(grid_x/self.perlin_scale, 
                               grid_y/self.perlin_scale)

        if (perlin >= 15) or (perlin <= -35):
            tile = "tree"
        else:
            if seed == 1:
                tile = "tree"
            elif seed == 2:
                tile = "rock"
            else:
                tile = ""  #* By default we use the block as a tile

        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny],
            "tile": tile
        }
        return out
    
    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y) / 2
        return iso_x, iso_y
    
    def load_images(self, path: str) -> dict:
        #?: Change assets for something more fitting
        block = pygame.image.load(path+"/block.png").convert_alpha() 
        rock = pygame.image.load(path+"/rock.png").convert_alpha()
        tree = pygame.image.load(path+"/tree.png").convert_alpha()
        
        return {"block": block, "rock": rock, "tree": tree}
    
#TODO: Rescale the images in /Data/assets to make them fit well with grass.png