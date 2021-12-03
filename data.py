import json
import os

class SavedData:

    def getFile(self):

        # OBJECTIVE: Check if JSON file exists or not

        # If file doesn't exist, create one
        if os.path.exists(self.fileName) == False:

            # Create JSON file
            with open(self.fileName, "w") as jsonFile:

                # Convert dictionary to JSON template
                templateJSON = json.dumps(self.templateDict)

                # Write new JSON template on computer's hard drive
                jsonFile.write(templateJSON)

        else:

            # Open JSON file
            with open(self.fileName, "r") as jsonFile:

                # Load JSON file to a dictionary
                self.templateDict = json.load(jsonFile)

    def saveFile(self):

        # OBJECTIVE: Before terminating program, update file with new data

        # Write to JSON file
        with open(self.fileName, "w") as jsonFile:

            # Convert dictionary to JSON template
            templateJSON = json.dumps(self.templateDict)

            # Write new JSON template on computer's hard drive
            jsonFile.write(templateJSON)

    def __init__(self) -> None:

        # Create variable to hold file name
        self.fileName = "./Miscellaneous/data.json"
        
        # JSON template
        self.templateDict = {
            "Odometer": "0000000",
            "Time": "000000",
            "Player Name": "Anthony"
        }

        # Load JSON file
        self.getFile()