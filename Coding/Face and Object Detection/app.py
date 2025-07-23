import cv2

face_cascade = cv2.CascadeClassifier(r"C:\Users\Vikas\Desktop\OpenCV\Coding\Face and Object Detection\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)
    """
    detectMultiScale() - scan & detect objects in the image
    1.1 balance, not too slow , blind 

    minneighbors - how many neighbors each candidate rectangle should have to retain it
    
    
    """

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)


        """
        face = [q
        (100,150,80,80) face 1
        (250,120,90,90 ) face 2
    ]

    x = how far from the left side of the image
    y = how far from the top side of the image
    w = width of the rectangle
    h = height of the rectangle
        
        """
    cv2.imshow("Face Detection", frame) 


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
