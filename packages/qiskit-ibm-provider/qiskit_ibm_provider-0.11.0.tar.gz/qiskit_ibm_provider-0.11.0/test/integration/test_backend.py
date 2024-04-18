# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""IBMBackend Test."""

from unittest import mock, skip
from unittest.mock import patch

from qiskit import QuantumCircuit, transpile
from qiskit.providers.models import QasmBackendConfiguration
from qiskit.providers.exceptions import QiskitBackendNotFoundError

from qiskit_ibm_provider import IBMBackend, IBMProvider
from qiskit_ibm_provider.ibm_qubit_properties import IBMQubitProperties
from qiskit_ibm_provider.exceptions import IBMBackendValueError

from ..decorators import (
    IntegrationTestDependencies,
    integration_test_setup_with_backend,
    production_only,
)
from ..ibm_test_case import IBMTestCase
from ..utils import bell


class TestIBMBackend(IBMTestCase):
    """Test ibm_backend module."""

    @classmethod
    @integration_test_setup_with_backend(simulator=False, min_num_qubits=2)
    def setUpClass(
        cls, backend: IBMBackend, dependencies: IntegrationTestDependencies
    ) -> None:
        """Initial class level setup."""
        # pylint: disable=arguments-differ
        super().setUpClass()
        cls.backend = backend
        cls.dependencies = dependencies

    def test_backend_pending_jobs(self):
        """Test pending jobs are returned."""
        backends = self.dependencies.provider.backends()
        self.assertTrue(any(backend.status().pending_jobs > 0 for backend in backends))

    def test_backend_status(self):
        """Check the status of a backend."""
        self.dependencies.provider.backends()
        self.assertTrue(self.backend.status().operational)

    @production_only
    def test_backend_properties(self):
        """Check the properties of calibration of a real chip."""
        self.assertIsNotNone(self.backend.properties())

    def test_backend_fetch_one_qubit_property(self):
        """Check retrieving properties of qubit 0"""
        qubit_properties = self.backend.qubit_properties(0)
        self.assertIsInstance(qubit_properties, IBMQubitProperties)

    def test_backend_fetch_all_qubit_properties(self):
        """Check retrieving properties of all qubits"""
        num_qubits = self.backend.num_qubits
        qubits = list(range(num_qubits))
        qubit_properties = self.backend.qubit_properties(qubits)
        self.assertEqual(len(qubit_properties), num_qubits)
        for i in qubits:
            self.assertIsInstance(qubit_properties[i], IBMQubitProperties)

    @skip("until terra #9092 is resolved")
    def test_backend_pulse_defaults(self):
        """Check the backend pulse defaults of each backend."""
        provider = self.backend.provider
        for backend in provider.backends():
            with self.subTest(backend_name=backend.name):
                defaults = backend.defaults()
                if backend.configuration().open_pulse:
                    self.assertIsNotNone(defaults)

    def test_sim_backend_options(self):
        """Test simulator backend options."""
        provider: IBMProvider = self.backend.provider
        backend = provider.get_backend("ibmq_qasm_simulator")
        backend.options.shots = 2048
        backend.set_options(memory=True)
        job = backend.run(bell(), shots=1024, foo="foo")
        backend_options = provider.backend.retrieve_job(job.job_id()).backend_options()
        self.assertEqual(backend_options["shots"], 1024)
        self.assertTrue(backend_options["memory"])
        self.assertEqual(backend_options["foo"], "foo")

    @production_only
    def test_paused_backend_warning(self):
        """Test that a warning is given when running jobs on a paused backend."""
        backend = self.dependencies.provider.get_backend("ibmq_qasm_simulator")
        paused_status = backend.status()
        paused_status.status_msg = "internal"
        backend.status = mock.MagicMock(return_value=paused_status)
        with self.assertWarns(Warning):
            backend.run(bell())

    def test_deprecate_id_instruction(self):
        """Test replacement of 'id' Instructions with 'Delay' instructions."""

        circuit_with_id = QuantumCircuit(2)
        circuit_with_id.id(0)
        circuit_with_id.id(0)
        circuit_with_id.id(1)

        config = QasmBackendConfiguration(
            basis_gates=["id"],
            supported_instructions=["delay"],
            dt=0.25,
            backend_name="test",
            backend_version="0.0",
            n_qubits=1,
            gates=[],
            local=False,
            simulator=False,
            conditional=False,
            open_pulse=False,
            memory=False,
            max_shots=1,
            coupling_map=[],
        )

        with patch.object(self.backend, "configuration", return_value=config):
            with self.assertWarnsRegex(DeprecationWarning, r"'id' instruction"):
                mutated_circuit = self.backend._deprecate_id_instruction(
                    [circuit_with_id]
                )
            self.assertEqual(mutated_circuit[0].count_ops(), {"delay": 3})
            self.assertEqual(circuit_with_id.count_ops(), {"id": 3})

    @skip("This is a Terra issue and test. Not related to Provider.")
    def test_transpile_converts_id(self):
        """Test that when targeting an IBM backend id is translated to delay."""
        circ = QuantumCircuit(2)
        circ.id(0)
        circ.id(1)
        tqc = transpile(circ, self.backend)
        op_counts = tqc.count_ops()
        self.assertNotIn("id", op_counts)
        self.assertIn("delay", op_counts)

    def test_backend_wrong_instance(self):
        """Test that an error is raised when retrieving a backend not in the instance."""
        backends = self.dependencies.provider.backends()
        hgps = self.dependencies.provider._hgps.values()
        if len(hgps) >= 2:
            for hgp in hgps:
                backend_names = list(hgp._backends)
                for backend in backends:
                    if backend.name not in backend_names:
                        with self.assertRaises(QiskitBackendNotFoundError):
                            self.dependencies.provider.get_backend(
                                backend.name,
                                instance=f"{hgp._hub}/{hgp._group}/{hgp._project}",
                            )
                        return

    def test_retrieve_backend_not_exist(self):
        """Test that an error is raised when retrieving a backend that does not exist."""
        with self.assertRaises(QiskitBackendNotFoundError):
            self.dependencies.provider.get_backend("nonexistent_backend")

    def test_too_many_qubits_in_circuit(self):
        """Check error message if circuit contains more qubits than supported on the backend."""
        num = len(self.backend.properties().qubits)
        num_qubits = num + 1
        circuit = QuantumCircuit(num_qubits, num_qubits)
        with self.assertRaises(IBMBackendValueError) as err:
            _ = self.backend.run(circuit)
        self.assertIn(
            f"Circuit contains {num_qubits} qubits, but backend has only {num}.",
            str(err.exception),
        )

    def test_job_backend_properties(self):
        """Test job backend properties."""
        job = self.backend.run(bell())
        backend_version = self.backend.properties().backend_version
        job_version = job.properties().backend_version
        self.assertEqual(job_version, backend_version)
