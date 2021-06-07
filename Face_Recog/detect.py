# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:09:16 2021

@author: Mehmet Akıncı
"""
import cv2
import numpy as np





modelConfiguration = "YOLO/yolov3.cfg"
modelWeights = "YOLO/yolov3.weights"

net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeights)

net.setPreferableBackend(cv2.dnn.DNN_TARGET_CPU)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


classes = []

with open("YOLO/coco.names.txt") as file:
        classes = file.read().splitlines()


whT = 320
confThreshold = 0.5
nmsThreshold = 0.3





colors = [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(0,0,0)]
font = cv2.FONT_HERSHEY_PLAIN

def Config(img):
    blob = cv2.dnn.blobFromImage(img, 1/255, (whT,whT), (0,0,0), swapRB=False, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)
    
    return layerOutputs

def Detect(img):
    height, width, _ = img.shape
    
    boxes = []
    confidences = []
    class_ids = []
    
    layerOutputs=Config(img)
    
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confThreshold:
                x_center = int(detection[0]*width)
                y_center = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
            
                x = int(x_center - w/2)
                y = int(y_center - h/2)
            
                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes,confidences,confThreshold,nmsThreshold)
    
    for i in indexes.flatten():
        x,y,w,h = boxes[i]
        
        label = str(classes[class_ids[i]]).capitalize()
        confidence = str(100*round(confidences[i]))
        color = colors[2]
        cv2.rectangle(img,(x,y),(x+w,y+h),color, 5)
        cv2.putText(img,label + " [%" + confidence + "]", (x,y-10), font,2,color,2) 
    return img





