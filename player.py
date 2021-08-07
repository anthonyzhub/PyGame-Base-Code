import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, gameClass, xPosition, yPosition) -> None:

        # Initialize parent class
        super().__init__()

        # Save parameters
        self.gameClass = gameClass
        self.xPosition = xPosition
        self.yPosition = yPosition