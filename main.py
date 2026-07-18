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

@app.route("/register", methods=["GET", "POST"])
def register_page():
    message = None
    success = False

    if request.method == "POST":
        user_data = request.form
        user_name = user_data.get('user_name')
        password = user_data.get('password')
        email_id = user_data.get('email_id')
        contact_number = user_data.get('contact_number')
        dob = user_data.get('dob')

        response = user_collection.find_one({"email_id": email_id})
        if not response:
            user_collection.insert_one({
                "user_name": user_name,
                "password": password,
                "email_id": email_id,
                "contact_number": contact_number,
                "dob": dob
            })
            message = "User Registered Successfully"
            success = True
        else:
            message = "User Already Exists"

    return render_template("register.html", title="Register", message=message, success=success)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    message = None
    success = False

    if request.method == "POST":
        user_data = request.form
        user_name = user_data.get('user_name')
        password = user_data.get('password')
        response = user_collection.find_one({"user_name": user_name, "password": password})
        if response:
            message = "Login Successful"
            success = True
        else:
            message = "Invalid Credentials"

    return render_template("login.html", title="Login", message=message, success=success)


@app.route("/forget_password", methods=["POST"])
def forget_passowrd():
    user_data = request.form
    user_name = user_data['user_name']
    dob = user_data['dob']
    new_password = user_data['new_password']
    response = user_collection.find_one({"user_name": user_name, "dob": dob})
    if response:
        user_collection.update_one({"user_name": user_name}, {"$set": {"password": new_password}})
        return jsonify({"status": "success","message": "Password updated successfully"})
    else:
        return jsonify({"status": "failure", "message": "Invalid Credentials"})


@app.route("/predict", methods=["GET", "POST"])
def predict_page():
    result = None

    if request.method == "POST":
        image_file = request.files.get("image")
        if image_file:
            image_bytes = image_file.read()
            image_stream = BytesIO(image_bytes)
            predicted_class, probabilities = image_recognition_obj.classify(image_stream)
            encoded_image = base64.b64encode(image_bytes).decode("utf-8")

            save_prediction(
                image_bytes=image_bytes,
                predicted_class=predicted_class,
                probabilities=probabilities,
                filename=image_file.filename,
                content_type=image_file.content_type,
            )

            result = {
                "prediction": predicted_class,
                "probabilities": probabilities,
                "image": encoded_image,
            }

    return render_template("predict.html", result=result)


@app.route("/")
def home():
    return redirect(url_for("register_page"))


if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=True, use_reloader=False)