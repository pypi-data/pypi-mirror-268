import cv2

from data.neuro.Rama_classify_class import Rama_classify_class


class Danila:

    def __init__(self):
        self.rama_classify_model = Rama_classify_class()

    # returns string - class of rama using CNN network
    def rama_classify(self, img):
        # img = cv2.imread(img_path)
        class_im = self.rama_classify_model.classify(img)
        return class_im.name
