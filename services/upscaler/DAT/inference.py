import torch
import cv2
import numpy as np

from utils import get_root_logger, imwrite, tensor2img, img2tensor
from utils.matlab_functions import rgb2ycbcr
from models.dat_model import DATModel
from models import build_model
from torchvision.transforms.functional import normalize

opt = {
    "name": "test_single_x4",
    "model_type": "DATModel",
    "scale": 4,
    "num_gpu": 1,
    "manual_seed": 10,
    "network_g": {
        "type": "DAT",
        "upscale": 4,
        "in_chans": 3,
        "img_size": 64,
        "img_range": 1.,
        "split_size": [8,32],
        "depth": [6,6,6,6,6,6],
        "embed_dim": 180,
        "num_heads": [6,6,6,6,6,6],
        "expansion_factor": 4,
        "resi_connection": '1conv'
    },
    "path": {
        "pretrain_network_g": "models/DAT_x4.pth",
        "strict_load_g": True
    },
    "val":{
        "save_img": True,
        "suffix": 'x4',  # add suffix to saved images, if None, use exp name
        "use_chop": False  # True to save memory, if img too large
    }
}
model: DATModel = build_model(opt)

def load_image(img_np: np.ndarray):
    img_lq = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

    # BGR to YCbCr
    img_lq = rgb2ycbcr(img_lq, y_only=True)[..., None]

    # BGR to RGB, HWC to CHW, numpy to tensor
    img_lq = img2tensor(img_lq, bgr2rgb=True, float32=True)

    # normalize
    mean, std = True, True
    normalize(img_lq, mean, std, inplace=True)
    return {'lq': img_lq, 'lq_path': ""}

def inference(image: np.ndarray):
    model.feed_data(load_image(image))
    model.test()

    visuals = model.get_current_visuals()
    sr_img = tensor2img([visuals['result']])

    # tentative for out of GPU memory
    del model.lq
    del model.output
    torch.cuda.empty_cache()

    # Save image
    cv2.imwrite(sr_img, 'res/result1.png')
    
if __name__ == '__main__':
    img = cv2.imread('images/baboon.png')
    inference(img)