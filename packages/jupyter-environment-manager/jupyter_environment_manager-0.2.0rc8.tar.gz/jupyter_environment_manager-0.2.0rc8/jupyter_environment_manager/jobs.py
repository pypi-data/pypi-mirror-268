# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Handlers for carrying out quantum jobs actions (enable, disable, etc.)

"""
import json
import logging
import threading
from pathlib import Path
from typing import Dict, Tuple, Union

import tornado
from notebook.base.handlers import APIHandler
from qbraid_core.services.environments import get_env_path, update_install_status, which_python
from qbraid_core.services.quantum import quantum_lib_proxy_state
from qbraid_core.services.quantum.proxy_braket import add_braket, disable_braket, enable_braket

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def quantum_jobs_supported_enabled(slug: str) -> Tuple[bool, bool]:
    """Checks if quantum jobs are enabled in environment"""
    slug_path = get_env_path(slug)
    state = quantum_lib_proxy_state("braket", is_default_python=False, slug_path=slug_path)
    supported = state.get("supported", False)
    enabled = state.get("enabled", False)
    return supported, enabled


class QuantumJobsHandler(APIHandler):
    """Handler for quantum jobs actions."""

    @tornado.web.authenticated
    def get(self):
        """Gets quantum jobs status of environment."""
        slug = self.get_query_argument("slug")
        supported, enabled = quantum_jobs_supported_enabled(slug)
        status = {"supported": int(supported), "enabled": int(enabled)}
        self.finish(json.dumps(status))

    @tornado.web.authenticated
    def put(self):
        """Enable/disable quantum jobs in environment."""
        input_data = self.get_json_body()
        slug = input_data.get("slug")
        action = input_data.get("action")  # enable or disable
        slug_path = get_env_path(slug)
        update_install_status(slug_path, 0, 0)
        thread = threading.Thread(
            target=self.toggle_quantum_jobs,
            args=(
                action,
                slug,
                slug_path,
            ),
        )
        thread.start()

        data = {"success": True, "stdout": f"{action[:-1]}ing quantum jobs", "stderr": ""}
        self.finish(json.dumps(data))

    def toggle_quantum_jobs(
        self, action: str, slug: str, slug_path: Path
    ) -> Dict[str, Union[int, str]]:
        """
        Toggles quantum jobs functionality using subprocess.

        Args:
            action (str): The action to perform ('enable' or 'disable').
            slug (str): Identifier for the quantum job setting.

        Returns:
            dict: A dictionary with keys 'success' (0 or 1), 'stdout', and 'stderr'.
        """
        try:
            _, enabled_in = quantum_jobs_supported_enabled(slug)
            python_exe = which_python(slug)
            success = False
            message = ""

            # Check if action is valid
            if action not in ["enable", "disable"]:
                message = "Invalid quantum jobs action. Must be 'enable' or 'disable'."

            # Check if action is necessary
            elif (action == "enable" and enabled_in) or (action == "disable" and not enabled_in):
                message = f"Quantum jobs are already {action}d."
                success = True

            # Perform the action
            else:
                if action == "enable":
                    enable_braket(python_exe)
                elif action == "disable":
                    disable_braket(python_exe)

                _, enabled_out = quantum_jobs_supported_enabled(slug)
                success = enabled_in != enabled_out
                if success:
                    message = f"Successfully {action}d Amazon Braket quantum jobs."
                else:
                    message = f"Failed to {action} Amazon Braket quantum jobs."

            update_install_status(slug_path, int(success), 1, message=message)
        except Exception as err:  # pylint: disable=broad-exception-caught
            update_install_status(slug_path, 0, 1, message=err)

    @tornado.web.authenticated
    def post(self):
        """Adds quantum jobs functionality to environment."""
        input_data = self.get_json_body()
        slug = input_data.get("slug")
        slug_path = get_env_path(slug)
        update_install_status(slug_path, 0, 0)
        thread = threading.Thread(
            target=self.add_quantum_jobs,
            args=(
                slug,
                slug_path,
            ),
        )
        thread.start()

        data = {"success": True, "stdout": "Adding quantum jobs", "stderr": ""}
        self.finish(json.dumps(data))

    def add_quantum_jobs(self, slug: str, slug_path: Path) -> Dict[str, Union[int, str]]:
        """Adds quantum jobs functionality using subprocess."""
        try:
            python_exe = which_python(slug)
            add_braket(python_exe)

            _, enabled = quantum_jobs_supported_enabled(slug)

            if enabled:
                message = "Successfully added Amazon Braket quantum jobs."
            else:
                message = "Failed to add Amazon Braket quantum jobs."

            update_install_status(slug_path, int(enabled), 1, message=message)
        except Exception as err:  # pylint: disable=broad-exception-caught
            update_install_status(slug_path, 0, 1, message=err)
