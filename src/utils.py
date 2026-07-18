import config
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


class ImageRecognition:
    def __init__(self):
        pass

    def load_model(self):
        self.model=load_model(config.model_path)
        return
    def preprocess_image(self, image_file):
        img = image.load_img(image_file, target_size=(config.IMG_HEIGHT, config.IMG_WIDTH))
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array


    def classify(self, image_file):
        self.load_model()
        preprocessed_image = self.preprocess_image(image_file)
        prediction = self.model.predict(preprocessed_image)
        class_index = np.argmax(prediction)
        class_labels = ["Building", "Forest", "Glacier", "Mountain", "Sea", "Street"]
        predicted_class = class_labels[class_index]
        return predicted_class



    


