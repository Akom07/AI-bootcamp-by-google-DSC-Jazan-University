import cv2

face = cv2.CascadeClassifier('myTriningData.xml')

camera = cv2.VideoCapture(0)
while True:
    read_ok, frame = camera.read()
    leabels = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
camera.release()
cv2.destroyAllWindows()
