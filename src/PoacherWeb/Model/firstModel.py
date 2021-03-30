from imageai.Detection import ObjectDetection
import os

def determineProbability(img):
    exec_path = os.getcwd()
    print(exec_path)
    exec_path,end_path = os.path.split(str(exec_path))
    print(exec_path,end_path)
    img_path = os.path.join(exec_path,'PoacherWeb','media',img)
    print(f'image path is: {img_path}')
    model_path=os.getcwd()
    model_path=os.path.join(model_path,'Model','resnet50_coco_best_v2.1.0.h5')
    print(f'model path is : {model_path}')

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(model_path)
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=img_path, output_image_path= "output "+img)
    person_probability = 0
    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        if(eachObject['name']=='person'):
            if(eachObject['percentage_probability']>person_probability):
                person_probability = eachObject['percentage_probability']
    print(detections)
    return person_probability
