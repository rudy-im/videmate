import numpy as np
import cv2
import mediapipe as mp



print("Connecting to camera...")

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Preparing face recognition...")

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, static_image_mode=True, max_num_faces=1)

print("Initialized!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            image_points = np.array([
                [face_landmarks.landmark[1].x, face_landmarks.landmark[1].y],      # Nose tip
                [face_landmarks.landmark[152].x, face_landmarks.landmark[152].y],  # Chin
                [face_landmarks.landmark[263].x, face_landmarks.landmark[263].y],  # Right eye outer
                [face_landmarks.landmark[33].x, face_landmarks.landmark[33].y],    # Left eye outer
                [face_landmarks.landmark[287].x, face_landmarks.landmark[287].y],  # Right mouth corner
                [face_landmarks.landmark[57].x, face_landmarks.landmark[57].y],    # Left mouth corner
            ], dtype="double") * [frame.shape[1], frame.shape[0]]
                

            model_points = np.array([
                [0.0, 0.0, 0.0],             # Nose tip
                [0.0, -63.6, -12.5],         # Chin
                [43.3, 32.7, -26.0],         # Right eye outer
                [-43.3, 32.7, -26.0],        # Left eye outer
                [28.9, -28.9, -24.1],        # Right mouth corner
                [-28.9, -28.9, -24.1]        # Left mouth corner
            ])

            focal_length = frame.shape[1]
            center = (frame.shape[1] / 2, frame.shape[0] / 2)
            camera_matrix = np.array([
                [focal_length, 0, center[0]],
                [0, focal_length, center[1]],
                [0, 0, 1]
            ], dtype="double")

            dist_coeffs = np.zeros((4, 1))

            success, rotation_vector, translation_vector = cv2.solvePnP(
                model_points, image_points, camera_matrix, dist_coeffs
            )

            if success:
                rmat, _ = cv2.Rodrigues(rotation_vector)
                angles, _, _, _, _, _ = cv2.RQDecomp3x3(rmat)
                pitch, yaw, roll = angles
                print(f"Yaw: {yaw:.2f}, Pitch: {pitch:.2f}, Roll: {roll:.2f}")
                cv2.putText(frame, f"Yaw: {yaw:.2f}, Pitch: {pitch:.2f}, Roll: {roll:.2f}", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.imshow('Head Turn', frame)


cap.release()
cv2.destroyAllWindows()

print("Camera released.")
