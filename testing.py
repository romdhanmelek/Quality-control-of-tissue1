import cv2
import tensorflow as tf


DATADIR = "D:/Malek/Projects/stage/Croping images"
CATEGORIES = ["Positive", "Negative"]

def prepare(filepath):
    IMG_SIZE = 70
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE,IMG_SIZE,1)

model = tf.keras.models.load_model("64x3-CNN.model")
prediction = model.predict([prepare('D:\\Malek\\Projects\\stage\\Croping images\\cropped\\Positive\\1629748627.9891236.JPG')])
print(prediction)