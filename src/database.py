import pymongo
import base64
import config


client = pymongo.MongoClient(config.MONGO_URL)
db = client[config.db_name]
data_collection = db[config.data_collection_name]

def save_prediction(image_file, predicted_class):
    image_file.seek(0)
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    data_collection.insert_one({"image": encoded_image,"predicted_class": predicted_class})
