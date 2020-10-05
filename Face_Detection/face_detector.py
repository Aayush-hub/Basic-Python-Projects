import cv2
import argparse


# Defining arguments to be obtained
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to input image")
args = vars(ap.parse_args())


image = cv2.imread(args['image']) 
gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.15, 5)

for (x, y, w, h) in faces:
	cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)

cv2.imshow("Faces Detected", image)
cv2.imwrite('output.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
  