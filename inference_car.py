from PIL import Image
from imageai.Detection import ObjectDetection
import os
import cv2
import datetime

if __name__ == "__main__":

    WEBCAM_ID = 0
    execution_path = os.getcwd()
    model_path = os.path.join(execution_path, "yolo.h5")

    if not os.path.exists(model_path):
        print("ERROR! Download the model from here: https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5")
        exit(-1)
    video_capture = cv2.VideoCapture(WEBCAM_ID)

    # Create the object detection network
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()

    while True:
        if not video_capture.isOpened():
            print('Unable to load camera')
            pass

        # Capture frame-by-frame
        ret, frame = video_capture.read()
        output_image, detections = detector.detectObjectsFromImage(input_image=frame, input_type='array', output_type='array')

        print({eachObject["name"]: eachObject["percentage_probability"] for eachObject in detections})

        cv2.imshow('Video', output_image)

        result_key = cv2.waitKey(1)
        if result_key & 0xFF == ord('q'):
            break
        elif result_key & 0xFF == ord('s'):
            now = datetime.datetime.now()
            fileName = "image-{}.png".format(now).replace(" ", "_")
            img = Image.fromarray(output_image, 'RGB')
            img.save(fileName)
            print("Captured", fileName)

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
