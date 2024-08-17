import cv2
import os
import numpy as np

save_path = "perspective_calibration/"

os.makedirs(save_path, exist_ok=True)

url = "http://192.145.18.102:4747/video"
video = cv2.VideoCapture(url)

image_index = 1

# Assume you have already computed the camera matrix (mtx) and distortion coefficients (dist)
# If not, you should replace the following dummy values with your actual calibration results.
mtx = np.array([[600, 0, 320], [0, 600, 240], [0, 0, 1]])
dist = np.array([0, 0, 0, 0, 0])

try:
    while True:
        ret, frame = video.read()
        if not ret:
            print("Failed to capture frame")
            break

        # Compute the center of the camera based on the principal point in the camera matrix
        principal_point = (mtx[0, 2], mtx[1, 2])

        # Vẽ một hình tròn tại tâm camera
        radius = 10
        color = (0, 255, 0)  # Màu xanh lá cây
        thickness = 2
        cv2.circle(frame, (int(principal_point[0]), int(principal_point[1])), radius, color, thickness)

        # Hiển thị frame
        cv2.imshow("IPCam", frame)

        key = cv2.waitKey(1)
        if key % 256 == 32:  # 'space' key
            image_name = f"captured_image_{image_index}.jpg"
            full_path = os.path.join(save_path, image_name)
            cv2.imwrite(full_path, frame)
            print(f"Image captured: {full_path}")
            image_index += 1

        elif key % 256 == 27:  # 'esc' key
            break

except KeyboardInterrupt:
    pass

finally:
    video.release()
    cv2.destroyAllWindows()

print("Frame size:", frame.shape)
