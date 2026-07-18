import os
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5005

MONGO_URL = "mongodb://localhost:27017"
db_name = "cnn_app"

user_collection_name = 'collection_user'
data_collection_name = "collection_data"

model_path= r"artifacts\best_model.keras"

IMG_HEIGHT = 150
IMG_WIDTH = 150
