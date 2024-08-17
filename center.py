import cv2

# Đường dẫn của ảnh
output_path = "perspective_calibration/pixel_coordinates.jpg"  # Thay đổi đường dẫn và tên file theo mong muốn của bạn

# Khởi tạo đối tượng VideoCapture với URL của video stream
url = "http://192.145.18.102:4747/video"
video = cv2.VideoCapture(url)

while True:
    # Đọc frame từ video
    ret, frame = video.read()
    if not ret:
        break

    # Chuyển đổi ảnh sang ảnh đen trắng
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Nhị phân hóa ảnh
    thresh = cv2.Canny(gray, 127, 255)

    # Tìm contours trong ảnh
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Lọc và chỉ hiển thị 9 contours có kích thước bằng nhau
    filtered_contours = []
    for contour in contours:
        # Lấy kích thước của hình chữ nhật bao quanh contour
        x, y, w, h = cv2.boundingRect(contour)

        # Kiểm tra xem contour có kích thước đủ lớn để được coi là hình tròn không
        if w > 10 and h > 10:
            filtered_contours.append(contour)

    # Sắp xếp contours theo diện tích
    filtered_contours = sorted(filtered_contours, key=cv2.contourArea, reverse=True)[0:9]

    # Vẽ hình chữ nhật bao quanh 9 contours
    for contour in filtered_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Tìm tâm của hình chữ nhật
        center_x = x + w // 2
        center_y = y + h // 2

        # Vẽ tâm của hình chữ nhật
        cv2.circle(frame, (center_x, center_y), 3, (0, 0, 255), -1)

        # Hiển thị tọa độ pixel tâm của hình chữ nhật
        text = f"({center_x}, {center_y})"
        cv2.putText(frame, text, (center_x - 50, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Hiển thị frame với contours, hình chữ nhật và tâm của hình chữ nhật
    cv2.imshow('Rectangles and Centers', frame)

    # Lưu ảnh đã được chỉnh sửa khi nhấn phím 's'
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite(output_path, frame)
        print(f"Image captured and saved: {output_path}")

    # Thoát khỏi vòng lặp khi nhấn phím 'q'
    elif key == ord('q'):
        break

# Giải phóng đối tượng VideoCapture và đóng cửa sổ hiển thị
video.release()
cv2.destroyAllWindows()