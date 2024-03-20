from ultralytics import YOLO
import cv2
import os
class OBJ_DET:

    def detect(img_path, id):
        items = []
        file = open("detection_results.txt", "w")
        file.write("")
        file.close()
        model = YOLO('yolo-weights/yolov8l.pt')
        array = cv2.imread('./'+img_path)
        results = model(source=array, save=True, project=f"recipe_gen/static/output_images/", name=f"{id}")
        for r in results:
            boxes = r.boxes
            path = r.path
            for box in boxes:
                c = box.cls
                items.append(model.names[int(c)])
                file = open("detection_results.txt", "a")
                file.write(f"{model.names[int(c)]}\n")
                file.close()
        return items, path