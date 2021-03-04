from imageai.Detection import ObjectDetection
import os

exec_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(exec_path , "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(exec_path , "image1.jpg"), output_image_path=os.path.join(exec_path , "output1.jpg"))
for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )