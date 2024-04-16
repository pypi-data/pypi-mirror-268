"""Test suite for jobs run on a remote backend."""

from copy import deepcopy
from typing import Optional
import unittest

import numpy as np
import scipy.sparse as sp

from qci_client import JobStatus
import qci_client.base
from tests.test_qci_client import TestQciClientFiles


class TestQciClientRemoteJobs(TestQciClientFiles):
    """Collection of tests for remote jobs."""

    def run_end_end(
        self, job_type: str, job_body: dict, result_keys: Optional[list] = None
    ):
        """
        Utility function for testing end to end pipeline.
        :param job_type: one of _supported_job_types
        :param job_body: a validate job request
        Testing each in series:
            - submit_job
            - get_job_status
            - get_job_response
            - get_file
        """

        result_keys = self.result_keys if result_keys is None else result_keys

        job_id = self.q1.submit_job(job_body=job_body, job_type=job_type)

        self.assertIn("job_id", job_id)
        self.assertIsInstance(job_id["job_id"], str)

        status = {"status": ""}

        while status["status"] not in self.final_status:
            status = self.q1.get_job_status(job_id=job_id["job_id"])
            self.assertIn(status["status"], self.all_statuses)

        self.assertEqual(JobStatus.COMPLETED, status["status"])
        response = self.q1.get_job_response(job_id=job_id["job_id"], job_type=job_type)

        # test job info has appropriate keys
        # self.assertEqual(self.job_info, set(response.keys()))  # FIXME

        result = self.q1.download_file(file_id=response["job_result"]["file_id"])
        result = list(result)
        # self.assertTrue(all(i in result[0] for i in result_keys))  # FIXME


    def process_job_check(self, job_type, job_body):
        """Utility function for checking job types."""
        process_key = ["job_info", "results"]
        job_output = self.q1.process_job(
            job_type=job_type, job_body=job_body, wait=True
        )
        self.assertTrue(all(key in process_key for key in list(job_output.keys())))

    def test_large_job(self):
        """Test large sample-qubo job."""
        num_variables = 1000
        large_qubo = sp.random(
               num_variables, num_variables, density=0.5, format='dok', dtype=np.float32
        )
        large_qubo = (large_qubo + large_qubo.T) / 2
        large_qubo_dict = {
            "file_name": "test_large_qubo",
            "file_config": {
                "qubo": {
                    "data": large_qubo
                }
            }
        }
        large_file_id = self.q1.upload_file(file=large_qubo_dict)["file_id"]
        print("LARGE FILE ID", large_file_id)
        large_job_body = {
            "job_submission": {
                "job_name": "large_qubo_test_job",
                "problem_config": {
                    "quadratic_unconstrained_binary_optimization": {
                        "qubo_file_id": large_file_id
                    }
                },
                "device_config": {
                    "dirac-1": {}
                }
            }
        }

        self.process_job_check(job_type="sample-qubo", job_body=large_job_body)

    def test_process_qubo(self):
        """Test that sample-qubo job process can be checked."""
        self.process_job_check(job_type="sample-qubo", job_body=self.qubo_job_body)

    def test_process_constraint(self):
        """Test that sample-constraint job process can be checked."""
        self.process_job_check(
            job_type="sample-constraint", job_body=self.constraint_job_body
        )

    def test_process_hamiltonian_ising_dirac1(self):
        """Test that sample-hamiltonian-ising process job on dirac-1 can be checked."""
        self.process_job_check(
            job_type="sample-hamiltonian-ising",
            job_body=self.hamiltonian_job_body_ising_dirac1,
        )

    def test_process_hamiltonian_dirac2(self):
        """Test that integer sample-hamiltonian process job on dirac-2 can be checked."""
        self.process_job_check(
            job_type="sample-hamiltonian",
            job_body=self.hamiltonian_job_body_integer_dirac2,
        )

    def test_process_hamiltonian_dirac3(self):
        """
        Test that undistilled sample-hamiltonian process on dirac-3 job can be checked.
        """
        self.process_job_check(
            job_type="sample-hamiltonian",
            job_body=self.hamiltonian_job_body_undistilled_dirac3,
        )

    def test_graph_partitioning(self):
        """Test graph-partitioning job."""
        self.run_end_end(job_type="graph-partitioning", job_body=self.graph_job_body)

    def test_sample_qubo(self):
        """Test sample-qubo job."""
        self.run_end_end(job_type="sample-qubo", job_body=self.qubo_job_body)

    def test_sample_constraint(self):
        """Test sample-constraint job."""
        self.run_end_end(
            job_type="sample-constraint",
            job_body=self.constraint_job_body,
        )

    def test_sample_hamiltonian_ising_polynomial_dirac1(self):
        """Test sample-hamiltonian-ising job using polynomial on dirac-1."""
        self.run_end_end(
            job_type="sample-hamiltonian-ising",
            job_body=self.polynomial_job_body_ising_dirac1
        )

    def test_sample_hamiltonian_ising_hamiltonian_dirac1(self):
        """Test sample-hamiltonian-ising job using hamiltonian matrix on dirac-1."""
        self.run_end_end(
            job_type="sample-hamiltonian-ising",
            job_body=self.hamiltonian_job_body_ising_dirac1
        )

    def test_sample_hamiltonian_polynomial_continuous_dirac2(self):
        """Test sample-hamiltonian continuous job using polynomial on dirac-2."""
        self.run_end_end(
            job_type="sample-hamiltonian",
            job_body=self.polynomial_job_body_hamiltonian_continuous_dirac2
        )

    def test_sample_hamiltonian_polynomial_integer_dirac2(self):
        """Test sample-hamiltonian integer job using polynomial on dirac-2."""
        self.run_end_end(
            job_type="sample-hamiltonian",
            job_body=self.polynomial_job_body_hamiltonian_integer_dirac2
        )

    def test_sample_hamiltonian_continuous_dirac2(self):
        """Test continuous sample-hamiltonian job on dirac-2."""
        self.run_end_end(
            job_type="sample-hamiltonian",job_body=self.hamiltonian_job_body_continous_dirac2
        )

    def test_sample_hamiltonian_integer_dirac2(self):
        """Test integer sample-hamiltonian job on dirac-2."""
        self.run_end_end(
            job_type="sample-hamiltonian",
            job_body=self.hamiltonian_job_body_integer_dirac2
        )

    def test_sample_hamiltonian_polynomial_distilled_continuous_dirac3(self):
        """
        Test distilled-to-continuous sample-hamiltonian job using polynomial on dirac-3.
        """
        self.run_end_end(
            job_type="sample-hamiltonian",
            job_body=self.polynomial_min_degree_2_max_degree_4_job_body_distilled_continuous_dirac3,
        )

    def test_sample_hamiltonian_undistilled_dirac3(self):
        """Test undistilled sample-hamiltonian job on dirac-3."""
        self.run_end_end(
            job_type="sample-hamiltonian",
            job_body=self.hamiltonian_job_body_undistilled_dirac3,
        )

    def test_sample_hamiltonian_distilled_continuous_dirac3(self):
        """Test distilled-to-continuous sample-hamiltonian job on dirac-3."""
        self.run_end_end(
            job_type="sample-hamiltonian",
            job_body=self.hamiltonian_job_body_distilled_continuous_dirac3,
        )

    def test_sample_hamiltonian_distilled_integer_dirac3(self):
        """Test distilled-to-integer sample-hamiltonian job on dirac-3."""
        self.run_end_end(
            job_type="sample-hamiltonian",
            job_body=self.hamiltonian_job_body_distilled_integer_dirac3,
        )


