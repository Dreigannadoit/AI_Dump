import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

while True:
    _,img = webcam.read()

    # make black and white
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(grey, 1.5, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, ( x, y ), (x + w, y + h), (0, 255, 0), 3)


    cv2.imshow("Face detection", img)

    key = cv2.waitKey(10)
    
    if key == 27:
        break


webcam.release()
cv2.destroyAllWindows()
