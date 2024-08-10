import cv2
import time 
import os 
import HandTrackingModule as htm

wCam ,hCam = 1080,480
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)


detector = htm.HandDetector(detectionCon=0.75)    

tipIds = [4,8,12,16,20]    

while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    #print(lmList)
    
    if len(lmList) !=0:
        fingers=[]
        
        #thumb
        
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #4 fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]: #finger is up 
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)
        totalFinger=fingers.count(1)
        #print(totalFinger)
        if totalFinger == 1 and lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2]:
            print("I")
            totalFinger = "I"
        elif totalFinger == 1 and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]:
            print("Fuck you")
            totalFinger = "Fuck You"
        elif totalFinger == 2 and lmList[tipIds[0]][2] < lmList[tipIds[0]-2][2] and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]:
            print("L")
            totalFinger ="L"
        
    
            
            
   
        
        cv2.rectangle(img,(20,225),(170,425),(0,255,0),cv2.FILLED)
        if totalFinger == "Fuck You":
            cv2.putText(img,str(totalFinger),(45,375),cv2.FONT_HERSHEY_COMPLEX,5,(255,0,0),18)
        else:
             cv2.putText(img,str(totalFinger),(45,375),cv2.FONT_HERSHEY_COMPLEX,5,(255,0,0),18)
        
        
    cv2.imshow("Image",img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
