import tqdm
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import base64
from PIL import Image
import io
import math
from math import sqrt
import urllib.request
import cv2


embed = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3),
                                          include_top=False,
                                          weights='imagenet')


class TensorVector():

    def __init__(self):
        pass

    def process(self, FileName):
        img = tf.io.read_file(FileName)
        img = tf.io.decode_jpeg(img, channels=3)
        img = tf.image.resize_with_pad(img, 224, 224)
        img = tf.image.convert_image_dtype(img, tf.float32)[tf.newaxis, ...]
        features = embed.predict(img)
        resize_feature = np.reshape(features, (7*7*1280))
        return resize_feature

    def cosineSim(self, a1, a2):
        sum = 0
        suma1 = 0
        sumb1 = 0
        for i, j in zip(a1, a2):
            suma1 += i * i
            sumb1 += j*j
            sum += i*j
        cosine_sim = sum / ((sqrt(suma1))*(sqrt(sumb1)))
        return cosine_sim

    def jaccard_similarity(self, list1, list2):
        intersection = len(list(set(list1).intersection(list2)))
        union = (len(list1) + len(list2)) - intersection
        return float(intersection) / union

    def average(self, x):
        assert len(x) > 0
        return float(sum(x)) / len(x)

    def pearson_def(self, x, y):
        assert len(x) == len(y)
        n = len(x)
        assert n > 0
        avg_x = self.average(x)
        avg_y = self.average(y)
        diffprod = 0
        xdiff2 = 0
        ydiff2 = 0
        for idx in range(n):
            xdiff = x[idx] - avg_x
            ydiff = y[idx] - avg_y
            diffprod += xdiff * ydiff
            xdiff2 += xdiff * xdiff
            ydiff2 += ydiff * ydiff

        return diffprod / math.sqrt(xdiff2 * ydiff2)

    def mean(self, vector1, vector2):
        cs = self.cosineSim(vector1, vector2)
        # js=self.jaccard_similarity(vector1,vector2)
        ps = self.pearson_def(vector1, vector2)
        # print(cs,js,ps)
        average = (cs+ps)/2
        # print(average)
        return average

    def compare(self, images):
        vector1 = self.process(images[0])
        vector2 = self.process(images[1])
        return self.mean(vector1, vector2)


def convertBase64(FileName):
    """
    Return the Numpy array for a image 
    """
    with open(FileName, "rb") as f:
        data = f.read()

    res = base64.b64encode(data)

    base64data = res.decode("UTF-8")

    imgdata = base64.b64decode(base64data)

    image = Image.open(io.BytesIO(imgdata))

    return np.array(image)


cls_obj = TensorVector()
col = ['Name', 'Product', 'Price', 'Link', 'Image', 'Type']
db1 = pd.read_csv("amazon_data_jeans.csv")
db1.columns = col
db2 = pd.read_csv("amazon_data_tshirt.csv")
db2.columns = col
print(db1.head())
img_url1 = db1[['Image']].values
img_url2 = db2[['Image']].values
db1['Vector'] = ""

img_name = 'sample.jpg'

for id, i in tqdm.tqdm(enumerate(img_url1)):
    try:
        urllib.request.urlretrieve(i[0], img_name)
        vc = cls_obj.process(img_name)
        db1['Vector'].iloc[id] = vc.tolist()
    except:
        db1['Vector'].iloc[id] = None
        print("Err")
db2['Vector'] = ""

img_name = 'sample.jpg'

for id, i in tqdm.tqdm(enumerate(img_url2)):
    try:
        urllib.request.urlretrieve(i[0], img_name)
        vc = cls_obj.process(img_name)
        db2['Vector'].iloc[id] = vc.tolist()
    except Exception as e:
        db2['Vector'].iloc[id] = None
        print(e)
final_db = pd.concat([db1, db2])
final_db.columns = ['Name', 'Product',
                    'Price', 'Link', 'Image', 'Type', 'Vector']
final_db.reset_index(inplace=True, drop=True)
final_db.drop(['Name'], axis=1)
final_db.to_csv("Data.csv", index=0)
