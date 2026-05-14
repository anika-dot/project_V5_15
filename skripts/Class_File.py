"""
Module providing file utility functions used by the city simulation.
Contains helper functionality for reading and cleaning map files.
"""

class File:
    """
    Utility class providing simple file manipulation methods.
    """
    def __init__(self):
        pass

    @staticmethod
    def remove_commas(path):
        """
        Remove all commas from a text file in place.
        Args:
            path (str): Path to the text file that should be cleaned.
        """
        with open(path, "r", encoding="utf-8") as file:
            filedata = file.read()
        filedata = filedata.replace(",", "")
        with open(path, "w", encoding="utf-8") as file:
            file.write(filedata)


File.remove_commas("Winterthur_neu.txt")
