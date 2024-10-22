import cv2
import mediapipe as mp
import numpy as np
from pynput.mouse import Button, Controller
import time

# Inicializa o controlador de mouse
mouse = Controller()

# Inicializa o MediaPipe Face Detection
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Captura vídeo da webcam
cap = cv2.VideoCapture(0)

# Variáveis para controle de piscar
last_blink_left = time.time()
last_blink_right = time.time()
blink_threshold = 0.2  # Tempo em segundos para considerar um piscar

with mp_face_mesh.FaceMesh(min_detection_confidence=0.5) as face_mesh:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Converte a imagem para RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Desenha os pontos do rosto
                mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACE_MESH_TESSELATION)

                # Coordenadas dos olhos
                left_eye = [face_landmarks.landmark[159], face_landmarks.landmark[145]]
                right_eye = [face_landmarks.landmark[386], face_landmarks.landmark[374]]

                # Calcula a altura dos olhos
                left_eye_height = abs(left_eye[0].y - left_eye[1].y)
                right_eye_height = abs(right_eye[0].y - right_eye[1].y)

                # Detecta piscar
                if left_eye_height < 0.01 and time.time() - last_blink_left > blink_threshold:
                    mouse.click(Button.left)
                    last_blink_left = time.time()
                
                if right_eye_height < 0.01 and time.time() - last_blink_right > blink_threshold:
                    mouse.click(Button.right)
                    last_blink_right = time.time()

                # Controla o mouse com a posição do rosto
                face_x = int(face_landmarks.landmark[1].x * frame.shape[1])
                face_y = int(face_landmarks.landmark[1].y * frame.shape[0])
                mouse.position = (face_x, face_y)

        # Mostra o quadro na tela
        cv2.imshow("Webcam", frame)

        # Sai do loop ao pressionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Libera a captura e fecha as janelas
cap.release()
cv2.destroyAllWindows()
