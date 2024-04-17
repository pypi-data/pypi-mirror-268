"""Copy valid pixels from input files to an output file."""

from contextlib import ExitStack, contextmanager
import logging
import os
import math
import cmath
import warnings
import numbers

import numpy as np

import rasterio
from rasterio.coords import disjoint_bounds
from rasterio.enums import Resampling
from rasterio.errors import RasterioDeprecationWarning, RasterioError
from rasterio.io import DatasetWriter
from rasterio import windows
from rasterio.transform import Affine
from rasterio.windows import window_split

logger = logging.getLogger(__name__)


def copy_first(merged_data, new_data, merged_mask, new_mask, **kwargs):
    """Returns the first available pixel."""
    mask = np.empty_like(merged_mask, dtype="bool")
    np.logical_not(new_mask, out=mask)
    np.logical_and(merged_mask, mask, out=mask)
    np.copyto(merged_data, new_data, where=mask, casting="unsafe")


def copy_last(merged_data, new_data, merged_mask, new_mask, **kwargs):
    """Returns the last available pixel."""
    mask = np.empty_like(merged_mask, dtype="bool")
    np.logical_not(new_mask, out=mask)
    np.copyto(merged_data, new_data, where=mask, casting="unsafe")


def copy_min(merged_data, new_data, merged_mask, new_mask, **kwargs):
    """Returns the minimum value pixel."""
    mask = np.empty_like(merged_mask, dtype="bool")
    np.logical_or(merged_mask, new_mask, out=mask)
    np.logical_not(mask, out=mask)
    np.minimum(merged_data, new_data, out=merged_data, where=mask, casting="unsafe")
    np.logical_not(new_mask, out=mask)
    np.logical_and(merged_mask, mask, out=mask)
    np.copyto(merged_data, new_data, where=mask, casting="unsafe")


def copy_max(merged_data, new_data, merged_mask, new_mask, **kwargs):
    """Returns the maximum value pixel."""
    mask = np.empty_like(merged_mask, dtype="bool")
    np.logical_or(merged_mask, new_mask, out=mask)
    np.logical_not(mask, out=mask)
    np.maximum(merged_data, new_data, out=merged_data, where=mask, casting="unsafe")
    np.logical_not(new_mask, out=mask)
    np.logical_and(merged_mask, mask, out=mask)
    np.copyto(merged_data, new_data, where=mask, casting="unsafe")


def copy_sum(merged_data, new_data, merged_mask, new_mask, **kwargs):
    """Returns the sum of all pixel values."""
    mask = np.empty_like(merged_mask, dtype="bool")
    np.logical_or(merged_mask, new_mask, out=mask)
    np.logical_not(mask, out=mask)
    np.add(merged_data, new_data, out=merged_data, where=mask, casting="unsafe")
    np.logical_not(new_mask, out=mask)
    np.logical_and(merged_mask, mask, out=mask)
    np.copyto(merged_data, new_data, where=mask, casting="unsafe")


def copy_count(merged_data, new_data, merged_mask, new_mask, **kwargs):
    """Returns the count of valid pixels."""
    mask = np.empty_like(merged_mask, dtype="bool")
    np.logical_or(merged_mask, new_mask, out=mask)
    np.logical_not(mask, out=mask)
    np.add(merged_data, mask, out=merged_data, where=mask, casting="unsafe")
    np.logical_not(new_mask, out=mask)
    np.logical_and(merged_mask, mask, out=mask)
    np.copyto(merged_data, mask, where=mask, casting="unsafe")


MERGE_METHODS = {
    "first": copy_first,
    "last": copy_last,
    "min": copy_min,
    "max": copy_max,
    "sum": copy_sum,
    "count": copy_count,
}


