import cv2
import mediapipe as mp

print("Connecting to camera...")

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Preparing face recognition...")

mp_face = mp.solutions.face_mesh
face = mp_face.FaceMesh(static_image_mode=True, max_num_faces=1)

print("Initialized!")

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    results = face.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    if results.multi_face_landmarks:
        for i, landmark in enumerate(results.multi_face_landmarks[0].landmark):
            h, w, _ = frame.shape
            x, y = int(landmark.x * w), int(landmark.y * h)
            #cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
            cv2.putText(frame, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0, 255, 0), 1)
            
    cv2.imshow('Face Mesh', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Camera released.")
