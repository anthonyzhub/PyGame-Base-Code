class GameSettings:

    def __init__(self) -> None:

        # Hold buttons' dimensions
        self.maxButtonWidth = 100
        self.maxButtonHeight = 20
        self.distanceBetweenButtons = 50

        # Colors to use
        self.colorPurple = (149, 67, 255)
        self.colorBlack = (0, 0, 0)
        self.colorLimeGreen = (50, 205, 50)
        self.colorBlueGreen = (117, 255, 196)
        self.colorYellow = (255, 255, 0)
        self.colorOrange = (255, 105, 50)
        self.colorRed = (255, 0, 0)
        self.colorBlue = (23, 93, 255)
        self.colorWhite = (255, 255, 255)

    def updateButtonDimensions(self, scale):

        # OBJECTIVE: Whenever window size changes, update buttons' dimension

        self.distanceBetweenButtons *= scale
        self.maxButtonWidth *= scale
        self.maxButtonHeight *= scale