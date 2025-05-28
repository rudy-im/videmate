import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_face = mp.solutions.face_mesh
face = mp_face.FaceMesh()

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    results = face.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.multi_face_landmarks:
        for landmark in results.multi_face_landmarks[0].landmark:
            h, w, _ = frame.shape
            x, y = int(landmark.x * w), int(landmark.y * h)
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
    cv2.imshow('Face Mesh', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
