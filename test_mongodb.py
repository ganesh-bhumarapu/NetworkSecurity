from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://ganeshbhumarapu:Ganesh@cluster0.axsi3ew.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to mongoDB!")
except Exception as e:
    print(e)