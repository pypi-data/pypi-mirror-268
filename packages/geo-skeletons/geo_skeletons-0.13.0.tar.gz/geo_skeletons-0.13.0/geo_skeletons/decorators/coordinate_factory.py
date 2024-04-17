from functools import partial
import pandas as pd
import numpy as np
from copy import deepcopy
from geo_parameters.metaparameter import MetaParameter
from geo_parameters.wave import Freq, DirsTo, DirsFrom
from typing import Union


def coord_decorator(name, grid_coord, c, stash_get=False):
    """stash_get = True means that the coordinate data can be accessed
    by method ._{name}() instead of .{name}()

    This allows for alternative definitions of the get-method elsewere."""

    def set_spacing(self, nx: int = None, dx: float = None):
        """Sets spacing for added variable"""
        z = self.get(name_str)

        if dx is not None:
            nx = int((max(z) - min(z)) / dx + 1)

        kwargs = {name_str: np.linspace(min(z), max(z), nx)}
        self._init_structure(
            self.x(strict=True),
            self.y(strict=True),
            self.lon(strict=True),
            self.lat(strict=True),
            **kwargs,
        )

    def get_coord(self, data_array=False, **kwargs):
        if not self._structure_initialized():
            return None
        data = self._ds_manager.get(name_str, **kwargs)
        if data_array:
            return data
        return data.values.copy()

    if c._coord_manager.initial_state:
        c._coord_manager = deepcopy(c._coord_manager)
        c._coord_manager.initial_state = False

    name_str = c._coord_manager.add_coord(name, grid_coord)
    if stash_get:
        exec(f"c._{name_str} = get_coord")
    else:
        exec(f"c.{name_str} = get_coord")

    exec(f"c.set_{name_str}_spacing = set_spacing")
    return c


def add_coord(name: Union[str, MetaParameter] = "dummy", grid_coord: bool = False):
    """Add a generic coordinate with no customized methods."""
    return partial(coord_decorator, name, grid_coord)


def add_time(grid_coord: bool = False):
    def wrapper(c):
        def unique_times(times, strf: str):
            return np.unique(np.array(pd.to_datetime(times).strftime(strf).to_list()))

        def hours(self, datetime=True, fmt: str = "%Y-%m-%d %H:00"):
            """Determins a Pandas data range of all the days in the time span."""
            if not self._structure_initialized():
                return None
            times = self._ds_manager.get(name).values.copy()
            if datetime:
                return pd.to_datetime(unique_times(times, "%Y-%m-%d %H"))
            else:
                return list(unique_times(times, fmt))

        def days(self, datetime=True, fmt: str = "%Y-%m-%d"):
            """Determins a Pandas data range of all the days in the time span."""
            if not self._structure_initialized():
                return None
            times = self._ds_manager.get(name).values.copy()
            if datetime:
                return pd.to_datetime(unique_times(times, "%Y-%m-%d"))
            else:
                return list(unique_times(times, fmt))

        def months(self, datetime=True, fmt: str = "%Y-%m"):
            """Determins a Pandas data range of all the months in the time span."""
            if not self._structure_initialized():
                return None
            times = self._ds_manager.get(name).values.copy()
            if datetime:
                return pd.to_datetime(unique_times(times, "%Y-%m"))
            else:
                return list(unique_times(times, fmt))

        def years(self, datetime=True, fmt: str = "%Y"):
            """Determins a Pandas data range of all the months in the time span."""
            if not self._structure_initialized():
                return None
            times = self._ds_manager.get(name).values.copy()
            if datetime:
                return pd.to_datetime(unique_times(times, "%Y"))
            else:
                return list(unique_times(times, fmt))

        def get_time(
            self,
            data_array=False,
            datetime: bool = True,
            fmt="%Y-%m-%d %H:%M:00",
            **kwargs,
        ):
            if not self._structure_initialized():
                return (None, None)
            data = self._ds_manager.get(name, **kwargs)
            if data_array:
                return data

            # if len(data.values) > 1:
            times = pd.to_datetime(data.values.copy())
            # else:
            #     times = pd.to_datetime([data.values[0].copy(), data.values[0].copy()])

            if not datetime:
                times = times.strftime(fmt).to_list()

            return times

        name = "time"
        if c._coord_manager.initial_state:
            c._coord_manager = deepcopy(c._coord_manager)
            c._coord_manager.initial_state = False

        _ = c._coord_manager.add_coord(name, grid_coord)
        c.time = get_time

        c.hours = hours
        c.days = days
        c.months = months
        c.years = years
        return c

    return wrapper


def add_frequency(name: Union[str, MetaParameter] = Freq, grid_coord: bool = False):
    def wrapper(c):
        def get_freq(self, angular=False):
            if not self._structure_initialized():
                return None
            freq = self._ds_manager.get(name_str).values.copy()
            if angular:
                freq = 2 * np.pi * freq
            return freq

        def df(self, angular=False):
            if not self._structure_initialized():
                return None
            freq = get_freq(self, angular=angular).copy()
            return (freq[-1] - freq[0]) / (len(freq) - 1)

        if c._coord_manager.initial_state:
            c._coord_manager = deepcopy(c._coord_manager)
            c._coord_manager.initial_state = False

        name_str = c._coord_manager.add_coord(name, grid_coord)
        exec(f"c.{name_str} = get_freq")
        c.df = df

        return c

    return wrapper


def add_direction(
    name: Union[str, MetaParameter] = None,
    grid_coord: bool = False,
    direction_from: bool = True,
):
    def wrapper(c):
        def get_dirs(self, angular=False):
            if not self._structure_initialized():
                return None
            dirs = self._ds_manager.get(name_str).data.copy()
            if angular:
                dirs = dirs * np.pi / 180
            return dirs

        def ddir(self, angular=False):
            if not self._structure_initialized():
                return None
            dirs = get_dirs(self, angular=False).copy()
            dmax = 2 * np.pi if angular else 360
            return dmax / len(dirs)

        if c._coord_manager.initial_state:
            c._coord_manager = deepcopy(c._coord_manager)
            c._coord_manager.initial_state = False

        name_str = c._coord_manager.add_coord(name, grid_coord)
        exec(f"c.{name_str} = get_dirs")
        c.dd = ddir
        return c

    if name is None:
        name = DirsFrom if direction_from else DirsTo
    return wrapper
