"""
Missing tests:
 - failures should be accounted for under the BaseApi
 - Each job should also be covered for process_job only 3/5 currently are.
"""

from contextlib import redirect_stdout
from datetime import datetime
import io
from math import ceil
from typing import Optional
import unittest
import unittest.mock

import networkx as nx
import numpy as np
import pytest
import requests
import scipy.sparse as sp

from qci_client import JobStatus, QciClient, compute_results_step_len


@pytest.mark.offline
class TestJobStatus(unittest.TestCase):
    """JobStatus-related test suite."""

    def test_jobstatus(self):
        """Test all job statuses."""
        job_status = JobStatus()
        self.assertEqual(job_status.QUEUED, "QUEUED")
        self.assertEqual(job_status.SUBMITTED, "SUBMITTED")
        self.assertEqual(job_status.RUNNING, "RUNNING")
        self.assertEqual(job_status.COMPLETED, "COMPLETED")
        self.assertEqual(job_status.ERRORED, "ERRORED")
        self.assertEqual(job_status.CANCELLED, "CANCELLED")


class TestQciClientFiles(unittest.TestCase):
    """Files-API-related test suite."""

    @classmethod
    def setUpClass(cls):
        cls.q1 = QciClient()
        cls.graph_dict_input = {
            "file_name": "graph.json",
            "file_config": {
                "graph": {
                    "data": nx.Graph(((1, 2), (1, 3)))
                }
            }
        }

        cls.qubo_dict_input = {
            "file_name": "qubo.json",
            "file_config": {
                "qubo": {
                    "data": sp.csr_matrix(
                        [
                            [-1.0, 1.0],
                            [1.0, -1.0]
                        ]
                    )
                }
            }
        }

        cls.objective_dict_input = {
            "file_name": "objective.json",
            "file_config": {
                "objective": {
                    "data": sp.csc_matrix(
                        [
                            [-1.0, 1.0],
                            [1.0, -1.0]
                        ]
                    )
                }
            }
        }

        cls.constraint_dict_input = {
            "file_name": "constraints.json",
            "file_config": {
                "constraints": {
                    "data": sp.coo_matrix(
                        [
                            [-1.0, 1.0, 1.0],
                        ]
                    )
                }
            }
        }

        cls.hamiltonian_dict_input = {
            "file_name": "hamiltonian.json",
            "file_config": {
                "hamiltonian": {
                    "data": np.array(
                        [
                            [1.0, 1.0, 0.0],
                            [2.0, 0.0, 1.0]
                        ]
                    )
                }
            }
        }

        cls.polynomial_dict_hamiltonian_input = {
            "file_name": "polynomial-hamiltonian.json",
            "file_config": {
                "polynomial": {
                    "min_degree": 1,
                    "max_degree": 2,
                    "num_variables": 2,
                    "data": [
                        {
                            "idx": [0, 1],
                            "val": 1.0
                        },
                        {
                            "idx": [1, 1],
                            "val": -2.0
                        },
                        {
                            "idx": [1, 2],
                            "val": 1.0
                        },
                        {
                            "idx": [2, 2],
                            "val": -1.0
                        }

                    ]
                }
            }
        }

        cls.polynomial_dict_input = {
            "file_name": "polynomial.json",
            "file_config": {
                "polynomial": {
                    "min_degree": 2,
                    "max_degree": 4,
                    "num_variables": 2,
                    "data": [
                        {
                            "idx": [0, 0, 1, 1],
                            "val": 1.0
                        },
                        {
                            "idx": [0, 1, 1, 1],
                            "val": -2.0
                        },
                        {
                            "idx": [1, 1, 1, 1],
                            "val": 1.0
                        }
                    ]
                }
            }
        }

        cls.graph_file_id = cls.q1.upload_file(file=cls.graph_dict_input)["file_id"]
        cls.qubo_file_id = cls.q1.upload_file(file=cls.qubo_dict_input)["file_id"]
        cls.objective_file_id = cls.q1.upload_file(file=cls.objective_dict_input)[
            "file_id"
        ]
        cls.constraints_file_id = cls.q1.upload_file(file=cls.constraint_dict_input)[
            "file_id"
        ]
        cls.hamiltonian_file_id = cls.q1.upload_file(file=cls.hamiltonian_dict_input)[
            "file_id"
        ]
        cls.polynomial_hamiltonian_file_id = cls.q1.upload_file(
            file=cls.polynomial_dict_hamiltonian_input
        )["file_id"]
        cls.polynomial_min_degree_2_max_degree_4_file_id = cls.q1.upload_file(
            file=cls.polynomial_dict_input)["file_id"]

        cls.all_statuses = [
            JobStatus.QUEUED,
            JobStatus.SUBMITTED,
            JobStatus.RUNNING,
            JobStatus.COMPLETED,
            JobStatus.ERRORED,
            JobStatus.CANCELLED,
        ]

        cls.final_status = [JobStatus.COMPLETED, JobStatus.ERRORED, JobStatus.CANCELLED]

        cls.job_info = set(("job_id", "details", "job_results", "job_submission",))
        cls.result_keys = ["samples", "energies", "file_name", "file_type"]

        cls.graph_job_body = {
            "job_submission": {
                "job_name": "job_0",
                "problem_config": {
                    "graph_partitioning": {
                        "graph_file_id": cls.graph_file_id
                    },
                },
                "device_config": {
                    "dirac-1": {}
                }
            }
        }

        cls.qubo_job_body = {
            "job_submission": {
                "job_name": "job_0",
                "problem_config": {
                    "quadratic_unconstrained_binary_optimization": {
                        "qubo_file_id": cls.qubo_file_id
                    },
                },
                "device_config": {
                    "dirac-1": {}
                }
            }
        }

        cls.constraint_job_body = {
            "job_submission": {
                "job_name": "job_0",
                "problem_config": {
                    "quadratic_linearly_constrained_binary_optimization": {
                        "objective_file_id": cls.objective_file_id,
                        "constraints_file_id": cls.constraints_file_id
                    }
                },
                "device_config": {
                    "dirac-1": {}
                }
            }
        }

        cls.hamiltonian_job_body_ising_dirac1 = {
            "job_submission": {
                "job_name": "dirac-1",
                "problem_config": {
                    "ising_hamiltonian_optimization": {
                        "hamiltonian_file_id": cls.hamiltonian_file_id
                    },
                },
                "device_config": {
                    "dirac-1": {
                        "num_samples": 2,
                    }
                }
            }
        }

        cls.polynomial_job_body_ising_dirac1 = {
            "job_submission": {
                "job_name": "dirac-1",
                "problem_config": {
                    "ising_hamiltonian_optimization": {
                        "polynomial_file_id": cls.polynomial_hamiltonian_file_id
                    },
                },
                "device_config": {
                    "dirac-1": {
                    }
                }
            }
        }

        cls.hamiltonian_job_body_continous_dirac2 = {
            "job_submission": {
                "job_name": "dirac-2",
                "problem_config": {
                    "normalized_qudit_hamiltonian_optimization_continuous": {
                        "hamiltonian_file_id": cls.hamiltonian_file_id
                    }
                },
                "device_config": {
                    "dirac-2": {}
                }
            }
        }

        cls.hamiltonian_job_body_integer_dirac2 = {
            "job_submission": {
                "job_name": "dirac-2",
                "problem_config": {
                    "normalized_qudit_hamiltonian_optimization_integer": {
                        "hamiltonian_file_id": cls.hamiltonian_file_id
                    },
                },
                "device_config": {
                    "dirac-2": {}
                }
            }
        }

        cls.polynomial_job_body_hamiltonian_continuous_dirac2 = {
            "job_submission": {
                "job_name": "dirac-2",
                "problem_config": {
                    "normalized_qudit_hamiltonian_optimization_continuous": {
                        "polynomial_file_id": cls.polynomial_hamiltonian_file_id
                    },
                },
                "device_config": {
                    "dirac-2": {}
                }
            }
        }

        cls.polynomial_job_body_hamiltonian_integer_dirac2 = {
            "job_submission": {
                "job_name": "dirac-2",
                "problem_config": {
                    "normalized_qudit_hamiltonian_optimization_integer": {
                        "polynomial_file_id": cls.polynomial_hamiltonian_file_id
                    },
                },
                "device_config": {
                    "dirac-2": {
                        "num_samples": 2,
                    }
                }
            }
        }

        cls.hamiltonian_job_body_undistilled_dirac3 = {
            "job_submission": {
                "job_name": "dirac-3",
                "problem_config": {
                    "normalized_qudit_hamiltonian_optimization": {
                        "hamiltonian_file_id": cls.hamiltonian_file_id
                    }
                },
                "device_config": {
                    "dirac-3": {
                        "relaxation_parameter": 1,
                        "sum_constraint": 2.4,
                    }
                }
            }
        }

        cls.hamiltonian_job_body_distilled_continuous_dirac3 = {
            "job_submission": {
                "job_name": "dirac-3",
                "problem_config": {
                    "normalized_qudit_hamiltonian_optimization": {
                        "hamiltonian_file_id": cls.hamiltonian_file_id
                    }
                },
                "device_config": {
                    "dirac-3": {
                        "relaxation_parameter": 1,
                        "sum_constraint": 2.4,
                        "solution_precision": 0.1,
                    }
                }
            }
        }

        cls.hamiltonian_job_body_distilled_integer_dirac3 = {
            "job_submission": {
                "job_name": "dirac-3",
                "problem_config": {
                    "normalized_qudit_hamiltonian_optimization": {
                        "hamiltonian_file_id": cls.hamiltonian_file_id
                    }
                },
                "device_config": {
                    "dirac-3": {
                        "relaxation_parameter": 1,
                        "solution_precision": 1,
                    }
                }
            }
        }

        cls.polynomial_min_degree_2_max_degree_4_job_body_distilled_continuous_dirac3 = {
            "job_submission": {
                "job_name": "dirac-3",
                "problem_config": {
                    "normalized_qudit_hamiltonian_optimization": {
                        "polynomial_file_id": cls.polynomial_min_degree_2_max_degree_4_file_id
                    },
                },
                "device_config": {
                    "dirac-3": {
                        "relaxation_parameter": 2,
                        "sum_constraint": 2.4,
                        "solution_precision": 0.1,
                    }
                }
            }
        }

    def test_upload_file_error(self):
        """Test uploading improperly formatted file."""
        with self.assertRaises(KeyError):
            error_input = {
                "file_type": "graph",
                "file_name": "qubo.json",
                "data": [
                    {"i": 0, "j": 0, "val": -1.0},
                    {"i": 0, "j": 1, "val": 1.0},
                    {"i": 1, "j": 0, "val": 1.0},
                    {"i": 1, "j": 1, "val": -1.0},
                ],
                "num_variables": 2,
            }
            self.q1.upload_file(file=error_input)

    def test_upload_file(self):
        """Test uploading of various file types."""
        graph_upload = self.q1.upload_file(file=self.graph_dict_input)
        self.assertIn("file_id", graph_upload)
        self.assertIsInstance(graph_upload["file_id"], str)

        qubo_upload = self.q1.upload_file(file=self.qubo_dict_input)
        self.assertIn("file_id", qubo_upload)
        self.assertIsInstance(qubo_upload["file_id"], str)

        objective_upload = self.q1.upload_file(file=self.objective_dict_input)
        self.assertIn("file_id", objective_upload)
        self.assertIsInstance(objective_upload["file_id"], str)

        constraint_upload = self.q1.upload_file(file=self.constraint_dict_input)
        self.assertIn("file_id", constraint_upload)
        self.assertIsInstance(constraint_upload["file_id"], str)

        hamiltonian_upload = self.q1.upload_file(file=self.hamiltonian_dict_input)
        self.assertIn("file_id", hamiltonian_upload)
        self.assertIsInstance(hamiltonian_upload["file_id"], str)

    def test_validate_job_type(self):
        """Test validation of job type against whitelist."""
        test_job_type = "fake_job_type"
        expected_err_str = f"Provided job_type '{test_job_type}' is not one of {self.q1._supported_job_types}"  # pylint: disable=protected-access

        with self.assertRaises(AssertionError) as context:
            self.q1.validate_job_type(job_type=test_job_type)

        # TODO: consider asserting on exception type instead of specific text of assert msg
        # because aserting on the specific text of the assert msg makes this test fairly fragile
        self.assertEqual(
            str(context.exception),
            expected_err_str
        )

        try:
            self.q1.validate_job_type(job_type="sample-qubo")
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.fail(
                f"validate_job_type failed with exception '{exc}' with supported job_type"
            )

    def test_build_job_body(self):
        """Test building of various jobs' request bodies."""
        with self.assertRaises(ValueError) as context:
            self.q1.build_job_body(
                job_type="sample-qubo",
                job_params={},
                qubo_file_id="qubo_file_id",
            )

        self.assertEqual(
            str(context.exception),
            "Must define sampler_type in job_params (dirac-1, dirac-2, or dirac-3)."
        )

        constraint_body = self.q1.build_job_body(
            job_type="sample-constraint",
            job_params={
                "sampler_type": "dirac-1",
                "alpha": 5.0,
            },
            objective_file_id="obj_fid",
            constraints_file_id="cons_fid",
            job_name="foobar_name",
            job_tags=["foobar_tag1", "foobar_tag2"],
        )

        self.assertDictEqual(
            constraint_body,
            {
                "job_submission": {
                    "job_name": "foobar_name",
                    "job_tags": ["foobar_tag1", "foobar_tag2"],
                    "problem_config": {
                        "quadratic_linearly_constrained_binary_optimization": {
                            "objective_file_id": "obj_fid",
                            "constraints_file_id": "cons_fid",
                            "alpha": 5.0
                        }
                    },
                    "device_config": {
                        "dirac-1": {}
                    }
                }
            }
        )

        qubo_body = self.q1.build_job_body(
            job_type="sample-qubo",
            job_params={
                "nsamples": 24,
                "sampler_type": "dirac-1",
            },
            qubo_file_id="qubo_fid",
            job_name="foobar_name",
        )

        self.assertDictEqual(
            qubo_body,
            {
                "job_submission": {
                    "job_name": "foobar_name",
                    "problem_config": {
                        "quadratic_unconstrained_binary_optimization": {
                            "qubo_file_id": "qubo_fid",
                        }
                    },
                    "device_config": {
                        "dirac-1": {
                            "num_samples": 24
                        }
                    }
                }
            }
        )

        hamiltonian_body = self.q1.build_job_body(
            job_type="sample-hamiltonian",
            job_params={
                "n_samples": 24,
                "sampler_type": "dirac-3",
                "sum_constraint": 200,
                "solution_precision": 1,
            },
            hamiltonian_file_id="hamiltonian_fid",
            job_tags=["foobar_tag1", "foobar_tag2"],
        )

        self.assertDictEqual(
            hamiltonian_body,
            {
                "job_submission": {
                    "job_tags": ["foobar_tag1", "foobar_tag2"],
                    "problem_config": {
                        "normalized_qudit_hamiltonian_optimization": {
                            "hamiltonian_file_id": "hamiltonian_fid",
                        }
                    },
                    "device_config": {
                        "dirac-3": {
                            "num_samples": 24,
                            "sum_constraint": 200,
                            "solution_precision": 1,
                        }
                    }
                }
            }
        )

        hamiltonian_body = self.q1.build_job_body(
            job_type="sample-hamiltonian",
            job_params={
                "sampler_type": "dirac-3",
                "sum_constraint": 200,
                "solution_precision": 1,
            },
            polynomial_file_id="polynomial_fid"
        )

        self.assertDictEqual(
            hamiltonian_body,
            {
                "job_submission": {
                    "problem_config": {
                        "normalized_qudit_hamiltonian_optimization": {
                            "polynomial_file_id": "polynomial_fid",
                        }
                    },
                    "device_config": {
                        "dirac-3": {
                            "sum_constraint": 200,
                            "solution_precision": 1,
                        }
                    }
                }
            }
        )

        hamiltonian_body = self.q1.build_job_body(
            job_type="sample-hamiltonian",
            job_params={
                "sampler_type": "dirac-3",
                "sum_constraint": 2.4
            },
            polynomial_file_id="polynomial_fid"
        )

        self.assertDictEqual(
            hamiltonian_body,
            {
                "job_submission": {
                    "problem_config": {
                        "normalized_qudit_hamiltonian_optimization": {
                            "polynomial_file_id": "polynomial_fid",
                        }
                    },
                    "device_config": {
                        "dirac-3": {
                            "sum_constraint": 2.4,
                        }
                    }
                }
            }
        )

        hamiltonian_body = self.q1.build_job_body(
            job_type="sample-hamiltonian",
            job_params={
                "sampler_type": "dirac-3",
                "sum_constraint": 2.4,
                "solution_precision": 0.1,
            },
            hamiltonian_file_id="hamiltonian_fid"
        )

        self.assertDictEqual(
            hamiltonian_body,
            {
                "job_submission": {
                    "problem_config": {
                        "normalized_qudit_hamiltonian_optimization": {
                            "hamiltonian_file_id": "hamiltonian_fid",
                        }
                    },
                    "device_config": {
                        "dirac-3": {
                            "sum_constraint": 2.4,
                            "solution_precision": 0.1,
                        }
                    }
                }
            }
        )

        graph_body = self.q1.build_job_body(
            job_type="graph-partitioning",
            job_params={
                "sampler_type": "dirac-1",
                "num_samples": 42,
            },
            graph_file_id="graph_fid"
        )

        self.assertDictEqual(
            graph_body,
            {
                "job_submission": {
                    "problem_config": {
                        "graph_partitioning": {
                            "graph_file_id": "graph_fid",
                        }
                    },
                    "device_config": {
                        "dirac-1": {
                            "num_samples": 42,
                        }
                    }
                }
            }
        )

    def test_print_job_log(self):
        """Test printing of job log messages."""
        string_io = io.StringIO()
        with redirect_stdout(string_io):
            self.q1.print_job_log(message="fake message")
        out = string_io.getvalue()
        date_now = str(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))[0:10]
        self.assertTrue(out.startswith(f"fake message: {date_now}"))


