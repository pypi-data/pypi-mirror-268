# Generated file. To retain edits, remove this comment.

from pathlib import Path, PurePosixPath
import os
from typing import Dict, Tuple, Optional, List, Any

from importlib_resources import files as file_resources

_pipeline = None

from itkwasm import (
    InterfaceTypes,
    PipelineOutput,
    PipelineInput,
    Pipeline,
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
    global _pipeline
    if _pipeline is None:
        _pipeline = Pipeline(file_resources('itkwasm_morphological_contour_interpolation_wasi').joinpath(Path('wasm_modules') / Path('morphological-contour-interpolation.wasi.wasm')))

    pipeline_outputs: List[PipelineOutput] = [
        PipelineOutput(InterfaceTypes.Image),
    ]

    pipeline_inputs: List[PipelineInput] = [
        PipelineInput(InterfaceTypes.Image, input_image),
    ]

    args: List[str] = ['--memory-io',]
    # Inputs
    args.append('0')
    # Outputs
    output_image_name = '0'
    args.append(output_image_name)

    # Options
    input_count = len(pipeline_inputs)
    if label:
        args.append('--label')
        args.append(str(label))

    if axis:
        args.append('--axis')
        args.append(str(axis))

    if no_heuristic_alignment:
        args.append('--no-heuristic-alignment')

    if no_use_distance_transform:
        args.append('--no-use-distance-transform')

    if use_custom_slice_positions:
        args.append('--use-custom-slice-positions')

    if no_use_extrapolation:
        args.append('--no-use-extrapolation')

    if use_ball_structuring_element:
        args.append('--use-ball-structuring-element')

    if labeled_slice_indices_axis:
        args.append('--labeled-slice-indices-axis')
        args.append(str(labeled_slice_indices_axis))

    if labeled_slice_indices_label:
        args.append('--labeled-slice-indices-label')
        args.append(str(labeled_slice_indices_label))

    if labeled_slice_indices is not None and len(labeled_slice_indices) < 1:
       raise ValueError('"labeled-slice-indices" kwarg must have a length > 1')
    if labeled_slice_indices is not None and len(labeled_slice_indices) > 0:
        args.append('--labeled-slice-indices')
        for value in labeled_slice_indices:
            args.append(str(value))


    outputs = _pipeline.run(args, pipeline_outputs, pipeline_inputs)

    result = outputs[0].data
    return result

