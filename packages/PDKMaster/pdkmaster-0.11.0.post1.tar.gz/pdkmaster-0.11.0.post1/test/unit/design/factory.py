# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

from pdkmaster.design import (
    circuit as _ckt, layout as _lay, cell as _cell, library as _lbry, factory as _fab,
)

from ..dummy import dummy_tech, dummy_lib, dummy_fab, dummy_cktfab, dummy_layoutfab


class MyFactoryCell(_fab.FactoryCell["MyFactory"]):
    pass


class MyFactoryOnDemandCell(MyFactoryCell, _fab.FactoryOnDemandCell["MyFactory"]):
    def _create_circuit(self):
        ...

    def _create_layout(self):
        ...


class MyFactory(_fab.CellFactory[MyFactoryCell]):
    def __init__(self, *,
        lib: _lbry.Library, cktfab: _ckt.CircuitFactory, layoutfab: _lay.LayoutFactory,
    ):
        super().__init__(
            lib=lib, cktfab=cktfab, layoutfab=layoutfab, cell_class=MyFactoryCell,
        )


class FactoryCellTest(unittest.TestCase):
    def test_factorycell(self):
        lib = _lbry.Library(name="testlib", tech=dummy_tech)
        fab = MyFactory(lib=lib, cktfab=dummy_cktfab, layoutfab=dummy_layoutfab)
        cell = fab.new_cell(name="test")

        self.assertIsInstance(cell, MyFactoryCell)
        self.assertEqual(cell.fab, fab)

        cell = fab.new_cell(name="od_test", cell_class=MyFactoryOnDemandCell)

        self.assertIsInstance(cell, MyFactoryCell)
        self.assertIsInstance(cell, MyFactoryOnDemandCell)
        self.assertEqual(cell.fab, fab)
        self.assertEqual(cell.lib, lib)
        self.assertEqual(cell.tech, dummy_tech)
        self.assertEqual(cell.cktfab, dummy_cktfab)
        self.assertEqual(cell.layoutfab, dummy_layoutfab)


class CellFactoryTest(unittest.TestCase):
    def test_property(self):
        self.assertEqual(dummy_fab.lib, dummy_lib)
        self.assertEqual(dummy_fab.cktfab, dummy_cktfab)
        self.assertEqual(dummy_fab.layoutfab, dummy_layoutfab)

    def test_new_cell(self):
        lib = _lbry.Library(name="test", tech=dummy_tech)
        fab = _fab.CellFactory(
            lib=lib, cktfab=dummy_cktfab, layoutfab=dummy_layoutfab,
            cell_class=MyFactoryCell,
        )

        called: bool = False
        def cb(cell: _fab.FactoryCell) -> None:
            nonlocal called
            called = True
            self.assertEqual(cell.name, "test")

        cell = fab.new_cell(name="test", create_cb=cb)
        self.assertIsInstance(cell, _fab.FactoryCell)
        self.assertIsInstance(cell, MyFactoryCell)
        self.assertTrue(called)

        # Already existing cell
        with self.assertRaises(ValueError):
            fab.new_cell(name="test", error="error")

    def test_getcreate_cell(self):
        lib = _lbry.Library(name="test", tech=dummy_tech)
        fab = _fab.CellFactory(
            lib=lib, cktfab=dummy_cktfab, layoutfab=dummy_layoutfab,
            cell_class=MyFactoryCell, name_prefix="pre_"
        )

        called: bool = False
        def cb(cell: _fab.FactoryCell) -> None:
            nonlocal called
            called = True
            self.assertEqual(cell.name, "pre_test")

        cell = fab.getcreate_cell(name="test", create_cb=cb)
        self.assertEqual(cell.name, "pre_test")
        self.assertIsInstance(cell, _fab.FactoryCell)
        self.assertIsInstance(cell, MyFactoryCell)
        self.assertTrue(called)

        called = False
        self.assertEqual(fab.getcreate_cell(name="test", create_cb=cb), cell)
        self.assertFalse(called)

        # Existing cell of wrong type
        with self.assertRaises(TypeError):
            fab.getcreate_cell(name="test", cell_class=MyFactoryOnDemandCell)


class BaseCellFactoryTest(unittest.TestCase):
    def test_new_cell(self):
        lib = _lbry.Library(name="test", tech=dummy_tech)
        fab = _fab.BaseCellFactory(lib=lib, cktfab=dummy_cktfab, layoutfab=dummy_layoutfab)

        cell = fab.new_cell(name="test")
        self.assertIs(type(cell), _cell.Cell)

        # Already existing cell
        with self.assertRaises(ValueError):
            fab.new_cell(name="test")
        # No extra arguments for new_cell()
        with self.assertRaises(TypeError):
            cell = fab.new_cell(name="error", error="error")
