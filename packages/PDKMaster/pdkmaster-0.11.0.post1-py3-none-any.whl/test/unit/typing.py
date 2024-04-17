# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

from pdkmaster.typing import cast_MultiT, cast_MultiT_n, cast_OptMultiT, cast_OptMultiT_n

class TestTyping(unittest.TestCase):
    def test_multit(self):
        self.assertEqual(cast_MultiT(2), (2,))
        self.assertEqual(cast_MultiT("ab"), ("ab",))
        self.assertEqual(cast_MultiT(range(2)), (0, 1))

        self.assertEqual(cast_MultiT_n(2, n=2), (2, 2))
        self.assertEqual(cast_MultiT_n("ab", n=3), ("ab", "ab", "ab"))
        self.assertEqual(cast_MultiT_n(range(2), n=2), (0, 1))
        with self.assertRaises(ValueError):
            cast_MultiT_n(range(2), n=3)

        self.assertIs(cast_OptMultiT(None), None)
        self.assertEqual(cast_OptMultiT(2), (2,))
        self.assertEqual(cast_OptMultiT("ab"), ("ab",))
        self.assertEqual(cast_OptMultiT(range(2)), (0, 1))

        self.assertIs(cast_OptMultiT_n(None, n=2), None)
        self.assertEqual(cast_OptMultiT_n(2, n=2), (2, 2))
        self.assertEqual(cast_OptMultiT_n("ab", n=3), ("ab", "ab", "ab"))
        self.assertEqual(cast_OptMultiT_n(range(2), n=2), (0, 1))
        # Value provided for n == 0
        with self.assertRaises(ValueError):
            cast_OptMultiT_n(1, n=0)
        # number of values mismatch with n
        with self.assertRaises(ValueError):
            cast_OptMultiT_n(range(2), n=3)
