# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

# Use mainly dummy_tech for checking and code coverage
from ..dummy import dummy_tech
dummy_prims = dummy_tech.primitives

from pdkmaster.technology import (
    property_ as _prp, geometry as _geo, primitive as _prm, technology_ as _tch,
)

class TechnologyTest(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(ValueError):
            # no Base primitive
            class ErrorTech(_tch.Technology):
                def name(self):
                    return "error"
                def grid(self):
                    return 0.005

                def __init__(self):
                    super().__init__(primitives=_prm.Primitives())
            ErrorTech()

        with self.assertRaises(ValueError):
            # base not of type Base
            class ErrorTech(_tch.Technology):
                def name(self):
                    return "error"
                def grid(self):
                    return 0.005

                def __init__(self):
                    super().__init__(primitives=_prm.Primitives(
                        _prm.Auxiliary(name="base")
                    ))
            ErrorTech()

    def test_rules(self):
        # This is mainly a test for coverage
        self.assertEqual(len(dummy_tech.rules), 161)

    def test_computed(self):
        nwell = dummy_prims.nwell
        active = dummy_prims.active
        nplus = dummy_prims.nplus
        pplus = dummy_prims.pplus
        hvox = dummy_prims.hvox
        poly = dummy_prims.poly
        contact = dummy_prims.contact
        metal = dummy_prims.metal
        via = dummy_prims.via

        # min_space
        nenc = active.min_implant_enclosure[active.implant.index(nplus)].min()
        penc = active.min_implant_enclosure[active.implant.index(pplus)].min()
        nwenc = active.min_well_enclosure[active.well.index(nwell)].min()
        hvoxenc = active.min_oxide_enclosure[active.oxide.index(hvox)].min()
        hvoxspace = dummy_tech.computed.min_space(hvox, active)

        self.assertAlmostEqual(
            dummy_tech.computed.min_space(primitive1=active),
            active.min_space,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.computed.min_space(primitive1=active.in_(nplus)),
            active.min_space,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.computed.min_space(
                primitive1=active, primitive2=active.in_((pplus, hvox, nwell)),
            ),
            hvoxenc + hvoxspace,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.computed.min_space(
                primitive1=active.in_(nplus), primitive2=active,
            ),
            active.min_space,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.computed.min_space(
                primitive1=active.in_(nplus), primitive2=active.in_(pplus),
            ),
            nenc + penc,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.computed.min_space(
                primitive1=active.in_(nplus),
                primitive2=active.in_((pplus, nwell, hvox)),
            ),
            nenc + max(penc, nwenc, hvoxenc),
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.computed.min_space(
                primitive1=metal, width=0.5,
            ),
            0.5, places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.computed.min_space(
                primitive1=metal, width=1.1,
            ),
            1.0, places=6,
        )
        with self.assertRaises(AttributeError):
            # No min_space between active and poly
            dummy_tech.computed.min_space(
                primitive1=active, primitive2=poly
            )
        with self.assertRaises(TypeError):
            # width provided and primitive1 is derived layer
            dummy_tech.computed.min_space(
                primitive1=active.in_(nplus), width=1.0,
            )
        with self.assertRaises(TypeError):
            # width provided and also primitive2
            dummy_tech.computed.min_space(
                primitive1=active, primitive2=poly, width=1.0,
            )

        # min_width
        self.assertAlmostEqual(
            dummy_tech.computed.min_width(primitive=active),
            active.min_width,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.computed.min_width(
                primitive=metal, up=True, down=True,
            ),
            max(
                metal.min_width,
                contact.width + 2*contact.min_top_enclosure[0].max(),
                via.width + 2*via.min_bottom_enclosure[0].max(),
            ),
            places=6,
        )

        # min_pitch
        self.assertAlmostEqual(
            dummy_tech.computed.min_pitch(primitive=active),
            active.min_width + active.min_space,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.computed.min_pitch(
                primitive=metal, up=True, down=True,
            ),
            max(
                metal.min_width,
                contact.width + 2*contact.min_top_enclosure[0].max(),
                via.width + 2*via.min_bottom_enclosure[0].max(),
            ) + metal.min_space,
            places=6,
        )

    def test_ongrid(self):
        grid = dummy_tech.grid

        # is_ongrid() method
        self.assertTrue(dummy_tech.is_ongrid(grid))
        self.assertFalse(dummy_tech.is_ongrid(grid/2))

        # on_grid() method
        with self.assertRaises(ValueError):
            # Wrong rounding specification
            dummy_tech.on_grid(1.1*grid, rounding="error")

        self.assertAlmostEqual(
            dummy_tech.on_grid(1.1*grid, rounding="nearest"),
            grid,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.on_grid(1.1*grid, rounding="floor"),
            grid,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.on_grid(1.1*grid, rounding="ceiling"),
            2*grid,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.on_grid(3.1*grid, mult=2, rounding="nearest"),
            4*grid,
            places=6,
        )

        self.assertEqual(
            dummy_tech.on_grid(_geo.Point(x=1.1*grid, y=1.1*grid)),
            _geo.Point(x=grid, y=grid),
        )

    def test_dbu1(self):
        self.assertAlmostEqual(dummy_tech.dbu, 1e-3, delta=_geo.epsilon)

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 2.5e-3

            def __init__(self):
                super().__init__(primitives=_prm.Primitives(
                    _prm.Base(type_=_prm.pBase),
                ))
        mytech = MyTech()
        self.assertAlmostEqual(mytech.dbu, 1e-4, delta=_geo.epsilon)

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 1.25e-3

            def __init__(self):
                super().__init__(primitives=_prm.Primitives(
                    _prm.Base(type_=_prm.pBase),
                ))
        mytech = MyTech()
        self.assertAlmostEqual(mytech.dbu, 1e-5, delta=_geo.epsilon)

    def test_padopening(self):
        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3

            def __init__(self):
                prims = _prm.Primitives(_prm.Base(type_=_prm.pBase))

                metal1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
                pad = _prm.PadOpening(
                    name="pad", min_width=20.0, min_space=3.0,
                    bottom=metal1, min_bottom_enclosure=2.0,
                )
                prims += (metal1, pad)

                super().__init__(primitives=prims)
        # Code coverage only
        MyTech()

    def test_substrate(self):
        self.assertEqual(
            dummy_tech.substrate_prim,
            dummy_prims.base.remove(dummy_prims.active.well).alias("substrate:Dummy"),
        )

    def test_mosfet(self):
        nmos = dummy_prims.nmos
        prim = _prm._derived._Intersect(prims=(nmos.gate, *nmos.implant)).remove(nmos.gate.active.well)
        alias = prim.alias("gate:mosfet:nmos")
        self.assertEqual(nmos.gate4mosfet._prim, prim)
        self.assertEqual(nmos.gate4mosfet, alias)

    def test_check(self):
        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 2.5e-3

            def __init__(self):
                prims = _prm.Primitives(_prm.Base(type_=_prm.pBase))

                prims += _prm.Well(
                    name="well", min_width=5.0, min_space=3.0, type_=_prm.nImpl,
                )

                super().__init__(primitives=prims)
        with self.assertRaises(_prm.UnconnectedPrimitiveError):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3

            def __init__(self):
                prims = _prm.Primitives(_prm.Base(type_=_prm.pBase))

                metal1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
                prims += metal1

                super().__init__(primitives=prims)
        with self.assertRaises(_prm.UnusedPrimitiveError):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3

            def __init__(self):
                prims = _prm.Primitives(_prm.Base(type_=_prm.pBase))

                nimpl = _prm.Implant(
                    name="nimplant", min_width=1.2, min_space=1.2, type_=_prm.nImpl,
                )
                pimpl = _prm.Implant(
                    name="pimplant", min_width=1.2, min_space=1.2, type_=_prm.pImpl,
                )
                nwell = _prm.Well(
                    name="nwell", min_width=5.0, min_space=3.0, type_=_prm.nImpl,
                )
                prims += (nimpl, pimpl, nwell)

                active = _prm.WaferWire(
                    name="active", min_width=0.8, min_space=0.8,
                    implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.2),
                    implant_abut="all", allow_contactless_implant=False,
                    allow_in_substrate=True,
                    well=nwell, min_well_enclosure=_prp.Enclosure(0.8),
                    allow_well_crossing=False,
                )
                poly = _prm.GateWire(name="poly", min_width=0.8, min_space=0.8)
                prims += (active, poly)

                gate = _prm.MOSFETGate(
                    active=active, poly=poly,
                )
                prims += gate

                super().__init__(primitives=prims)
        with self.assertRaises(_prm.UnusedPrimitiveError):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3

            def __init__(self):
                prims = _prm.Primitives(_prm.Base(type_=_prm.pBase))

                nimpl = _prm.Implant(
                    name="nimplant", min_width=1.2, min_space=1.2, type_=_prm.nImpl,
                )
                pimpl = _prm.Implant(
                    name="pimplant", min_width=1.2, min_space=1.2, type_=_prm.pImpl,
                )
                nwell = _prm.Well(
                    name="nwell", min_width=5.0, min_space=3.0, type_=_prm.nImpl,
                )
                prims += (nimpl, pimpl, nwell)

                active = _prm.WaferWire(
                    name="active", min_width=0.8, min_space=0.8,
                    implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.2),
                    implant_abut="all", allow_contactless_implant=False,
                    allow_in_substrate=True,
                    well=nwell, min_well_enclosure=_prp.Enclosure(0.8),
                    allow_well_crossing=False,
                )
                poly = _prm.GateWire(name="poly", min_width=0.8, min_space=0.8)
                metal1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
                contact = _prm.Via(
                    name="contact", width=0.8, min_space=0.8,
                    bottom=poly, min_bottom_enclosure=_prp.Enclosure(0.0),
                    top=metal1, min_top_enclosure=_prp.Enclosure(0.2),
                )
                prims += (active, poly, contact, metal1)

                gate = _prm.MOSFETGate(
                    active=active, poly=poly,
                    min_sd_width=0.35, min_polyactive_extension=0.35,
                )
                nmos = _prm.MOSFET(
                    name="nmos", gate=gate, implant=nimpl,
                    min_gateimplant_enclosure=_prp.Enclosure(0.3),
                )
                prims += (gate, nmos)

                super().__init__(primitives=prims)
        with self.assertRaises(_tch.Technology.ConnectionError):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3

            def __init__(self):
                prims = _prm.Primitives(_prm.Base(type_=_prm.pBase))

                nimpl = _prm.Implant(
                    name="nimplant", min_width=1.2, min_space=1.2, type_=_prm.nImpl,
                )
                pimpl = _prm.Implant(
                    name="pimplant", min_width=1.2, min_space=1.2, type_=_prm.pImpl,
                )
                nwell = _prm.Well(
                    name="nwell", min_width=5.0, min_space=3.0, type_=_prm.nImpl,
                )
                prims += (nimpl, pimpl, nwell)

                active = _prm.WaferWire(
                    name="active", min_width=0.8, min_space=0.8,
                    implant=nimpl, min_implant_enclosure=_prp.Enclosure(0.2),
                    implant_abut="all", allow_contactless_implant=False,
                    allow_in_substrate=True,
                    well=nwell, min_well_enclosure=_prp.Enclosure(0.8),
                    allow_well_crossing=False,
                )
                poly = _prm.GateWire(name="poly", min_width=0.8, min_space=0.8)
                metal1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
                contact = _prm.Via(
                    name="contact", width=0.8, min_space=0.8,
                    bottom=(active, poly), min_bottom_enclosure=_prp.Enclosure(0.0),
                    top=metal1, min_top_enclosure=_prp.Enclosure(0.2),
                )
                prims += (active, poly, contact, metal1)

                gate = _prm.MOSFETGate(
                    active=active, poly=poly,
                    min_sd_width=0.35, min_polyactive_extension=0.35,
                )
                nmos_impl = _prm.MOSFET(
                    name="nmos_impl", gate=gate, implant=nimpl,
                    min_gateimplant_enclosure=_prp.Enclosure(0.3),
                )
                nmos_noimpl = _prm.MOSFET(
                    name="nmos_noimpl", gate=gate, implant=(),
                    min_gateimplant_enclosure=(),
                )
                prims += (gate, nmos_impl, nmos_noimpl)

                super().__init__(primitives=prims)
        with self.assertRaises(ValueError):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3

            def __init__(self):
                prims = _prm.Primitives(_prm.Base(type_=_prm.pBase))

                metal1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
                metal2 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
                via = _prm.Via(
                    name="via", width=0.8, min_space=0.8,
                    bottom=metal1, min_bottom_enclosure=_prp.Enclosure(0.2),
                    top=metal2, min_top_enclosure=_prp.Enclosure(0.2),
                )
                prims += (metal1, via, metal2)

                super().__init__(primitives=prims)
        with self.assertRaises(_tch.Technology.ConnectionError):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3

            def __init__(self):
                super().__init__(primitives=_prm.Primitives((
                    _prm.Base(type_=_prm.pBase),
                    _prm.MIMTop(name="error", min_width=1.0, min_space=1.0),
                )))
        with self.assertRaises(_prm.UnusedPrimitiveError):
            MyTech()

        # Accessing substrate_prim before primitives were added
        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3

            def __init__(self):
                self.substrate_prim
        with self.assertRaises(AttributeError):
            MyTech()
