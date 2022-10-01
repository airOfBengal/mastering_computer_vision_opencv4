import cv2

frame_width = 640
frame_height = 480

cam_video = cv2.VideoCapture(0)
cam_video.set(3, frame_width)
cam_video.set(4, frame_height)

while True:
    success, img = cam_video.read()
    if success:
        cv2.imshow("Default webcam", img)

        k = cv2.waitKey(40)
        if k & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
