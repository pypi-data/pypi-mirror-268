# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

from pdkmaster.io import spice as _sp

from ...dummy import dummy_tech
dummy_prims = dummy_tech.primitives

class SpicePrimsParamSpec(unittest.TestCase):
    def test_error(self):
        params = _sp.SpicePrimsParamSpec()

        # __setitem__() may not be used directly
        with self.assertRaises(TypeError):
            params["error"] = "error"

        # subcircuit_paramalias when not a subcircuit
        with self.assertRaises(ValueError):
            params.add_device_params(
                prim=dummy_prims.resistor, subcircuit_paramalias={"error": "error"},
            )

        # subcircuit_paramalias not a dict with keys == {"width", "height"}
        with self.assertRaises(ValueError):
            params.add_device_params(
                prim=dummy_prims.resistor,
                is_subcircuit=True, subcircuit_paramalias={"error": "error"},
            )

        # subcircuit_paramalias given when not a subcircuit
        with self.assertRaises(TypeError):
            params.add_device_params(
                prim=dummy_prims.resistor, sheetres=10.0,
                is_subcircuit=True, subcircuit_paramalias={"width": "w", "length": "l"},
            )
