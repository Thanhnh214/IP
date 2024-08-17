import cv2
import mediapipe as mp
import time

mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils

# Specify the directory to save the image
save_directory = r'G:\University\Image Processing and Robot Vision\Final\hta0-horizontal-robot-arm-master\perspective_calibration'

url = "http://192.145.18.102:4747/video"
cap = cv2.VideoCapture(url)

with mp_objectron.Objectron(static_image_mode=False,
                            max_num_objects=2,
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.8,
                            model_name='Cup') as objectron:

    save_image = False 

    while cap.isOpened():

        success, image = cap.read()

        start = time.time()

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = objectron.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.detected_objects:
            for detected_objects in results.detected_objects:
                mp_drawing.draw_landmarks(image, detected_objects.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
                mp_drawing.draw_axis(image, detected_objects.rotation, detected_objects.translation)

        end = time.time()
        totalTime = end - start

        fps = 1 / totalTime

        cv2.putText(image, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

        cv2.imshow('MediaPipe Objectron', image)

        key = cv2.waitKey(1)
        #Press Esc to Escape. Space to Captured Image
        if key == 27:  # Ấn Esc để thoát
            break
        elif key == 32:
            save_image = True

        if save_image:
            image_path = save_directory + '\\captured_image.jpg'
            cv2.imwrite(image_path, image)
            print("Done! Image saved at:", image_path)
            save_image = False

cap.release()
cv2.destroyAllWindows()
