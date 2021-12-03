import pygame

class Button:

    def updateProperties(self, xPosition, yPosition):

        # OBJECTIVE: Create/Update rect's object with pygame's update() function

        # Update center position variables
        self.xPosition = xPosition
        self.yPosition = yPosition

        # Get new size from Settings class
        self.width = self.settingsClass.maxButtonWidth
        self.height = self.settingsClass.maxButtonHeight

        # Update vertices
        self.buttonDict = {
            "Center": [self.xPosition, self.yPosition],
            "Top Left": [self.xPosition - self.width, self.yPosition - self.height],
            "Top Right": [self.xPosition + self.width, self.yPosition - self.height],
            "Bottom Left": [self.xPosition - self.width, self.yPosition + self.height],
            "Bottom Right": [self.xPosition + self.width, self.yPosition + self.height]
        }

        # Update rectangular object
        # NOTE: Created "extraRectCoverage" to cover all edges
        extraRectCoverage = 1 
        innerWidth = extraRectCoverage + self.buttonDict["Top Right"][0] - self.buttonDict["Top Left"][0]
        innerHeight = extraRectCoverage + self.buttonDict["Bottom Right"][1] - self.buttonDict["Top Right"][1]
        self.innerRect = pygame.Rect(self.buttonDict["Top Left"][0], self.buttonDict["Top Left"][1], innerWidth, innerHeight)

    def __init__(self, gameClass, settingsClass, text, command, xPosition, yPosition) -> None:
        
        # Save parameters
        self.gameClass = gameClass
        self.settingsClass = settingsClass
        self.text = text
        self.command = command

        # Create/Update button's vertices and rectangular object
        self.updateProperties(xPosition, yPosition)

    def displayText(self):

        # OBJECTIVE: Write a text to label button

        # Create a text
        buttonFont = pygame.font.SysFont(None, 22)
        buttonText = buttonFont.render(self.text, True, self.settingsClass.colorWhite)
        buttonPosition = [self.xPosition - 50, self.yPosition]

        # Draw text
        self.gameClass.screen.blit(buttonText, buttonPosition)

    def draw(self):

        # OBJECTIVE: Draw button on screen

        # Draw perimeter
        pygame.draw.line(self.gameClass.screen, self.settingsClass.colorBlue, self.buttonDict["Top Left"], self.buttonDict["Top Right"])
        pygame.draw.line(self.gameClass.screen, self.settingsClass.colorBlue, self.buttonDict["Bottom Left"], self.buttonDict["Bottom Right"])
        pygame.draw.line(self.gameClass.screen, self.settingsClass.colorBlue, self.buttonDict["Top Left"], self.buttonDict["Bottom Left"])
        pygame.draw.line(self.gameClass.screen, self.settingsClass.colorBlue, self.buttonDict["Top Right"], self.buttonDict["Bottom Right"])

        # Draw rectangle inside perimeter
        pygame.draw.rect(self.gameClass.screen, self.settingsClass.colorBlue, self.innerRect)

        # Display button text
        self.displayText()

    def wasButtonPressed(self, mousePosition):

        # OBJECTIVE: If button was pressed, execute command

        # Check if mouse's X & Y value sare within the buttons' vertices
        if (mousePosition[0] >= self.buttonDict["Top Left"][0] and 
        mousePosition[0] <= self.buttonDict["Top Right"][0] and 
        mousePosition[1] >= self.buttonDict["Top Left"][1] and 
        mousePosition[1] <= self.buttonDict["Bottom Left"][1]):

            # NOTE: Added parentheses to excute as command
            self.command()