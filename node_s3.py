import io
import numpy as np
from PIL import Image, ImageSequence, ImageOps

# SaveImageToS3
class SaveImageToS3:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { 
                "images": ("IMAGE",),
                "presigned_url":  ("STRING", {"multiline": False, "default": ""}),
                },
                "hidden": {
                }}
    RETURN_TYPES = ()
    FUNCTION = "save_image_to_presignurl"
    CATEGORY = "image"
    OUTPUT_NODE = True

    def save_image_to_presignurl(self, images, presigned_url):
        image = images[0]
        i = 255. * image.cpu().numpy()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        response = requests.put(presigned_url, data=img_byte_arr)

        print(response.status_code)
        