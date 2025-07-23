import cv2

# Load Haar cascade classifiers for face, eye, and smile detection
face_cascade = cv2.CascadeClassifier(r"C:\Users\Vikas\Desktop\OpenCV\Coding\Face and Object Detection\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"C:\Users\Vikas\Desktop\OpenCV\Coding\Face and Object Detection\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(r"C:\Users\Vikas\Desktop\OpenCV\Coding\Face and Object Detection\haarcascade_smile.xml")

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Resize frame for better performance (optional)
    frame = cv2.resize(frame, (640, 480))
    
    # Convert frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Regions of interest for face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)
        if len(eyes) > 0:
            cv2.putText(frame, "Eyes Detected", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        # Detect smile within the face region
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)
        if len(smiles) > 0:
            cv2.putText(frame, "Smile Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Display the result
    cv2.imshow("Face, Eyes & Smile Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()
