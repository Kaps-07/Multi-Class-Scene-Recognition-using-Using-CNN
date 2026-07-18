# Image Classification Web App

## Project Overview

This repository contains a Flask-based image classification application. It uses a trained Keras model to classify uploaded images into one of six categories and stores prediction results in a MongoDB collection.

## Features

- User registration and login using Flask endpoints
- Password reset endpoint
- Image upload prediction endpoint
- Model inference using a saved Keras model (`artifacts/best_model.keras`)
- MongoDB persistence for user data and prediction results
- Response includes predicted class and the uploaded image encoded in base64

## Tech Stack

- Python 3
- Flask
- Flask-JWT-Extended
- TensorFlow / Keras
- PyMongo
- MongoDB

## Repository Structure

- `main.py` - Flask application entrypoint and route definitions
- `config.py` - Application configuration values for Flask, MongoDB, and model paths
- `src/utils.py` - Image preprocessing and classification helper
- `src/database.py` - MongoDB data access helper
- `artifacts/best_model.keras` - Saved Keras image classification model
- `requirements.txt` - Python dependencies
- `.gitignore` - Files and directories to ignore in Git

## Prerequisites

- Python 3.11 (or compatible Python 3.x)
- MongoDB running locally or reachable by the configured connection string
- Required Python packages installed

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure MongoDB is running.

4. Confirm the model file exists at `artifacts/best_model.keras`.

## Configuration

The app configuration is stored in `config.py`:

- `FLASK_HOST` and `FLASK_PORT` for Flask server binding
- `MONGO_URL` for MongoDB connection
- `db_name`, `user_collection_name`, `data_collection_name` for MongoDB collections
- `model_path` for the saved Keras model
- `IMG_HEIGHT`, `IMG_WIDTH` for image preprocessing dimensions

## Running the App

Start the Flask app with:

```bash
python main.py
```

The API should be available at `http://127.0.0.1:5005` by default.

## API Endpoints

### `POST /register`

Register a new user.

Form fields:

- `user_name`
- `password`
- `email_id`
- `contact_number`
- `dob`

Response:

- `status`: `success` or `exists`
- `message`

### `POST /login`

Login an existing user.

Form fields:

- `user_name`
- `password`

Response:

- `status`: `success` or `failure`
- `message`
- `access_token` on success

### `POST /forget_password`

Reset a user password.

Form fields:

- `user_name`
- `dob`
- `new_password`

Response:

- `status`: `success` or `failure`
- `message`

### `POST /predict`

Upload an image for classification.

Form field:

- `image` (file upload)

Response:

- `status`: `success`
- `prediction`: predicted class label
- `image`: base64-encoded uploaded image

## Notes

- The current application stores predictions using the helper in `src/database.py`.
- The prediction endpoint returns the uploaded image as a base64 string in the response so it can be rendered in a client application.
- If you want a frontend preview, decode the base64 string and display it as an image source.

## Troubleshooting

- If `flask` is missing, install dependencies using `pip install -r requirements.txt`.
- If MongoDB is not running, start it or update `MONGO_URL` in `config.py`.
- If the model file is missing, ensure `artifacts/best_model.keras` exists and is accessible.
