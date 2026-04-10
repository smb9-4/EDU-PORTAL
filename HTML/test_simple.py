# test_simple.py

try:
    import pymongo
    print("✅ PyMongo installed successfully!")
    print(f"✅ PyMongo version: {pymongo.__version__}")
    
    try:
        import flask_pymongo
        print("✅ Flask-PyMongo installed successfully!")
    except ImportError:
        print("❌ Flask-PyMongo not installed")
        
except ImportError as e:
    print(f"❌ PyMongo not installed: {e}")
    print("Please run: pip install pymongo flask-pymongo")

print("\n📦 Checking other required packages:")
try:
    import flask
    print(f"✅ Flask version: {flask.__version__}")
except ImportError:
    print("❌ Flask not installed")

try:
    import bcrypt
    print("✅ bcrypt installed successfully!")
except ImportError:
    print("❌ bcrypt not installed")