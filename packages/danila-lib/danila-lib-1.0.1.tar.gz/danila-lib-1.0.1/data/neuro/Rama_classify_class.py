import os

import cv2
import keras
import numpy as np

from data.result.Class_im import Class_im
import zipfile

class Rama_classify_class:
    def __init__(self):
        with zipfile.ZipFile('17_model.zip', 'r') as zip_ref:
            zip_ref.extractall()
        self.rama_classify_model = keras.models.load_model('17_model')
    # сделать картинку чб 512-512
    def prepare_img(self, image_initial):
        img_grey = cv2.cvtColor(image_initial, cv2.COLOR_BGR2GRAY)
        img_grey_size = cv2.resize(img_grey, (512, 512))
        data = np.array(img_grey_size, dtype="float") / 255.0
        data = data.reshape((1, 512, 512))
        return data

    # прогнать через нейронку, получить числовой вектор
    def work_img(self, image_initial):
        data = self.prepare_img(image_initial)
        res = self.rama_classify_model.predict(data)
        res_list = res[0].tolist()
        return res_list

    # прогнать через нейронку, получить значения rama_no_spring = 0
    #     rama_spring = 1 no_rama = 2
    def classify(self, image_initial):
        res_list = self.work_img(image_initial)
        res_index = res_list.index(max(res_list))
        class_im = Class_im(res_index)
        return class_im

    # Протестировать картинку с заданным ответом и процентом согласия с ответом
    def test_img(self, image_initial, class_im, per_cent):
        res_list = self.work_img(image_initial)
        return (res_list[class_im.value] > per_cent)

    # Протестировать картинки директории с заданными ответами и процентом согласия с ответом
    def test_directory(self, directory, per_cent):
        n = 1
        dir = directory + '\\rama-no-spring'
        files = os.listdir(dir)
        correct_answers = 0
        for file in files:
            if (n % 100) == 1:
                per_cent = correct_answers / float(n)
                print(str(n) + ' tests are ready - current percent ' + str(per_cent))
            whole_file_name = dir + '\\' + file

            img = cv2.imread(whole_file_name)
            result = self.test_img(img, Class_im(0), per_cent)
            if result:
                correct_answers += 1
            n += 1
        dir = directory + '\\rama-spring'
        files = os.listdir(dir)
        for file in files:
            if (n % 100) == 1:
                per_cent = correct_answers / float(n)
                print(str(n) + ' tests are ready - current percent ' + str(per_cent))
            whole_file_name = dir + '\\' + file
            img = cv2.imread(whole_file_name)
            result = self.test_img(img, Class_im(0), per_cent)
            if result:
                correct_answers += 1
            n += 1
        print(str(n) + ' tests are ready - current percent ' + str(per_cent))
