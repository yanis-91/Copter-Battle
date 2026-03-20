import pygame

SPEED = 5

class Obstacle:
    def __init__(self, x: int, y: int, image : pygame.Surface, is_transparent: bool, lives: int, mobile: bool, armed: bool):
        self.x = x
        self.y = y
        self.image = image
        self.is_transparent = is_transparent
        self.lives = lives
        self.mobile = mobile
        self.armed = armed
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self):
        if self.mobile:
            while self.lives > 0:
                self.x -= SPEED
                self.y -= SPEED
                self.y += SPEED
                self.rect.topleft = (self.x, self.y)

    
    def shoot(self):
        if self.armed:
            pass

    def take_damage(self):       
        self.lives -= 1
        if self.lives <= 0:
            self.is_transparent = True

    def check_collision(self, other_rect):
        return self.rect.colliderect(other_rect)
