import pymongo
import base64
import config
from datetime import datetime


client = pymongo.MongoClient(config.MONGO_URL)
db = client[config.db_name]
data_collection = db[config.data_collection_name]

def save_prediction(image_bytes, predicted_class, probabilities=None, filename=None, content_type=None):
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")
    document = {
        "image": encoded_image,
        "predicted_class": predicted_class,
        "probabilities": probabilities or {},
        "created_at": datetime.utcnow(),
    }
    if filename:
        document["filename"] = filename
    if content_type:
        document["content_type"] = content_type

    data_collection.insert_one(document)
