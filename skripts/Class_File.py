class File:
    # Kommas aus dem Text-File löschen
    def __init__(self):
        pass
        
    def adapt_file(path):
        with open(path, "r") as file:
            filedata = file.read()
        filedata = filedata.replace(',', '')
        with open(path, "w") as file:
            file.write(filedata)

File.adapt_file("Winterthur_neu.txt")