import pygame
import sys
from typing import Tuple
from System.game.Game import Game

class MenuScreen():
    def __init__(self, screen: pygame.Surface, config_dict: dict, clock: pygame.time.Clock) -> None:
        self.screen = screen
        self.config_dict = config_dict
        self.clock = clock
        self.running = True

        # Set fonts
        self.title_font = pygame.font.SysFont('Arial', 74)
        self.button_font = pygame.font.SysFont('Arial', 50)

        # Game title
        self.title_text = self.title_font.render("Test Game", True, self.config_dict["color_white"])
        self.title_rect = self.title_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 4))

        # Positioning variables
        base_y = self.screen.get_height() // 2
        step_y = 100

        # Buttons
        ## Start button
        self.start_button_text = self.button_font.render("Start", True, self.config_dict["color_white"])
        self.start_button_rect = self.start_button_text.get_rect(center=(self.screen.get_width() // 2, base_y))

        ## Load button
        self.load_button_text = self.button_font.render("Load", True, self.config_dict["color_white"])
        self.load_button_rect = self.load_button_text.get_rect(center=(self.screen.get_width() // 2, base_y + step_y))

        ## Save button
        self.save_button_text = self.button_font.render("Save", True, self.config_dict["color_white"])
        self.save_button_rect = self.save_button_text.get_rect(center=(self.screen.get_width() // 2, base_y + 2 * step_y))

        ## Options button
        self.options_button_text = self.button_font.render("Options", True, self.config_dict["color_white"])
        self.options_button_rect = self.options_button_text.get_rect(center=(self.screen.get_width() // 2, base_y + 3 * step_y))

        ## Exit button
        self.exit_button_text = self.button_font.render("Quit", True, self.config_dict["color_white"])
        self.exit_button_rect = self.exit_button_text.get_rect(center=(self.screen.get_width() // 2, base_y + 4 * step_y))

    def event_handler(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button_rect.collidepoint(event.pos):
                    self.running = False
                    Game(self.screen, self.clock, self.config_dict).run()
                elif self.exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def draw_menu(self):
        self.screen.fill(self.config_dict["color_black"])  # Later replace with texturing and images
        self.screen.blit(self.title_text, self.title_rect)

        # Change button color
        ## Start button
        if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
            self.start_button_text = self.button_font.render("New game", True, self.config_dict["button_hover_color"])
        else:
            self.start_button_text = self.button_font.render("New game", True, self.config_dict["color_white"])
        self.start_button_rect = self.start_button_text.get_rect(center=(self.screen.get_width() // 2, self.start_button_rect.centery))

        ## Load button
        if self.load_button_rect.collidepoint(pygame.mouse.get_pos()):
            self.load_button_text = self.button_font.render("Load game", True, self.config_dict["button_hover_color"])
        else:
            self.load_button_text = self.button_font.render("Load game", True, self.config_dict["color_white"])
        self.load_button_rect = self.load_button_text.get_rect(center=(self.screen.get_width() // 2, self.load_button_rect.centery))

        ## Save button
        if self.save_button_rect.collidepoint(pygame.mouse.get_pos()):
            self.save_button_text = self.button_font.render("Save game", True, self.config_dict["button_hover_color"])
        else:
            self.save_button_text = self.button_font.render("Save game", True, self.config_dict["color_white"])
        self.save_button_rect = self.save_button_text.get_rect(center=(self.screen.get_width() // 2, self.save_button_rect.centery))

        ## Options button
        if self.options_button_rect.collidepoint(pygame.mouse.get_pos()):
            self.options_button_text = self.button_font.render("Options", True, self.config_dict["button_hover_color"])
        else:
            self.options_button_text = self.button_font.render("Options", True, self.config_dict["color_white"])
        self.options_button_rect = self.options_button_text.get_rect(center=(self.screen.get_width() // 2, self.options_button_rect.centery))

        ## Exit button
        if self.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
            self.exit_button_text = self.button_font.render("Quit", True, self.config_dict["button_hover_color"])
        else:
            self.exit_button_text = self.button_font.render("Quit", True, self.config_dict["color_white"])
        self.exit_button_rect = self.exit_button_text.get_rect(center=(self.screen.get_width() // 2, self.exit_button_rect.centery))

        # Drawing buttons
        self.screen.blit(self.start_button_text, self.start_button_rect)
        self.screen.blit(self.load_button_text, self.load_button_rect)
        self.screen.blit(self.save_button_text, self.save_button_rect)
        self.screen.blit(self.options_button_text, self.options_button_rect)
        self.screen.blit(self.exit_button_text, self.exit_button_rect)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.event_handler()
            self.draw_menu()
            self.clock.tick(60)
