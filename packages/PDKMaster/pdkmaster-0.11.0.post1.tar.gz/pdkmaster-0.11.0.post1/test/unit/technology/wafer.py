# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

from pdkmaster.technology import mask as _msk, wafer_ as _wfr

class WaferTest(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(ValueError):
            _wfr._Wafer()

    def test_wafer(self):
        self.assertEqual(_wfr.wafer, _wfr.wafer)
        self.assertEqual(hash(_wfr.wafer), hash(_wfr.wafer))
        self.assertEqual(_wfr.wafer.designmasks, tuple())


    def test_substratenet(self):
        self.assertNotEqual(
            _wfr.SubstrateNet(name="substrate"),
            _wfr.SubstrateNet(name="sub2"),
        )