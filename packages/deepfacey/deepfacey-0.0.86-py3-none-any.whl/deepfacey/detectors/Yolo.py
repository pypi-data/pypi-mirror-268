import os
from typing import Any, List
import numpy as np
import gdown
import cv2
from deepfacey.models.Detector import Detector, FacialAreaRegion
from deepfacey.commons import folder_utils
from deepfacey.commons.logger import Logger

logger = Logger()

# Model's weights paths
PATH = "/.deepface/weights/yolov8m-face.onnx"

# Google Drive URL from repo (https://github.com/derronqi/yolov8-face) ~6MB
WEIGHT_URL = "https://drive.usercontent.google.com/u/0/uc?id=1UX8saXoKt36H9uMsZIPJt4jk3NoDvNTL"

# Confidence thresholds for landmarks detection
# used in alignment_procedure function
LANDMARKS_CONFIDENCE_THRESHOLD = 0.5


class YoloClient(Detector):
    def __init__(self):
        self.model = self.build_model()

    def build_model(self) -> Any:
        """
        Build a yolo detector model
        Returns:
            model (Any)
        """

        opencv_version = cv2.__version__.split(".")

        if len(opencv_version) > 2 and int(opencv_version[0]) == 4 and int(opencv_version[1]) < 8:
            # min requirement: https://github.com/opencv/opencv_zoo/issues/172
            raise ValueError(
                f"Yolo onnx requires opencv-python >= 4.8 but you have {cv2.__version__}"
            )

        # Import the Ultralytics YOLO model

        weight_path = f"{folder_utils.get_deepface_home()}{PATH}"

        # Download the model's weights if they don't exist
        if not os.path.isfile(weight_path):
            gdown.download(WEIGHT_URL, weight_path, quiet=False)
            logger.info(f"Downloaded YOLO model {os.path.basename(weight_path)}")

        # Return face_detector
        return cv2.dnn.readNetFromONNX(weight_path)

    def detect_faces(self, img: np.ndarray) -> List[FacialAreaRegion]:
        """
        Detect and align face with yolo

        Args:
            img (np.ndarray): pre-loaded image as numpy array

        Returns:
            results (List[FacialAreaRegion]): A list of FacialAreaRegion objects
        """
        resp = []

        # # Detect faces

        INPUT_WIDTH = 640
        INPUT_HEIGHT = 640
        SCORE_THRESHOLD = 0.2
        NMS_THRESHOLD = 0.4
        CONFIDENCE_THRESHOLD = 0.4

        blob = cv2.dnn.blobFromImage(
            img, 1 / 255.0, (INPUT_WIDTH, INPUT_HEIGHT), swapRB=True, crop=False
        )
        self.model.setInput(blob)
        preds = self.model.forward()
        preds = preds.transpose((0, 2, 1))
        class_ids, confs, boxes = list(), list(), list()
        image_height, image_width, _ = img.shape
        x_factor = image_width / INPUT_WIDTH
        y_factor = image_height / INPUT_HEIGHT

        rows = preds[0].shape[0]
        for i in range(rows):
            row = preds[0][i]
            conf = row[4]

            classes_score = row[4:]
            _, _, _, max_idx = cv2.minMaxLoc(classes_score)
            class_id = max_idx[1]
            if classes_score[class_id] > 0.25:
                confs.append(conf)
                label = int(class_id)
                class_ids.append(label)

                # extract boxes
                x, y, w, h = row[0].item(), row[1].item(), row[2].item(), row[3].item()
                left = int((x - 0.5 * w) * x_factor)
                top = int((y - 0.5 * h) * y_factor)
                width = int(w * x_factor)
                height = int(h * y_factor)
                box = np.array([left, top, width, height])
                boxes.append(box)

        r_class_ids, r_confs, r_boxes = list(), list(), list()
        indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.25, 0.45)
        for i in indexes:
            r_class_ids.append(class_ids[i])
            r_confs.append(confs[i])
            r_boxes.append(boxes[i])

        for i in indexes:
            box = boxes[i]
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]
            confidence = confs[i]
            left_eye = (left + int(0.3 * width), (top + int(0.3 * height)))
            right_eye = (left + int(0.7 * width), (top + int(0.3 * height)))
            facial_area = FacialAreaRegion(
                x=left,
                y=top,
                w=width,
                h=height,
                left_eye=left_eye,  # type: ignore
                right_eye=right_eye,  # type: ignore
                confidence=confidence,
            )
            resp.append(facial_area)

        return resp
