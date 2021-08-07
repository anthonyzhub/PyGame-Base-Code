#! /usr/bin/python3

import pygame

class Game:

    def __init__(self, width, height) -> None:
        
        # Initialize PyGame
        pygame.init()

        # Get screen's dimensions
        self.width = width
        self.height = height

        # Create a window
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Initialize PyGame's clock for FPS (frames-per-second)
        self.clock = pygame.time.Clock()

        # Create a boolean variable to start/stop game
        self.continueGame = True

    def updateScreen(self):

        # OBJECTIVE: Update all changes made on the screen

        # Update screen
        pygame.display.flip()

        # Set FPS
        self.clock.tick(60)

    def mainLoop(self):

        # OBJECTIVE: Main function that controls the game by calling other functions

        while self.continueGame:

            # Look for events from the user
            for event in pygame.event.get():

                # Close window if "closed" button was pressed
                if event.type == pygame.QUIT:
                    self.continueGame = False

            # Save all keys that were pressed
            keysPressedList = pygame.key.get_pressed()

            # Update screen
            self.updateScreen()

        # If "self.continueGame" is false, release all PyGame's resources
        pygame.quit()

if __name__ == "__main__":

    # Initialize class and start program
    game = Game(840, 720)
    game.mainLoop()