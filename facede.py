#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2 
casclf=cv2.CascadeClassifier('file_name.xml')
[i for i in dir(cv2.CascadeClassifier) if 'detect' in i]


# In[2]:


# appliyng or calling classifier
cap=cv2.VideoCapture(0)
while cap.isOpened() :
        status,frame=cap.read()
        #applying classifier in live frame
        face=casclf.detectMultiScale(frame,1.5,5) #classifying tuning parameter
        #print(face)
        for x,y,h,w in face:
            cv2.rectangle(frame,(x,y),(x+y,y+w),(0,0,255),2)
        cv2.imshow('face',frame)
        if   cv2.waitKey(10) & 0xff == ord('q'):
            break
cv2.destroyAllWindows()
cap.release()

