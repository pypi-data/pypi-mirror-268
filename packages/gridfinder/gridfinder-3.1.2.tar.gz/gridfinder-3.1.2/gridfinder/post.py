from __future__ import annotations

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio as rs
import shapely.wkt
from affine import Affine
from rasterio.features import rasterize
from rasterio.transform import xy
from shapely.geometry import LineString, Point
from skimage.morphology import skeletonize

from gridfinder.util import Pathy


def threshold(dists_in: Pathy, cutoff: float = 0.0) -> tuple[np.ndarray, Affine]:
    """Convert distance array into binary array of connected locations.

    Parameters
    ----------
    dists_in : 2D array output from gridfinder algorithm.
    cutoff : Cutoff value below which consider the cells to be grid.

    Returns
    -------
    guess : Binary representation of input array.
    affine: Affine transformation for raster.
    """
    with rs.open(dists_in) as ds:
        dists_r = ds.read(1)
        affine = ds.transform

    guess = threshold_arr(dists_r, cutoff)

    return guess, affine


def threshold_arr(dists: np.ndarray, cutoff: float = 0.0) -> np.ndarray:
    guess = dists.copy()
    guess[dists > cutoff] = 0
    guess[dists <= cutoff] = 1
    return guess


def thin(guess_in: Pathy) -> tuple[np.ndarray, Affine]:
    """
    Use scikit-image skeletonize to 'thin' the guess raster.

    Parameters
    ----------
    guess_in : Output from threshold().

    Returns
    -------
    guess_skel : Thinned version.
    affine : affine
    """
    with rs.open(guess_in) as ds:
        guess_arr = ds.read(1)
        affine = ds.transform
    guess_skel = thin_arr(guess_arr)
    return guess_skel, affine


def thin_arr(guess: np.ndarray) -> np.ndarray:
    guess_skel = skeletonize(guess)
    guess_skel = guess_skel.astype("int32")
    return guess_skel


def raster_to_lines(guess_skel_in: Pathy) -> gpd.GeoDataFrame:
    """
    Convert thinned raster to linestring geometry.

    Parameters
    ----------
    guess_skel_in : Output from thin().

    Returns
    -------
    guess_gdf : Converted to geometry.
    """

    with rs.open(guess_skel_in) as ds:
        arr = ds.read(1)
        rast_crs = ds.crs
        affine = ds.transform

    max_row = arr.shape[0]
    max_col = arr.shape[1]
    lines = []

    for row in range(0, max_row):
        for col in range(0, max_col):
            loc = (row, col)
            if arr[loc] == 1:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        next_row = row + i
                        next_col = col + j
                        next_loc = (next_row, next_col)

                        # ensure we're within bounds
                        # ensure we're not looking at the same spot
                        if (
                            next_row < 0
                            or next_col < 0
                            or next_row >= max_row
                            or next_col >= max_col
                            or next_loc == loc
                        ):
                            continue

                        if arr[next_loc] == 1:
                            line = (loc, next_loc)
                            rev = (line[1], line[0])
                            if line not in lines and rev not in lines:
                                lines.append(line)

    real_lines = []
    for line in lines:
        real = (xy(affine, line[0][0], line[0][1]), xy(affine, line[1][0], line[1][1]))
        real_lines.append(real)

    shapes = []
    for line in real_lines:
        shapes.append(LineString([Point(line[0]), Point(line[1])]).wkt)

    guess_gdf = pd.DataFrame(shapes)
    geometry = guess_gdf[0].map(shapely.wkt.loads)
    guess_gdf = guess_gdf.drop(0, axis=1)
    guess_gdf = gpd.GeoDataFrame(guess_gdf, crs=rast_crs, geometry=geometry)

    guess_gdf["same"] = 0
    guess_gdf = guess_gdf.dissolve(by="same")
    guess_gdf = guess_gdf.to_crs(epsg=4326)

    return guess_gdf


def accuracy(
    grid_in: Pathy,
    guess_in: Pathy,
    aoi_in: Pathy,
    buffer_amount: float = 0.01,
) -> tuple[float, float]:
    """Measure accuracy against a specified grid 'truth' file.

    Parameters
    ----------
    grid_in : Path to vector truth file.
    guess_in : Path to guess output from guess2geom.
    aoi_in : Path to AOI feature.
    buffer_amount : Leeway in decimal degrees in calculating equivalence.
        0.01 DD equals approximately 1 mile at the equator.
    """

    if isinstance(aoi_in, gpd.GeoDataFrame):
        aoi = aoi_in
    else:
        aoi = gpd.read_file(aoi_in)

    grid = gpd.read_file(grid_in, mask=aoi)
    grid_buff = grid.buffer(buffer_amount)

    with rs.open(guess_in) as ds:
        guesses = ds.read(1)
        out_shape = ds.shape
        affine = ds.transform

    grid_for_raster = [(row.geometry) for _, row in grid.iterrows()]
    grid_raster = rasterize(
        grid_for_raster,
        out_shape=out_shape,
        fill=1,
        default_value=0,
        all_touched=True,
        transform=affine,
    )
    grid_buff_raster = rasterize(
        grid_buff,
        out_shape=out_shape,
        fill=1,
        default_value=0,
        all_touched=True,
        transform=affine,
    )

    grid_raster = flip_arr_values(grid_raster)
    grid_buff_raster = flip_arr_values(grid_buff_raster)

    tp = true_positives(guesses, grid_buff_raster)
    fn = false_negatives(guesses, grid_raster)

    return tp, fn


def true_positives(guesses: np.ndarray, truths: np.ndarray) -> float:
    """Calculate true positives, used by accuracy().

    Parameters
    ----------
    guesses : Output from model.
    truths : Truth feature converted to array.

    Returns
    -------
    tp : Ratio of true positives.
    """

    yes_guesses = 0
    yes_guesses_correct = 0
    rows = guesses.shape[0]
    cols = guesses.shape[1]

    for x in range(0, rows):
        for y in range(0, cols):
            guess = guesses[x, y]
            truth = truths[x, y]
            if guess == 1:
                yes_guesses += 1
                if guess == truth:
                    yes_guesses_correct += 1

    tp = yes_guesses_correct / yes_guesses

    return tp


def false_negatives(guesses: np.ndarray, truths: np.ndarray) -> float:
    """Calculate false negatives, used by accuracy().

    Parameters
    ----------
    guesses : Output from model.
    truths : Truth feature converted to array.

    Returns
    -------
    fn : Ratio of false negatives.
    """

    actual_grid = 0
    actual_grid_missed = 0

    rows = guesses.shape[0]
    cols = guesses.shape[1]

    for x in range(0, rows):
        for y in range(0, cols):
            guess = guesses[x, y]
            truth = truths[x, y]

            if truth == 1:
                actual_grid += 1
                if guess != truth:
                    found = False
                    for i in range(-5, 6):
                        for j in range(-5, 6):
                            if i == 0 and j == 0:
                                continue

                            shift_x = x + i
                            shift_y = y + j
                            if shift_x < 0 or shift_y < 0:
                                continue
                            if shift_x >= rows or shift_y >= cols:
                                continue

                            other_guess = guesses[shift_x, shift_y]
                            if other_guess == 1:
                                found = True
                    if not found:
                        actual_grid_missed += 1

    fn = actual_grid_missed / actual_grid

    return fn


def flip_arr_values(arr: np.ndarray) -> np.ndarray:
    """Simple helper function used by accuracy()"""

    arr[arr == 1] = 2
    arr[arr == 0] = 1
    arr[arr == 2] = 0
    return arr
