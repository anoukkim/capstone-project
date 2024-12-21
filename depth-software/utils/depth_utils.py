import torch
from transformers import AutoImageProcessor, AutoModelForDepthEstimation
import cv2


def generate_depth_image(image):
    processor = AutoImageProcessor.from_pretrained("LiheYoung/depth-anything-large-hf")
    model = AutoModelForDepthEstimation.from_pretrained("LiheYoung/depth-anything-large-hf").to("cpu")
    input_image = processor(images=image, return_tensors='pt').to("cpu")

    with torch.no_grad():
        outputs = model(**input_image)
        depth = outputs.predicted_depth
    depth_image = depth.squeeze().cpu().numpy()
    depth_normalized = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    return cv2.applyColorMap(depth_normalized, cv2.COLORMAP_MAGMA)