@qci_client.base.BaseApi.refresh_token
def refresh_token_wrapped_function(*_, **__) -> None:
    """Mock function wrapped with token checking/fetching."""


class TestBaseApi(unittest.TestCase):
    """BaseApi-related test suite."""

    def test_is_bearer_token_expired_uninit(self):
        """Test is_bearer_token_expired when not retrieved during intialization."""
        # This should initialize with unset bearer info that is considered to have expired token.
        base_api = qci_client.base.BaseApi(set_bearer_token_on_init=False)
        self.assertTrue(base_api.is_bearer_token_expired())

        # Calling this function should set bearer info expiration.
        refresh_token_wrapped_function(base_api)
        self.assertFalse(base_api.is_bearer_token_expired())
        original_bearer_info = deepcopy(base_api._bearer_info)

        # Calling this function again should not reset set bearer info expiration.
        refresh_token_wrapped_function(base_api)
        self.assertFalse(base_api.is_bearer_token_expired())
        self.assertDictEqual(base_api._bearer_info, original_bearer_info)

    def test_is_bearer_token_expired_init(self):
        """Test is_bearer_token_expired when retrieved during intialization."""
        # This should initialize with set bearer info with unexpired token.
        base_api = qci_client.base.BaseApi()
        self.assertFalse(base_api.is_bearer_token_expired())
        original_bearer_info = deepcopy(base_api._bearer_info)

        # Calling this function again should not reset set bearer info expiration.
        refresh_token_wrapped_function(base_api)
        self.assertFalse(base_api.is_bearer_token_expired())
        self.assertDictEqual(base_api._bearer_info, original_bearer_info)
