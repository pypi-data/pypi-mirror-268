import cv2
"""main module for user"""
from data.neuro.Rama_classify_class import Rama_classify_class


class Danila:
    """main class for user"""
    def __init__(self):
        self.rama_classify_model = Rama_classify_class()

    # returns string - class of rama using CNN network
    # img - openCV frame

    def rama_classify(self, img):
        """rama_classify(Img : openCv frame): String - returns class of rama using CNN network"""
        """rama_classify uses Rama_classify_class method - classify(Img)"""
        # img = cv2.imread(img_path)
        class_im = self.rama_classify_model.classify(img)
        return class_im.name

