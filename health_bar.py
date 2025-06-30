import pygame

class HealthBar:
    def __init__(self, game, max_health, x, y, color=(0, 255, 0)):
        self.game = game
        self.screen = game.screen
        self.max_health = max_health
        self.current_health = max_health

        self.width = 200
        self.height = 20
        self.x = x
        self.y = y
        self.bg_color = (100, 100, 100)
        self.color = color  # Color for the health bar (green, red, etc.)

    def take_damage(self, amount):
        self.current_health = max(0, self.current_health - amount)

    def heal(self, amount):
        self.current_health = min(self.max_health, self.current_health + amount)

    def draw(self):
        # Background bar
        pygame.draw.rect(self.screen, self.bg_color, (self.x, self.y, self.width, self.height))

        # Foreground health bar
        health_ratio = self.current_health / self.max_health
        health_width = int(self.width * health_ratio)
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, health_width, self.height))

        # Optional: border
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.height), 2)
