from pymongo import MongoClient
from urllib.parse import quote_plus

password = "SHRI@2005"
encoded_password = quote_plus(password)
uri = f"mongodb+srv://SHRI:{encoded_password}@web.hmirxrb.mongodb.net/?retryWrites=true&w=majority&appName=WEB"

try:
    client = MongoClient(uri)
    db = client['edu_portal']
    
    # Create professors collection with sample data
    professors_collection = db['professors']
    
    # Insert a sample professor
    result = professors_collection.insert_one({
        'username': 'prof_admin',
        'password': 'prof123',
        'email': 'prof@eduportal.com',
        'created_at': '2025-01-01'
    })
    
    print("✅ Collection 'professors' created successfully!")
    print(f"✅ Sample professor inserted with ID: {result.inserted_id}")
    
    # List all collections
    collections = db.list_collection_names()
    print(f"✅ Collections in database: {collections}")
    
except Exception as e:
    print(f"❌ Error: {e}")