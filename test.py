# from keras.models import load_model

# model = load_model('Model/Outputs/finalModel.h5')

# import the opencv library 
import cv2 
import numpy as np
# define a video capture object 
vid = cv2.VideoCapture(0) 


    
while(True):
    ret, frame = vid.read() 
    #print(type(frame))
    print(np.array(frame).shape)
    frame1 = cv2.resize(frame,(30,30))
    image = np.expand_dims(frame1, axis=0)
    image = np.array(image)
    print(image)
    

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vid.release() 
cv2.destroyAllWindows() 

