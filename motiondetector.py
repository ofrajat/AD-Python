#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[5]:


cap=cv2.VideoCapture(0) #camera no..or we can give url of video

# status of camera
tp1=cap.read()[1]   #take1
tp2=cap.read()[1]   #take2
tp3=cap.read()[1]   #take3

#to make more perfect 
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)    #converting into grey
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)    
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)

#now creating image diferentiater
def img_diff(x,y,z):
    # differnece between x,y --grey1,grey2  --d1
    d1=cv2.absdiff(x,y)
    #diff b/w y,z --grey2,grey3 ----d2
    d2=cv2.absdiff(x,y) 
    # absolute differnce d1-d2
    finaling=cv2.bitwise_and(d1,d2)
    return finaling 

#now apply function 
while cap.isOpened():
    status,frame=cap.read()  #continue image taker   
     
    motionimg= img_diff(gray1,gray2,gray3)
        #replacing image frame 
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # passing live image to grey3
    cv2.imshow('live',frame)
    cv2.imshow('motion',motionimg)
    if   cv2.waitKey(10) & 0xff == ord('q'):
        break


cv2.destroyAllWindows()
cap.release()


# In[ ]:


#opencv2 support XML , JSON ,CSV 

