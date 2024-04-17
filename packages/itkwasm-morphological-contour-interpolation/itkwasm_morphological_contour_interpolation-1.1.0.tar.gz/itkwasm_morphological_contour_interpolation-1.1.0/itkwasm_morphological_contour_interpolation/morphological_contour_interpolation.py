# Generated file. Do not edit.

import os
from typing import Dict, Tuple, Optional, List, Any

from itkwasm import (
    environment_dispatch,
    Image,
)

def morphological_contour_interpolation(
    input_image: Image,
    label: int = 0,
    axis: int = -1,
    no_heuristic_alignment: bool = False,
    no_use_distance_transform: bool = False,
    use_custom_slice_positions: bool = False,
    no_use_extrapolation: bool = False,
    use_ball_structuring_element: bool = False,
    labeled_slice_indices_axis: int = -1,
    labeled_slice_indices_label: int = 1,
    labeled_slice_indices: Optional[List[int]] = None,
) -> Image:
    """Interpolates contours between slices.

    :param input_image: The input image
    :type  input_image: Image

    :param label: The label to interpolate. Interpolates all labels if set to 0 (default).
    :type  label: int

    :param axis: Interpolate only along this axis. Interpolates along all axes if set to -1 (default).
    :type  axis: int

    :param no_heuristic_alignment: Heuristic alignment of regions for interpolation is faster than optimal alignment.
    :type  no_heuristic_alignment: bool

    :param no_use_distance_transform: Using distance transform instead of repeated dilations to calculate the median contour is slightly faster, but produces lower quality interpolations.
    :type  no_use_distance_transform: bool

    :param use_custom_slice_positions: Use custom slice positions (not slice auto-detection).
    :type  use_custom_slice_positions: bool

    :param no_use_extrapolation: Perform extrapolation for branch extremities. Branch extremities are defined as regions having no overlap with any region in the next slice. Extrapolation helps generate smooth surface closings.
    :type  no_use_extrapolation: bool

    :param use_ball_structuring_element: Use ball instead of default cross structuring element for repeated dilations.
    :type  use_ball_structuring_element: bool

    :param labeled_slice_indices_axis: Axis along which the labeled slice indices are defined. Default is -1 (that is, auto-detection).
    :type  labeled_slice_indices_axis: int

    :param labeled_slice_indices_label: Label of the slice indices. Default is 1.
    :type  labeled_slice_indices_label: int

    :param labeled_slice_indices: List of labeled slice indices. Default is empty.
    :type  labeled_slice_indices: int

    :return: The output image
    :rtype:  Image
    """
    func = environment_dispatch("itkwasm_morphological_contour_interpolation", "morphological_contour_interpolation")
    output = func(input_image, label=label, axis=axis, no_heuristic_alignment=no_heuristic_alignment, no_use_distance_transform=no_use_distance_transform, use_custom_slice_positions=use_custom_slice_positions, no_use_extrapolation=no_use_extrapolation, use_ball_structuring_element=use_ball_structuring_element, labeled_slice_indices_axis=labeled_slice_indices_axis, labeled_slice_indices_label=labeled_slice_indices_label, labeled_slice_indices=labeled_slice_indices)
    return output
