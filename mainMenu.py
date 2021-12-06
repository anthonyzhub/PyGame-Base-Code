import pygame

from button import Button

class MainMenu:

    def __init__(self, gameClass, settingsClass) -> None:
        
        # Save parameters
        self.gameClass = gameClass
        self.settingsClass = settingsClass

        # Calculate screen's area for future use
        self.oldScreenArea = self.gameClass.width * self.gameClass.height

    def updateAllButtons(self):

        # OBJECTIVE: Update all buttons' properities

        # If screen size hasn't changed, exit function
        if self.oldScreenArea == self.gameClass.width * self.gameClass.height:
            return

        # Manually update button's X & Y value
        self.settingsButton.updateProperties(self.gameClass.width / 2, self.playButton.yPosition + self.settingsClass.distanceBetweenButtons)

        # Get new screen's area
        self.oldScreenArea = self.gameClass.width * self.gameClass.height

    def draw(self):

        # OBJECTIVE: Draw all buttons and labels on main menu

        for currButton in self.buttonsList:
            currButton.draw()

    def buttonPressedHandler(self, mousePosition):

        # OBJECTIVE: Call function associated with button pressed

        # Iterate list of buttons
        for currButton in self.buttonsList:
            
            # If a button was pressed, immediately exit loop
            if currButton.wasButtonPressed(mousePosition):
                break

    def mainLoop(self):

        # OBJECTIVE: Display and handle main menu

        # Create buttons
        self.playButton = Button(self.gameClass, self.settingsClass, "Play", None, self.gameClass.width / 2, self.gameClass.height / 2)
        self.settingsButton = Button(self.gameClass, self.settingsClass, "Settings", None, self.gameClass.width / 2, self.playButton.yPosition + self.settingsClass.distanceBetweenButtons)

        # Create a list to hold all buttons
        self.buttonsList = [self.playButton, self.settingsButton]

        while self.gameClass.showMainMenu:

            # Get mouse position over window
            mousePosition = pygame.mouse.get_pos()

            # Look for events from the user
            for event in pygame.event.get():

                # Close window if "closed" button was pressed
                if event.type == pygame.QUIT:
                    self.gameClass.quitPygame()
                    exit(0)

                # Change window's screen size if user pressed window button
                elif event.type == pygame.VIDEOEXPOSE:
                    self.gameClass.adjustScreen()
                    self.updateAllButtons()

                # When a mouse button gets pressed, check if a button was selected
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttonPressedHandler(mousePosition)

            # Double check if window size changed
            # NOTE: Player might have changed window size in a different window then decided to press "back"
            self.updateAllButtons()

            # In case "closed" button was clicked on, exit while-loop
            # NOTE: Boolean variable won't need to be resetted because the program will stop running
            if self.gameClass.showMainMenu == False:
                break

            # Update screen
            self.gameClass.updateScreen(self.draw)

        # Release all pygame's resources
        self.gameClass.quitPygame()