import sys
import os
import numpy as np
import cv2
import json

import retinex

data_path = 'data'
img_list = os.listdir(data_path)
if len(img_list) == 0:
    print 'Data directory is empty.'
    exit()

with open('config.json', 'r') as f:
    config = json.load(f)

for img_name in img_list:
    if img_name == '.gitkeep':
        continue
    
    img = cv2.imread(os.path.join(data_path, img_name))

    img_msrcr = retinex.MSRCR(
        img,
        config['sigma_list'],
        config['G'],
        config['b'],
        config['alpha'],
        config['beta'],
        config['low_clip'],
        config['high_clip']
    )
    #cv2.imwrite('./result/msrcr/%s'%(img_name),img_msrcr)
    img_gray = cv2.cvtColor(img_msrcr, cv2.COLOR_RGB2GRAY)  
    img_gray_histeq = cv2.equalizeHist(img_gray)
    cv2.imwrite('./result/rrm/%s'%(img_name),img_gray_histeq)
    #img_amsrcr = retinex.automatedMSRCR(
    #    img,
    #    config['sigma_list']
    #)

    #img_msrcp = retinex.MSRCP(
    #    img,
    #    config['sigma_list'],
    #    config['low_clip'],
    #    config['high_clip']        
    #)    

    #shape = img.shape
    #img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #darker_hsv = img_hsv.copy()
    #if np.mean(darker_hsv[:, :, 2])<90:
    	#cv2.imwrite('./result/msrcr/%s'%(img_name),img_msrcr)
    #else:
	#cv2.imwrite('./result/msrcr/%s'%(img_name),img)
    #cv2.imwrite('./result/amsrcr/%s'%(img_name), img_amsrcr)
    #cv2.imwrite('./result/msrcp/%s'%(img_name),img_msrcp)
    #cv2.imshow('Image', img)
    #cv2.imshow('retinex', img_msrcr)
    #cv2.imshow('Automated retinex', img_amsrcr)
    #cv2.imshow('MSRCP', img_msrcp)
    #cv2.waitKey()
