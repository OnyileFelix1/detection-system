import cv2

def is_motion_detected(frame, prev_frame, threshold=25):
    diff_frame = cv2.absdiff(prev_frame, frame)
    _, threshold_frame = cv2.threshold(diff_frame, threshold, 255, cv2.THRESH_BINARY)
    return cv2.countNonZero(threshold_frame) > 0

cap = cv2.VideoCapture()  
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  
cap.set(cv2.CAP_PROP_FPS, 15)


_, prev_frame = cap.read()
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

_, current_frame = cap.read()
current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

while True:
   
    _, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    if is_motion_detected(frame_gray, prev_frame):
        print("Motion detected!")

    cv2.imshow("Motion Detection", frame_gray)

    prev_frame = frame_gray

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
