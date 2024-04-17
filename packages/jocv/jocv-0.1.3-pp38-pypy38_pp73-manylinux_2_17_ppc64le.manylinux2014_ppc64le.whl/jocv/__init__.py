from . import jocv
from pathlib import Path, Path
import numpy as np

Point3D = jocv.Point3D
Camera = jocv.Camera
Image = jocv.Image


def read_images_bin(path: str | Path) -> dict:
    """
    Read images from a binary file.

    Args:
        path (str | Path): The path to the binary file.

    Returns:
        dict: A dictionary containing the images read from the file.
    """
    return jocv.read_images_bin(str(path))

def read_points3D_bin(path: str | Path) -> dict:
    """
    Read 3D points from a binary file.

    Args:
        path (str or Path): The path to the binary file.

    Returns:
        dict: A dictionary containing the 3D points.

    """
    return jocv.read_points3D_bin(str(path))

def read_cameras_bin(path: str | Path) -> dict:
    """
    Reads camera data from a binary file.

    Args:
        path (str or Path): The path to the binary file.

    Returns:
        dict: A dictionary containing the camera data.

    """
    return jocv.read_cameras_bin(str(path))

def compute_overlaps(points3D: dict[int, dict[int, Point3D]]) -> dict:
    """
    Compute the overlaps between 3D points.

    Args:
        points3D (dict): A dictionary containing 3D points.

    Returns:
        dict: A dictionary containing the computed overlaps.

    """
    return jocv.compute_overlaps(points3D)