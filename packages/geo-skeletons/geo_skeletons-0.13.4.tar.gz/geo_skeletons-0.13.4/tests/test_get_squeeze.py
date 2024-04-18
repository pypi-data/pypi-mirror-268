from geo_skeletons import GriddedSkeleton, PointSkeleton
from geo_skeletons.decorators import add_datavar, add_coord
from geo_skeletons.errors import DataWrongDimensionError
import dask.array as da
import numpy as np
import pytest


def test_squeeze_trivial_spatial():
    @add_datavar(name="dummy", default_value=-9)
    @add_coord(name="z")
    class DummySkeleton(PointSkeleton):
        pass

    points = DummySkeleton(x=0, y=0, z=[1, 2, 3])
    points.set_dummy(0)

    assert points.dummy(squeeze=False).shape == (1, 3)
    assert points.dummy(squeeze=True).shape == (3,)
    assert points.dummy().shape == (3,)
    assert points.get("dummy", squeeze=False).shape == (1, 3)
    assert points.get("dummy", squeeze=True).shape == (3,)
    assert points.get("dummy").shape == (3,)


def test_squeeze_trivial_gridded():
    @add_datavar(name="dummy", default_value=-9)
    @add_coord(name="z")
    class DummySkeleton(GriddedSkeleton):
        pass

    points = DummySkeleton(x=0, y=0, z=[1, 2, 3])
    points.set_dummy(0)

    assert points.dummy(squeeze=False).shape == (1, 1, 3)
    assert points.dummy(squeeze=True).shape == (3,)


def test_squeeze_save_spatial():
    @add_datavar(name="dummy", default_value=-9)
    @add_coord(name="z")
    class DummySkeleton(PointSkeleton):
        pass

    points = DummySkeleton(x=0, y=0, z=1)
    points.set_dummy(0)

    assert points.dummy(squeeze=False).shape == (1, 1)
    assert points.dummy(squeeze=True).shape == (1,)


def test_squeeze_save_spatial_gridded():
    @add_datavar(name="dummy", default_value=-9)
    @add_coord(name="z")
    class DummySkeleton(GriddedSkeleton):
        pass

    points = DummySkeleton(x=0, y=0, z=1)
    points.set_dummy(0)

    assert points.dummy(squeeze=False).shape == (1, 1, 1)
    assert points.dummy(squeeze=True).shape == (1, 1)