class TestMultipartUpload(unittest.TestCase):
    """Multipart-file upload test suite."""

    @classmethod
    def setUpClass(cls):
        cls.q1 = QciClient()

    # TODO This client no longer uploads results files, only test download.
    def test_multipart_results_upload_and_download(self):
        """Test uploading/downloading multipart qubo results file."""
        # BIG number of samples, each one num_vars in length
        num_vars = 1700
        num_samp = 300
        is_results_file = True
        samples = np.ones((num_samp, num_vars)).astype(int)
        counts = np.ones((num_samp, 1)).astype(int)
        energies = np.ones((num_samp, 1))

        resdata = {
            "file_name": "test-file.json",
            "file_type": "job_results_sample_qubo",
            "organization_id": "5ddf5db3fed87d53b6bf392a",
            "username": "test_user",
            "counts": counts.flatten().tolist(),
            "energies": energies.flatten().tolist(),
            "samples": samples.tolist(),
        }

        step_len = compute_results_step_len(resdata["samples"][0])
        expected_parts = ceil(num_samp / step_len)
        self.assertGreater(expected_parts, 1)

        #resp = self.q1.upload_file(file=resdata)
        #meta = self.q1.get_file_metadata(file_id=resp["file_id"], is_results_file=is_results_file)
        #self.assertEqual(meta["num_parts"], expected_parts)

        #test_res_whole = self.q1.get_file_whole(file_id=resp["file_id"], is_results_file=is_results_file)
        #self.assertEqual(len(test_res_whole["counts"]), counts.shape[0])
        #self.assertEqual(len(test_res_whole["energies"]), energies.shape[0])
        #self.assertEqual(len(test_res_whole["samples"]), samples.shape[0])
        #self.assertEqual(len(test_res_whole["samples"][0]), samples.shape[1])

        #del_resp = self.q1.delete_file(resp["file_id"])
        #assert del_resp["num_deleted"] == 1

    # TODO This client no longer uploads results files, only test download.
    def test_multipart_results_upload_and_download_hamiltonian(self):
        """Test uploading/downloading multipart hamiltonian results file."""
        # Tests float uploads, so we use Hamiltonian job type so the API can handle floats
        num_vars = 20000
        num_samp = 30
        samples = np.ones((num_samp, num_vars)).astype(float)
        counts = np.ones((num_samp, 1)).astype(int)
        energies = np.ones((num_samp, 1))
        is_results_file = True

        resdata = {
            "file_name": "test-file.json",
            "file_type": "job_results_sample_hamiltonian",
            "organization_id": "5ddf5db3fed87d53b6bf392a",
            "username": "test_user",
            #"solution_type": "continuous",
            "counts": counts.flatten().tolist(),
            "energies": energies.flatten().tolist(),
            "samples": samples.tolist(),
        }

        step_len = compute_results_step_len(resdata["samples"][0])
        expected_parts = ceil(num_samp / step_len)
        self.assertGreater(expected_parts, 1)

        # resp = self.q1.upload_file(file=resdata)
        #meta = self.q1.get_file_metadata(file_id=resp["file_id"], is_results_file=is_results_file)
        #self.assertEqual(meta["num_parts"], expected_parts)

        #test_res_whole = self.q1.get_file_whole(file_id=resp["file_id"], is_results_file=is_results_file)
        #self.assertEqual(len(test_res_whole["counts"]), len(test_vec_int))
        #self.assertEqual(len(test_res_whole["energies"]), test_vec.shape[0])
        #self.assertEqual(len(test_res_whole["samples"]), num_samples)
        #self.assertEqual(len(test_res_whole["samples"][0]), num_nodes)

        # del_resp = self.q1.delete_file(resp["file_id"])
        # assert del_resp["num_deleted"] == 1

    # TODO This client no longer uploads results files, only test download.
    def test_multipart_results_upload_and_download_huge(self):
        """Test uploading/downloading very large multipart qubo results file."""
        # Now try something too large
        # BIG number of samples, each one num_vars in length
        num_vars = 100000
        num_samp = 300
        samples = np.ones((num_samp, num_vars)).astype(int)
        counts = np.ones((num_samp, 1)).astype(int)
        energies = np.ones((num_samp, 1))
        is_results_file = True

        resdata = {
            "file_name": "test-file.json",
            "file_type": "job_results_sample_qubo",
            "organization_id": "5ddf5db3fed87d53b6bf392a",
            "username": "test_user",
            "counts": counts.flatten().tolist(),
            "energies": energies.flatten().tolist(),
            "samples": samples.tolist(),
        }

        step_len = compute_results_step_len(samples[0])
        expected_parts = ceil(num_samp / step_len)
        self.assertGreater(expected_parts, 1)

        # resp = self.q1.upload_file(file=resdata)
        #meta = self.q1.get_file_metadata(file_id=resp["file_id"], is_results_file=is_results_file)
        #self.assertEqual(meta["num_parts"], expected_parts)

        #test_res_whole = self.q1.get_file_whole(file_id=resp["file_id"], is_results_file=is_results_file)
        #self.assertEqual(len(test_res_whole["counts"]), counts.shape[0])
        #self.assertEqual(len(test_res_whole["energies"]), energies.shape[0])
        #self.assertEqual(len(test_res_whole["samples"]), samples.shape[0])
        #self.assertEqual(len(test_res_whole["samples"][0]), samples.shape[1])


    # TODO This client no longer uploads results files, only test download.
    def test_multipart_graph_partitioning_results_upload_and_download(self):
        """Test uploading/downloading multipart graph-partitioning results file."""
        num_samples = 10
        num_nodes = 10000
        test_vec = np.arange(num_samples)
        test_vec_int = np.arange(num_samples).astype(int)
        is_results_file = True

        samples = [
            [
                {"id": int(np.random.randint(0, 10)), "class": np.random.randint(0, 3)}
                for _ in range(num_nodes)
            ]  # pretend we have a graph with 100 nodes
            for _ in range(num_samples)  # and we asked for 1000 samples
        ]

        gp_results = {
            "file_name": "test-file.json",
            "file_type": "job_results_graph_partitioning",
            "organization_id": "5ddf5db3fed87d53b6bf392a",
            "username": "test_user",
            "balance": test_vec.tolist(),
            "counts": test_vec.tolist(),
            "cut_size": test_vec_int.tolist(),
            "energies": test_vec.tolist(),
            "is_feasible": [True] * num_samples,
            "samples": samples,
        }

        step_len = compute_results_step_len(samples[0])
        expected_parts = ceil(num_samples / step_len)
        self.assertGreater(expected_parts, 1)

        # resp = self.q1.upload_file(file=gp_results)

        #meta = self.q1.get_file_metadata(file_id=resp["file_id"], is_results_file=is_results_file)
        #self.assertEqual(meta["num_parts"], expected_parts)

        #del_resp = self.q1.delete_file(resp["file_id"])
        #assert del_resp["num_deleted"] == 1


