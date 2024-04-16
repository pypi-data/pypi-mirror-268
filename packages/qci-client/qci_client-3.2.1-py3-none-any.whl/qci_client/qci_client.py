"""
QciClient
Utility class for user interactions with QCI API
"""

import concurrent.futures
from dataclasses import dataclass
from datetime import datetime
import gzip
from io import BytesIO
import json
from posixpath import join
import time
from typing import ClassVar, Optional

from requests.adapters import HTTPAdapter, Retry
from requests_futures.sessions import FuturesSession

from qci_client import utilities
from qci_client.base import BaseApi, BACKOFF_FACTOR, RETRY_TOTAL, STATUS_FORCELIST
from qci_client.data_converter import data_to_json

TIMEOUT_DEFAULT: Optional[float] = 2 * 60.0  # seconds, or None for infinite.
COMPRESS_DEFAULT = False
MAX_WORKERS = 8

class JobStatus:  # pylint: disable=too-few-public-methods
    """Allowed jobs statuses."""

    QUEUED = "QUEUED"
    SUBMITTED = "SUBMITTED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    ERRORED = "ERRORED"
    CANCELLED = "CANCELLED"

FINAL_STATUSES = frozenset([JobStatus.COMPLETED, JobStatus.ERRORED, JobStatus.CANCELLED])

