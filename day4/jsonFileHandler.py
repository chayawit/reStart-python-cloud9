import json
from pathlib import Path

def readJsonFile(fileName):
    data = ""
    try:
        with fileName.open() as json_file:
            data = json.load(json_file)
            print(data)
    except IOError:
        print("Could not read file")
    return data
