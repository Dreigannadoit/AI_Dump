import cv2
import mediapipe as mp

# Initialize MediaPipe FaceMesh

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()