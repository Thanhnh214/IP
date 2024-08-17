import cv2
import os

save_path = "perspective_calibration/"

os.makedirs(save_path, exist_ok=True)

url = "http://192.145.18.102:4747/video"
video = cv2.VideoCapture(url)

image_index = 1

while True:
    ret, frame = video.read()
    if ret:
        cv2.imshow("IPCam", frame)

        # Check for the key 'space'
        key = cv2.waitKey(1)
        if key%256 == 32:
            image_name = f"calib{image_index}.jpg"
            full_path = os.path.join(save_path, image_name)
            cv2.imwrite(full_path, frame)
            print(f"Image captured: {full_path}")
            image_index += 1

        # Check for the key 'esc' to exit the loop
        elif key%256 == 27:
            break

video.release()
cv2.destroyAllWindows()