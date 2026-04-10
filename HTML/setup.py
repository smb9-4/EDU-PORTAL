from pymongo import MongoClient
from urllib.parse import quote_plus

# Replace YOUR_PASSWORD with your actual password
password = "SHRI@2005"
encoded_password = quote_plus(password)
uri = f"mongodb+srv://SHRI:{encoded_password}@web.hmirxrb.mongodb.net/?retryWrites=true&w=majority&appName=WEB"

try:
    client = MongoClient(uri)
    
    # Create database and collection
    db = client['edu_portal']
    
    # Create students collection with a sample document
    students_collection = db['students']
    
    # Insert a test document to create the collection
    result = students_collection.insert_one({
        'username': 'admin',
        'password': 'admin123',
        'email': 'admin@eduportal.com',
        'created_at': '2025-01-01'
    })
    
    print("✅ Database 'edu_portal' created successfully!")
    print("✅ Collection 'students' created successfully!")
    print(f"✅ Sample document inserted with ID: {result.inserted_id}")
    
    # List all collections to verify
    collections = db.list_collection_names()
    print(f"✅ Collections in database: {collections}")
    
except Exception as e:
    print(f"❌ Error: {e}")