@dataclass
class QciClient(BaseApi):  # pylint: disable=too-many-public-methods
    """
    Provides requests for QCi's public API for running optimization problems on Dirac
    devices, including file uploads/downloads and submitting/retrieving entire jobs.

    Accepts same parameters as :class:`qci_client.base.BaseApi` as well as:

    :param files: url path fragment to specify files API endpoint
    :param jobs: url path fragment to specify jobs API endpoint
    :param max_workers: number of threads for concurrent file download calls
    :param compress: compress file metadata and parts before uploading
    """
    files: str = "optimization/v1/files"
    jobs: str = "optimization/v1/jobs"
    max_workers: int = 8
    compress: bool = COMPRESS_DEFAULT

    _supported_job_types: ClassVar[frozenset] = frozenset(
        [
            "sample-qubo",
            "graph-partitioning",
            "sample-constraint",
            "sample-hamiltonian",
            "sample-hamiltonian-ising",
        ]
    )

    @property
    def jobs_url(self):
        """Get jobs URL."""
        return join(self.url, self.jobs)

    def get_job_id_url(self, job_id: str) -> str:
        """Get job URL with job ID."""
        return join(self.jobs_url, job_id)

    def get_job_status_url(self, job_id: str) -> str:
        """Get job status using job ID."""
        return join(self.get_job_id_url(job_id), "status")

    def get_job_allocations_url(self) -> str:
        """Get job allocations"""
        return join(self.jobs_url, "allocations")

    @property
    def files_url(self):
        """Get files URL."""
        return join(self.url, self.files)

    def get_file_id_url(self, file_id: str) -> str:
        """Get file URL with file ID."""
        return join(self.files_url, file_id)

    def get_file_contents_url(self, file_id: str, part_num: int) -> str:
        """Get file contents URL with file ID and file part number."""
        return join(self.get_file_id_url(file_id), "contents", str(part_num))

    @property
    def headers_without_authorization(self) -> dict:
        """HTTP headers without bearer token."""
        headers = {
            "Content-Type": "application/json",
            # Simple, sessionless requests, so close connection proactively.
            "Connection": "close",
        }

        if self.timeout is not None:
            # Tell server when client will stop waiting for response.
            headers["X-Request-Timeout-Nano"] = str(int(10**9 * self.timeout))

        return headers

    @BaseApi.refresh_token
    def upload_file(  # pylint: disable=too-many-branches, too-many-locals, too-many-statements
        self,
        file: dict,
    ) -> dict:
        """
        Upload file (metadata and then parts concurrently). Returns dict with file ID.
        """
        # Use session with maintained connection and multipart concurrency for
        # efficiency.
        file = data_to_json(file=file)

        with FuturesSession(max_workers=self.max_workers) as session:
            session.mount(
                "https://",
                HTTPAdapter(
                    max_retries=Retry(
                        total=RETRY_TOTAL,
                        backoff_factor=BACKOFF_FACTOR,
                        status_forcelist=STATUS_FORCELIST,
                    )
                ),
            )

            post_response_future = session.post(
                self.files_url,
                headers=self.headers_without_connection_close,
                timeout=self.timeout,
                json=utilities.get_post_request_body(file=file),
            )

            for response_future in concurrent.futures.as_completed(
                [post_response_future], self.timeout
            ):
                response = response_future.result()
                self._check_response_error(response)

            file_id = response.json()["file_id"]
            file_part_generator = utilities.file_part_generator(
                file=file, compress=self.compress
            )
            patch_response_futures = []

            if self.compress:
                for part_body, part_number in file_part_generator:
                    patch_response_futures.append(
                        session.patch(
                            join(self.files_url, f"{file_id}/contents/{part_number}"),
                            headers=self.headers_without_connection_close,
                            timeout=self.timeout,
                            data=utilities.zip_payload(
                                payload=utilities.get_patch_request_body(file=part_body)
                            ),
                        )
                    )
            else:
                for part_body, part_number in file_part_generator:
                    patch_response_futures.append(
                        session.patch(
                            join(self.files_url, f"{file_id}/contents/{part_number}"),
                            headers=self.headers_without_connection_close,
                            timeout=self.timeout,
                            json=utilities.get_patch_request_body(file=part_body),
                        )
                    )

            # Due to timeout in underlying PATCH, this should not hang despite no
            # timeout.
            for response_future in concurrent.futures.as_completed(
                patch_response_futures
            ):
                response = response_future.result()
                self._check_response_error(response)

        return {"file_id": file_id}

    @BaseApi.refresh_token
    def download_file(self, *, file_id: str) -> dict:
        """Download file (metadata and then parts concurrently)."""
        # Use session with maintained connection and multipart concurrency for
        # efficiency.
        with FuturesSession(max_workers=self.max_workers) as session:
            session.mount(
                "https://",
                HTTPAdapter(
                    max_retries=Retry(
                        total=RETRY_TOTAL,
                        backoff_factor=BACKOFF_FACTOR,
                        status_forcelist=STATUS_FORCELIST,
                    )
                ),
            )

            get_response_future = session.get(
                #urljoin(self.files_url, file_id),
                join(self.files_url, file_id),
                headers=self.headers_without_connection_close,
                timeout=self.timeout,
            )

            for response_future in concurrent.futures.as_completed(
                [get_response_future], self.timeout
            ):
                response = response_future.result()
                self._check_response_error(response)

            # File metadata is base for returned fully assembled file.
            file = {**response.json()}

            # Remove metadata fields that are not well-defined for fully assembled file.
            file.pop("last_accessed_rfc3339")
            file.pop("upload_date_rfc3339")

            get_response_futures = [
                session.get(
                    #urljoin(self.files_url, f"{file_id}/contents/{part_number}"),
                    join(self.files_url, f"{file_id}/contents/{part_number}"),
                    headers=self.headers_without_connection_close,
                    timeout=self.timeout,
                )
                for part_number in range(1, file["num_parts"] + 1)
            ]

            # Due to timeout in underlying GET, this should not hang despite no timeout.
            for response_future in concurrent.futures.as_completed(
                get_response_futures
            ):
                response = response_future.result()
                self._check_response_error(response)

            # Unpack in order.
            for response_future in get_response_futures:
                file_part = response_future.result().json()
                # Append to all array fields.
                for file_type, file_type_config in file_part["file_config"].items():
                    if file_type not in file["file_config"]:
                        file["file_config"][file_type] = {}

                    for key, value in file_type_config.items():
                        if key not in file["file_config"][file_type]:
                            file["file_config"][file_type][key] = []

                        file["file_config"][file_type][key] += value

        return file

    @BaseApi.refresh_token
    def submit_job(self, job_body: dict, job_type: str) -> dict:
        """
        Submit a job via a request to QCI public API.

        Args:
            job_body: formatted json body that includes all parameters for the job
            job_type: one of the _supported_job_types

        Returns:
            Response from POST call to API
        """
        self.validate_job_type(job_type=job_type)
        response = self.session.request(
            "POST",
            self.jobs_url,
            json=job_body,
            headers=self.headers,
            timeout=self.timeout,
        )
        self._check_response_error(response=response)
        return response.json()

    @BaseApi.refresh_token
    def get_job_status(self, job_id: str) -> dict:
        """
        Get the status of a job by its ID.

        Args:
            job_id: ID of job

        Returns:
            Response from GET call to API
        """
        response = self.session.request(
            "GET",
            self.get_job_status_url(job_id),
            headers=self.headers,
            timeout=self.timeout,
        )

        self._check_response_error(response=response)
        return response.json()

    @BaseApi.refresh_token
    def get_job_response(self, job_id: str, job_type: str) -> dict:
        """
        Get a response for a job by id and type, which may/may not be finished.

        :param job_id: ID of job
        :param job_type: type of job, one of []

        :return dict: loaded json file
        """
        self.validate_job_type(job_type=job_type)
        response = self.session.request(
            "GET",
            self.get_job_id_url(job_id),
            headers=self.headers,
            timeout=self.timeout,
        )

        self._check_response_error(response=response)
        return response.json()

    def validate_job_type(self, job_type: str) -> None:
        """
        Checks if a provided job type is a supported job type.

        Args:
            job_type: a job type to validate

        Returns:
            None

        Raises AssertionError if job_type is not one of the _supported_job_types.
        """
        if job_type not in self._supported_job_types:
            raise AssertionError(
                f"Provided job_type '{job_type}' is not one of "
                f"{self._supported_job_types}"
            )

    def build_job_body(  # pylint: disable=too-many-arguments
        self,
        job_type: str,
        job_params: dict,
        qubo_file_id: Optional[str] = None,
        graph_file_id: Optional[str] = None,
        hamiltonian_file_id: Optional[str] = None,
        objective_file_id: Optional[str] = None,
        constraints_file_id: Optional[str] = None,
        polynomial_file_id: Optional[str] = None,
        job_name: Optional[str] = None,
        job_tags: Optional[list] = None,
    ) -> dict:
        """
        Constructs body for job submission requests

        Args:
            job_type: one of _supported_job_types
            job_params: dict of params to be passed to job submission in "params" key
            qubo_file_id: file id from files API for uploaded qubo
            graph_file_id: file id from files API for uploaded graph
            hamiltonian_file_id: file id from files API for uploaded hamiltonian
            objective_file_id: file id from files API for uploaded objective
            constraints_file_id: file id from files API for uploaded constraints
            polynomial_file_id: file id from files API for uploaded polynomial
            job_name: user specified name for job submission
            job_tags: user specified labels for classifying and filtering user jobs after submission

        Returns:
            None
        """
        # TODO: Need to add validation for job parameters
        self.validate_job_type(job_type=job_type)

        problem_config = {}
        device_config = {}

        if "sampler_type" not in job_params:
            raise ValueError(
                "Must define sampler_type in job_params (dirac-1, dirac-2, or dirac-3)."
            )

        device_name = job_params['sampler_type']

        # TODO: remove this in the future for now map dirac- to eqc but warn of deprecation
        if "eqc" in device_name:
            print("WARNING: " + device_name + " will be a deprecated sampler type dirac-(1-3) will be the supported sampler types in the future")
            device_name = device_name.replace("eqc", "dirac-")

        # Optional nsamples.
        num_samples = job_params.get("nsamples")

        if num_samples is None:
            # Fallback to checking deprecated fields.
            if "n_samples" in job_params:
                print("WARNING: the key n_samples will be a deprecated parameter in the future, nsamples will be the supported parameter.")
                num_samples = job_params["n_samples"]
            elif "num_samples" in job_params:
                print("WARNING: the key num_samples will be a deprecated parameter in the future, nsamples will be the supported parameter.")
                num_samples = job_params["num_samples"]
            elif "num_solutions" in job_params:
                print("WARNING: the key num_solutions will be a deprecated parameter in the future, nsamples will be the supported parameter.")
                num_samples = job_params["num_solutions"]

        if num_samples is not None:
            # Optional parameter.
            device_config["num_samples"] = num_samples

        if job_type == 'sample-qubo':
            if device_name in ('dirac-2', 'dirac-3'):
                raise ValueError(
                    f"{job_type} not supported on dirac-2 and dirac-3. Consider using "
                    "job_type sample-hamiltonian for dirac-2 and dirac-3."
                )

            problem_name = 'quadratic_unconstrained_binary_optimization'

            if not qubo_file_id:
                raise AssertionError(
                    "qubo_file_id must be specified for job_type='sample-qubo'"
                )

            problem_config["qubo_file_id"] = qubo_file_id
        elif job_type == 'sample-hamiltonian':
            if device_name == 'dirac-2':
                if job_params.get("solution_precision") != 1:
                    problem_name = 'normalized_qudit_hamiltonian_optimization_continuous'
                else:
                    problem_name = 'normalized_qudit_hamiltonian_optimization_integer'
            elif device_name == 'dirac-3':
                problem_name = 'normalized_qudit_hamiltonian_optimization'

                if "relaxation_schedule" in job_params:
                    # Optional parameter.
                    device_config["relaxation_schedule"] = job_params["relaxation_schedule"]

                if "solution_precision" in job_params:
                    # Optional parameter.
                    device_config["solution_precision"] = job_params["solution_precision"]

                if "sum_constraint" in job_params:
                    # Optional parameter.
                    device_config["sum_constraint"] = job_params["sum_constraint"]
            else:
                raise ValueError(f"{job_type} not supported on {device_name}.")

            if (not hamiltonian_file_id and not polynomial_file_id) or \
                (hamiltonian_file_id and polynomial_file_id):
                raise AssertionError(
                    "exactly one of hamiltonian_file_id or polynomial_file_id must be "
                    "specified for job_type='sample-hamiltonian'"
                )

            if hamiltonian_file_id:
                problem_config["hamiltonian_file_id"] = hamiltonian_file_id
            else:
                problem_config["polynomial_file_id"] = polynomial_file_id
        elif job_type == 'sample-hamiltonian-ising':
            if device_name in ('dirac-2', 'dirac-3'):
                raise ValueError(
                    f"{job_type} not supported on dirac-2 and dirac-3. Consider using "
                    "job_type sample-hamiltonian for dirac-2 and dirac-3."
                )

            problem_name = 'ising_hamiltonian_optimization'
            
            if (not hamiltonian_file_id and not polynomial_file_id) or \
                (hamiltonian_file_id and polynomial_file_id):
                raise AssertionError(
                    "exactly one of hamiltonian_file_id or polynomial_file_id must be "
                    "specified for job_type='sample-hamiltonian-ising'"
                )

            if hamiltonian_file_id:
                problem_config["hamiltonian_file_id"] = hamiltonian_file_id
            else:
                problem_config["polynomial_file_id"] = polynomial_file_id
        elif job_type == "sample-constraint":
            if device_name in ('dirac-2', 'dirac-3'):
                raise ValueError(
                    f"{job_type} not supported on dirac-2 and dirac-3. Consider using "
                    "job_type sample-hamiltonian for dirac-2 and dirac-3."
                )

            problem_name = 'quadratic_linearly_constrained_binary_optimization'

            if not constraints_file_id:
                raise AssertionError(
                    "At least constraints_file_id must be specified for "
                    "job_type='sample-constraint'"
                )

            problem_config["constraints_file_id"] = constraints_file_id
            problem_config["objective_file_id"] = objective_file_id  # Optional.

            if "alpha" in job_params:
                # Optional parameter.
                problem_config["alpha"] = job_params["alpha"]

            if "atol" in job_params:
                # Optional parameter.
                problem_config["atol"] = job_params["atol"]
        elif job_type == "graph-partitioning":
            if device_name in ('dirac-2', 'dirac-3'):
                raise ValueError(
                    f"{job_type} not supported on dirac-2 and dirac-3. Consider using "
                    "job_type sample-hamiltonian for dirac-2 and dirac-3."
                )

            problem_name = 'graph_partitioning'

            if not graph_file_id:
                raise AssertionError(
                    "graph_file_id must be specified for the given "
                    "job_type='graph-partitioning'"
                )

            problem_config["graph_file_id"] = graph_file_id

            if "num_paritions" in job_params:
                # Optional parameter.
                problem_config["num_paritions"] = job_params["num_paritions"]

            if "alpha" in job_params:
                # Optional parameter.
                problem_config["alpha"] = job_params["alpha"]

            if "gamma" in job_params:
                # Optional parameter when num_paritions > 2.
                problem_config["gamma"] = job_params["gamma"]
        else:
            raise ValueError(f"Unsupported job_type '{job_type}'.")

        job_submission = {
            "problem_config": {problem_name: problem_config},
            "device_config": {device_name: device_config},
        }

        if job_name is not None:
            # Optional field.
            job_submission["job_name"] = job_name

        if job_tags is not None:
            # Optional field.
            job_submission["job_tags"] = job_tags

        return {"job_submission": job_submission}

    def print_job_log(self, message: str) -> None:
        """
        Formats a messages for updating user with a time stamp appended
        :param message: a string to be passed in print statement
        """
        print(f"{message}: {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}")

    def process_job(self, job_type: str, job_body: dict, wait: bool = True) -> dict:
        """
        :param job_type: the type of job being processed must be one of _supported_job_types
        :param job_body: formatted json dict for body of job submission request
        :param wait: bool indicating whether or not user wants to wait for job to complete

        :return:
            if wait is True, then dict with job_info response and results file
                (results is None if ERRORED or CANCELLED)
            if wait is False, then response dict from submitted job, which includes job
                ID for subsequent retrieval
        :note: what else do we want to return with the results? response_id, obviously job_id
        """
        self.validate_job_type(job_type=job_type)

        allocations_response = self.session.request(
            "GET",
            self.get_job_allocations_url(),
            headers=self.headers,
            timeout=self.timeout,
        ).json()
        dirac_allocation = allocations_response['allocations']['dirac']['seconds']
    
        if allocations_response['allocations']['dirac']['metered']:
            print(f"Dirac allocation balance = {dirac_allocation} s")
        else:
            print(f"Dirac allocation balance = {dirac_allocation} s (unmetered)")
    
        submit_response = self.submit_job(job_body=job_body, job_type=job_type)
        job_id = submit_response["job_id"]
        self.print_job_log(message=f"Job submitted job_id='{job_id}'-")

        if wait:
            curr_status = ""
            while curr_status not in FINAL_STATUSES:
                time.sleep(1)
                iter_status = self.get_job_status(job_id=job_id)["status"]

                if iter_status != curr_status:
                    self.print_job_log(message=iter_status)
                    curr_status = iter_status

            job_response = self.get_job_response(job_id=job_id, job_type=job_type)
            job_response['details'] = {'status': curr_status}

            if curr_status in [JobStatus.CANCELLED, JobStatus.ERRORED]:
                results = None
            else:
                results = self.download_file(file_id=job_response["job_result"]["file_id"])

            allocations_response = self.session.request(
                "GET",
                self.get_job_allocations_url(),
                headers=self.headers,
                timeout=self.timeout,
            ).json()
            dirac_allocation = allocations_response['allocations']['dirac']['seconds']
        
            if allocations_response['allocations']['dirac']['metered']:
                print(f"Dirac allocation balance = {dirac_allocation} s")
            else:
                print(f"Dirac allocation balance = {dirac_allocation} s (unmetered)")

            return {"job_info": job_response, "results": results}

        return submit_response

    @BaseApi.refresh_token
    def list_files(self, username: Optional[str] = None) -> dict:
        """
        :param username: Optional str - username (to search for files owned by the named user)
            mostly useful when run by users with administrator privileges (such as QCI users) who can see all files.
            When called by an administrator, the username parameter is used to restrict the list files returned
            to be only the files owned by the user specified in the username parameter.
            When run by non-privileged users, this parameter is truly optional because non-privileged users
            will only ever see lists of files that they created.

        :return: dict containing list of files
        """
        if username:
            querystring = {"regname": "username", "regvalue": username}

            response = self.session.request(
                "GET",
                self.files_url,
                headers=self.headers,
                params=querystring,
                timeout=self.timeout,
            )
        else:
            response = self.session.request(
                "GET",
                self.files_url,
                headers=self.headers,
                timeout=self.timeout,
            )

        self._check_response_error(response=response)
        return response.json()

    @BaseApi.refresh_token
    def delete_file(self, file_id: str) -> dict:
        """
        :param file_id: str - file_id of file to be deleted

        :return: dict containing information about file deleted (or error)
        """

        if self.debug:
            print(f"Deleting file with ID {file_id}...")

        start_time_s = time.perf_counter()

        response = self.session.request(
            "DELETE",
            self.get_file_id_url(file_id),
            headers=self.headers,
            timeout=self.timeout,
        )

        stop_time_s = time.perf_counter()

        if self.debug:
            print(f"Deleting file with ID {file_id}...done.")
            print(f"\tElapsed time: {stop_time_s - start_time_s} s.")

        self._check_response_error(response=response)

        return response.json()

    @BaseApi.refresh_token
    def zip_payload(self, payload: str) -> bytes:
        """
        Zip contents of json file

        Args:
            payload: str - json contents of file to be zipped

        Returns:
            zipped request_body
        """
        out = BytesIO()
        with gzip.GzipFile(fileobj=out, mode="w", compresslevel=6) as file:
            file.write(json.dumps(payload).encode("utf-8"))
        request_body = out.getvalue()
        out.close()
        return request_body

    def get_job_type_from_job_id(self, job_id: str) -> str:
        """
        Get job type from job ID.

        Args:
            job_id: ID of the job

        Returns:
            Type of the job
        """
        response_job_metadata_short = self.session.request(
            "GET",
            self.get_job_id_url(job_id),
            headers=self.headers,
            timeout=self.timeout,
        )
        self._check_response_error(response=response_job_metadata_short)

        return response_job_metadata_short.json()["type"].replace("_", "-")
