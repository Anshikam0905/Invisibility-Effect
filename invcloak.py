import cv2
import numpy as np

# Start the webcam
cap = cv2.VideoCapture(0)

# Load the background image and resize it
background = cv2.imread('Background.jpg')
background = cv2.resize(background, (640, 480))

# Kernel for morphology
kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize and blur the frame for smoother detection
    frame = cv2.resize(frame, (640, 480))
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # Convert to HSV color space
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    # WIDER HSV range for better green detection
    lower_green = np.array([25, 30, 30])
    upper_green = np.array([95, 255, 255])

    # Create green mask
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Morphological operations to clean up noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    # Invert mask
    mask_inv = cv2.bitwise_not(mask)

    # Segment green area from background
    green_area = cv2.bitwise_and(background, background, mask=mask)

    # Segment non-green from original frame
    non_green_area = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Merge final output
    final_output = cv2.add(non_green_area, green_area)

    # Show the result
    cv2.imshow("Strong Invisible Cloak", final_output)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
