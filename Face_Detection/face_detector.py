import cv2
import argparse


# Defining arguments to be obtained
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to input image")
args = vars(ap.parse_args())

# Read the image from the path given in the command line
image = cv2.imread(args['image'])

# Convert image from BGR to Grayscale 
gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Create a cascade classifier as shown below using Haarcascades for face detection
face_cascade=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# Pass in the grayscale image and perform face detection
faces = face_cascade.detectMultiScale(gray, 1.15, 5)

# For every face detected, draw a bounding box around it
for (x, y, w, h) in faces:
	cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)

# Display the images with faces detected
cv2.imshow("Faces Detected", image)

# Save the image as output.jpg
cv2.imwrite('output.jpg', image)

# Wait for a key press to close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
  