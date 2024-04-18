# -*- coding: utf-8 -*-

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

"""Setup qiskit_ibm_provider"""

import os

import setuptools

REQUIREMENTS = [
    "qiskit>=0.45.0",
    "requests>=2.19",
    "requests-ntlm>=1.1.0",
    "numpy>=1.13",
    "urllib3>=1.21.1",
    "python-dateutil>=2.8.0",
    "websocket-client>=1.5.1",
    "websockets>=10.0",
    "typing_extensions>=4.3",
]

# Handle version.
VERSION_PATH = os.path.join(
    os.path.dirname(__file__), "qiskit_ibm_provider", "VERSION.txt"
)
with open(VERSION_PATH, "r") as version_file:
    VERSION = version_file.read().strip()

# Read long description from README.
README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
with open(README_PATH) as readme_file:
    README = readme_file.read()


setuptools.setup(
    name="qiskit-ibm-provider",
    version=VERSION,
    description="Qiskit IBM Quantum Provider for accessing the quantum devices and "
    "simulators at IBM",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Qiskit/qiskit-ibm-provider",
    author="Qiskit Development Team",
    author_email="qiskit@us.ibm.com",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit, quantum",
    packages=setuptools.find_packages(exclude=["test*"]),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    python_requires=">=3.8",
    zip_safe=False,
    extras_require={
        "visualization": [
            "matplotlib>=2.1",
            "ipywidgets<8.0.0",
            "seaborn>=0.9.0",
            "plotly>=4.4",
            "ipyvuetify>=1.1",
            "pyperclip>=1.7",
            "ipython>=5.0.0",
            "traitlets!=5.0.5",
            "ipyvue>=1.8.5",
        ]
    },
    project_urls={
        "Bug Tracker": "https://github.com/Qiskit/qiskit-ibm-provider/issues",
        "Documentation": "https://docs.quantum.ibm.com/api/qiskit-ibm-provider/",
        "Source Code": "https://github.com/Qiskit/qiskit-ibm-provider",
    },
    entry_points={
        "qiskit.transpiler.translation": [
            "ibm_backend = qiskit_ibm_provider.transpiler.plugin:IBMTranslationPlugin",
            "ibm_dynamic_circuits = qiskit_ibm_provider.transpiler.plugin:IBMDynamicTranslationPlugin",
        ]
    },
)
