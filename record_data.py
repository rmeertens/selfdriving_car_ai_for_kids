import cv2
import time

if __name__ == "__main__":
    WEBCAM_ID = 1

    video_capture = cv2.VideoCapture(WEBCAM_ID)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)

    anterior = 0

    while True:
        if not video_capture.isOpened():
            print('Unable to load camera. Use the command "xhost +"')
            pass

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Display the resulting frame
        cv2.imshow('Video', frame)

        result_key = cv2.waitKey(1)
        print(result_key)
        if result_key & 0xFF == ord('q'):
            break
        if result_key & 0xFF == ord('b'):
            cv2.imwrite("unlabeled_images/"+time.strftime("%Y-%m-%d-%H:%M:%S") + ".png", frame)


    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()