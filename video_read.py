import cv2

frame_width = 640
frame_height = 480

video = cv2.VideoCapture("luckys_tale.mp4")

while True:
    success, img = video.read()
    if success:
        cv2.resize(img, (frame_width, frame_height))
        cv2.imshow("Luckys Tale", img)

        k = cv2.waitKey(40)  # 25 fps

        if k & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
