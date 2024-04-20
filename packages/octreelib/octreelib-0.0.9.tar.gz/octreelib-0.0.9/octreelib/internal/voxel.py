import itertools
from typing import Optional

import numpy as np

from octreelib.internal.interfaces import WithID
from octreelib.internal.point import Point, PointCloud

__all__ = ["Voxel", "VoxelBase"]


class VoxelBase(WithID):
    """
    Represents a Voxel with ID
    :param corner_min: corner point with all minimal coordinates
    :param edge_length: edge_length of the voxel
    """

    _static_voxel_id_map = {}

    def __init__(
        self,
        corner_min: Point,
        edge_length: float,
    ):
        self._corner_min = corner_min
        self._edge_length = edge_length

        if self not in self._static_voxel_id_map:
            self._static_voxel_id_map[self] = len(self._static_voxel_id_map)

        WithID.__init__(self, self._static_voxel_id_map[self])

    def __hash__(self):
        return hash((tuple(self._corner_min), self._edge_length))

    def __eq__(self, other: "VoxelBase"):
        return (
            all(self.corner_min == other.corner_min)
            and self.edge_length == other.edge_length
        )

    @property
    def corner_min(self):
        return self._corner_min

    @property
    def edge_length(self):
        return self._edge_length

    @property
    def corner_max(self):
        return self.corner_min + self.edge_length

    @property
    def all_corners(self):
        """
        :return: 8 points, which represent the corners of the voxel
        """
        return [
            self._corner_min + offset
            for offset in itertools.product([0, self._edge_length], repeat=3)
        ]


class Voxel(VoxelBase):
    """
    Voxel with a mutable point cloud.
    :param corner_min: corner point with all minimal coordinates
    :param edge_length: edge_length of the voxel
    """

    def __init__(
        self,
        corner_min: Point,
        edge_length: float,
        points: Optional[PointCloud] = None,
    ):
        super().__init__(corner_min, edge_length)

        self._points: PointCloud = (
            points if points is not None else np.empty((0, 3), dtype=float)
        )

    def get_points(self) -> PointCloud:
        """
        :return: Points, which are stored inside the voxel.
        """
        return self._points.copy()

    def insert_points(self, points: PointCloud):
        """
        :param points: Points to insert
        """
        self._points = np.vstack([self._points, points])