def merge(
    sources,
    bounds=None,
    res=None,
    nodata=None,
    dtype=None,
    precision=None,
    indexes=None,
    output_count=None,
    resampling=Resampling.nearest,
    method="first",
    target_aligned_pixels=False,
    mem_limit=64,
    dst_path=None,
    dst_kwds=None,
):
    """Copy valid pixels from input files to an output file.

    All files must have the same number of bands, data type, and
    coordinate reference system.

    Input files are merged in their listed order using the reverse
    painter's algorithm (default) or another method. If the output file exists,
    its values will be overwritten by input values.

    Geospatial bounds and resolution of a new output file in the
    units of the input file coordinate reference system may be provided
    and are otherwise taken from the first input file.

    Parameters
    ----------
    sources : list of dataset objects opened in 'r' mode, filenames or PathLike objects
        source sources to be merged.
    bounds: tuple, optional
        Bounds of the output image (left, bottom, right, top).
        If not set, bounds are determined from bounds of input rasters.
    res: tuple, optional
        Output resolution in units of coordinate reference system. If not set,
        the resolution of the first raster is used. If a single value is passed,
        output pixels will be square.
    nodata: float, optional
        nodata value to use in output file. If not set, uses the nodata value
        in the first input raster.
    dtype: numpy.dtype or string
        dtype to use in outputfile. If not set, uses the dtype value in the
        first input raster.
    precision: int, optional
        This parameters is unused, deprecated in rasterio 1.3.0, and
        will be removed in version 2.0.0.
    indexes : list of ints or a single int, optional
        bands to read and merge
    output_count: int, optional
        If using callable it may be useful to have additional bands in the output
        in addition to the indexes specified for read
    resampling : Resampling, optional
        Resampling algorithm used when reading input files.
        Default: `Resampling.nearest`.
    method : str or callable
        pre-defined method:
            first: reverse painting
            last: paint valid new on top of existing
            min: pixel-wise min of existing and new
            max: pixel-wise max of existing and new
        or custom callable with signature:
            merged_data : array_like
                array to update with new_data
            new_data : array_like
                data to merge
                same shape as merged_data
            merged_mask, new_mask : array_like
                boolean masks where merged/new data pixels are invalid
                same shape as merged_data
            index: int
                index of the current dataset within the merged dataset collection
            roff: int
                row offset in base array
            coff: int
                column offset in base array

    target_aligned_pixels : bool, optional
        Whether to adjust output image bounds so that pixel coordinates
        are integer multiples of pixel size, matching the ``-tap``
        options of GDAL utilities.  Default: False.
    mem_limit : int, optional
        Process merge output in chunks of mem_limit MB in size.
    dst_path : str or PathLike, optional
        Path of output dataset
    dst_kwds : dict, optional
        Dictionary of creation options and other paramters that will be
        overlaid on the profile of the output dataset.

    Returns
    -------
    tuple
        Two elements:
            dest: numpy.ndarray
                Contents of all input rasters in single array
            out_transform: affine.Affine()
                Information for mapping pixel coordinates in `dest` to another
                coordinate system
    """
    if precision is not None:
        warnings.warn(
            "The precision parameter is unused, deprecated, and will be removed in 2.0.0.",
            RasterioDeprecationWarning,
        )

    if method in MERGE_METHODS:
        copyto = MERGE_METHODS[method]
    elif callable(method):
        copyto = method
    else:
        raise ValueError('Unknown method {0}, must be one of {1} or callable'
                         .format(method, list(MERGE_METHODS.keys())))

    # Create a dataset_opener object to use in several places in this function.
    if isinstance(sources[0], (str, os.PathLike)):
        dataset_opener = rasterio.open
    else:

        @contextmanager
        def nullcontext(obj):
            try:
                yield obj
            finally:
                pass

        dataset_opener = nullcontext

    dst = None

    with ExitStack() as exit_stack:
        with dataset_opener(sources[0]) as first:
            first_profile = first.profile
            first_crs = first.crs
            first_res = first.res
            nodataval = first.nodatavals[0]
            dt = first.dtypes[0]

            if indexes is None:
                src_count = first.count
            elif isinstance(indexes, int):
                src_count = indexes
            else:
                src_count = len(indexes)

            try:
                first_colormap = first.colormap(1)
            except ValueError:
                first_colormap = None

        if not output_count:
            output_count = src_count

        # Extent from option or extent of all inputs
        if bounds:
            dst_w, dst_s, dst_e, dst_n = bounds
        else:
            # scan input files
            xs = []
            ys = []
            for dataset in sources:
                with dataset_opener(dataset) as src:
                    left, bottom, right, top = src.bounds
                xs.extend([left, right])
                ys.extend([bottom, top])
            dst_w, dst_s, dst_e, dst_n = min(xs), min(ys), max(xs), max(ys)

        # Resolution/pixel size
        if not res:
            res = first_res
        elif isinstance(res, numbers.Number):
            res = (res, res)
        elif len(res) == 1:
            res = (res[0], res[0])

        if target_aligned_pixels:
            dst_w = math.floor(dst_w / res[0]) * res[0]
            dst_e = math.ceil(dst_e / res[0]) * res[0]
            dst_s = math.floor(dst_s / res[1]) * res[1]
            dst_n = math.ceil(dst_n / res[1]) * res[1]

        # Compute output array shape. We guarantee it will cover the output
        # bounds completely
        output_width = int(round((dst_e - dst_w) / res[0]))
        output_height = int(round((dst_n - dst_s) / res[1]))

        output_transform = Affine.translation(dst_w, dst_n) * Affine.scale(
            res[0], -res[1]
        )

        if dtype is not None:
            dt = dtype
            logger.debug("Set dtype: %s", dt)

        if nodata is not None:
            nodataval = nodata
            logger.debug("Set nodataval: %r", nodataval)

        inrange = False
        if nodataval is not None:
            # Only fill if the nodataval is within dtype's range
            if np.issubdtype(dt, np.integer):
                info = np.iinfo(dt)
                inrange = info.min <= nodataval <= info.max
            else:
                if cmath.isfinite(nodataval):
                    info = np.finfo(dt)
                    inrange = info.min <= nodataval <= info.max
                    inrange = inrange
                else:
                    inrange = True

            if not inrange:
                warnings.warn(
                    "The nodata value, %s, cannot safely be represented "
                    "in the chosen data type, %s. Consider overriding it "
                    "using the --nodata option for better results." % (nodataval, dt)
                )
        else:
            logger.debug("Set nodataval to 0")
            nodataval = 0

        # When dataset output is selected, we might need to create one
        # and will also provide the option of merging by chunks.
        if dst_path is not None:
            if isinstance(dst_path, DatasetWriter):
                dst = dst_path
            else:
                out_profile = first_profile
                out_profile.update(**(dst_kwds or {}))
                out_profile["transform"] = output_transform
                out_profile["height"] = output_height
                out_profile["width"] = output_width
                out_profile["count"] = output_count
                out_profile["dtype"] = dt
                if nodata is not None:
                    out_profile["nodata"] = nodata
                dst = rasterio.open(dst_path, "w", **out_profile)
                exit_stack.enter_context(dst)

            max_pixels = mem_limit * 1.0e6 / np.dtype(dt).itemsize * output_count

            if output_width * output_height < max_pixels:
                chunks = [((0, 0), windows.Window(0, 0, output_width, output_height))]
            else:
                chunks = window_split(
                    output_height, output_width, max_pixels=max_pixels
                )
        else:
            chunks = [((0, 0), windows.Window(0, 0, output_width, output_height))]

        logger.debug("Chunks=%r", chunks)

        for _, chunk in chunks:
            dst_w, dst_s, dst_e, dst_n = windows.bounds(chunk, output_transform)
            dest = np.zeros((output_count, chunk.height, chunk.width), dtype=dt)
            if inrange:
                dest.fill(nodataval)

            for idx, dataset in enumerate(sources):
                with dataset_opener(dataset) as src:
                    # 0. Precondition checks
                    #    - Check that source is within destination bounds
                    #    - Check that CRS is same

                    if disjoint_bounds((dst_w, dst_s, dst_e, dst_n), src.bounds):
                        logger.debug(
                            "Skipping source: src=%r, bounds=%r",
                            src,
                            (dst_w, dst_s, dst_e, dst_n),
                        )
                        continue

                    if first_crs != src.crs:
                        raise RasterioError(f"CRS mismatch with source: {dataset}")

                    # 1. Compute the source window
                    src_window = windows.from_bounds(
                        dst_w, dst_s, dst_e, dst_n, src.transform
                    ).round(3)

                    temp_shape = (src_count, chunk.height, chunk.width)

                    temp_src = src.read(
                        out_shape=temp_shape,
                        window=src_window,
                        boundless=True,
                        masked=True,
                        indexes=indexes,
                        resampling=resampling,
                    )

                region = dest[:, :, :]

                if cmath.isnan(nodataval):
                    region_mask = np.isnan(region)
                elif not np.issubdtype(region.dtype, np.integer):
                    region_mask = np.isclose(region, nodataval)
                else:
                    region_mask = region == nodataval

                # Ensure common shape, resolving issue #2202.
                temp = temp_src[:, : region.shape[1], : region.shape[2]]
                temp_mask = np.ma.getmask(temp)
                copyto(
                    region,
                    temp,
                    region_mask,
                    temp_mask,
                    index=idx,
                    roff=0,
                    coff=0,
                )

            if dst:
                dst_window = windows.from_bounds(
                    dst_w, dst_s, dst_e, dst_n, output_transform
                ).round(3)
                dst.write(dest, window=dst_window)

        if dst is None:
            return dest, output_transform
        else:
            if first_colormap:
                dst.write_colormap(1, first_colormap)
            dst.close()
