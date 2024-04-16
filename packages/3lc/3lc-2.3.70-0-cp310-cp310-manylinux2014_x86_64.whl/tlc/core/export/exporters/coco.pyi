from _typeshed import Incomplete
from tlc.core.builtins.constants.column_names import BOUNDING_BOXES as BOUNDING_BOXES, BOUNDING_BOX_LIST as BOUNDING_BOX_LIST, HEIGHT as HEIGHT, IMAGE as IMAGE, WIDTH as WIDTH
from tlc.core.builtins.types.bounding_box import BoundingBox as BoundingBox, SegmentationBoundingBox as SegmentationBoundingBox
from tlc.core.export.exporter import Exporter as Exporter, register_exporter as register_exporter
from tlc.core.objects.table import Table as Table
from tlc.core.schema import StringValue as StringValue
from tlc.core.url import Url as Url
from tlc.core.utils.progress import track as track
from typing import Any

logger: Incomplete

class COCOExporter(Exporter):
    """Exporter for the COCO format.

    Tables which are originally instances of the TableFromCoco class will be compatible with this exporter.
    """
    supported_format: str
    priority: int
    @classmethod
    def can_export(self, table: Table, output_url: Url) -> bool: ...
    @classmethod
    def serialize(cls, table: Table, output_url: Url, weight_threshold: float = 0.0, image_folder: Url | str = '', absolute_image_paths: bool = False, include_segmentation: bool | None = None, indent: int = 4, **kwargs: Any) -> str:
        """Serialize a table to the COCO format.

        Default behavior is to write a COCO file with image paths relative to the (output) annotations file. Written
        paths can be further configured with the `absolute_image_paths` and `image_folder` argument.

        Note that for a coco file to be valid, the image paths should be absolute or relative w.r.t. the annotations
        file itself.

        :param table: The table to serialize
        :param output_url: The output URL
        :param weight_threshold: The weight threshold
        :param image_folder: A path with which image filenames are relativized.
        :param absolute_image_paths: Whether to use absolute image paths. If this is set to True, the image_folder
            cannot be set.
        :param include_segmentation: Whether to include segmentation information. Currently only supports bounding box
            segmentation. By default it will take information from the table, but this can be overridden by setting a
            boolean
        :param indent: The number of spaces to use for indentation
        :param kwargs: Any additional arguments
        :return: The serialized table
        """
