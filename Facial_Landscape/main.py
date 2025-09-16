import cv2
import mediapipe as mp

# Initialize MediaPipe FaceMesh

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh( static_image_mode=False, max_num_faces = 3 )

# Drawing utils
map_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Start webcam capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("Ignoring empty camera frame.")
        continue


    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and find face mesh
    