@pytest.mark.offline
class TestJobsApiWithRequestMocks(unittest.TestCase):
    """Jobs-API-related test suite that can be run without backend."""

    def setUp(self):
        with pytest.MonkeyPatch().context() as mp:
            mp.setenv('QCI_TOKEN', 'test_api_token')
            mp.setenv('QCI_API_URL', 'test_url')
            self.qci_client = QciClient(set_bearer_token_on_init=False)
        self.job_id = "63b717a22da68618ec444eac"
        self.job_type = "sample-hamiltonian"
        self.file_id = "73b717a22da68618ec444eab"

        # Bad GET jobs response.
        self.get_response_bad = requests.Response()
        self.get_response_bad.status_code = 404

    def test_jobs_url(self) -> None:
        """Test getting jobs URL."""
        self.assertEqual(self.qci_client.jobs_url, "test_url/optimization/v1/jobs")

    def test_get_job_id_url(self) -> None:
        """Test getting jobs URL for given job ID."""
        self.assertEqual(
            self.qci_client.get_job_id_url(self.job_id), f"test_url/optimization/v1/jobs/{self.job_id}"
        )

    def test_get_job_status_url(self) -> None:
        """Test getting jobs-status URL for given job ID."""
        self.assertEqual(
            self.qci_client.get_job_status_url(self.job_id),
            f"test_url/optimization/v1/jobs/{self.job_id}/status",
        )

    def test_files_url(self) -> None:
        """Test getting files URL."""
        self.assertEqual(self.qci_client.files_url, "test_url/optimization/v1/files")

    def test_get_file_id_url(self) -> None:
        """Test getting files URL for given file ID."""
        self.assertEqual(
            self.qci_client.get_file_id_url(self.file_id),
            f"test_url/optimization/v1/files/{self.file_id}",
        )

    def test_get_job_type_from_job_id(self) -> None:
        """Test getting job type from job ID."""
        # GET short jobs response.
        get_jobs_response_short = requests.Response()
        get_jobs_response_short.status_code = 200
        get_jobs_response_short._content = (  # pylint: disable=protected-access
            b"""{
    "job_id": "%b",
    "status": "COMPLETED",
    "type": "sample_hamiltonian",
    "organization_id": "6edf5db3def87d53b6bf375b",
    "username": "test_user"
}"""
            % self.job_id.encode()
        )

        self.qci_client.session.request = unittest.mock.MagicMock(
            return_value=get_jobs_response_short
        )
        self.assertEqual(
            self.qci_client.get_job_type_from_job_id(self.job_id), self.job_type
        )

        self.qci_client.session.request = unittest.mock.MagicMock(
            return_value=self.get_response_bad
        )
        with self.assertRaises(requests.HTTPError):
            self.qci_client.get_job_type_from_job_id(self.job_id)
