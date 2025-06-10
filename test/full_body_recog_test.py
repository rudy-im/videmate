import cv2
import mediapipe as mp



print("Connecting to camera...")

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Preparing face recognition...")

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

print("Initialized!")

with mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    enable_segmentation=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as pose:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = pose.process(image_rgb)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
            )

            for idx, landmark in enumerate(results.pose_landmarks.landmark):
                h, w, _ = frame.shape
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                cv2.putText(frame, str(idx), (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 0, 255), 1, cv2.LINE_AA)


        cv2.imshow('Full Body Pose Tracking', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



cap.release()
cv2.destroyAllWindows()



print("Camera released.")






