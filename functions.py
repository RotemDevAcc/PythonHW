import json
import os

def GetNames():
    firstname = input("Enter Your First Name: ")
    lastname = input("Enter Your Last Name: ")
    return firstname, lastname

def OpenTargetFile(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

def SaveToTargetFile(var,filename):
    if not os.path.exists(filename):
        print("File does not exist, Creating...")

    with open(filename, 'w') as json_file:
        json.dump(var, json_file, indent=4)