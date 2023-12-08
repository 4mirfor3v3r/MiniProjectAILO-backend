import tensorflow as tf
import numpy as np
import pandas as pd

model = tf.keras.models.load_model('CardClassification-(224x224)-99.62.h5')

def load_image(image_path):
    img = tf.io.read_file(image_path)
    img = tf.image.decode_jpeg(img, channels=3)
    return img

def predict(image_path):
    img = load_image(image_path)
    img = tf.image.resize(img, (224, 224))
    img = tf.expand_dims(img, axis=0)
    img = img / 255.0
    prediction = model.predict(img)
    return prediction

if __name__ == '__main__':
    df = pd.read_csv('Cards-Classification-class_dict.csv')
    # index, cls, height, width = df.iloc[np.argmax(predict('jack.jpg'))]
    # print(cls)

