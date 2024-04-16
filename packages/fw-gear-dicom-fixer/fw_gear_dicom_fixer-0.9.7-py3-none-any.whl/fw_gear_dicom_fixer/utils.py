"""Utility module for helpful functions"""

import logging
import zipfile

from fw_file.dicom import DICOMCollection
from fw_file.dicom.utils import sniff_dcm

from .fixers import is_dcm

log = logging.getLogger(__name__)


def calculate_decompressed_size(dicom_path: str) -> int:
    """Estimate size of decompressed file, to assist in calculating
    whether the container has enough memory available to successfully
    decompress without running afoul of the OOM killer.

    Args:
        dicom_path: Path to directory containing dicom files

    Returns:
        int: Estimated size of decompressed file in bytes
    """
    if sniff_dcm(dicom_path):
        dcms = DICOMCollection(dicom_path, filter_fn=is_dcm, force=True)
    elif zipfile.is_zipfile(str(dicom_path)):
        dcms = DICOMCollection.from_zip(dicom_path, filter_fn=is_dcm, force=True)
    else:
        raise RuntimeError(
            "Invalid file type passed in, not a DICOM nor a Zip Archive."
        )

    if len(dcms) > 1:
        frames = len(dcms)
    elif len(dcms) == 1:
        frames = dcms.get("NumberOfFrames")
        if not frames:
            try:
                frames = len(dcms.get("PerFrameFunctionalGroupsSequence"))
            except TypeError:
                frames = 1
    else:  # len(dcms) == 0:
        # No valid dicoms is handled later on in dicom-fixer,
        # so for now, we're logging and moving on.
        log.warning(
            "Unable to estimate size of decompressed file; no valid dicoms found."
        )
        return 0

    rows = dcms.bulk_get("Rows")
    cols = dcms.bulk_get("Columns")
    samples = dcms.bulk_get("SamplesPerPixel")
    allocated = dcms.bulk_get("BitsAllocated")

    try:
        max_rows = float(max([i for i in rows if i is not None]))
        max_cols = float(max([i for i in cols if i is not None]))
        max_samples = float(max([i for i in samples if i is not None]))
        max_allocated = float(max([i for i in allocated if i is not None]))

    except ValueError:
        # If above max + list comprehension raises a ValueError, then
        # all values in one or more utilized tags is None
        log.warning(
            "Unable to estimate size of decompressed file due to missing tags. Continuing."
        )
        return 0

    total_bytes = (
        max_rows
        * max_cols
        * frames
        * max_samples
        * max_allocated
        / 8  # convert from bits to bytes
    )
    return total_bytes
