# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

from pdkmaster.technology import (
    property_ as _prp, rule as _rle, wafer_ as _wfr, mask as _msk, primitive as _prm,
    technology_ as _tch,
)
from pdkmaster.technology.primitive import (
    _core as _prmcore, _param as _prmparm, _derived as _prmderv, conductors as _prmcond,
    rules as _prmrule
)

from ..dummy import dummy_tech


class ParamTest(unittest.TestCase):
    def test_primparam(self):
        dummy_prims = dummy_tech.primitives

        p = _prmparm._PrimParam(
            primitive=dummy_prims.active, name="width", allow_none=True, default=3.0
        )

        self.assertEqual(p, p)
        self.assertAlmostEqual(p.cast(None), 3.0)
        self.assertAlmostEqual(p.cast(1), 1.0)

        self.assertIsInstance(p == 3.0, _rle.RuleT)


class PrimitiveTest(unittest.TestCase):
    def test_simple(self):
        """Some simple tests not wanting to define own method
        """
        dummy_prims = dummy_tech.primitives

        active = dummy_prims.active
        nplus = dummy_prims.nplus
        pplus = dummy_prims.pplus
        poly = dummy_prims.poly

        # _Primitive
        with self.assertRaises(TypeError):
            _prmcore._Primitive(name="error")
        with self.assertRaises(ValueError):
            dummy_prims.metal._derive_rules(tech=dummy_tech)

        # _PrimParam
        with self.assertRaises(TypeError):
            _prmparm._PrimParam(
                primitive=active, name="error", default=dummy_prims,
            )

        # _DesignMaskPrimitive
        with self.assertRaises(TypeError):
            class MyPrim(_prmcore._DesignMaskPrimitive):
                def __init__(self, *, name: str, **super_args):
                    super().__init__(name=name, **super_args)

                def _generate_rules(self, *, tech, gen_mask):
                    return super()._generate_rules(tech=tech, gen_mask=gen_mask)
            mask = _msk.DesignMask(name="error")
            MyPrim(name="error", mask=mask)

        # _MaskPrimitive.remove()
        self.assertEqual(
            active.remove(poly).mask,
            active.mask.remove(poly.mask)
        )
        self.assertEqual(
            active.remove((nplus, pplus)).mask,
            active.mask.remove(_msk.Join((nplus.mask, pplus.mask)))
        )
        with self.assertRaises(ValueError):
            active.remove(())

        # _Intersect
        self.assertEqual(
            active.in_(nplus).mask,
            _msk.Intersect((active.mask, nplus.mask)),
        )
        with self.assertRaises(ValueError):
            # only one prim for _Intersect
            _prmderv._Intersect(prims=(active,))

        # _Alias
        self.assertEqual(
            active.alias("alias").mask,
            active.mask.alias("alias"),
        )

    def test_marker(self):
        marker = _prm.Marker(name="TestMarker")
        marker2 = _prm.Marker(name="TestMarker2")

        with self.assertRaises(AttributeError):
            # Accessing rules before they are generated.
            marker2.rules

        rules = tuple(marker._generate_rules(tech=dummy_tech))
        self.assertEqual(rules[0], _msk.DesignMask(name="TestMarker"))

    def test_auxiliary(self):
        prim1 = _prm.Auxiliary(name="prim1")
        prim1bis = _prm.Auxiliary(name="prim1")
        prim2 = _prm.Auxiliary(name="prim2")

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)

    def test_extraprocess(self):
        with self.assertRaises(TypeError):
            _prm.ExtraProcess(name="Step1")

        prim1 = _prm.ExtraProcess(
            name="prim1", min_width=1.0, min_space=1.0,
        )
        prim1bis = _prm.ExtraProcess(
            name="prim1", min_width=1.0, min_space=1.0,
        )
        prim2 = _prm.ExtraProcess(
            name="prim2", min_width=0.2, min_space=0.5,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)

    def test_implanttype(self):
        self.assertEqual(_prm.nImpl, _prm.nImpl)
        self.assertNotEqual(_prm.nImpl, _prm.pImpl)

        self.assertEqual(hash(_prm.nImpl), hash(_prm.nImpl))
        self.assertNotEqual(hash(_prm.nImpl), hash(_prm.pImpl))

        with self.assertWarns(UserWarning):
            _prm.nImpl == "n"

    def test_implant(self):
        prim1 = _prm.Implant(
            name="prim1", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )
        prim1bis = _prm.Implant(
            name="prim1", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )
        prim2 = _prm.Implant(
            name="prim2", min_width=0.2, min_space=0.5, type_=_prm.pImpl,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)

    def test_insulator(self):
        prim1 = _prm.Insulator(
            name="prim1", min_width=0.5, min_space=0.5,
        )
        prim1bis = _prm.Insulator(
            name="prim1", min_width=0.5, min_space=0.5,
        )
        prim2 = _prm.Insulator(
            name="prim2", min_width=0.5, min_space=0.5,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)

    def test_well(self):
        with self.assertRaises(TypeError):
            _prm.Well(name="prim1", min_width=1.0, min_space=1.0)
        with self.assertRaises(ValueError):
            _prm.Well(
                name="prim2", min_width=0.2, min_space=0.5, min_space_samenet=0.6,
                type_=_prm.nImpl,
            )

        prim1 = _prm.Well(
            name="prim1", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )
        prim1bis = _prm.Well(
            name="prim1", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )
        prim2 = _prm.Well(
            name="prim2", min_width=0.2, min_space=0.5, min_space_samenet=0.25,
            type_=_prm.nImpl,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

    def test_deepwell(self):
        with self.assertRaises(TypeError):
            _prm.DeepWell(name="prim1", min_width=1.0, min_space=1.0)
        with self.assertRaises(TypeError):
            _prm.DeepWell(
                name="prim1", min_width=1.0, min_space=1.0, type_=_prm.pImpl,
            )

        well1 = _prm.Well(
            name="well1", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )
        well2 = _prm.Well(
            name="well2", min_width=1.0, min_space=1.0, type_=_prm.pImpl,
        )

        with self.assertRaises(ValueError):
            _prm.DeepWell(
                name="typemismatch", min_width=1.0, min_space=1.0, well=well1,
                type_=_prm.pImpl,
                min_well_overlap=1.5, min_well_enclosure=2.0,
            )

        prim1 = _prm.DeepWell(
            name="prim1", min_width=1.0, min_space=1.0, well=well1, type_=_prm.nImpl,
            min_well_overlap=1.5, min_well_enclosure=2.0,
        )
        prim1bis = _prm.DeepWell(
            name="prim1", min_width=1.0, min_space=1.0, well=well1, type_=_prm.nImpl,
            min_well_overlap=1.5, min_well_enclosure=2.0,
        )
        prim2 = _prm.DeepWell(
            name="prim2", min_width=0.2, min_space=0.5, well=well2,
            min_well_overlap=1.5, min_well_enclosure=2.0,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

    def test_waferwire(self):
        nimpl = _prm.Implant(
            name="nimplant", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )
        pimpl = _prm.Implant(
            name="pimplant", min_width=1.0, min_space=1.0, type_=_prm.pImpl,
        )
        oxide = _prm.Insulator(name="oxide", min_width=1.0, min_space=1.0)
        well = _prm.Well(
            name="well", min_width=1.0, min_space=1.0, type_=_prm.pImpl,
        )
        well2 = _prm.Well(
            name="well2", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )

        with self.assertRaises(TypeError):
            _prm.WaferWire(name="prim1", min_width=1.0, min_space=1.0)

        with self.assertRaises(TypeError):
            # well not implant
            _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True,
                implant=(nimpl, well), min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(ValueError):
            # wrong implant_abut string
            _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True,
                implant=pimpl, min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="", allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(ValueError):
            # wrong implant_abut value
            _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True,
                implant=pimpl, min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut=nimpl, allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(TypeError):
            # min_well_enclosure not specified for multiple wells
            _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True,
                implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=(well, well), min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(TypeError):
            # min_substrate_enclosure_same_type not None with min_substrate_enclosure
            # None
            prim1 = _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True, min_substrate_enclosure_same_type=_prp.Enclosure(0.08),
                implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(TypeError):
            # min_substrate_enclosure given with allow_in_substrate=False
            prim1 = _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=False, min_substrate_enclosure=_prp.Enclosure(0.1),
                implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(ValueError):
            # min_oxide_enclosure without oxide
            prim1 = _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True,
                implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
                min_oxide_enclosure=_prp.Enclosure(0.01),
            )

        prim1 = _prm.WaferWire(
            name="prim1", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_well_enclosure_same_type=_prp.Enclosure(0.08),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            min_substrate_enclosure_same_type=_prp.Enclosure(0.1),
            allow_well_crossing=False,
        )
        prim1bis = _prm.WaferWire(
            name="prim1", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_well_enclosure_same_type=_prp.Enclosure(0.08),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            min_substrate_enclosure_same_type=_prp.Enclosure(0.1),
            allow_well_crossing=False,
        )
        prim2 = _prm.WaferWire(
            name="prim2", min_width=0.2, min_space=0.5,
            allow_in_substrate=False,
            implant=pimpl, min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut=pimpl, allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_well_enclosure_same_type=_prp.Enclosure(0.08),
            allow_well_crossing=False,
            oxide=oxide, min_oxide_enclosure=_prp.Enclosure(0.08),
        )
        prim3 = _prm.WaferWire(
            name="prim3", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_well_enclosure_same_type=(None,),
            allow_well_crossing=False,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)
        self.assertNotEqual(prim1, prim3)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)
        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)
        rules = tuple(prim3._generate_rules(tech=dummy_tech))
        self.assertIn(prim3.mask, rules)

        # _WaferWireIntersect
        # Not a good layer for prim1
        with self.assertRaises(ValueError):
            prim1.in_(_wfr.wafer)

    def test_metalwire(self):
        with self.assertRaises(TypeError):
            # Wrong value in space_table
            _prm.MetalWire(
                name="prim1", min_width=1.0, min_space=1.0, space_table=(
                    (2.0, 2.0),
                    ((10.0, 3.0, 2.0), 3.0),
                ),
                min_area=2.0, min_density=0.4, max_density=0.8,
            )
        with self.assertRaises(ValueError):
            # wrong min_density value
            _prm.MetalWire(
                name="prim1", min_width=1.0, min_space=1.0, space_table=(
                    (2.0, 2.0),
                    ((10.0, 3.0), 3.0),
                ),
                min_area=2.0, min_density=40, max_density=0.8,
            )
        with self.assertRaises(ValueError):
            # wrong max_density value
            _prm.MetalWire(
                name="prim1", min_width=1.0, min_space=1.0, space_table=(
                    (2.0, 2.0),
                    ((10.0, 3.0), 3.0),
                ),
                min_area=2.0, min_density=0.4, max_density=80,
            )

        pin = _prm.Marker(name="pin")
        prim1 = _prm.MetalWire(
            name="prim1", min_width=1.0, min_space=1.0, space_table=(
                (2.0, 2.0),
                ((10.0, 3.0), 3.0),
            ),
            min_area=2.0, min_density=0.4, max_density=0.8,
        )
        prim1bis = _prm.MetalWire(
            name="prim1", min_width=1.0, min_space=1.0, space_table=(
                (2.0, 2.0),
                ((10.0, 3.0), 3.0),
            ),
            min_area=2.0, min_density=0.4, max_density=0.8,
        )
        prim2 = _prm.MetalWire(
            name="prim2", min_width=1.0, min_space=1.0, grid=0.2, pin=pin,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        with self.assertRaises(AttributeError):
            prim1.pin
        self.assertEqual(prim2.pin, pin)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)
        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

    def test_via(self):
        nimpl = _prm.Implant(
            name="nimplant", min_width=0.5, min_space=0.5, type_=_prm.nImpl,
        )
        nimpl2 = _prm.Implant(
            name="nimplant2", min_width=0.5, min_space=0.5, type_=_prm.nImpl,
        )
        pimpl = _prm.Implant(
            name="pimplant", min_width=0.5, min_space=0.5, type_=_prm.pImpl,
        )
        oxide = _prm.Insulator(name="oxide", min_width=1.0, min_space=1.0)
        well = _prm.Well(
            name="well", min_width=1.0, min_space=1.0, type_=_prm.pImpl,
        )
        well2 = _prm.Well(
            name="well2", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )
        active = _prm.WaferWire(
            name="aa", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            allow_well_crossing=False,
            oxide=oxide,
        )
        active2 = _prm.WaferWire(
            name="aa2", min_width=1.0, min_space=1.0,
            allow_in_substrate=False,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            allow_well_crossing=False,
            oxide=oxide,
        )
        m1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
        m2 = _prm.TopMetalWire(name="metal2", min_width=1.0, min_space=1.0)
        m3 = _prm.MetalWire(name="metal3", min_width=1.0, min_space=1.0)

        with self.assertRaises(TypeError):
            # TopMetalWire as bottom
            _prm.Via(
                name="prim1", width=0.8, min_space=0.8,
                bottom=m2, min_bottom_enclosure=_prp.Enclosure(0.2),
                top=m2, min_top_enclosure=_prp.Enclosure(0.2),
            )

        prim1 = _prm.Via(
            name="prim1", width=0.8, min_space=0.8,
            bottom=active, min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m1, min_top_enclosure=_prp.Enclosure(0.2),
        )
        prim1bis = _prm.Via(
            name="prim1", width=0.8, min_space=0.8,
            bottom=active, min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m1, min_top_enclosure=_prp.Enclosure(0.2),
        )
        prim2 = _prm.Via(
            name="prim2", width=0.8, min_space=0.8,
            bottom=m1, min_bottom_enclosure=_prp.Enclosure(0.2),
            top=(m1, m2), min_top_enclosure=_prp.Enclosure(0.2),
        )
        prim3 = _prm.Via(
            name="prim3", width=0.8, min_space=0.8,
            bottom=(m1, active2), min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m2, min_top_enclosure=_prp.Enclosure(0.2),
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)
        self.assertNotEqual(prim1, prim3)

        # prims have to be in technolgy in order to generate the rules
        class MyTech(_tch.Technology):
            @property
            def name(self):
                return "MyTech"
            @property
            def grid(self):
                return 0.005

            def __init__(self):
                super().__init__(primitives=_prm.Primitives((
                    _prm.Base(type_=_prm.pBase),
                    nimpl, pimpl, well, oxide, active, prim1, m1,
                )))
        mytech = MyTech()

        rules = tuple(prim1._generate_rules(tech=mytech))
        self.assertIn(prim1.mask, rules)

        # in_()
        with self.assertRaises(ValueError):
            prim1.in_(nimpl)
        self.assertEqual(
            prim1.in_(active),
            _prmcond._ViaIntersect(via=prim1, prim=active),
        )
        self.assertEqual(
            prim1.in_(active.in_(nimpl)),
            _prmcond._ViaIntersect(via=prim1, prim=active.in_(nimpl)),
        )

    def test_padopening(self):
        m1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
        m2 = _prm.MetalWire(name="metal2", min_width=1.0, min_space=1.0)
        m3 = _prm.TopMetalWire(name="metal3", min_width=1.0, min_space=1.0)

        with self.assertRaises(TypeError):
            # Missing arguments
            _prm.PadOpening(name="error")
        with self.assertRaises(TypeError):
            # TopMetalWire as bottom
            _prm.PadOpening(
                name="error", min_width=1.0, min_space=1.0,
                bottom=m3, min_bottom_enclosure=_prp.Enclosure(0.2)
            )

        prim1 = _prm.PadOpening(
            name="prim1", min_width=1.0, min_space=1.0,
            bottom=m1, min_bottom_enclosure=_prp.Enclosure(0.2)
        )
        prim1bis = _prm.PadOpening(
            name="prim1", min_width=1.0, min_space=1.0,
            bottom=m1, min_bottom_enclosure=_prp.Enclosure(0.2)
        )
        prim2 = _prm.PadOpening(
            name="prim2", min_width=0.2, min_space=0.5,
            bottom=m2, min_bottom_enclosure=_prp.Enclosure(0.2)
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)

        # designmasks
        self.assertEqual(set(prim1.designmasks), {prim1.mask, m1.mask})

    def test_resistor(self):
        well = _prm.Well(
            name="well", min_width=1.0, min_space=1.0, type_=_prm.pImpl,
        )
        nimpl = _prm.Implant(
            name="nimplant", min_width=0.5, min_space=0.5, type_=_prm.nImpl,
        )
        nimpl2 = _prm.Implant(
            name="nimplant2", min_width=0.5, min_space=0.5, type_=_prm.nImpl,
        )
        pimpl = _prm.Implant(
            name="pimplant", min_width=0.5, min_space=0.5, type_=_prm.pImpl,
        )
        active = _prm.WaferWire(
            name="aa", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            allow_well_crossing=False,
        )
        actres = _prm.Marker(name="actres")
        poly = _prm.GateWire(name="poly", min_width=1.0, min_space=1.0)
        polyres = _prm.Marker(name="polyres")
        m1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
        m1res = _prm.Marker(name="m1res")
        via = _prm.Via(
            name="via", width=0.8, min_space=0.8,
            bottom=poly, min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m1, min_top_enclosure=_prp.Enclosure(0.2),
        )

        with self.assertRaises(TypeError):
            # grid not allowed
            _prm.Resistor(
                name="error", grid=0.1,
                wire=poly, contact=None, indicator=polyres, min_indicator_extension=0.5,
            )
        with self.assertRaises(ValueError):
            # min_width too small
            _prm.Resistor(
                name="error", min_width=0.5,
                wire=poly, contact=None, indicator=polyres, min_indicator_extension=0.5,
            )
        with self.assertRaises(ValueError):
            # min_length too small
            _prm.Resistor(
                name="error", min_length=0.5,
                wire=poly, contact=None, indicator=polyres, min_indicator_extension=0.5,
            )
        with self.assertRaises(ValueError):
            # min_space too small
            _prm.Resistor(
                name="error", min_space=0.5,
                wire=poly, contact=None, indicator=polyres, min_indicator_extension=0.5,
            )
        with self.assertRaises(TypeError):
            # well not allowed as implant
            _prm.Resistor(
                name="error",
                wire=active, contact=None, indicator=actres, min_indicator_extension=0.5,
                implant=well,
            )
        with self.assertRaises(ValueError):
            # wrong implant
            _prm.Resistor(
                name="error",
                wire=active, contact=None, indicator=actres, min_indicator_extension=0.5,
                implant=nimpl2,
            )
        with self.assertRaises(ValueError):
            # implant for wire that is not WaferWire or GateWire
            _prm.Resistor(
                name="error",
                wire=m1, contact=None, indicator=m1res, min_indicator_extension=0.5,
                implant=nimpl,
            )
        with self.assertRaises(ValueError):
            # min_implant_enclosure without implant
            prim1 = _prm.Resistor(
                name="error", min_width=1.2,
                wire=poly, contact=None, indicator=polyres, min_indicator_extension=0.5,
                min_implant_enclosure=_prp.Enclosure(0.2),
            )
        with self.assertRaises(ValueError):
            # wire not in via bottom or top
            _prm.Resistor(
                name="error", min_width=1.2,
                wire=active, contact=via, min_contact_space=0.1,
                indicator=polyres, min_indicator_extension=0.5,
                implant=nimpl, min_implant_enclosure=_prp.Enclosure(0.1),
            )
        with self.assertRaises(TypeError):
            # min_contact_space without contact
            _prm.Resistor(
                name="error", min_width=1.2,
                wire=poly, contact=None, indicator=polyres, min_indicator_extension=0.5,
                min_contact_space=0.1,
            )
        with self.assertRaises(TypeError):
            # min_contact_space missing with given contact
            _prm.Resistor(
                name="error", min_width=1.2,
                wire=poly, contact=via,
                indicator=polyres, min_indicator_extension=0.5,
                implant=nimpl, min_implant_enclosure=_prp.Enclosure(0.1),
            )

        prim1 = _prm.Resistor(
            name="prim1", min_width=1.2,
            wire=poly, contact=via, min_contact_space=0.1,
            indicator=polyres, min_indicator_extension=0.5,
            implant=nimpl, min_implant_enclosure=_prp.Enclosure(0.1),
        )
        prim1bis = _prm.Resistor(
            name="prim1",
            wire=poly, contact=via, min_contact_space=0.1,
            indicator=polyres, min_indicator_extension=0.5,
            implant=nimpl, min_implant_enclosure=_prp.Enclosure(0.1),
        )
        prim2 = _prm.Resistor(
            name="prim2", min_width=1.0, min_space=1.5,
            wire=m1, contact=None, indicator=m1res, min_indicator_extension=0.5,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)
        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

        # Test technology with only one mask to remove for conn_mask
        # of _Conductor
        m1 = _prm.TopMetalWire(name="m1", min_width=1.0, min_space=1.0)
        via = _prm.Via(
            name="via", width=0.8, min_space=0.8,
            bottom=(active, poly), min_bottom_enclosure=_prp.Enclosure(0.4),
            top=m1, min_top_enclosure=_prp.Enclosure(0.4),
        )
        class MyTech(_tch.Technology):
            @property
            def name(self):
                return "MyTech"
            @property
            def grid(self):
                return 0.005

            def __init__(self):
                super().__init__(primitives=_prm.Primitives((
                    _prm.Base(type_=_prm.pBase),
                    well, nimpl, pimpl, active,
                    poly, polyres, prim1,
                    via, m1,
                )))
        MyTech()

    def test_mimcapacitor(self): # Also include MIMTop
        m1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
        m2 = _prm.MetalWire(name="metal2", min_width=1.0, min_space=1.0)
        m3 = _prm.MetalWire(name="metal3", min_width=1.0, min_space=1.0)
        mimtop = _prm.MIMTop(name="mimtop", min_width=1.0, min_space=1.0)
        mimtop2 = _prm.MIMTop(name="mimtop2", min_width=1.0, min_space=1.0)
        via = _prm.Via(
            name="via", width=0.8, min_space=0.8,
            bottom=(m1, mimtop), min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m2, min_top_enclosure=_prp.Enclosure(0.2),
        )
        via2 = _prm.Via(
            name="via2", width=0.8, min_space=0.8,
            bottom=(m1, mimtop), min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m3, min_top_enclosure=_prp.Enclosure(0.2),
        )
        with self.assertRaises(ValueError):
            # bottom not in via.bottom
            _prm.MIMCapacitor(
                name="error",
                bottom=m3, top=mimtop, via=via,
                min_bottom_top_enclosure=_prp.Enclosure(0.2),
                min_bottomvia_top_space=0.1,
                min_top_via_enclosure=_prp.Enclosure(0.1),
                min_bottom_space=None, min_top2bottom_space=None,
            )
        with self.assertRaises(ValueError):
            # top not in via.bottom
            _prm.MIMCapacitor(
                name="error",
                bottom=m1, top=mimtop2, via=via,
                min_bottom_top_enclosure=_prp.Enclosure(0.2),
                min_bottomvia_top_space=0.1,
                min_top_via_enclosure=_prp.Enclosure(0.1),
                min_bottom_space=None, min_top2bottom_space=None,
            )
        with self.assertRaises(ValueError):
            # min_width too small
            _prm.MIMCapacitor(
                name="error", min_width=0.5,
                bottom=m1, top=mimtop, via=via,
                min_bottom_top_enclosure=_prp.Enclosure(0.2),
                min_bottomvia_top_space=0.1,
                min_top_via_enclosure=_prp.Enclosure(0.1),
                min_bottom_space=None, min_top2bottom_space=None,
            )

        prim1 = _prm.MIMCapacitor(
            name="prim1",
            bottom=m1, top=mimtop, via=via,
            min_bottom_top_enclosure=_prp.Enclosure(0.2),
            min_bottomvia_top_space=0.1,
            min_top_via_enclosure=_prp.Enclosure(0.1),
            min_bottom_space=None, min_top2bottom_space=None,
        )
        prim1bis = _prm.MIMCapacitor(
            name="prim1",
            bottom=m1, top=mimtop, via=via,
            min_bottom_top_enclosure=_prp.Enclosure(0.2),
            min_bottomvia_top_space=0.1,
            min_top_via_enclosure=_prp.Enclosure(0.1),
            min_bottom_space=None, min_top2bottom_space=None,
        )
        prim2 = _prm.MIMCapacitor(
            name="prim2",
            bottom=m1, top=mimtop, via=via2,
            min_bottom_top_enclosure=_prp.Enclosure(0.2),
            min_bottomvia_top_space=0.1,
            min_top_via_enclosure=_prp.Enclosure(0.1),
            min_bottom_space=None, min_top2bottom_space=None,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(mimtop._generate_rules(tech=dummy_tech))
        self.assertIn(mimtop.mask, rules)
        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)
        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

    def test_diode(self):
        nwell = _prm.Well(
            name="nwell", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )
        pwell = _prm.Well(
            name="pwell", min_width=1.0, min_space=1.0, type_=_prm.pImpl,
        )
        nimpl = _prm.Implant(
            name="nimplant", min_width=0.5, min_space=0.5, type_=_prm.nImpl,
        )
        nimpl2 = _prm.Implant(
            name="nimplant2", min_width=0.5, min_space=0.5, type_=_prm.nImpl,
        )
        pimpl = _prm.Implant(
            name="pimplant", min_width=0.5, min_space=0.5, type_=_prm.pImpl,
        )
        active = _prm.WaferWire(
            name="aa", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=pwell, min_well_enclosure=_prp.Enclosure(0.1),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            allow_well_crossing=False,
        )
        active2 = _prm.WaferWire(
            name="aa2", min_width=1.0, min_space=1.0,
            allow_in_substrate=False,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=(nwell, pwell), min_well_enclosure=_prp.Enclosure(0.1),
            allow_well_crossing=False,
        )
        actdiode = _prm.Marker(name="aadiode")
        mask = _msk.DesignMask(name="mask")

        with self.assertRaises(TypeError):
            # grid parameter given
            _prm.Diode(
                name="error", wire=active, grid=0.01,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl,
            )
        with self.assertRaises(ValueError):
            prim1 = _prm.Diode(
                name="prim1", wire=active, min_width=1.2,
                indicator=(), min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl,
            )
        with self.assertRaises(ValueError):
            # min_width too small
            _prm.Diode(
                name="error", wire=active, min_width=0.5,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl,
            )
        with self.assertRaises(TypeError):
            # implant is a well
            _prm.Diode(
                name="error", wire=active,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pwell,
            )
        with self.assertRaises(ValueError):
            # wrong implant
            _prm.Diode(
                name="error", wire=active,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=nimpl2,
            )
        with self.assertRaises(TypeError):
            # mask parameter given
            _prm.Diode(
                name="error", mask=mask, wire=active,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl,
            )
        with self.assertRaises(TypeError):
            # well nbt provided for WaferWire with allow_in_substrate == False
            _prm.Diode(
                name="error", wire=active2,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=nimpl,
            )
        with self.assertRaises(TypeError):
            # min_well_enclsoure without well
            _prm.Diode(
                name="error", wire=active,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl, min_well_enclosure=_prp.Enclosure(0.2),
            )
        with self.assertRaises(ValueError):
            # well not valid for wire
            _prm.Diode(
                name="error", wire=active,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl, well=nwell,
            )
        with self.assertRaises(ValueError):
            # well type euqal to implant type
            _prm.Diode(
                name="error", wire=active2,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl, well=pwell,
            )

        prim1 = _prm.Diode(
            name="prim1", wire=active, min_width=1.2,
            indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
            implant=pimpl, min_implant_enclosure=_prp.Enclosure(0.05),
        )
        prim1bis = _prm.Diode(
            name="prim1", wire=active, min_width=1.2,
            indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
            implant=pimpl,
        )
        prim2 = _prm.Diode(
            name="prim2", wire=active2,
            indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
            implant=nimpl, well=pwell,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)
        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

    def test_mosfet(self): # also test MOSFETGate
        well = _prm.Well(
            name="well", min_width=1.0, min_space=1.0, type_=_prm.pImpl,
        )
        well2 = _prm.Well(
            name="well2", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )
        nimpl = _prm.Implant(
            name="nimplant", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )
        nimpl2 = _prm.Implant(
            name="nimplant2", min_width=1.0, min_space=1.0, type_=_prm.nImpl,
        )
        pimpl = _prm.Implant(
            name="pimplant", min_width=1.0, min_space=1.0, type_=_prm.pImpl,
        )
        adjust = _prm.Implant(
            name="nimplant", min_width=1.0, min_space=1.0, type_=_prm.adjImpl,
        )
        oxide = _prm.Insulator(name="oxide", min_width=1.0, min_space=1.0)
        oxide2 = _prm.Insulator(name="oxide2", min_width=1.0, min_space=1.0)
        active = _prm.WaferWire(
            name="aa", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl, adjust), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            allow_well_crossing=False,
            oxide=oxide,
        )
        active2 = _prm.WaferWire(
            name="aa2", min_width=1.0, min_space=1.0,
            allow_in_substrate=False,
            implant=(nimpl, pimpl, adjust), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=(well, well2), min_well_enclosure=_prp.Enclosure(0.1),
            allow_well_crossing=False,
            oxide=oxide,
        )
        poly = _prm.GateWire(name="poly", min_width=1.0, min_space=1.0)
        m1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
        ch = _prm.Via(
            name="ch", width=0.8, min_space=0.8,
            bottom=(active, poly), min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m1, min_top_enclosure=_prp.Enclosure(0.2),
        )
        hv = _prm.Marker(name="hv")

        # MOSFETGate
        with self.assertRaises(ValueError):
            # wrong oxide for active
            _prm.MOSFETGate(
                name="error", active=active, poly=poly,
                min_sd_width=0.15, min_polyactive_extension=0.2,
                oxide=oxide2,
            )
        with self.assertRaises(TypeError):
            # min_gateoxide_enclosure without oxide
            _prm.MOSFETGate(
                name="error", active=active, poly=poly,
                min_sd_width=0.15, min_polyactive_extension=0.2,
                min_gateoxide_enclosure=_prp.Enclosure(0.2),
            )
        with self.assertRaises(TypeError):
            # min_gateinside_enclosure without oxide
            _prm.MOSFETGate(
                name="error", active=active, poly=poly,
                min_sd_width=0.15, min_polyactive_extension=0.2,
                min_gateinside_enclosure=_prp.Enclosure(0.2),
            )
        with self.assertRaises(TypeError):
            # min_contactgate_space without contact
            _prm.MOSFETGate(
                name="error", active=active, poly=poly,
                min_sd_width=0.15, min_polyactive_extension=0.2,
                min_contactgate_space=0.15,
            )
        with self.assertRaises(TypeError):
            # contact with min_contactgate_space
            _prm.MOSFETGate(
                name="error", active=active, poly=poly, min_gate_space=1.5,
                min_sd_width=0.15, min_polyactive_extension=0.2,
                contact=ch,
            )

        gate1 = _prm.MOSFETGate(
            name="gate1", active=active, poly=poly, min_gate_space=1.5,
            min_sd_width=0.15, min_polyactive_extension=0.2,
            contact=ch, min_contactgate_space=0.1,
        )
        gate2 = _prm.MOSFETGate(
            active=active, poly=poly, oxide=oxide, min_w=1.5,
            inside=hv, min_gateinside_enclosure=_prp.Enclosure(0.2),
        )
        gate3 = _prm.MOSFETGate(
            active=active2, poly=poly, oxide=oxide, min_w=1.5,
            inside=hv, min_gateinside_enclosure=_prp.Enclosure(0.2),
        )

        self.assertNotEqual(gate1, gate2)
        self.assertNotEqual(gate1, gate3)

        self.assertAlmostEqual(gate1.min_contactgate_space, 0.1, places=6)
        self.assertAlmostEqual(gate2.computed.min_l, 1.0, places=6)

        # MOSFET
        with self.assertRaises(ValueError):
            # both n and p type implants
            _prm.MOSFET(
                name="error", gate=gate1, min_l=1.5, min_w=1.5,
                implant=(nimpl, pimpl), min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_contactgate_space=0.15, well=well,
            )
        with self.assertRaises(ValueError):
            # invalid implant for gate.active
            _prm.MOSFET(
                name="error", gate=gate1, min_l=1.5, min_w=1.5,
                implant=nimpl2, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_contactgate_space=0.15, well=well,
            )
        with self.assertRaises(ValueError):
            # no well when gate.active.allow_in_substrate is None
            _prm.MOSFET(
                name="error", gate=gate3, min_l=1.5, min_w=1.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_contactgate_space=0.15,
            )
        with self.assertRaises(ValueError):
            # invalid well for gate.active
            _prm.MOSFET(
                name="error", gate=gate1, min_l=1.5, min_w=1.5,
                implant=pimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_contactgate_space=0.15, well=well2,
            )
        with self.assertRaises(ValueError):
            _prm.MOSFET(
                name="error", gate=gate1, min_l=1.5, min_w=1.5,
                implant=pimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_contactgate_space=0.15, well=well,
            )
        with self.assertRaises(ValueError):
            # too low min_l,
            _prm.MOSFET(
                name="error", gate=gate1, min_l=0.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
            )
        with self.assertRaises(ValueError):
            # too low min_w,
            _prm.MOSFET(
                name="error", gate=gate1, min_w=0.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
            )
        with self.assertRaises(ValueError):
            # no min_sd_width
            _prm.MOSFET(
                name="error", gate=gate2, min_gate_space=1.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_polyactive_extension=0.2,
            )
        with self.assertRaises(ValueError):
            # no min_polyactive_extension
            _prm.MOSFET(
                name="error", gate=gate2, min_gate_space=1.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_sd_width=0.15,
            )
        with self.assertRaises(ValueError):
            # min_contactgate_space without contact
            _prm.MOSFET(
                name="error", gate=gate2, min_gate_space=1.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_sd_width=0.15, min_polyactive_extension=0.2,
                min_contactgate_space=0.1,
            )
        with self.assertRaises(ValueError):
            # contact without min_contactgate_space
            _prm.MOSFET(
                name="error", gate=gate2, min_gate_space=1.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_sd_width=0.15, min_polyactive_extension=0.2,
                contact=ch,
            )

        prim1 = _prm.MOSFET(
            name="prim1", gate=gate1, min_l=1.5, min_w=1.5,
            implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
        )
        prim1bis = _prm.MOSFET(
            name="prim1", gate=gate1, min_l=1.5, min_w=1.5,
            implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
        )
        prim2 = _prm.MOSFET(
            name="prim2", gate=gate2, min_gate_space=1.5,
            implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
            min_sd_width=0.15, min_polyactive_extension=0.2,
            contact=ch, min_contactgate_space=0.1,
        )
        prim3 = _prm.MOSFET(
            name="prim3", gate=gate1, min_l=1.5, max_l=10.0, min_w=1.5,
            implant=(), min_gateimplant_enclosure=(),
            min_contactgate_space=0.15, well=well,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)
        self.assertNotEqual(prim1, prim3)

        self.assertTrue(prim1.has_typeimplant)
        self.assertTrue(prim2.has_typeimplant)
        self.assertFalse(prim3.has_typeimplant)

        self.assertAlmostEqual(prim1.computed.min_l, 1.5, places=6)
        self.assertAlmostEqual(prim1.computed.min_sd_width, 0.15, places=6)
        self.assertAlmostEqual(prim1.computed.min_contactgate_space, 0.1, places=6)
        self.assertAlmostEqual(prim3.computed.min_contactgate_space, 0.15, places=6)
        self.assertEqual(prim1.computed.contact, ch)
        self.assertAlmostEqual(prim2.computed.min_l, 1.0, places=6)
        self.assertAlmostEqual(prim2.computed.min_sd_width, 0.15, places=6)
        self.assertAlmostEqual(prim3.computed.max_l, 10.0, places=6)
        self.assertIsNone(prim3.computed.max_w)

        # Use primitives from dummy_tech for generate_rules testing
        # This is to be sure proper connectivity is there
        dummy_prims = dummy_tech.primitives
        dummy_mosgate = dummy_prims.mosgate
        dummy_nmos = dummy_prims.nmos
        dummy_pmos = dummy_prims.pmos
        self.assertIn(dummy_mosgate.mask, dummy_mosgate.rules)
        self.assertNotIn(dummy_mosgate.mask, dummy_nmos.rules)
        self.assertNotIn(dummy_mosgate.mask, dummy_pmos.rules)

    def test_bipolartype(self):
        self.assertEqual(_prm.npnBipolar, _prm.npnBipolar)
        self.assertNotEqual(_prm.npnBipolar, _prm.pnpBipolar)

        self.assertEqual(hash(_prm.npnBipolar), hash(_prm.npnBipolar))
        self.assertNotEqual(hash(_prm.npnBipolar), hash(_prm.pnpBipolar))

        with self.assertWarns(UserWarning):
            _prm.npnBipolar == "npn"

    def test_bipolar(self):
        npn = _prm.Marker(name="npn")
        pnp = _prm.Marker(name="pnp")

        prim1 = _prm.Bipolar(name="prim1", type_=_prm.npnBipolar, indicator=npn)
        prim1bis = _prm.Bipolar(name="prim1", type_=_prm.npnBipolar, indicator=npn)
        prim2 = _prm.Bipolar(name="prim2", type_=_prm.pnpBipolar, indicator=pnp)

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        tuple(prim1._generate_rules(tech=dummy_tech))
        tuple(prim2._generate_rules(tech=dummy_tech))

        self.assertIn(npn.mask, prim1.designmasks)
        self.assertIn(pnp.mask, prim2.designmasks)

    def test_ruleprimitive(self):
        with self.assertRaises(TypeError):
            # abstract methods
            _prmrule._RulePrimitive(name="error")

    def test_minwidth(self):
        dummy_prims = dummy_tech.primitives
        active = dummy_prims.active
        hvox = dummy_prims.hvox
        nplus = dummy_prims.nplus

        prim1 = _prm.MinWidth(prim=active.in_(hvox), min_width=0.5)
        prim1bis = _prm.MinWidth(prim=active.in_(hvox), min_width=0.5)
        prim2 = _prm.MinWidth(prim=active.in_(hvox), min_width=0.4)
        prim3 = _prm.MinWidth(prim=active.in_(nplus), min_width=0.5)

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)
        self.assertNotEqual(prim1, prim3)

    def test_spacing(self):
        dummy_prims = dummy_tech.primitives
        nplus = dummy_prims.nplus
        pplus = dummy_prims.nplus
        poly = dummy_prims.poly
        mosgate = dummy_prims.mosgate

        prim1 = _prm.Spacing(primitives1=(nplus, pplus), min_space=0.2)
        prim1bis = _prm.Spacing(primitives1=(nplus, pplus), min_space=0.2)
        prim2 = _prm.Spacing(primitives1=(nplus, pplus, poly), min_space=0.2)
        prim3 = _prm.Spacing(
            primitives1=(nplus, pplus), primitives2=mosgate, min_space=0.25,
        )

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(
            _msk.Join(prim.mask for prim in (nplus, pplus)).space >= prim1.min_space,
            rules,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)
        self.assertNotEqual(prim1, prim3)

        self.assertEqual(
            repr(prim1),
            "Spacing((nplus,nplus),None,0.2)",
        )
        self.assertIn(nplus.mask, prim1.designmasks)
        self.assertIn(nplus.mask, prim3.designmasks)
        self.assertIn(poly.mask, prim3.designmasks)

    def test_enclosure(self):
        # Use primitives from dummy_tech
        dummy_prims = dummy_tech.primitives
        nplus = dummy_prims.nplus
        pplus = dummy_prims.pplus
        poly = dummy_prims.poly

        prim1 = _prm.Enclosure(prim=poly, by=nplus, min_enclosure=_prp.Enclosure(0.2))
        prim1bis = _prm.Enclosure(prim=poly, by=nplus, min_enclosure=_prp.Enclosure(0.2))
        prim2 = _prm.Enclosure(prim=poly, by=pplus, min_enclosure=_prp.Enclosure(0.2))
        prim3 = _prm.Enclosure(prim=poly, by=nplus, min_enclosure=_prp.Enclosure(0.15))

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)
        self.assertNotEqual(prim1, prim3)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(
            poly.mask.enclosed_by(nplus.mask) >= _prp.Enclosure(0.2),
            rules,
        )

        self.assertIn(poly.mask, prim1.designmasks)
        self.assertIn(nplus.mask, prim1.designmasks)

        self.assertEqual(
            repr(prim1),
            "Enclosure(prim=GateWire(name=poly),by=Implant(name=nplus),min_enclosure=Enclosure(0.2))",
        )

    def test_nooverlap(self):
        # Use primitives from dummy_tech
        dummy_prims = dummy_tech.primitives
        nplus = dummy_prims.nplus
        pplus = dummy_prims.pplus
        poly = dummy_prims.poly

        prim1 = _prm.NoOverlap(prim1=nplus, prim2=pplus)
        prim1bis = _prm.NoOverlap(prim1=nplus, prim2=pplus)
        prim2 = _prm.NoOverlap(prim1=nplus, prim2=poly)

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(
            _prmderv._Intersect(prims=(nplus, pplus)).mask.area == 0.0,
            rules,
        )

        self.assertIn(nplus.mask, prim1.designmasks)
        self.assertIn(poly.mask, prim2.designmasks)

        self.assertEqual(
            repr(prim1),
            "NoOverlap(prim1=Implant(name=nplus),prim2=Implant(name=pplus))",
        )

    def test_primitives(self):
        # Use primitives from dummy_tech
        dummy_prims = dummy_tech.primitives
        nplus = dummy_prims.nplus
        active = dummy_prims.active

        with self.assertRaises(TypeError):
            # _DerivedPrimitive
            prims = _prm.Primitives()
            prims += active.in_(nplus)
        with self.assertRaises(ValueError):
            # Primitive added twice
            prims = _prm.Primitives(nplus)
            prims += nplus


    # The exceptions will be used and tested by the technology_ unit test
