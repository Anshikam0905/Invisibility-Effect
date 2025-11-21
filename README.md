# Invisible Cloak using Python + OpenCV

This project creates a Green Screen Invisibility Cloak Effect using Python and OpenCV.
When the camera detects green color in the frame, it replaces that area with a background image — creating a high-quality invisibility effect.

# Features

• Written 100% in Python
• Real-time invisibility cloak effect
• Works using green cloth / green screen
• Uses HSV color masking for accurate detection
• Clean output using morphological operations
• Includes high-quality background replacement

# Technologies Used

• Python 3.x
• OpenCV
• NumPy

# Installation

1️⃣ Clone the Repository
git clone https://github.com/Anshikam0905/InvisibilityCloak.git
cd InvisibilityCloak

2️⃣ Install Dependencies
pip install opencv-python numpy

# How to Run

Place your background image inside the project folder
(example: Background.jpg)

**Run the script:**

python cloak.py


Show a green cloth in front of the webcam

Press q to exit

