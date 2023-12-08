import tensorflow as tf
import numpy as np
import pandas as pd

model = tf.keras.models.load_model('CardClassification-(224x224)-99.62.h5')
df = pd.read_csv('Cards-Classification-class_dict.csv')

def predict(img) -> str:
    img = tf.image.resize(img, (224, 224))
    img = tf.expand_dims(img, axis=0)
    img = img / 255.0
    prediction = model.predict(img)
    index, cls, height, width = df.iloc[np.argmax(prediction)]
    return cls