import base64
from PIL import Image
from io import BytesIO

# def encode_image(image):
#     with open(image, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
#     return encoded_string

def encode_reduced_image(image_path):
    with Image.open(image_path) as img:
        img.thumbnail((256, 256))
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
