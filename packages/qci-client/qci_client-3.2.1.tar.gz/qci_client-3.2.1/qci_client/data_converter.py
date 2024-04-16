"""Functions for data conversion."""

from math import floor
import sys
import time
from typing import Union

import networkx as nx
import numpy as np
import scipy.sparse as sp

from qci_client import enum

# We want to limit the memory size of each uploaded chunk to be safely below the max of 15 * MebiByte (~15MB).
# See https://git.qci-dev.com/qci-dev/qphoton-files-api/-/blob/main/service/files.go#L32.
MEMORY_MAX: int = 8 * 1000000  # 8MB


def get_size(obj, seen=None) -> int:
    """
    Recursively finds size of objects

    :param obj: data object to recursively compute size of
    :param seen: takes a set and is used in the recursive step only to record whether an object has been counted yet.

    :return int:
    """
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum(get_size(v, seen) for v in obj.values())
        size += sum(get_size(k, seen) for k in obj.keys())
    elif hasattr(obj, "__dict__"):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
        size += sum(get_size(i, seen) for i in obj)
    return size


def _get_soln_size(soln):
    # Check whether first entry is a graph node/class assignment, eg., {'id': 4, 'class': 2}
    if isinstance(soln[0], dict):
        return get_size(soln)

    return sys.getsizeof(soln[0]) * len(soln)


def compute_results_step_len(data: Union[np.ndarray, list]) -> int:
    """
    Compute the step length for "chunking" the providd data.

    Args:
        data: An numpy array or list of data

    Returns:
        The step length for "chunking" the data
    """
    # total mem size of soln vector
    soln_mem = _get_soln_size(data)
    # num_vars * step_len < 30k => step_len < 30k/num_vars
    chunk_ratio = MEMORY_MAX / soln_mem
    step_len = floor(chunk_ratio) if chunk_ratio >= 1 else 1
    return step_len

def data_to_json(file: dict, debug: bool = False) -> dict:
    """
    Converts data in file input into JSON-serializable dictionary that can be passed to Qatalyst REST API

    Args:
        file: file dictionary whose data of type numpy.ndarray, scipy.sparse.spmatrix, or networkx.Graph is to be converted
        debug: Optional, if set to True, enables debug output (default = False for no debug output)

    Returns:
        file dictionary with JSON-serializable data
    """
    start_time_s = time.perf_counter()

    supported_file_types = [type.value for type in enum.JOB_INPUTS_FILE_TYPES]
    supported_file_types.sort()
    supported_file_types = tuple(supported_file_types)
    matrix_file_types = [type.value for type in enum.JOB_INPUTS_MATRIX_FILE_TYPES]
    matrix_file_types.sort()
    matrix_file_types = tuple(matrix_file_types)

    file_type = enum.get_file_type(file=file).value

    if file_type not in supported_file_types:
        raise AssertionError(
            f"data conversion not supported for file type '{file_type}', supported "
            f"types are {supported_file_types}"
        )

    data = file['file_config'][file_type]['data']

    if file_type == "graph":
        if not isinstance(data, nx.Graph):
            raise AssertionError("file_type 'graph' data must be a networkx.Graph")

        file_config = {
            **nx.node_link_data(data),
            "num_edges": data.number_of_edges(),
            "num_nodes": data.number_of_nodes(),
        }
    elif file_type in matrix_file_types:
        if isinstance(data, nx.Graph):
            raise AssertionError(
                f"file_type '{file_type}' data cannot be a networkx.Graph"
            )

        data_ls = []

        if sp.isspmatrix_dok(data):
            for idx, val in zip(data.keys(), data.values()):
                # dok type has trouble subsequently serializing to json without type
                # casts. For example, uint16 and float32 cause problems.
                data_ls.append({"i": int(idx[0]), "j": int(idx[1]), "val": float(val)})
        elif sp.isspmatrix(data) or isinstance(data, np.ndarray):
            data = sp.coo_matrix(data)

            for i, j, val in zip(
                data.row.tolist(), data.col.tolist(), data.data.tolist()
            ):
                data_ls.append({"i": i, "j": j, "val": val})
        else:
            raise ValueError(
                f"file_type '{file_type}' only supports types numpy.ndarray and "
                f"scipy.sparse.spmatrix, got {type(data)}"
            )

        file_config = {"data": data_ls}
        rows, cols = data.get_shape()

        if file_type == "constraints":
            # Constraints matrix is [A | -b]
            file_config.update({"num_constraints": rows, "num_variables": cols-1})
        else:
            # This works for hamiltonians, qubos, and objectives.
            file_config["num_variables"] = rows
    else:
        # Polynomial file types do not require translation.
        file_config = file["file_config"][file_type]

    if debug:
        print(f"Time to convert data to json: {time.perf_counter()-start_time_s} s.")

    return {
        "file_name": file.get("file_name", f"{file_type}.json"),
        "file_config": {file_type: file_config}
    }
