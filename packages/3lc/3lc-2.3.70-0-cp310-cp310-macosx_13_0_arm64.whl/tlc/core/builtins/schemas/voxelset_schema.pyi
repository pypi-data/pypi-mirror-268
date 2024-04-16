from tlc.core.builtins.constants.number_roles import NUMBER_ROLE_VOXEL_COUNT as NUMBER_ROLE_VOXEL_COUNT
from tlc.core.schema import DimensionNumericValue as DimensionNumericValue, Float32Value as Float32Value, Int32Value as Int32Value, Schema as Schema

def voxelset_schema() -> Schema:
    """
    Returns a standard schema describing a 3D voxel set
    """
