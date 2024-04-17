# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

from pdkmaster.technology import property_ as _prp, primitive as _prm
from pdkmaster.dispatch.primitive import PrimitiveDispatcher

from ..dummy import dummy_tech
dummy_prims = dummy_tech.primitives


# Simple dispatcher that just returns the type of the edge
class MyDispatcher(PrimitiveDispatcher):
    def _Primitive(self, prim: _prm.PrimitiveT):
        return type(prim)


class IsWidthSpaceConductor(PrimitiveDispatcher):
    def _Primitive(self, prim: _prm.PrimitiveT, *args, **kwargs):
        return False

    def _WidthSpaceConductor(self, prim: _prm.WidthSpaceConductorT, *args, **kwargs):
        return True


class EdgeDispatchTest(unittest.TestCase):
    def test_notimplemented(self):
        with self.assertRaises(NotImplementedError):
            # Call ShapeDispatched._Shape() method
            PrimitiveDispatcher()(dummy_prims.active)

    def test_dispatch(self):
        disp = MyDispatcher()

        with self.assertRaises(RuntimeError):
            disp("error")

        pad = _prm.PadOpening(
            name="pad", min_width=20.0, min_space=5.0,
            bottom=dummy_prims.metal, min_bottom_enclosure=_prp.Enclosure(1.0),
        )
        sect1 = dummy_prims.active.in_(dummy_prims.nplus)
        sect2 = dummy_prims.contact.in_(dummy_prims.active)
        rm1 = dummy_prims.active.remove(dummy_prims.nplus)
        for prim in (*dummy_prims, pad, sect1, sect2, rm1):
            self.assertIs(disp(prim), type(prim))

    def test_hier(self):
        disp = IsWidthSpaceConductor()

        self.assertTrue(disp(dummy_prims.nwell))
        self.assertFalse(disp(dummy_prims.nplus))
