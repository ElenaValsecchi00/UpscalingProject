import numpy as np

import torch
import torchvision.transforms.functional as tf

import harmo_model as model

enhancer = model.Enhancer()
weights = torch.load("pretrained/enhancer.pth", map_location=torch.device("cpu"))
enhancer.load_state_dict(weights, strict=True)
enhancer.eval()

def inference(image: np.ndarray) -> np.ndarray:
    """
    Enhance the input image using the Harmonizer model.

    Args:
        image (np.ndarray): The input image to enhance.
    
    Returns:
        np.ndarray: The enhanced image.
    """
    original = tf.to_tensor(image)[None, ...]
    
    # NOTE: all pixels in the mask are equal to 1 as the mask is not used in image enhancement
    mask = original * 0 + 1
    
    # Enhance the image
    with torch.no_grad():
        arguments = enhancer.predict_arguments(original, mask)
        enhanced = enhancer.restore_image(original, mask, arguments)[-1]

    # RGB image
    enhanced = np.transpose(enhanced[0].cpu().numpy(), (1, 2, 0)) * 255
    return enhanced.astype(np.uint8)