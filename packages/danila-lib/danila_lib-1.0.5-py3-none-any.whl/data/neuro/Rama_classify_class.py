import os

import cv2
import keras
import numpy as np

from data.neuro.models import RAMA_CLASSIFY_MODEL_ADDRESS
from data.result.Class_im import Class_im
import zipfile
import requests
from urllib.parse import urlencode
"""module for classifying rama"""
class Rama_classify_class:
    """module for classifying rama"""

    # reads CNN taught model and includes it in class example
    def __init__(self):
        """reads CNN taught model and includes it in class example"""
        base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
        public_key = RAMA_CLASSIFY_MODEL_ADDRESS  # Сюда вписываете вашу ссылку
        # Получаем загрузочную ссылку
        final_url = base_url + urlencode(dict(public_key=public_key))
        response = requests.get(final_url)
        download_url = response.json()['href']
        # Загружаем файл и сохраняем его
        download_response = requests.get(download_url)

        # print(download_response.content)
        with open('17_model.zip', 'wb') as f:
            f.write(download_response.content)

        with zipfile.ZipFile('17_model.zip', 'r') as zip_ref:
            zip_ref.extractall()
        self.rama_classify_model = keras.models.load_model('17_model')

    # сделать картинку чб 512-512
    # makes NumPy Array(1,512,512) of doubles[0..1] from openCV image - make it 512-512 and grey
    def prepare_img(self, image_initial):
        """prepare_img(img:openCV frame):NumPy Array - makes NumPy Array(1,512,512) of doubles[0..1] from openCV image - make it 512-512 and grey"""
        img_grey = cv2.cvtColor(image_initial, cv2.COLOR_BGR2GRAY)
        img_grey_size = cv2.resize(img_grey, (512, 512))
        data = np.array(img_grey_size, dtype="float") / 255.0
        data = data.reshape((1, 512, 512))
        return data

    # classify openCV img with CNN, returns list with double[0..1] values
    def work_img(self, image_initial):
        """work_img(img:openCV frame):Double[0..1] list - classify openCV img with CNN, returns list with double[0..1] values"""
        data = self.prepare_img(image_initial)
        res = self.rama_classify_model.predict(data)
        res_list = res[0].tolist()
        return res_list

    # classify openCV img with CNN, returns Class_im
    def classify(self, image_initial):
        """classify(img:openCV frame):Class_im - classify openCV img with CNN, returns Class_im"""
        res_list = self.work_img(image_initial)
        res_index = res_list.index(max(res_list))
        class_im = Class_im(res_index)
        return class_im

