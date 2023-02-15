import json
def llegirBook():
    with open("arxiu1.json",'r') as file:
        result = json.load(file)
        print(result)
