"""
Enumerations for Python client for files REST API for optimization service.

Copyright 2023, Quantum Computing Incorporated
"""

from enum import Enum


class FileType(Enum):
    """Enumeration of all file types."""

    # Enums should match corresponding literals in types module.
    # Job input files.
    CONSTRAINTS = "constraints"
    GRAPH = "graph"
    HAMILTONIAN = "hamiltonian"
    OBJECTIVE = "objective"
    POLYNOMIAL = "polynomial"
    QUBO = "qubo"
    # Job results files.
    GP_RESULTS = "graph_partitioning_results"
    IHO_RESULTS = "ising_hamiltonian_optimization_results"
    NQHO_CONTINUOUS_RESULTS = (
        "normalized_qudit_hamiltonian_optimization_continuous_results"
    )
    NQHO_INTEGER_RESULTS = "normalized_qudit_hamiltonian_optimization_integer_results"
    QLCBO_RESULTS = "quadratic_linearly_constrained_binary_optimization_results"
    QUBO_RESULTS = "quadratic_unconstrained_binary_optimization_results"


FILE_TYPES = frozenset(type.value for type in FileType)
JOB_INPUTS_FILE_TYPES = frozenset(
    type for type in FileType if "results" not in type.value
)
JOB_INPUTS_MATRIX_FILE_TYPES = JOB_INPUTS_FILE_TYPES - frozenset([FileType.GRAPH, FileType.POLYNOMIAL])
JOB_INPUTS_NON_GRAPH_FILE_TYPES = JOB_INPUTS_FILE_TYPES - frozenset([FileType.GRAPH])
JOB_RESULTS_FILE_TYPES = frozenset(type for type in FileType if "results" in type.value)


def get_file_type(file: dict) -> FileType:
    """Get file type from a file."""
    file_config_keys = list(file["file_config"].keys())

    if len(file_config_keys) != 1:
        raise ValueError(
            "improper number of files specified in file_config (should be exactly one)"
        )

    return FileType(file_config_keys[0])
