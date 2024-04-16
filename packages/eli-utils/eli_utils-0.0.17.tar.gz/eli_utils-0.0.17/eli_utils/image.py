import io
import base64
import numpy as np
import cv2
from PIL import Image


def base64_to_image(data):
    return Image.open(io.BytesIO(base64.b64decode(data)))

def image_to_base64(image, for_web: bool=True):
    is_pil = isinstance(image, Image.Image)
    image = image if is_pil else Image.fromarray(image)
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = str(base64.b64encode(buffered.getvalue()), "utf-8")
    if for_web is True:
        img_base64 = f"data:image/png;base64,{img_base64}"
    return img_base64

def resize_image(image: Image.Image, desired_size: int):
    width, height = image.size
    aspect_ratio = width / height

    if width > height:
        new_width = desired_size
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = desired_size
        new_width = int(new_height * aspect_ratio)

    resized_image = image.resize((new_width, new_height))
    return resized_image

def change_dpi(image: Image.Image, output_path: str, dpi: int = 300):
    dpi = (dpi, dpi)
    image.info['dpi'] = dpi
    image.save(output_path, dpi=dpi)


def change_dpi_from_file(input_path, output_path: str, dpi: int = 300):
    image = Image.open(input_path)
    dpi = (dpi, dpi)
    image.info['dpi'] = dpi
    image.save(output_path, dpi=dpi)

def transform_image_to_k_colors(image: np.ndarray, num_clusters: int) -> np.ndarray:
    from sklearn.cluster import KMeans


    h, w, c = image.shape
    image_flattened = image.reshape((h * w, c))

    kmeans = KMeans(n_clusters=num_clusters, n_init="auto")
    kmeans.fit(image_flattened)
    labels = kmeans.predict(image_flattened)
    centroid_colors = kmeans.cluster_centers_.astype(int)
    transformed_image = centroid_colors[labels].reshape((h, w, c))

    return transformed_image

def make_canny(image: np.ndarray, low: int = 100, high: int=200):
    is_pil = isinstance(image, Image.Image)
    image = np.array(image)
    canny_image = cv2.Canny(image, low, high)
    canny_image = canny_image[:, :, None]
    if is_pil:
        canny_image = np.concatenate([canny_image, canny_image, canny_image], axis=2)
        canny_image = Image.fromarray(canny_image)
    return canny_image
