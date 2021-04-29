from imageai.Detection import ObjectDetection, VideoObjectDetection
import os

def determineProbability(img):
    print('IMAGE--------------------', img)
    exec_path = os.getcwd()
    print(exec_path)
    exec_path,end_path = os.path.split(str(exec_path))
    print(exec_path,end_path)
    outputPath=os.path.join(exec_path,'PoacherWeb','media')
    exec_path = os.path.join(exec_path,'PoacherWeb','media',img)
    print(f'image path: {exec_path}')
    model_path=os.getcwd()
    print(model_path)

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(model_path,'Model', "resnet50_coco_best_v2.1.0.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=str(exec_path), output_image_path=os.path.join(outputPath,'output-'+img))
    person_probability = 0
    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        if(eachObject['name']=='person'):
            if(eachObject['percentage_probability']>person_probability):
                person_probability = eachObject['percentage_probability']
    print(detections)
    return [person_probability, 'output-'+img]
# determineProbability('abc')

def determineProbabilityFromVideo(vidName):
    print('#################################')
    print(vidName)
    # current Execution Path
    execution_path = os.getcwd()
    # Video execution Path
    input_path = os.path.join(execution_path, 'media', vidName)
    # output path
    output_path = os.path.join(execution_path, 'media', 'output-' + vidName)
    # Model Path
    model_path = os.path.join(execution_path, 'Model', 'resnet50_coco_best_v2.1.0.h5')

    # checking
    print("Cwd", execution_path)
    print("input path", input_path)
    print("output_path", output_path)
    print("model path", model_path)

    # detector = VideoObjectDetection()
    # detector.setModelTypeAsRetinaNet()
    # detector.setModelPath(model_path)
    # detector.loadModel()

    # video_path = detector.detectObjectsFromVideo(
    #             input_file_path = input_path,
    #             output_file_path = output_path,
    #             frames_per_second=1, log_progress=True)
    print('output-' + vidName)
    return 'output-' + vidName

if __name__ == '__main__':
    determineProbabilityFromVideo('abcd.mp4')

    
