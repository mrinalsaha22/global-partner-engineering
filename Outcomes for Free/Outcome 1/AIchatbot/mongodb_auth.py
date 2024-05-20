# Import the necessary libraries
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import credentials
import certifi


uri = credentials.mongodb_uri

# Function to purge the collection
def purge_collection(collection):
    result = collection.delete_many({})
    return('Deleted {} documents from collection.'.format(result.deleted_count))

def addData(data,collection):
    # Insert all documents
    result = collection.insert_many(data)
    return(len(result.inserted_ids))

def authenticatedb(dbname='maindb'):
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'),tlsCAFile=certifi.where())
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        import sys
        #print (sys._getframe(1).f_code.co_name)
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    # Get the database
    return client[dbname]

if __name__ == '__main__':
    authenticatedb()
