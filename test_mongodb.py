import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://subhampradhan:Admin123@cluster0.le6n6fy.mongodb.net/?appName=Cluster0"

# Pass the certifi path directly via the standard tlsCAFile keyword argument
client = MongoClient(
    uri,
    server_api=ServerApi('1'),
    tlsCAFile=certifi.where()  # This explicitly hands Python the missing root certificates
)

try:
    print("Testing connection with verified certificate authorities...")
    client.admin.command('ping')
    print("\n✅ Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"\n❌ Connection failed: {e}")