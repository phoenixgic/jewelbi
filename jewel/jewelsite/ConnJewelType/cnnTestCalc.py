#coding:utf-8
import cnnJewelType
from tensorflow.python.platform import gfile

typeNo=range(12)
typeName=['摆件','耳环', '耳钉', '挂件', '耳坠', '挂坠', '裸宝石','戒指', '手镯', '手链', '印章', '项链']
resultdic = dict(zip(typeNo, typeName))

def testOnJpg(filename):
    image_data = gfile.FastGFile(filename, 'rb').read()
    return image_data

def getImageResult(filename):
    cnnJewelType.prepare_model()
    result = cnnJewelType.calc_model_result(testOnJpg(filename))
    return resultdic[result[0]]
