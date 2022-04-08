from pymongo import MongoClient
from collections import OrderedDict
import sys
from inputs.config import username, password, atlas_cluster_name  # database credentials are accessed from config.py
db_name = "myCollection"
client = MongoClient(
        f"mongodb+srv://{username}:{password}@{atlas_cluster_name}.net/{db_name}?retryWrites=true&w=majority")
db = client.testX

db.myColl.drop()  # this code here drops the existing collection if it existed previously

db.create_collection("myColl")  # Force create!

#  $jsonSchema expression type is prefered.  New since v3.6 (2017):
vexpr = {"$jsonSchema":
    {
        "bsonType": "object",
        "required": ["name", "year", "major", "gpa"],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "gender": {
                "bsonType": "string",
                "description": "must be a string and is not required"
            },
            "year": {
                "bsonType": "int",
                "minimum": 2017,
                "maximum": 3017,
                "exclusiveMaximum": False,
                "description": "must be an integer in [ 2017, 3017 ] and is required"
            },
            "major": {
                "enum": ["Math", "English", "Computer Science", "History", None],
                "description": "can only be one of the enum values and is required"
            },
            "gpa": {
                # In case you might want to allow doubles OR int, then add
                # "int" to the bsonType array below:
                "bsonType": ["double"],
                "minimum": 0,
                "description": "must be a double and is required"
            }
        }
    }
}

# Per the docs, args to command() require that the first kev/value pair
# be the command string and its principal argument, followed by other
# arguments.  There are two ways to do this:  Using an OrderDict:
cmd = OrderedDict([('collMod', 'myColl'),
                   ('validator', vexpr),
                   ('validationLevel', 'moderate')])
db.command(cmd)

# Or, use the kwargs construct:
# db.command('collMod','myColl', validator=vexpr, validationLevel='moderate')

try:
    db.myColl.insert_one({"x": 1})
    print("NOT good; the insert above should have failed.")
except:
    print("OK. Expected exception:", sys.exc_info())

try:
    okdoc = {"name": "buzz", "year": 2019, "major": "Math", "gpa": 3.8}
    db.myColl.insert_one(okdoc)
    print("All good.")
except:
    print("exc:", sys.exc_info())
