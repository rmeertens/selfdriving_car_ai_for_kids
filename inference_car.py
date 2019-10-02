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
    detector.loadModel(detection_speed="faster")

    while True:
        if not video_capture.isOpened():
            print('Unable to load camera')
            pass

        # Capture frame-by-frame
        ret, frame = video_capture.read()
        output_image, detections = detector.detectObjectsFromImage(input_image=frame, input_type='array', output_type='array')

        print({eachObject["name"]: eachObject["percentage_probability"] for eachObject in detections})
        h,w,c = output_image.shape

        toshow = cv2.resize(output_image, (2*w, 2*h))

        cv2.imshow('Video', toshow)

        result_key = cv2.waitKey(1)
        if result_key & 0xFF == ord('q'):
            break
        elif result_key & 0xFF == ord('s'):
            now = datetime.datetime.now()
            fileName = "image-{}.png".format(now).replace(" ", "_")
            output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(output_image, 'RGB')
            img.save(fileName)
            print("Captured", fileName)
        elif result_key & 0xFF == ord('l'):
            if detector.numbers_to_names[1] == 'bicycle': # looks like its english now.... lets switch to German
                detector.numbers_to_names = {0: 'Person', 1: 'Fahrrad', 2: 'Auto', 3: 'Motorrad', 4: 'Flugzeug', 5: 'Bus',
                                         6: 'Zug',
                                         7: 'LKW', 8: 'Boot', 9: 'Ampel', 10: 'Hydrant', 11: 'Stoppschild',
                                         12: 'Parkuhr',
                                         13: 'Bank', 14: 'Vogel', 15: 'Katze', 16: 'Hund', 17: 'Pferd', 18: 'Schaf',
                                         19: 'Kuh',
                                         20: 'Elefant',
                                         21: 'Bär', 22: 'Zebra', 23: 'Giraffe', 24: 'Rucksack', 25: 'Regenschirm',
                                         26: 'Handtasche',
                                         27: 'Krawatte',
                                         28: 'Koffer', 29: 'Frisbee', 30: 'Ski', 31: 'Snowboard', 32: 'Sportball',
                                         33: 'Drachen',
                                         34: 'Baseballschläger', 35: 'Baseballhandschuhe', 36: 'Skateboard', 37: 'Surfbrett',
                                         38: 'Tennisschläger',
                                         39: 'Flasche', 40: 'Weinglas', 41: 'Tasse', 42: 'Gabel', 43: 'Messer',
                                         44: 'Löffel',
                                         45: 'bowl',
                                         46: 'Banane', 47: 'Apfel', 48: 'Sandwich', 49: 'Orange', 50: 'Brokkoli',
                                         51: 'Karotte',
                                         52: 'Hot Dog',
                                         53: 'Pizza', 54: 'Donut', 55: 'Kuchen', 56: 'Stuhl', 57: 'Couch',
                                         58: 'Topfpflanze',
                                         59: 'Bett',
                                         60: 'Esstisch', 61: 'Toilette', 62: 'Fernseher', 63: 'Laptop', 64: 'Maus',
                                         65: 'Fernbedienung',
                                         66: 'Tastatur',
                                         67: 'Handy', 68: 'Mikrowelle', 69: 'Backofen', 70: 'Toaster', 71: 'Spüle',
                                         72: 'Kühlschrank',
                                         73: 'Buch', 74: 'Uhr', 75: 'Vase', 76: 'Schere', 77: 'Teddybär',
                                         78: 'Föhn',
                                         79: 'Zahnbürste'}
            else:
                detector.numbers_to_names = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane',
                                             5: 'bus',
                                             6: 'train',
                                             7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant',
                                             11: 'stop sign',
                                             12: 'parking meter',
                                             13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep',
                                             19: 'cow',
                                             20: 'elephant',
                                             21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella',
                                             26: 'handbag',
                                             27: 'tie',
                                             28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard',
                                             32: 'sports ball',
                                             33: 'kite',
                                             34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard',
                                             37: 'surfboard',
                                             38: 'tennis racket',
                                             39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife',
                                             44: 'spoon',
                                             45: 'bowl',
                                             46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli',
                                             51: 'carrot',
                                             52: 'hot dog',
                                             53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch',
                                             58: 'potted plant',
                                             59: 'bed',
                                             60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse',
                                             65: 'remote',
                                             66: 'keyboard',
                                             67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink',
                                             72: 'refrigerator',
                                             73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear',
                                             78: 'hair dryer',
                                             79: 'toothbrush'}

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
