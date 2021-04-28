import cv2

data = cv2.CascadeClassifier('haarcascade.xml')

video = cv2.VideoCapture('pedestrians.mp4')

while True:
    ret, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    human_coordinates = data.detectMultiScale(gray_frame)
    
    for x in human_coordinates:
        cv2.rectangle(frame, (x[0], x[1]), (x[0]+x[2], x[1]+x[3]), (0, 255, 0), 2)
    
    cv2.imshow('pedestrian detector', frame)
    
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break

video.release()
cv2.destroyAllWindows()

# print('code completed')