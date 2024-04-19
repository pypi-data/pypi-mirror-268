#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @time:2024/4/10 11:16
# Author:Zhang HongTao
# @File:test_decorator.py

import numpy as np
import wrapt
from typing import Dict, List, Tuple, Union, Optional


def convert_output(
        outputs: Union[Dict, List, Tuple], wrapped=None, instance=None
):
    """Converts output from tuple ot list to dictionary.

    It is utility function useful for mapping output list into dictionary of outputs.
    Currently, it is used in @sample and @batch decorators (we assume that user can return list or tuple of outputs
    instead of dictionary if this list matches output list in model config (size and order).
    """
    if isinstance(outputs, dict):
        return outputs
    # elif isinstance(outputs, (list, tuple)):
    #     if model_config is None:
    #         model_config = get_model_config(wrapped, instance)
    #     if len(outputs) != len(model_config.outputs):
    #         raise PyTritonValidationError("Outputs length different than config outputs length")
    #     outputs = {config_output.name: output for config_output, output in zip(model_config.outputs, outputs)}
    #     return outputs
    else:
        raise ValueError(f"Unsupported output type {type(outputs)}.")


@wrapt.decorator
def batch(wrapped, instance, args, kwargs):
    """Decorator for converting list of request dicts to dict of input batches.

    Converts list of request dicts to dict of input batches.
    It passes **kwargs to inference callable where each named input contains numpy array with batch of requests
    received by Triton server.
    We assume that each request has the same set of keys (you can use group_by_keys decorator before
    using @batch decorator if your requests may have different set of keys).
    """
    print(args, "args[0]")
    print(kwargs, "kwargs")
    req_list = args[0]
    input_names = req_list[0].keys()
    print(input_names, "input_names")

    inputs = {}
    for model_input in input_names:
        concatenated_input_data = np.concatenate([req[model_input] for req in req_list])
        inputs[model_input] = concatenated_input_data

    args = args[1:]
    new_kwargs = dict(kwargs)
    new_kwargs.update(inputs)
    outputs = wrapped(*args, **new_kwargs)

    outputs = convert_output(outputs, wrapped, instance)
    output_names = outputs.keys()

    out_list = []
    start_idx = 0
    for request in req_list:
        # get batch_size of first input for each request - assume that all inputs have same batch_size
        first_input = next(iter(request.values()))
        request_batch_size = first_input.shape[0]
        req_output_dict = {}
        for _output_ind, output_name in enumerate(output_names):
            req_output = outputs[output_name][start_idx: start_idx + request_batch_size, ...]
            req_output_dict[output_name] = req_output
        out_list.append(req_output_dict)
        start_idx += request_batch_size
    return out_list


@batch
def _multiply2(image, test_1):
    # label = image * 2.0
    none_res = {"none": -1}
    # return {"res": np.array([[1, 2, 3, 4]]), "res_1": np.array([[1, 2, 3, 1]])}
    return {"label": np.array([none_res])}


@batch
def _multiply4(image, test_1):
    # label = image * 4.0
    return [None]


_multiply2([{"image": np.array([[1, 2, 3]])}, {"image": np.array([[3, 4, 5]])}], test_1=2)
# _multiply4(image=2)
