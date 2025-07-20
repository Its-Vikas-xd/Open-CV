# Opening Webcam

import cv2
'''
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # ret = True / Flase Frame = Image

    if not ret:
        print("Could not read frame")
        break

    cv2.imshow("Webcam feed",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Quitting....")
        break

cap.release()
cv2.destroyAllWindows()
'''

#Saving Video 

import cv2

camera = cv2.VideoCapture(0)

frame_heigh = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))

codec = cv2.VideoWriter_fourcc(*'XVID')  # Corrected here
recoder = cv2.VideoWriter("My_Video.avi", codec, 20, (frame_width, frame_heigh))  # Corrected here

while True:
    success, image = camera.read()

    if not success:  # Corrected here
        break

    recoder.write(image)
    cv2.imshow("Recording live", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
recoder.release()
cv2.destroyAllWindows()

















