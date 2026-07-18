import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FLASK_PORT = int(os.environ.get("PORT", 8000))
FLASK_HOST = os.environ.get("FLASK_HOST", "0.0.0.0")

MONGO_URL = os.environ.get("MONGO_URL") or os.environ.get("MONGO_CLIENT") or "mongodb+srv://Kaps:pkp%2428feb@docdb-cluster-20260701-0629.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"

db_name = os.environ.get("DB_NAME", "cnn_app")

user_collection_name = os.environ.get("USER_COLLECTION_NAME", "collection_user")
data_collection_name = os.environ.get("DATA_COLLECTION_NAME", "collection_data")

model_path = os.path.join(BASE_DIR, "artifacts", "best_model.keras")

IMG_HEIGHT = 150
IMG_WIDTH = 150