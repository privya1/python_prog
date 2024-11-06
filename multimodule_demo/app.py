"""
For importing entire module
"""
# import database
"""
Instatiating the object i.e. creating an object "db" from class Database() present in the module database.
In python each python file represents a module
"""
# db = database.Database()
"""
calling functions by objects
"""
# db.connect()
# db.disconnect()


"""
For importing particular class
"""
# from database import Database
# db = Database()
# db.connect()
# db.disconnect()

# from utils import HttpUtils, FileUtils

# instatiating objects of FileUtils
# file_utils = FileUtils()
# # instatiating objects of HttpUtils
# http_utils = HttpUtils()

"""
To import all classes and functions from the module use
"""
# from utils import *
from random import Random

rand_int = Random()

print(rand_int.randint(10,100))

