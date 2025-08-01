# Import OpenCV library
import cv2

# ==========================
# Load Haar Cascade Classifiers
# ==========================
# Load the pre-trained Haar cascade files for detecting faces, eyes, and smiles.
face_cascade = cv2.CascadeClassifier(r"C:\Users\Vikas\Desktop\Projects\OpenCV\Coding\Face and Object Detection\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"C:\Users\Vikas\Desktop\Projects\OpenCV\Coding\Face and Object Detection\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(r"C:\Users\Vikas\Desktop\Projects\OpenCV\Coding\Face and Object Detection\haarcascade_smile.xml")

# ==========================
# Initialize Webcam
# ==========================
cap = cv2.VideoCapture(0)  # 0 is the default camera

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# ==========================
# Real-time Video Processing Loop
# ==========================
while True:
    ret, frame = cap.read()  # Read frame from the webcam
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Optional: Resize the frame for performance
    frame = cv2.resize(frame, (640, 480))

    # Convert the frame to grayscale (Haar cascades work on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ==========================
    # Face Detection
    # ==========================
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # Loop through all detected faces
    for (x, y, w, h) in faces:
        # Draw a green rectangle around each face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Define region of interest (ROI) within the face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # ==========================
        # Eye Detection within Face ROI
        # ==========================
        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=10
        )
        if len(eyes) > 0:
            # If eyes are detected, display label
            cv2.putText(frame, "Eyes Detected", (x, y - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        # ==========================
        # Smile Detection within Face ROI
        # ==========================
        smiles = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.7,
            minNeighbors=20
        )
        if len(smiles) > 0:
            # If smile is detected, display label
            cv2.putText(frame, "Smile Detected", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # ==========================
    # Display the Processed Frame
    # ==========================
    cv2.imshow("Face, Eyes & Smile Detection", frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ==========================
# Release Resources
# ==========================
cap.release()
cv2.destroyAllWindows()
