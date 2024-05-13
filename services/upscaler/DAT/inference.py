import torch
import cv2
import numpy as np

from utils import get_root_logger, imwrite, tensor2img, img2tensor
from utils.matlab_functions import rgb2ycbcr
from models.dat_model import DATModel
from models import build_model
from torchvision.transforms.functional import normalize

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
        "pretrain_network_g": "models/DAT_x4.pth",
        "strict_load_g": True
    },
    "val": {
        "save_img": True,
        "suffix": 'x4',  # add suffix to saved images, if None, use exp name
        "use_chop": False  # True to save memory, if img too large
    }
}
model: DATModel = build_model(opt)


def load_image(image_path: str) -> dict:
    """
    Take a path to an image and return a dictionary containing the image as a tensor.

    Args:
        img_np (np.ndarray): Image as numpy array.
    """
    # Load image
    # TODO: Load image from AWS S3 bucket
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img = img.astype(np.float32) / 255.

    # To tensor
    img = img2tensor(img, bgr2rgb=True, float32=True)

    return {'lq': img}


def inference(image_path: str):
    """
    Take an image path, upscale it and save the result.

    Args:
        image_path (str): Path to the image.
    """
    # Load image
    image = load_image(image_path)
    model.feed_data(image)

    # Inference
    model.test()
    visuals = model.get_current_visuals()
    sr_img = tensor2img([visuals['result']])

    # Save image
    # TODO: Save image to AWS S3 bucket
    imwrite(sr_img, OUTPUT_PATH + 'sr.png')


if __name__ == '__main__':
    inference('images/baboon.png')
