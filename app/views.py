import sys
from django.http import HttpResponse
from utils import create_database, create_collection_and_validate  # Communicates with MongoDB
from inputs.schema import test_validation
from collections import OrderedDict

from inputs.user_inputs import one_inp, single_input, usr_inp, multiple_input

# Create your views here.


def page_home(response):  # Views that the specific pages show on local host
    return HttpResponse("<h1>This is Home Page!</h1>")


def page_1(response):
    return HttpResponse("<h1>This is Page 1!</h1>")


def page_2(response):
    return HttpResponse("<h1>This is Page 2!</h1>")


db_handle, mongo_client = create_database("data_base_name")  # Calling a method from util.py to get the database_handle
collection = create_collection_and_validate(db_handle, "collection_name", test_validation)

# Per the docs, args to command() require that the first kev/value pair
# be the command string and its principal argument, followed by other
# arguments.  There are two ways to do this:  Using an OrderDict:
cmd = OrderedDict([('collMod', 'myColl'),
                   ('validator', test_validation),
                   ('validationLevel', 'moderate')])
db_handle.command(cmd)

# Or, use the kwargs construct:
# db.command('collMod','myColl', validator=test_validation, validationLevel='moderate')

# An example of data to show how it was works
# Insert One Function
try:
    db_handle.myColl.insert_one({"x": 1})
    print("NOT good; the insert above should have failed.")
except:
    print("OK. Expected exception:", sys.exc_info())

try:
    okdoc = {"name": "buzz", "year": 2019, "major": "Math", "gpa": 3.8}
    db_handle.myColl.insert_one(okdoc)
    print("All good.")
except:
    print("exc:", sys.exc_info())

try:  # should success
    collection.insert_one(one_inp)
    print("one_inp added\n")
except:
    print(sys.exc_info(), "\none_inp failed")

try:  # should fail
    collection.insert_one(single_input)
    print("single_input added\n")
except:
    print(sys.exc_info(), "\nsingle_inp failed")

try:  # should fail
    collection.insert_many(multiple_input)
    print("multiple_input added\n")
except:
    print(sys.exc_info(), "\nmultiple_inp failed")

try:  # should success
    collection.insert_many(usr_inp)
    print("usr_input added\n")
except:
    print(sys.exc_info(), "\nusr_inp failed")

one_output = collection.find_one({'_id': 1})
print(one_output)

for results in collection.find({}, {"name": 1, "_id": 0}):
    print(results)

