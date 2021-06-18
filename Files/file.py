import os


class File:
    def __init__(self, filePath):
        self.filePath = filePath

    def count_lines(self):
        lineNr = 0
        with open(self.filePath, 'r') as reader:
            line = reader.readline()
            while line != '':
                lineNr += 1
                line = reader.readline()
        return lineNr

    def count_letters(self, searched_letter):
        letterNr = 0
        with open(self.filePath, 'r') as reader:
            line = reader.readline()
            while line != '':
                if line.find(searched_letter) != -1:
                    letterNr += 1
                line = reader.readline()
        return letterNr

    def copy_file(self, new_filepath):
        with open(self.filePath, 'r') as reader:
            file = reader.readlines()
        with open(new_filepath, 'w') as writer:
            writer.writelines(file)
