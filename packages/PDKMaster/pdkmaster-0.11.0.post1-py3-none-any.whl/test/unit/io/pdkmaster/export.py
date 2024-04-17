# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

from pdkmaster.technology import property_ as _prp, primitive as _prm
from pdkmaster.design import library as _lib
from pdkmaster.io.pdkmaster import generate
from pdkmaster.io.pdkmaster.export import _PrimitiveGenerator

from ...dummy import DummyTech, dummy_tech, dummy_lib


class ExportTest(unittest.TestCase):
    def test_primitivegenerator(self):
        # Some more test to cover code not covered by test_pdkmastergenerator()
        primgen = _PrimitiveGenerator()

        prim = _prm.Well(
            type_=_prm.pImpl, name="pwell",
            min_width=1.5, min_space=1.5, min_space_samenet=1.0,
        )
        primgen(prim)

        prim = _prm.MetalWire(
            name="M1", min_width=0.1, min_space=0.1, grid=0.010,
            min_density=0.20, max_density=0.80,
            blockage=_prm.Marker(name="M1block"),
        )
        primgen(prim)

        prim = _prm.PadOpening(
            name="pad", min_width=20.0, min_space=3.0, bottom=_prm.MetalWire(
                name="metal", min_width=1.0, min_space=1.0,
            ), min_bottom_enclosure=_prp.Enclosure(1.5),
        )
        primgen(prim)

    def test_pdkmastergenerator(self):
        generate(dummy_tech)
        generate(dummy_lib.cells.cell1.circuit)
        generate(dummy_lib)

        with self.assertRaises(TypeError):
            generate("error")

        # cell instance but not exporting full lib
        with self.assertRaises(ValueError):
            generate(dummy_lib.cells.cell2.circuit)

        # inter-library cell instances not allowed
        with self.assertRaises(ValueError):
            generate._gen_ckt(dummy_lib.cells.cell2.circuit, lib=_lib.Library(
                name="error", tech=dummy_tech,
            ))