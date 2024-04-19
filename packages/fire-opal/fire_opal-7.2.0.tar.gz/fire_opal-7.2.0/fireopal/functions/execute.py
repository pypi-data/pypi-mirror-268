# Copyright 2024 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

from __future__ import annotations

import logging
from typing import Optional

from qctrlcommons.exceptions import QctrlArgumentsValueError

from fireopal._utils import log_activity
from fireopal.config import get_config
from fireopal.credentials import Credentials

from .base import fire_opal_workflow


@fire_opal_workflow("compile_and_run_workflow")
def execute(
    circuits: str | list[str],
    shot_count: int,
    credentials: Credentials,
    backend_name: str,
) -> dict:
    """
    Execute a batch of `circuits` where `shot_count` measurements are taken per circuit.

    Parameters
    ----------
    circuits : str or list[str]
        Quantum circuit(s) in the form of a QASM strings. You may use Qiskit to
        generate these strings.
    shot_count : int
        Number of bitstrings that are sampled from the final quantum state.
    credentials : Credentials
        The credentials for running circuits. See the `credentials` module for functions
        to generate credentials for your desired provider.
    backend_name : str
        The backend device name that should be used to run circuits.

    Returns
    -------
    dict
        A dictionary containing probability mass functions and warnings.
    """
    log_activity(
        function_called="execute",
        circuits=circuits,
        shot_count=shot_count,
        backend_name=backend_name,
    )

    _check_execute_validity(
        circuits=circuits,
        shot_count=shot_count,
        credentials=credentials,
        backend_name=backend_name,
    )
    circuits = _handle_single_circuit(circuits)

    settings = get_config()
    credentials_with_org = credentials.copy()
    credentials_with_org.update({"organization": settings.organization})
    return {
        "circuits": circuits,
        "shot_count": shot_count,
        "credentials": credentials_with_org,
        "backend_name": backend_name,
    }


def _handle_single_circuit(strings: str | list[str]) -> list[str]:
    """
    Convert a single string to a list holding containing it, if applicable.

    Parameters
    ----------
    strings : str or list[str]
        One or more strings.

    Returns
    -------
    list[str]
        The input if originally provided as a list. Otherwise, the input string in
        a list.
    """
    if isinstance(strings, str):
        return [strings]
    return strings


def _check_single_circuit_validity(
    circuit: str, circuit_index: Optional[int] = None
) -> None:
    """
    Validate that circuits are of type string as well as nonempty.
    Parameters
    ----------
    circuit : str
        The input circuit
    circuit_index : int, optional
        The index of the circuit if the input is a list. Defaults to None.
    """

    extras = {"circuit_index": circuit_index} if circuit_index is not None else None
    if not isinstance(circuit, str):
        logging.error(
            "QCTRL - Invalid type received for circuits input. The circuit must be a string."
        )
        raise QctrlArgumentsValueError(
            "Invalid type received for circuits input. The circuit must be a string.",
            arguments={"circuits": circuit},
            extras=extras,
        )
    if not circuit:
        logging.error("QCTRL - The circuit string provided must be non-empty.")
        raise QctrlArgumentsValueError(
            "The circuit string provided must be non-empty.",
            arguments={"circuits": circuit},
            extras=extras,
        )


def _check_execute_validity(
    circuits: str | list[str],
    shot_count: int,
    credentials: Credentials,
    backend_name: str,
) -> None:
    """
    Check if the inputs are valid for execute function.

    Parameters
    ----------
    circuits : str or list[str]
        Quantum circuit(s) in the form of a QASM strings. You may use Qiskit to
        generate these strings. This list or string must be non-empty.
    shot_count : int
        Number of bitstrings that are sampled from the final quantum state.
    credentials : Credentials
        The credentials for running circuits. See the `credentials` module for functions
        to generate credentials for your desired provider.
    backend_name : str
        The backend device name that should be used to run circuits.
    """

    if isinstance(circuits, list):
        if not all(isinstance(circuit, str) for circuit in circuits):
            logging.error(
                "QCTRL - Invalid type received for circuits input. All circuits must be strings."
            )
            raise QctrlArgumentsValueError(
                "Invalid type received for circuits input. All circuits must be strings.",
                arguments={"circuits": circuits},
            )
        if len(circuits) == 0:
            logging.error("QCTRL - The list of circuits must be non-empty.")
            raise QctrlArgumentsValueError(
                "The list of circuits must be non-empty.",
                arguments={"circuits": circuits},
            )
        for index, circuit in enumerate(circuits):
            _check_single_circuit_validity(circuit=circuit, circuit_index=index)
    else:
        _check_single_circuit_validity(circuit=circuits)
    if not isinstance(shot_count, int):
        logging.error(
            "QCTRL - Invalid type received for shot_count input. The shot_count must be an integer."
        )
        raise QctrlArgumentsValueError(
            "Invalid type received for shot_count input. The shot_count must be an integer.",
            arguments={"shot_count": shot_count},
        )
    if not isinstance(credentials, dict):
        logging.error(
            "QCTRL - Invalid type received for credentials input. "
            "The credentials must be a dictionary."
        )
        raise QctrlArgumentsValueError(
            "Invalid type received for credentials input. The credentials must be a dictionary.",
            arguments={
                "credentials": credentials,
                "credentials type": type(credentials),
            },
        )
    if not isinstance(backend_name, str):
        logging.error(
            "QCTRL - Invalid type received for backend_name input. "
            "The backend_name must be a string."
        )
        raise QctrlArgumentsValueError(
            "Invalid type received for backend_name input. The backend_name must be a string.",
            arguments={"backend_name": backend_name},
        )
