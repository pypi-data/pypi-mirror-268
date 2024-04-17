# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

from pdkmaster.technology import geometry as _geo
from pdkmaster.design import (
    circuit as _ckt, cell as _cell, library as _lbry, factory as _fab,
)
from pdkmaster.design.layout import layout_ as _laylay

from ..dummy import dummy_tech, dummy_cktfab, dummy_layoutfab, dummy_lib, dummy_fab


class CellTest(unittest.TestCase):
    def test_property(self):
        class MyOD(_cell.OnDemandCell):
            def _create_circuit(self):
                return
            def _create_layout(self):
                return

        empty_cell = _cell.Cell(
            name="empty",
            tech=dummy_tech, cktfab=dummy_cktfab, layoutfab=dummy_layoutfab,
        )
        empty_odcell = MyOD(
            name="empty_od",
            tech=dummy_tech, cktfab=dummy_cktfab, layoutfab=dummy_layoutfab,
        )

        cell1 = dummy_lib.cells.cell1

        self.assertEqual(cell1.tech, dummy_tech)
        self.assertEqual(cell1.cktfab, dummy_cktfab)
        self.assertEqual(cell1.layoutfab, dummy_layoutfab)

        with self.assertRaises(ValueError):
            empty_cell.circuit
        with self.assertRaises(ValueError):
            empty_cell.circuit_lookup(name="error")
        with self.assertRaises(ValueError):
            empty_cell.layout
        with self.assertRaises(ValueError):
            empty_cell.layout_lookup(name="error")
        with self.assertRaises(ValueError):
            empty_cell.new_circuitlayouter()
        with self.assertRaises(ValueError):
            empty_cell.new_circuitlayouter(name="error")

        with self.assertRaises(NotImplementedError):
            empty_odcell.circuit
        with self.assertRaises(NotImplementedError):
            empty_odcell.layout
        with self.assertRaises(NotImplementedError):
            empty_odcell.new_circuitlayouter()
        with self.assertRaises(ValueError):
            empty_odcell.new_circuitlayouter(name="error")

    def test_instsublayout(self):
        cell = dummy_fab.new_cell(name="test")
        cell.new_circuit()
        bb = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=2.0)
        cell.new_layout(boundary=bb)

        self.assertEqual(
            cell.circuit, cell.circuit_lookup(name=cell.name)
        )
        self.assertEqual(
            cell.layout, cell.layout_lookup(name=cell.name)
        )

        rot = _geo.Rotation.R90
        inst = _ckt._CellInstance(name="inst", cell=cell)
        sublay = _laylay._InstanceSubLayout(
            inst=inst, origin=_geo.origin, layoutname=None, rotation=rot,
        )
        self.assertEqual(sublay.boundary, rot*bb)

        cell2 = dummy_fab.new_cell(name="test2")
        ckt = cell2.new_circuit()
        inst = ckt.instantiate(cell, name="inst")
        layouter = cell2.new_circuitlayouter()

        instlay = layouter.inst_layout(inst=inst, rotation=rot)
        self.assertEqual(instlay.boundary, rot*bb)
