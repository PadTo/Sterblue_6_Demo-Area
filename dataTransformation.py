import os
import re
import geopandas as gpd
from kml2geojson import convert
import json


class dataTransformation():

    def __init__(self, outputFolderPath):
        """
        Input: 
        outputFolderPath (String): Output folder path
        """
        self.outputFolderPath = outputFolderPath

    def convertKML2GeoJsonAndSave(self, pathToData):
        """
        Automatically converts .kml file types to .geojson and saved the to the chosen folder path

        Input:
        pathToData (String): The path to the file that needs to be converted   

        Output:
        GeoJSON: The GeoJSON output file at the specified location "outputFolderPath" which was set when initializing this dataTransformation class
        """

        # Split Patterns
        splitPattern = r"\\"
        splitPatternDot = r"\."

        # Splitting string path into separate strings
        pathInParts = re.split(splitPattern, pathToData)
        file = pathInParts[-1]

        # Splitting the whole file into its name and file type
        name, fileType = re.split(splitPatternDot, file)

        # print(f"File: {file} \n",
        #       f"File name: {name} \n",
        #       f"File type: {fileType} \n")

        geojsonData = convert(pathToData, separate_folders=False)

        outputFilePath = os.path.join(self.outputFolderPath, name + ".geojson")

        with open(outputFilePath, 'w') as f:
            json.dump(geojsonData[0], f)
