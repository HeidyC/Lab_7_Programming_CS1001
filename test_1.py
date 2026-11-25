"""CS 1001 - Lab Programming 7 (Nov 18): starter unit tests.

Before coding, the tests fail with NotImplementedError; this is expected.
ADD TWO tests of your own: one for sum_pair and one for sum_file.
Run: python -m unittest test_1.py
"""

import io
import tempfile
import os
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from day1 import sum_pair, keyboard_sum, sum_file


class TestSumPair(unittest.TestCase):
    def test_two_positive_values(self):
        self.assertEqual(7.0, sum_pair("3 4"))

    def test_negative_and_whitespace(self):
        self.assertEqual(4.5, sum_pair("  -2.5    7  "))

    # TODO: Add ONE more test, for example zero or two decimal values.
    def test_sum_pair_zero_and_decimal(self):
        self.assertAlmostEqual(sum_pair("0 2.5"), 2.5)


class TestKeyboardSum(unittest.TestCase):
    def test_reads_and_prints(self):
        """We simulate typing in the test; you don't need to write a mock."""
        output = io.StringIO()
        with patch("builtins.input", return_value="3 4"):
            with redirect_stdout(output):
                result = keyboard_sum()
        self.assertEqual("Sum: 7.0\n", output.getvalue())
        self.assertEqual(None, result)

    # No additional automated keyboard tests are required.


class TestSumFile(unittest.TestCase):
    def test_three_lines(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "input.txt"
            destination = Path(folder) / "output.txt"
            source.write_text("3.0 4.0\n1.5 2.5\n-2.0 7.0\n", encoding="utf-8")
            result = sum_file(str(source), str(destination))
            self.assertEqual("7.0\n4.0\n5.0\n", destination.read_text(encoding="utf-8"))
            self.assertEqual(None, result)

    def test_empty_file(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "empty.txt"
            destination = Path(folder) / "output.txt"
            source.write_text("", encoding="utf-8")
            sum_file(str(source), str(destination))
            self.assertEqual("", destination.read_text(encoding="utf-8"))

    # TODO: Add ONE more test, for example a single input line or a zero sum.
    def test_sum_file_pair_summing_to_zero(self):
        with tempfile.TemporaryDirectory() as folder:
            input_path = os.path.join(folder, "input.txt")
            output_path = os.path.join(folder, "output.txt")

            with open(input_path, "w") as input_file:
                input_file.write("-2.5 2.5\n")

            sum_file(input_path, output_path)

            with open(output_path, "r") as output_file:
                self.assertEqual(output_file.read(), "0.0\n")

if __name__ == "__main__":
    unittest.main()
