import cv2

# Load the image
img = cv2.imread(r"C:\Users\Vikas\Desktop\OpenCV\Images\Img15.png")

# Check if image loaded successfully
if img is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours in green
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Iterate through each contour to detect shapes
for contour in contours:
    # Approximate the contour
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    corners = len(approx)
    
    # Determine shape based on number of corners
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        # Further check for square or rectangle
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        shape_name = "Square" if 0.95 <= aspect_ratio <= 1.05 else "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners > 5:
        shape_name = "Circle"
    else:
        shape_name = "Unknown"

    # Draw the approximated shape in red
    cv2.drawContours(img, [approx], 0, (0, 0, 255), 2)

    # Put the name of the shape on the image
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(img, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# Show the final image with detected shapes
cv2.imshow("Shape Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
