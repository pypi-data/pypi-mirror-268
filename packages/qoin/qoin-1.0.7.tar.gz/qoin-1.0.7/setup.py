# Qoin provides random number generation using quantum computing.
# Copyright (C) 2024  Amir Ali Malekani Nezhad

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import codecs
import os
from setuptools import setup, find_packages # type: ignore


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.7'
DESCRIPTION = 'Quantum Random Number Generator.'
LONG_DESCRIPTION = '`qoin` is the analogue of `random` package implemented through \
gate-based quantum computing.'

# Setting up
setup(
    name="qoin",
    version=VERSION,
    author="Amir Ali Malekani Nezhad",
    author_email="<amiralimlk07@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'qiskit', 'qiskit_aer'],
    keywords=['quantum computing', 'quantum random number generator', 'random',
              'qrandom', 'qoin'],
    classifiers=[
        "Development Status :: DONE",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)