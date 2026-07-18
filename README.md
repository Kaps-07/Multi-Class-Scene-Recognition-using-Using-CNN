# CNN Image Insight

## Project Overview

CNN Image Insight is a Flask-based web application for image classification using a trained Keras convolutional neural network. Users can register, log in, upload an image, and view prediction results with probability details.

## Key Features

- User registration and login workflow
- Image upload prediction interface
- CNN-based inference with a saved Keras model
- Prediction persistence in MongoDB
- Responsive interface with a polished web UI

## Tech Stack

- Python 3.11
- Flask
- TensorFlow / Keras
- PyMongo
- MongoDB
- Jinja2 templates

## Repository Structure

- `main.py` - Flask application and route definitions
- `config.py` - Application configuration for Flask, MongoDB, and model settings
- `src/utils.py` - Image preprocessing and CNN inference utilities
- `src/database.py` - MongoDB persistence helpers
- `artifacts/best_model.keras` - Pre-trained Keras model for classification
- `templates/` - Jinja2 HTML templates for register, login, and prediction pages
- `static/style.css` - Application styling and layout
- `requirements.txt` - Python package dependencies

## Prerequisites

- Python 3.11 or compatible Python 3.x
- MongoDB accessible via the configured connection string
- Required Python packages installed using `requirements.txt`

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

3. Make sure MongoDB is running and reachable.

4. Verify the model file exists at `artifacts/best_model.keras`.

## Configuration

Update `config.py` as needed:

- `FLASK_HOST` and `FLASK_PORT` for web server binding
- `MONGO_URL` for MongoDB connection
- `db_name`, `user_collection_name`, and `data_collection_name`
- `model_path`, `IMG_HEIGHT`, and `IMG_WIDTH`

## Running the Application

Start the app with:

```bash
python main.py
```

Open the app in your browser at `http://127.0.0.1:5005` (or the configured host and port).

## Application Flow

1. Register a new account
2. Log in with your credentials
3. Upload an image for prediction
4. View the predicted class and probability scores

## API Endpoints

### `POST /register`

Register a new user with:

- `user_name`
- `password`
- `email_id`
- `contact_number`
- `dob`

### `POST /login`

Log in with:

- `user_name`
- `password`

### `POST /forget_password`

Reset password with:

- `user_name`
- `dob`
- `new_password`

### `POST /predict`

Upload an image using form field:

- `image`

The app returns the predicted label and prediction details.

## Notes

- Prediction entries are saved to MongoDB for later reference.
- Uploaded images are encoded in base64 for rendering in the client.
- The current UI is styled to match a CNN-based image analytics application.

## Troubleshooting

- Install dependencies if packages are missing:

```bash
pip install -r requirements.txt
```

- Ensure MongoDB is running or update `MONGO_URL` in `config.py`.
- Confirm `artifacts/best_model.keras` is present and accessible.

## License

This project is available for educational and demo purposes.
