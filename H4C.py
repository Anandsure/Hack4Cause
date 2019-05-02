import cv2
'''
f_c = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
e_c = cv2.CascadeClassifier('haarcascade_eye.xml')
'''
f_c = cv2.CascadeClassifier('/Users/anandsure/Downloads/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
e_c= cv2.CascadeClassifier('/Users/anandsure/Downloads/opencv-master/data/haarcascades/haarcascade_smile.xml')
#ub_c = cv2.CascadeClassifier('/Users/anandsure/Downloads/opencv-master/data/haarcascades/haarcascade_upperbody.xml')

def detect(gray,frame):
    faces = f_c.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces and eyes:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h , x:x+w]
        roi_color = frame[y:y+h , x:x+w]
        eyes = e_c.detectMultiScale(roi_gray,1.1,3)
        #for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(x,y),(x+w,y+h),(0,255,0),2)
    return frame
v_c = cv2.VideoCapture(0)
while True:
    _,frame = v_c.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas = detect(gray,frame)
    cv2.imshow('Video',canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
v_c.release()
cv2.destroyAllWindows()
    
