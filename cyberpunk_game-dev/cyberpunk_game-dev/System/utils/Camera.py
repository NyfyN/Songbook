import pygame


class Camera:
    def __init__(self, screen: pygame.Surface):
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.scroll = pygame.Vector2(0, 0)
        self.screen = screen
        self.dx = 0
        self.dy = 0
        self.speed = 25
        self.zoom_info = False

    def update(self):
        mouse_position = pygame.mouse.get_pos()

        # * Logic for x axis camera movement
        if mouse_position[0] > self.width * 0.97:
            self.dx = -self.speed
        elif mouse_position[0] < self.width * 0.03:
            self.dx = self.speed
        else:
            self.dx = 0

        # * Logic for y axis camera movement
        if mouse_position[1] > self.height * 0.97:
            self.dy = -self.speed
        elif mouse_position[1] < self.height * 0.03:
            self.dy = self.speed
        else:
            self.dy = 0

        # * Update camera
        self.scroll.x += self.dx
        self.scroll.y += self.dy

        # * Zoom camera
    def zoom(self):
        if self.zoom:
            scale = 3
            print("HERE")
            self.screen = pygame.transform.rotozoom(self.screen, 0, scale)
        else:
            scale = 1

        # TODO: Make camera positions dependent on the player's position.
        # TODO: Add blocking the camera from going beyond the map range
