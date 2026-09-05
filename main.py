import cv2
from ultralytics import YOLO

model = YOLO('yolov8s.pt')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model(frame, stream=True)

    for result in results:
        annotated_frame = result.plot()

    cv2.imshow("Real-Time Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()