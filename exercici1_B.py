import json

def ferJson():
    ex1BJson = """
        {
        "book":[
            {"titel":"Dracula",
            "cover":"Bram Stoker",
            "year":"1897",
            "pages":"576"
            }
        
            {"titel":"Starship troopers",
            "cover":"Robert A. Heinlein",
            "year":"1959",
            "pages":"596"
            }
        
            {"titel":"The gods of mars",
            "cover":"Edgar Rice Burroughs",
            "year":"1913",
            "pages":"204"
            }
        
            {"titel":"The cats of ulthar",
            "cover":"H. P. Lovecraft",
            "year":"1920",
            "pages":"27"
            }
        
        ]
    }
    """
    with open("arxiu1.json",'w') as file:
        json.dump(ex1BJson,file, indent=2)