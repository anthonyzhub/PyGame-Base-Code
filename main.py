#! /usr/bin/python3

import pygame
from mainMenu import MainMenu
from settings import GameSettings

# Default screen size
DEFAULT_WIDTH = 840
DEFAULT_HEIGHT = 720

class Game:

    def __init__(self, width, height) -> None:
        
        # Initialize PyGame
        pygame.init()

        # Get screen's dimensions
        self.width = width
        self.height = height
        self.scale = 1

        # Create a window
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

        # Initialize PyGame's clock for FPS (frames-per-second)
        self.clock = pygame.time.Clock()

        # Create boolean variables to start/stop game
        self.continueGame = True
        self.showMainMenu = True
        self.showGameModeMenu = True

        # Initialize other classes
        self.settingsClass = GameSettings()
        self.mainMenu = MainMenu(self, self.settingsClass)

    def adjustScreen(self):

        # OBJECTIVE: Check if screen was readjusted

        # Get current window size
        currWidth, currHeight = self.screen.get_size()

        # If new dimensions are small, restrict screen size and exit function
        if currWidth < DEFAULT_WIDTH or currHeight < DEFAULT_HEIGHT:
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
            return

        # Compare values
        if (self.width, self.height) != (currWidth, currHeight):
            # print("Window size changed from {}x{} to {}x{}".format(self.width, self.height, currWidth, currHeight))

            # Calculate scale
            oldArea = self.height * self.width
            newArea = currHeight * currWidth
            self.scale = newArea / oldArea

            # Update variables
            self.width = currWidth
            self.height = currHeight
            
            # Update screen with new dimensions
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

    def updateScreen(self, commandToCall):

        # OBJECTIVE: Update screen with additional things to draw
        # NOTE: commandToCall is literally a command used to call the caller's draw functions
        # E.g. If MainMenu class calls this updateScreen(), it will have its own draw() listed as "commandToCall"

        # Set background color
        self.screen.fill(self.settingsClass.colorBlack)

        # Draw additional objects
        commandToCall()

        # Update screen
        pygame.display.flip()

        # Set FPS
        self.clock.tick(60)

    def quitPygame(self):

        print("Qutting PyGame")
        pygame.quit()

if __name__ == "__main__":

    # Initialize class and start program
    game = Game(DEFAULT_WIDTH, DEFAULT_HEIGHT)
    game.mainMenu.mainLoop()