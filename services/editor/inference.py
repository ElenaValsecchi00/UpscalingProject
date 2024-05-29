import torch
import cv2
import numpy as np

from utils import get_root_logger, imwrite, tensor2img, img2tensor
from utils.matlab_functions import rgb2ycbcr
from models.dat_model import DATModel
from models import build_model
from torchvision.transforms.functional import normalize
from buckets import upload_to_aws, download_from_aws


OUTPUT_PATH = 'res/'
opt = {
    "name": "test_single_x4",
    "model_type": "DATModel",
    "scale": 4,
    "num_gpu": 1 if torch.cuda.is_available() else 0,
    "manual_seed": 10,
    "is_train": False,
    "dist": False,
    "network_g": {
        "type": "DAT",
        "upscale": 4,
        "in_chans": 3,
        "img_size": 64,
        "img_range": 1.,
        "split_size": [8, 32],
        "depth": [6, 6, 6, 6, 6, 6],
        "embed_dim": 180,
        "num_heads": [6, 6, 6, 6, 6, 6],
        "expansion_factor": 4,
        "resi_connection": '1conv'
    },
    "path": {
        "pretrain_network_g": "pretrained/DAT_x4.pth",
        "strict_load_g": True
    },
    "val": {
        "save_img": True,
        "suffix": 'x4',  # add suffix to saved images, if None, use exp name
        "use_chop": False  # True to save memory, if img too large
    }
}
model: DATModel = build_model(opt)
def get_model():
    return model


def inference(image, model) -> np.ndarray:
    """
    Take an image path, upscale it and save the result.

    Args:
        image_path (str): Path to the image.
    """    
    # Convert image to tensor
    # To tensor
    image = img2tensor(image, bgr2rgb=True, float32=True)

    
    model.feed_data({'lq':image})

    # Inference
    model.test()
    visuals = model.get_current_visuals()
    sr_img = tensor2img([visuals['result']])
    
    return sr_img


if __name__ == '__main__':
    inference('images/baboon.png')
