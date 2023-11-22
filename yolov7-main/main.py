import os
import subprocess

from database.helper import *

def train_yolov7(image_dir, annotated_dir):
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_dir, filename)

            train_command = f"python train.py --workers 1 --device 0 --batch-size 4 --epochs 100 --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-custom_2 --weights yolov7.py"
            subprocess.run(train_command.split())

            detect_command = f"python detect.py --weights yolov7_custom.pt --conf 0.5 --img-size 640 --source {image_path} --view-img --no-trace"
            subprocess.run(detect_command.split())

            annotated_image_path = os.path.join(annotated_dir, filename)
            os.rename("path/to/your/detected/image.jpg", annotated_image_path)

    return annotated_dir

images_directory = r"yolov7-main\data\test"
annotated_images_directory = r"yolov7-main\data\train\images"
data = train_yolov7(images_directory, annotated_images_directory)
insert_directory(data)  