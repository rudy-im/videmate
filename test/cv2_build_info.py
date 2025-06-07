import cv2

info = cv2.getBuildInformation()

for line in info.split('\n'):
    print(line.strip())
