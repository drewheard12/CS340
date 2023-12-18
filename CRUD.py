from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'MONGO_HOST'
        PORT = 'MONGO_PORT'
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
            return "True"
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return "False"

# Create method to implement the R in CRUD.

    def read(self, key, value):
        try:
            result= self.database.animals.find(key,value)  # data should be dictionary            
            return result
        except:
            empty =''
            return empty
        
# Create method to implement the U in CRUD.

    def update(self, key, value):
        try:
            result = self.collection.update_many(key, {"$set": value})
            if result.modified_count > 0:
                uCount= result.modified_count
                print(uCount)
                return True
        except:
            fail = '0'
            print(fail)
        return False

# Create method to implement the D in CRUD.  

    def delete(self, key):
        try:
            result = self.collection.delete_many(key)
            if result.deleted_count > 0:
                uCount= result.modified_count
                print(uCount)
                return True
        except Exception as e:
            print(e)
        return False      