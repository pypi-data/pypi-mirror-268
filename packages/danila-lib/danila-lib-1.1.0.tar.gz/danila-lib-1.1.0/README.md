# danila_lib
 python library for Danila

# To install project made 
    pip install danila-lib

# To use in your project 
    from danila.danila import Danila

# All use methods are in 
    class Danila

# returns string - class of rama using CNN network
# img - openCV frame
    def rama_classify(self, img):

# additional classes
# neuro-model classe
# in package data/neuro there is module Rama_classify_class
    class Rama_classify_class

# reads CNN taught model and includes it in class example
    def __init__():

# makes NumPy Array(1,512,512) of doubles[0..1] from openCV image - make it 512-512 and grey
    def prepare_img(img : openCV frame): NumPy Array(1,512,512)[0..1]

# classify openCV img with CNN, returns list with double[0..1] values 
    def work_img(img : openCV frame): Double[0..1] list

# classify openCV img with CNN, returns Class_im
    def classify(img : openCV frame): Class_im

# result classes

# in package data/result Class_im
    class Class_im(Enum):
        rama_no_spring = 0
        rama_spring = 1


# exapmles of using you can find 
https://github.com/Arseniy-Zhuck/danila_lib_demo