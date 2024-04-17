# Generated file. To retain edits, remove this comment.

from pathlib import Path
import os
from typing import Dict, Tuple, Optional, List, Any

from .js_package import js_package

from itkwasm.pyodide import (
    to_js,
    to_py,
    js_resources
)
from itkwasm import (
    InterfaceTypes,
    Image,
)

async def morphological_contour_interpolation_async(
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
    js_module = await js_package.js_module
    web_worker = js_resources.web_worker

    kwargs = {}
    if label:
        kwargs["label"] = to_js(label)
    if axis:
        kwargs["axis"] = to_js(axis)
    if no_heuristic_alignment:
        kwargs["noHeuristicAlignment"] = to_js(no_heuristic_alignment)
    if no_use_distance_transform:
        kwargs["noUseDistanceTransform"] = to_js(no_use_distance_transform)
    if use_custom_slice_positions:
        kwargs["useCustomSlicePositions"] = to_js(use_custom_slice_positions)
    if no_use_extrapolation:
        kwargs["noUseExtrapolation"] = to_js(no_use_extrapolation)
    if use_ball_structuring_element:
        kwargs["useBallStructuringElement"] = to_js(use_ball_structuring_element)
    if labeled_slice_indices_axis:
        kwargs["labeledSliceIndicesAxis"] = to_js(labeled_slice_indices_axis)
    if labeled_slice_indices_label:
        kwargs["labeledSliceIndicesLabel"] = to_js(labeled_slice_indices_label)
    if labeled_slice_indices:
        kwargs["labeledSliceIndices"] = to_js(labeled_slice_indices)

    outputs = await js_module.morphologicalContourInterpolation(to_js(input_image), webWorker=web_worker, noCopy=True, **kwargs)

    output_web_worker = None
    output_list = []
    outputs_object_map = outputs.as_object_map()
    for output_name in outputs.object_keys():
        if output_name == 'webWorker':
            output_web_worker = outputs_object_map[output_name]
        else:
            output_list.append(to_py(outputs_object_map[output_name]))

    js_resources.web_worker = output_web_worker

    if len(output_list) == 1:
        return output_list[0]
    return tuple(output_list)
