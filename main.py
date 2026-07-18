from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request
import pymongo
import config
from src.utils import ImageRecognition
from src.database import save_prediction
import datetime
from io import BytesIO
import base64


app = Flask(__name__)
image_recognition_obj = ImageRecognition()

app.config["JWT_SECRET_KEY"] = "secret"
app.config["SECRET_KEY"] = "flask-session-secret"
jwt = JWTManager(app)

mongo_client = pymongo.MongoClient(config.MONGO_URL)
db = mongo_client[config.db_name]
user_collection = db[config.user_collection_name]

@app.route("/register", methods = ["POST"])
def register():
    user_data = request.form
    user_name = user_data['user_name']
    password = user_data['password']
    email_id = user_data['email_id']
    contact_number = user_data['contact_number']
    dob = user_data['dob']

    response = user_collection.find_one({"email_id": email_id})
    if not response:
        user_collection.insert_one({
            "user_name": user_name,
            "password": password,
            "email_id": email_id,
            "contact_number": contact_number,
            "dob": dob
            })
        return jsonify({"status": "success", "message":"User Registered Successfully"})
    else:
        return jsonify({"status": "exists", "message": "User Already Exists"})

@app.route("/login", methods = ["POST"])
def login():
    user_data = request.form
    user_name = user_data['user_name']
    password = user_data['password']
    response = user_collection.find_one({"user_name": user_name, "password": password})
    if response:
        access_token = create_access_token(
            identity=user_name,            
            expires_delta=datetime.timedelta(minutes=1))
        return jsonify({"status": "success","message": "Login Successful", 
                        "access_token":access_token})
    else:
        return jsonify({"status": "failure", "message": "Invalid Credentials"})

@app.route("/forget_password", methods=["POST"])
def forget_passowrd():
    user_data = request.form
    user_name = user_data['user_name']
    dob = user_data['dob']
    new_password = user_data['new_password']
    response = user_collection.find_one({"user_name": user_name, "dob": dob})
    if response:
        user_collection.update_one({"user_name": user_name}, {"$set": {"password": new_password}})
        return jsonify({"status": "success","message": "Password updated successfully"
                       })
    else:
        return jsonify({"status": "failure", "message": "Invalid Credentials"})


@app.route("/predict", methods=["POST"])
def predict():
    image_file = request.files["image"]
    image_bytes = BytesIO(image_file.read())
    prediction = image_recognition_obj.classify(image_bytes)
    image_file.seek(0)
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    save_prediction(image_file, prediction)

    return jsonify({
        "status": "success",
        "prediction": prediction,
        "image": encoded_image
    })
if __name__ == "__main__":
    app.run(host = config.FLASK_HOST, port = config.FLASK_PORT,debug = True)