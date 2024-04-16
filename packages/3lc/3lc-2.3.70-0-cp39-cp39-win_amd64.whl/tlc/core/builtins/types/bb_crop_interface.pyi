from PIL import Image
from tlc.core.builtins.constants.column_names import X0 as X0, X1 as X1, Y0 as Y0, Y1 as Y1
from tlc.core.builtins.types.bounding_box import BoundingBox as BoundingBox
from tlc.core.schema import Schema as Schema

class BBCropInterface:
    """Interface for creating bounding box crops."""
    @staticmethod
    def crop(image_path: str | Image.Image, bb_dict: dict[str, float | int], bb_schema: Schema, image_height: int = 0, image_width: int = 0) -> Image.Image:
        """Crops an image according to a bounding box and returns the cropped image.

        :param image_path: Path to the image to crop.
        :param bb_dict: Dictionary containing bounding box coordinates under the keys X0, Y0, X1, Y1.
        :param bb_schema: Schema for the bounding box.
        :param image_height: Height of the original image (only necessary if box is in relative coordinates).
        :param image_width: Width of the original image (only necessary if box is in relative coordinates).
        :returns: Cropped image.
        """
