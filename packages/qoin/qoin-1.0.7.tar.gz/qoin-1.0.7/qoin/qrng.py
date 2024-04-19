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

from __future__ import annotations

__all__ = ['QRNG']

from collections.abc import MutableSequence
from typing import Any
import math

# Import `Qiskit` modules
from qiskit import QuantumCircuit # type: ignore
from qiskit.primitives import BackendSampler # type: ignore
from qiskit_aer.aerprovider import AerSimulator # type: ignore


class QRNG:
    """ `QRNG` class provides random number generation using quantum computing.
    """
    def __init__(self) -> None:
        """ Initialize a `QRNG` instance.
        """
        self._backend = BackendSampler(AerSimulator())

    def randint(self,
                lowerbound: int,
                upperbound: int) -> int:
        """ Generate a random integer from [lowerbound, upperbound).

        Parameters
        ----------
        `lowerbound` : int
            The lowerbound of the selection.
        `upperbound` : int
            The upperbound of the selection.

        Returns
        -------
        `return_int` : int
            The random number generated from the selection.

        Raises
        ------
        TypeError
            If the lowerbound and upperbound are not integers.
        ValueError
            If the upperbound is less than the lowerbound.

        Notes
        -----
        The random integer is generated using the quantum circuit. The quantum
        circuit generates a uniform distribution over all possible integers
        between the lowerbound and upperbound. The distribution is then
        measured to extract the random integer.

        The random integer is generated using the following steps:

        1. Calculate the difference between the upperbound and lowerbound.
        2. Scale the difference to the closest power of 2.
        3. Calculate the number of qubits needed to represent the selection.
        4. Create a uniform distribution over all possible integers.
        5. Apply measurement to the distribution.
        6. Extract the quasi-probability distribution from the result.
        7. Convert the quasi-probability distribution to counts.
        8. Postprocess the measurement result.
        9. Scale the integer back.
        10. Shift range from [0;upperbound-lowerbound-1] to [lowerbound;upperbound-1].
        11. Return the random integer.

        Usage
        -----
        >>> random_integer = qrng.randint(0, 10)
        >>> type_checker = isinstance(random_integer, int)
        >>> bound_checker = random_integer < 10 and random_integer >= 0
        >>> type_checker and bound_checker
        True
        >>> qrng.randint(5.5, 10)
        Traceback (most recent call last):
            ...
        TypeError: Lowerbound and upperbound must be integers.
        >>> qrng.randint(10, 5)
        Traceback (most recent call last):
            ...
        ValueError: Upperbound must be greater than lowerbound.
        """
        # Ensure that the lowerbound and upperbound are integers
        if not (isinstance(lowerbound, int) and isinstance(upperbound, int)):
            raise TypeError("Lowerbound and upperbound must be integers.")

        # Ensure that the upperbound is greater than the lowerbound
        if upperbound < lowerbound:
            raise ValueError("Upperbound must be greater than lowerbound.")

        # Define delta (difference between upperbound and lowerbound)
        delta = upperbound - lowerbound

        # Scale delta to the closest power of 2
        scale = delta/2 ** math.ceil(math.log2(delta))
        delta = int(delta/scale)

        # Calculate the number of qubits needed to represent the selection
        num_qubits = math.ceil(math.log2(delta))

        # Define the circuit
        circuit = QuantumCircuit(num_qubits, num_qubits)

        # Create a uniform distribution over all possible integers
        circuit.h(range(num_qubits))

        # Apply measurement
        circuit.measure(range(num_qubits), range(num_qubits))

        # Run the circuit
        result = self._backend.run(circuit, shots=1).result()

        # Extract the quasi-probability distribution from the first result
        quasi_dist = result.quasi_dists[0]

        # Convert the quasi-probability distribution to counts
        counts = {bin(k)[2:].zfill(num_qubits): int(v * 1)
                  for k, v in quasi_dist.items()}

        # Sort the counts by their keys (basis states)
        counts = dict(sorted(counts.items()))

        # Postprocess measurement result
        random_int = int(list(counts.keys())[0], 2)

        # Scale the integer back
        random_int = int(random_int*scale)

        # shift random integer's range from [0;upperbound-lowerbound-1]
        # to [lowerbound;upperbound-1]
        random_int += lowerbound

        # Return random integer
        return random_int

    def randbin(self) -> bool:
        """ Generate a random boolean.

        Returns
        -------
        `random_bin` : bool
            The random boolean.

        Notes
        -----
        The random boolean is generated using the quantum circuit. The quantum
        circuit generates a uniform distribution over all possible booleans.
        The distribution is then measured to extract the random boolean.

        The random boolean is generated using the following steps:

        1. Create a uniform distribution over all possible booleans.
        2. Apply measurement to the distribution.
        3. Extract the quasi-probability distribution from the result.
        4. Convert the quasi-probability distribution to counts.
        5. Postprocess the measurement result.
        6. Return the random boolean.

        Examples
        --------
        >>> random_bool = qrng.randbin()
        >>> type_checker = isinstance(random_bool, bool)
        >>> bound_checker = random_bool == True or random_bool == False
        >>> type_checker and bound_checker
        True
        """
        return bool(self.randint(0, 2))

    def random(self,
               num_digits: int) -> float:
        """ Generate a random float between 0 and 1.

        Parameters
        ----------
        `num_digits` : int
            The number of bits used to represent the angle divider.

        Returns
        -------
        `random_float` : float
            The random generated float.

        Raises
        ------
        TypeError
            If the number of digits is not an integer.
        ValueError
            If the number of digits is less than or equal to 0.

        Notes
        -----
        The random float is generated using the quantum circuit. The quantum
        circuit generates a uniform distribution over all possible floats
        between 0 and 1. The distribution is then measured to extract the
        random float.

        The random float is generated using the following steps:

        1. Calculate the number of bits used to represent the angle divider.
        2. Create a uniform distribution over all possible floats.
        3. Apply measurement to the distribution.
        4. Extract the quasi-probability distribution from the result.
        5. Convert the quasi-probability distribution to counts.
        6. Postprocess the measurement result.
        7. Return the random float.

        Examples
        --------
        >>> random_float = qrng.random(5)
        >>> type_checker = isinstance(random_float, float)
        >>> bound_checker = random_float < 1 and random_float >= 0
        >>> bound_checker = bound_checker and len(str(random_float)) == 7
        >>> type_checker and bound_checker
        True
        >>> qrng.random(3.2)
        Traceback (most recent call last):
            ...
        TypeError: Number of digits must be an integer.
        >>> qrng.random(0)
        Traceback (most recent call last):
            ...
        ValueError: Number of digits must be greater than 0.
        """
        # Ensure that the number of digits is an integer
        if not isinstance(num_digits, int):
            raise TypeError("Number of digits must be an integer.")

        # Ensure that the number of digits is valid
        if num_digits <= 0:
            raise ValueError("Number of digits must be greater than 0.")

        # Initialize the digit
        random_float = "0."

        for _ in range(num_digits):
            # Generate a random integer between 0 and 9
            random_float += str(self.randint(0, 9))

        # Return the random float
        return float(random_float)

    def choice(self,
               items: MutableSequence[Any]) -> Any:
        """ Choose a random element from the list of items.

        Parameters
        ----------
        `items` : MutableSequence[Any]
            The list of items.

        Returns
        -------
        Any
            The item selected.

        Raises
        ------
        TypeError
            If the items are not an instance of MutableSequence.

        Notes
        -----
        The random element is selected using the quantum circuit. The quantum
        circuit generates a uniform distribution over all possible elements in
        the list. The distribution is then measured to extract the random
        element.

        The random element is selected using the following steps:

        1. Create a uniform distribution over all possible elements.
        2. Apply measurement to the distribution.
        3. Extract the quasi-probability distribution from the result.
        4. Convert the quasi-probability distribution to counts.
        5. Postprocess the measurement result.
        6. Return the random element.

        Examples
        --------
        >>> random_choice = qrng.choice([1, 2, 3, 4, 5])
        >>> random_choice in [1, 2, 3, 4, 5]
        True
        >>> qrng.choice(1)
        Traceback (most recent call last):
            ...
        TypeError: Population must be a MutableSequence.
        """
        # Ensure that the items are MutableSequence
        if not isinstance(items, MutableSequence):
            raise TypeError("Population must be a MutableSequence.")

        return items[self.randint(0, len(items))]

    def choices(self,
                items: MutableSequence[Any],
                num_selections: int) -> Any | list[Any]:
        """ Choose random element(s) from the list of items.

        Parameters
        ----------
        `items` : MutableSequence[Any]
            The list of items.
        `num_selections` : int
            The number of selections.

        Returns
        -------
        Any | list[Any]
            The item(s) selected.

        Raises
        ------
        TypeError
            If the items are not MutableSequence.
        ValueError
            If the number of selections is less than or equal to 0.

        Notes
        -----
        The random element(s) are selected using the quantum circuit. The
        quantum circuit generates a uniform distribution over all possible
        elements in the list. The distribution is then measured to extract the
        random element(s).

        The random element(s) are selected using the following steps:

        1. Calculate the number of selections.
        2. Create a uniform distribution over all possible elements.
        3. Apply measurement to the distribution.
        4. Extract the quasi-probability distribution from the result.
        5. Convert the quasi-probability distribution to counts.
        6. Postprocess the measurement result.
        7. Return the random element(s).

        Examples
        --------
        >>> random_choices = qrng.choices([1, 2, 3, 4, 5], 3)
        >>> all(random_choice in [1, 2, 3, 4, 5] for random_choice in random_choices)
        True
        >>> qrng.choices(1, 3)
        Traceback (most recent call last):
            ...
        TypeError: Population must be a MutableSequence.
        >>> qrng.choices([1, 2, 3, 4, 5], 0)
        Traceback (most recent call last):
            ...
        ValueError: Sample larger than population or is negative.
        """
        # Ensure that the items are MutableSequence
        if not isinstance(items, MutableSequence):
            raise TypeError("Population must be a MutableSequence.")

        # Ensure that the number of selections is valid
        if num_selections <= 0:
            raise ValueError("Sample larger than population or is negative.")

        # Define indices list
        indices = []

        # If number of selections is 1, run `.choice` instead
        if num_selections == 1:
            return self.choice(items)

        # Generate the random indices
        indices = [self.randint(0, len(items)) for _ in range(num_selections)]

        # Return the selections
        return [items[i] for i in indices]

    def sample(self,
               items: MutableSequence[Any],
               num_selections: int) -> Any | list[Any]:
        """ Choose random element(s) from the list of items.

        Parameters
        ----------
        `items` : MutableSequence[Any]
            The list of items.
        `num_selections` : int
            The number of selections.

        Returns
        -------
        Any | list[Any]
            The item(s) selected.

        Raises
        ------
        TypeError
            If the items are not MutableSequence.
        ValueError
            If the number of selections is less than or equal to 0.

        Notes
        -----
        The random element(s) are selected using the quantum circuit. The
        quantum circuit generates a uniform distribution over all possible
        elements in the list. The distribution is then measured to extract the
        random element(s).

        The random element(s) are selected using the following steps:

        1. Calculate the number of selections.
        2. Create a uniform distribution over all possible elements.
        3. Apply measurement to the distribution.
        4. Extract the quasi-probability distribution from the result.
        5. Convert the quasi-probability distribution to counts.
        6. Postprocess the measurement result.
        7. Return the random element(s).

        Examples
        --------
        >>> random_samples = qrng.sample([1, 2, 3, 4, 5], 3)
        >>> bound_checker = all(random_sample in [1, 2, 3, 4, 5]
        ... for random_sample in random_samples)
        >>> unique_checker = len(set(random_samples)) == 3
        >>> bound_checker and unique_checker
        True
        >>> qrng.sample(1, 3)
        Traceback (most recent call last):
            ...
        TypeError: Population must be a MutableSequence.
        >>> qrng.sample([1, 2, 3, 4, 5], 6)
        Traceback (most recent call last):
            ...
        ValueError: Sample larger than population or is negative.
        """
        if not isinstance(items, MutableSequence):
            raise TypeError("Population must be a MutableSequence.")

        # Ensure that the number of selections is valid
        if not (num_selections > 0 and num_selections <= len(items)):
            raise ValueError("Sample larger than population or is negative.")

        # Define indices list
        indices: list[Any] = []

        # If number of selections is 1, run `.choice` instead
        if num_selections == 1:
            return self.choice(items)

        while True:
            # If the number of selections is met, break the loop
            if len(indices) == num_selections:
                break

            # Generate a random index
            random_index = self.randint(0, len(items))

            # If the random index generated is not unique, do not append it
            if random_index not in indices:
                indices.append(random_index)

        # Return the selections
        return [items[i] for i in indices]

    def shuffle(self,
                items: MutableSequence[Any]) -> list[Any]:
        """ Shuffle the list of items.

        Parameters
        ----------
        `items` : list[Any]
            The list of items to shuffle.

        Returns
        -------
        list[Any]
            The shuffled list of items.

        Raises
        ------
        TypeError
            If the items are not a list.

        Notes
        -----
        The list of items is shuffled using the quantum circuit. The quantum
        circuit generates a uniform distribution over all possible permutations
        of the list. The distribution is then measured to extract the random
        permutation.

        The list of items is shuffled using the following steps:

        1. Create a uniform distribution over all possible permutations.
        2. Apply measurement to the distribution.
        3. Extract the quasi-probability distribution from the result.
        4. Convert the quasi-probability distribution to counts.
        5. Postprocess the measurement result.
        6. Return the shuffled list of items.

        Examples
        --------
        >>> shuffled = qrng.shuffle([1, 2, 3, 4, 5])
        >>> len(set(shuffled)) == 5
        True
        >>> qrng.shuffle(1)
        Traceback (most recent call last):
            ...
        TypeError: Population must be a MutableSequence.
        """
        # Ensure that the items are a list
        if not isinstance(items, list):
            raise TypeError("Population must be a MutableSequence.")

        return self.sample(items, len(items))

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'qrng': QRNG()})