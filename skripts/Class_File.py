class File:
    def __init__(self):
        pass

    def remove_commas(path):
        with open(path, "r") as file:
            filedata = file.read()
        filedata = filedata.replace(",", "")
        with open(path, "w") as file:
            file.write(filedata)


File.remove_commas("Winterthur_neu.txt")
