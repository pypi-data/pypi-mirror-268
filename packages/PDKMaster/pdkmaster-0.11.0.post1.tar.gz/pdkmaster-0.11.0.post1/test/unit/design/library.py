# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

from pdkmaster.technology import primitive as _prm
from pdkmaster.design import cell as _cell, routinggauge as _rg, library as _lbry, factory as _fab

from ..dummy import dummy_tech, dummy_cktfab, dummy_layoutfab, dummy_lib, dummy_fab
dummy_prims = dummy_tech.primitives


class LibraryTest(unittest.TestCase):
    def test_property(self):
        # Can't assign to .cells
        with self.assertRaises(AttributeError):
            dummy_lib.cells = _cell._Cells()

        self.assertEqual(dummy_lib.tech, dummy_tech)
        self.assertEqual(dummy_fab.cktfab, dummy_cktfab)
        self.assertEqual(dummy_fab.layoutfab, dummy_layoutfab)

    def test___init__(self):
        # code coverage
        tuple(dummy_lib.sorted_cells)

        lib = _lbry.Library(name="test", tech=dummy_tech)
        fab = _fab.BaseCellFactory(lib=lib, cktfab=dummy_cktfab, layoutfab=dummy_layoutfab)
        cell = fab.new_cell(name="test")
        ckt = cell.new_circuit()

        cell2 = fab.new_cell(name="test2")
        ckt2 = cell2.new_circuit()

        # Instantiate in first created in order to try to trigger code
        # in sorted_cells.
        ckt.instantiate(cell2, name="cell2")

        tuple(lib.sorted_cells)


class RoutingGaugeLibraryTest(unittest.TestCase):
    def test_routinggauge(self):
        mw = _prm.MetalWire(name="mw", min_width=1.0, min_space=1.0)

        with self.assertRaises(ValueError):
            # wrong bottom
            _rg.RoutingGauge(
                tech=dummy_tech, bottom=mw, bottom_direction="horizontal",
                top=dummy_prims.metal2,
                pingrid_pitch=0.4, row_height=10.0,
            )
        with self.assertRaises(ValueError):
            # wrong top
            _rg.RoutingGauge(
                tech=dummy_tech, bottom=dummy_prims.metal, bottom_direction="horizontal",
                top=mw,
                pingrid_pitch=0.4, row_height=10.0,
            )
        with self.assertRaises(ValueError):
            # top not above bottom
            _rg.RoutingGauge(
                tech=dummy_tech, bottom=dummy_prims.metal2, bottom_direction="horizontal",
                top=dummy_prims.metal,
                pingrid_pitch=0.4, row_height=10.0,
            )
        with self.assertRaises(ValueError):
            # wrong direction
            _rg.RoutingGauge(
                tech=dummy_tech, bottom=dummy_prims.metal, bottom_direction="error",
                top=dummy_prims.metal2,
                pingrid_pitch=0.4, row_height=10.0,
            )
        with self.assertRaises(ValueError):
            # wrong metalwire in pitches
            _rg.RoutingGauge(
                tech=dummy_tech, bottom=dummy_prims.metal, bottom_direction="horizontal",
                top=dummy_prims.metal2,
                pitches={
                    mw: 2.0,
                    dummy_prims.metal2: 2.0,
                },
                offsets={
                    dummy_prims.metal: 0.0,
                    dummy_prims.metal2: 1.0,
                },
                pingrid_pitch=0.4, row_height=10.0,
            )
        with self.assertRaises(ValueError):
            # wrong metalwire in offsets
            _rg.RoutingGauge(
                tech=dummy_tech, bottom=dummy_prims.metal, bottom_direction="horizontal",
                top=dummy_prims.metal2,
                pitches={
                    dummy_prims.metal: 2.0,
                    dummy_prims.metal2: 2.0,
                },
                offsets={
                    dummy_prims.metal: 0.0,
                    mw: 1.0,
                },
                pingrid_pitch=0.4, row_height=10.0,
            )

    def test_stdcelllibrary(self):
        rg = _rg.RoutingGauge(
            tech=dummy_tech, bottom=dummy_prims.metal, bottom_direction="horizontal",
            top=dummy_prims.metal2,
            pitches={
                dummy_prims.metal: 2.0,
                dummy_prims.metal2: 2.0,
            },
            offsets={
                dummy_prims.metal: 0.0,
                dummy_prims.metal2: 1.0,
            },
            pingrid_pitch=0.4, row_height=10.0,
        )
        lib = _lbry.RoutingGaugeLibrary(
            name="test", tech=dummy_tech, routinggauge=rg,
        )

        self.assertEqual(rg.tech, dummy_tech)

        self.assertEqual(lib.routinggauge[0], rg)
        self.assertAlmostEqual(lib.pingrid_pitch, 0.4)
        self.assertAlmostEqual(lib.row_height, 10.0)
