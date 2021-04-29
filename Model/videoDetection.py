from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()

custom_objects = detector.CustomObjects(person=True, bicycle=True, motorcycle=True)

video_path = detector.detectObjectsFromVideo(
                input_file_path=os.path.join(execution_path, "Animal.mp4"),
                output_file_path=os.path.join(execution_path, "Animal_output"),
                frames_per_second=1, log_progress=True)
print(video_path)