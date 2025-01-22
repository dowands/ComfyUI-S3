import io
import requests
import numpy as np
from PIL import Image, ImageSequence, ImageOps

# SaveImageToS3
class SaveImageToS3:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { 
                "images": ("IMAGE",),
                "presigned_url":  ("STRING", {"multiline": False, "default": ""}),
            },
            "hidden": {}
        }
    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("images", )
    FUNCTION = "save_image_to_presignurl"
    CATEGORY = "image"
    OUTPUT_NODE = True

    def save_image_to_presignurl(self, images, presigned_url):
        image = images[0]
        i = 255. * image.cpu().numpy()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        response = requests.put(presigned_url, data=img_byte_arr)

        print(response.status_code)
        return ( images, )
        


NODE_CLASS_MAPPINGS = {
    "SaveImageToS3": SaveImageToS3,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveImageToS3": "Save image to s3 presignUrl",
}