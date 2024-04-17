# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest
from typing import cast

from pdkmaster.technology import (
    property_ as _prp, mask as _msk, net as _net, geometry as _geo, primitive as _prm,
)
from pdkmaster.design import layout as _lay, cell as _cell
from pdkmaster.design.layout import (
    layout_ as _laylay, _primitivelayouter as _layprim,
)

from ..dummy import dummy_tech, dummy_cktfab, dummy_layoutfab, dummy_lib
prims = dummy_tech.primitives


class TestNet(_net._Net):
    # Non-abstract net class
    def __init__(self, name: str):
        super().__init__(name)


class LayoutParamTest(unittest.TestCase):
    def test_enclosurelayoutparam(self):
        param = _layprim._EnclosureLayoutParam(primitive=prims.active, name="test")

        with self.assertRaises(TypeError):
            param.cast(None)
        with self.assertRaises(TypeError):
            param.cast("error")

        param = _layprim._EnclosureLayoutParam(
            primitive=prims.active, name="test", default=_prp.Enclosure(2.0),
        )

        enc = cast(_prp.Enclosure, param.cast(None))
        self.assertFalse(enc.is_assymetric)
        self.assertAlmostEqual(enc.first, 2.0)

        enc = cast(_prp.Enclosure, param.cast(3.0))
        self.assertFalse(enc.is_assymetric)
        self.assertAlmostEqual(enc.first, 3.0)

    def test_enclosureslayoutparam(self):
        param = _layprim._EnclosuresLayoutParam(primitive=prims.active, name="test", n=2)

        with self.assertRaises(TypeError):
            param.cast(None)
        with self.assertRaises(TypeError):
            param.cast("error")
        with self.assertRaises(TypeError):
            param.cast(("error", "error"))

        default = (_prp.Enclosure(0.2), _prp.Enclosure(0.3))
        param = _layprim._EnclosuresLayoutParam(
            primitive=prims.active, name="test", n=2, default=default,
        )

        self.assertEqual(param.cast(None), default)

        v = 0.25
        enc = _prp.Enclosure(v)
        self.assertEqual(param.cast(v), (enc, enc))

        v = (None, _prp.Enclosure(0.15))
        self.assertEqual(param.cast(v), v)


class LayoutParamCasterTest(unittest.TestCase):
    def test_caster(self):
        caster = _layprim._LayoutParamCaster()

        nwell = prims.nwell
        active = prims.active
        poly = prims.poly
        nplus = prims.nplus
        pplus = prims.pplus
        sub = prims.substrate
        hvox = prims.hvox
        ch = prims.contact
        metal = prims.metal
        metalpin = prims.metalpin
        metal2 = prims.metal2
        metal2pin = prims.metal2pin
        diodemark = prims.diodemark
        ndiode = cast(_prm.Diode, prims.ndiode)
        nmos = prims.nmos

        # WaferWire with single implant
        active2 = _prm.WaferWire(
            name="active2", min_width=0.2, min_space=0.5,
            allow_in_substrate=False,
            implant=nplus, min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut=nplus, allow_contactless_implant=False,
            well=nwell, min_well_enclosure=_prp.Enclosure(0.1),
            min_well_enclosure_same_type=_prp.Enclosure(0.08),
            allow_well_crossing=False,
            oxide=hvox, min_oxide_enclosure=_prp.Enclosure(0.08),
        )

        class MyNet(_net._Net):
            def __init__(self, name: str):
                super().__init__(name)
        net = MyNet("net")

        # Unexpected parameter
        with self.assertRaises(TypeError):
            caster(prim=active, implant=nplus, error="error")

        # Wrong extra_net type
        with self.assertRaises(TypeError):
            caster(prim=nwell, extra=sub, extra_net=2.0)

        # Wrong number of extra_net arguments
        with self.assertRaises(ValueError):
            caster(prim=poly, extra=(nplus, sub), extra_net=(None, None, None))

        # Wrong number of extra_enclosure arguments
        with self.assertRaises(ValueError):
            caster(prim=poly, extra=(nplus, sub), extra_enclosure=(None, None, None))

        params = caster(prim=active, implant=nplus, height=4.0, extra=sub, extra_net=(None,))

        self.assertAlmostEqual(params["width"], active.min_width)
        self.assertAlmostEqual(params["height"], 4.0)
        self.assertEqual(params["extra"], (sub,))
        self.assertEqual(params["extra_net"], (None,))
        self.assertEqual(params["extra_enclosure"], (None,))

        enc = _prp.Enclosure(0.005)
        params = caster(
            prim=active, extra=(hvox, sub), extra_net=(None,), extra_enclosure=enc,
        )

        self.assertEqual(params["extra_net"], (None, None))
        self.assertEqual(params["extra_enclosure"], (enc, enc))

        params = caster(prim=metalpin, width=2.0)

        self.assertAlmostEqual(params["width"], 2.0)
        self.assertIsNone(params["height"])

        with self.assertRaises(ValueError):
            caster(prim=metal, pin=metal2pin)

        ### WaferWire
        enc = _prp.Enclosure(1.0)
        params = caster(prim=active, implant=(nplus, pplus), implant_enclosure=enc)
        self.assertEqual(
            params["implant_enclosure"], (enc, enc),
        )

        params = caster(prim=active2, well_net=net, oxide=hvox)
        self.assertEqual(params["implant"], ())
        self.assertEqual(params["implant_enclosure"], ())
        self.assertEqual(params["well"], nwell)
        self.assertAlmostEqual(params["oxide_enclosure"].first, 0.08)

        # Wrong implant type
        with self.assertRaises(TypeError):
            caster(prim=active2, implant=5, well_net=net)
        with self.assertRaises(TypeError):
            caster(prim=active2, implant=(5,), well_net=net)
        with self.assertRaises(ValueError):
            caster(prim=active2, implant=metal, well_net=net)
        with self.assertRaises(ValueError):
            caster(prim=active2, implant=(metal,), well_net=net)

        # implant_enclosure without implant
        with self.assertRaises(TypeError):
            caster(prim=active, implant_enclosure=1.0)

        # Wrong number of enclosures
        with self.assertRaises(ValueError):
            caster(prim=active, implant=(nplus, pplus), implant_enclosure=3*(enc,))

        ### Via errors

        # bottom WaferWire parameters given for GateWire bottom
        with self.assertRaises(TypeError):
            caster(prim=ch, bottom=poly, bottom_implant=nplus)
        with self.assertRaises(TypeError):
            caster(prim=ch, bottom=poly, bottom_implant_enclosure=0.3)
        with self.assertRaises(TypeError):
            caster(prim=ch, bottom=poly, bottom_well=nwell)
        with self.assertRaises(TypeError):
            caster(prim=ch, bottom=poly, bottom_well_enclosure=0.3)
        with self.assertRaises(TypeError):
            caster(prim=ch, bottom=poly, well_net=net)

        ### Via coverage

        # default bottom_well_enclosure
        params = caster(
            prim=ch, bottom=active, bottom_implant=pplus, bottom_well=nwell,
        )

        # via with one bottom and one top
        via2 = _prm.Via(
            name="via2", width=0.35, min_space=0.35,
            bottom=metal, top=metal2,
            min_bottom_enclosure=_prp.Enclosure(0.2), min_top_enclosure=_prp.Enclosure(0.15),
        )
        # default bottom & top
        params = caster(prim=via2)

        self.assertEqual(params["bottom"], metal)
        self.assertEqual(params["top"], metal2)

        # Diode to cover _DevicePrimitive
        params = caster(prim=ndiode, width=2.0, height=None)

        self.assertAlmostEqual(params["width"], 2.0)
        self.assertAlmostEqual(params["height"], active.min_width)
        self.assertEqual(params["implant_enclosure"], ndiode.min_implant_enclosure)

        dio2 = _prm.Diode(
            name="test_diode", wire=active, indicator=diodemark, min_indicator_enclosure=(None,),
            implant=(),
        )
        params = caster(prim=dio2, width=2.0, height=1.0)

        self.assertNotIn("implant_enclosure", params)

        # Wrong number of implant enclosures for MOSFET gate

        with self.assertRaises(TypeError):
            caster(prim=nmos, gateimplant_enclosures=(1.0, 2.0))


class LayoutTest(unittest.TestCase):
    def test__rect(self):

        self.assertEqual(
            _layprim._rect(left=0.0, bottom=0.0, right=1.0, top=1.0, enclosure=1.0),
            _layprim._rect(
                left=0.0, bottom=0.0, right=1.0, top=1.0,
                enclosure=_prp.Enclosure(1.0),
            ),
        )

    def test__via_array(self):
        left = 0.0
        bottom = 0.0
        width = 1.0
        pitch = 2.0

        via = _geo.Rect.from_size(width=width, height=width)
        point = _geo.Point(x=(left + 0.5*width), y=(bottom + 0.5*width))

        self.assertEqual(
            _layprim._via_array(
                left=left, bottom=bottom, width=width, pitch=pitch, rows=1, columns=1,
            ),
            via + point,
        )
        self.assertEqual(
            _layprim._via_array(
                left=left, bottom=bottom, width=width, pitch=pitch, rows=2, columns=2,
            ),
            _geo.ArrayShape(
                shape=via, offset0=point, rows=2, columns=2, pitch_x=pitch, pitch_y=pitch,
            ),
        )

    def test_maskshapessublayout(self):
        m1 = _msk.DesignMask(name="mask1")
        m2 = _msk.DesignMask(name="mask2")
        n1 = TestNet("net1")
        p = _geo.Point(x=3.0, y=-2.0)
        rot = _geo.Rotation.R90
        r1 = _geo.Rect(left=-3.0, bottom=-1.0, right=-1.0, top=1.0)
        r2 = _geo.Rect(left=1.0, bottom=-1.0, right=3.0, top=1.0)
        ms1 = _geo.MaskShape(mask=m1, shape=r1)
        ms2 = _geo.MaskShape(mask=m2, shape=r2)
        mssl1 = _laylay._MaskShapesSubLayout(
            net=n1, shapes=_geo.MaskShapes(ms1),
        )
        mssl2 = _laylay._MaskShapesSubLayout(
            net=None, shapes=_geo.MaskShapes(ms1),
        )
        mssl3 = _laylay._MaskShapesSubLayout(
            net=n1, shapes=_geo.MaskShapes((ms1, ms2)),
        )
        mssl4 = mssl1.dup()
        mssl4.add_shape(shape=ms2)

        self.assertNotEqual(mssl1, "")
        self.assertNotEqual(mssl1, mssl2)
        with self.assertRaises(TypeError):
            hash(mssl1)
        self.assertNotEqual(mssl1, mssl4)
        self.assertEqual(mssl3, mssl4)
        # Get coverage for _hier_strs_, don't check output
        s = "\n".join(mssl1._hier_strs_)

        mssl5 = mssl3.moved(dxy=p)
        mssl4.move(dxy=p)

        self.assertNotEqual(mssl3, mssl5)
        self.assertEqual(mssl4, mssl5)

        mssl6 = mssl3.rotated(rotation=rot).moved(dxy=p)
        mssl7 = mssl3.dup()
        mssl7.rotate(rotation=rot)
        mssl7.move(dxy=p)

        self.assertEqual(mssl6, mssl7)

    def test__instancesublayout(self):
        cell = _cell.Cell(
            name="cell",
            tech=dummy_tech, cktfab=dummy_cktfab, layoutfab=dummy_layoutfab,
        )
        ckt = cell.new_circuit()

        inst = ckt.instantiate(dummy_lib.cells.cell1, name="libcell1")

        cell2 = _cell.Cell(
            name="cell2",
            tech=dummy_tech, cktfab=dummy_cktfab, layoutfab=dummy_layoutfab,
        )
        # Create empty layout for cell2
        cell2.new_circuit()
        cell2.new_circuitlayouter()

        cell3 = _cell.Cell(
            name="cell3",
            tech=dummy_tech, cktfab=dummy_cktfab, layoutfab=dummy_layoutfab,
        )
        ckt3 = cell3.new_circuit()

        inst2 = ckt3.instantiate(cell, name="cell")
        inst3 = ckt3.instantiate(cell2, name="cell2")

        dxy = _geo.Point(x=0.0, y=1.0)
        rot = _geo.Rotation.MX

        with self.assertRaises(ValueError):
            # No layout
            _laylay._InstanceSubLayout(
                inst=inst2, origin=_geo.origin, layoutname=None, rotation=_geo.Rotation.R0,
            )
        with self.assertRaises(ValueError):
            # wrong layoutname
            _laylay._InstanceSubLayout(
                inst=inst2, origin=_geo.origin, layoutname="error", rotation=_geo.Rotation.R0,
            )

        sl1 = _laylay._InstanceSubLayout(
            inst=inst, origin=_geo.origin, layoutname=None, rotation=_geo.Rotation.R0,
        )
        sl2 = _laylay._InstanceSubLayout(
            inst=inst3, origin=_geo.origin, layoutname=None, rotation=_geo.Rotation.R0,
        )
        sl3 = sl2.rotated(rotation=rot).moved(dxy=dxy)
        sl4 = sl2.moved(dxy=dxy).rotated(rotation=rot)

        # Code coverage
        tuple(sl1.polygons)

        self.assertIs(sl2.boundary, None)

        self.assertEqual(sl2.origin, _geo.origin)
        sl2.rotate(rotation=rot)
        sl2.move(dxy=dxy)
        self.assertEqual(sl2.origin, sl3.origin)
        self.assertEqual(sl2.origin*rot, sl4.origin)
        self.assertEqual(sl2.rotation, sl3.rotation)
        self.assertEqual(sl2.rotation, sl4.rotation)

        # Code coverage
        tuple(sl1._hier_strs_)

    def test_sublayouts(self):
        mask = prims.metal.mask

        r1 = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        r2 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))
        r3 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))

        ms1 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=r1))
        ms2 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=r2))
        ms3 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=r3))

        sl1 = _laylay._MaskShapesSubLayout(net=None, shapes=ms1)
        sl2 = _laylay._MaskShapesSubLayout(net=None, shapes=ms2)
        sl3 = _laylay._MaskShapesSubLayout(net=None, shapes=ms3)

        with self.assertRaises(ValueError):
            # sublayouts for same net
            _laylay._SubLayouts((sl1, sl2))

        sls = _laylay._SubLayouts((sl1,))

        # Code coverage
        self.assertEqual(len(sls), 1)
        sls += sl2
        self.assertEqual(len(sls), 1)
        sls2 = sls.dup()

        sls3 = sls2 + sl3

    def test_add(self):
        mask = prims.metal.mask

        r1 = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        r2 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))
        r12 = _geo.Rect.from_floats(values=(0.0, 0.0, 2.0, 1.0))

        mps = _geo.MultiPartShape(fullshape=r12, parts=(r1, r2))

        ms1 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[0]))
        ms2 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[1]))

        sl1 = _laylay._MaskShapesSubLayout(net=None, shapes=ms1)
        sl2 = _laylay._MaskShapesSubLayout(net=None, shapes=ms2)

        lay = dummy_layoutfab.new_layout()
        lay += sl1
        lay += sl2

        lay2 = dummy_layoutfab.new_layout()
        lay2.add_shape(net=None, shape=ms1[0])
        lay2.add_shape(layer=prims.metal.mask, net=None, shape=mps.parts[1])

        for l, m in ((lay, "lay"), (lay2, "lay2")):
            self.assertEqual(len(l._sublayouts), 1)
            sl = cast(_laylay._MaskShapesSubLayout, l._sublayouts[0])
            self.assertIsInstance(sl, _laylay._MaskShapesSubLayout)
            self.assertIsNone(sl.net)
            self.assertEqual(len(sl.shapes), 1)
            ms = sl.shapes[0]
            s = cast(_geo.MultiShape, ms.shape)
            self.assertIsInstance(s, _geo.MultiShape)
            self.assertIn(mps.parts[0], s.shapes)
            self.assertIn(mps.parts[1], s.shapes)

    def test_move(self):
        mask = prims.metal.mask

        dxy = _geo.Point(x=0.0, y=1.0)

        r1 = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        r2 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))
        r12 = _geo.Rect.from_floats(values=(0.0, 0.0, 2.0, 1.0))

        mps = _geo.MultiPartShape(fullshape=r12, parts=(r1, r2))

        mss1 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[0]))
        mss2 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[1]))
        mus = _geo.MultiShape(shapes=(mps.parts[0], mps.parts[1]))
        mss3 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mus))

        sl1 = _laylay._MaskShapesSubLayout(net=None, shapes=mss1)
        sl2 = _laylay._MaskShapesSubLayout(net=None, shapes=mss2)
        sl3 = _laylay._MaskShapesSubLayout(net=None, shapes=mss3)

        layout = dummy_layoutfab.new_layout(sublayouts=sl3)

        mps_moved = mps.moved(dxy=dxy)

        # Make different version of the layout with the same move
        layout2 = layout.moved(dxy=dxy)
        layout.move(dxy=dxy)
        layout3 = dummy_layoutfab.new_layout()
        layout3 += layout

        l = dummy_layoutfab.new_layout()
        l += sl1
        l += sl2
        layout4 = l.moved(dxy=dxy)

        def get_parts(l: _lay.LayoutT):
            for sl in l._sublayouts.__iter_type__(_laylay._MaskShapesSubLayout):
                for ms in sl.shapes:
                    s = ms.shape
                    if isinstance(s, _geo.MultiPartShape._Part):
                        yield s
                    elif isinstance(s, _geo.MultiShape):
                        yield from filter(
                            lambda s2: isinstance(s2, _geo.MultiPartShape._Part),
                            s.shapes,
                        )

        # Check if all layouts conform
        for l, m in (
            (layout, "layout"), (layout2, "layout2"), (layout3, "layout3"), (layout4, "layout4"),
        ):
            parts = tuple(get_parts(l))
            self.assertEqual(len(parts), 2, msg=m)
            self.assertIn(mps_moved.parts[0], parts, msg=m)
            self.assertIn(mps_moved.parts[1], parts, msg=m)

    def test__layout(self):
        metalpin = dummy_tech.primitives.metalpin
        dxy = _geo.Point(x=0.0, y=1.0)
        rot = _geo.Rotation.MY

        ###

        cell3 = dummy_lib.cells.cell3

        ckt = cell3.circuit
        lay = cell3.layout

        i_net = ckt.nets.i

        # Code coverage
        lay2 = lay.dup()

        tuple(lay.filter_polygons(net=i_net))
        tuple(lay.filter_polygons(net=i_net, mask=metalpin.mask))
        tuple(lay.filter_polygons(net=i_net, mask=metalpin.mask, split=True))

        lay.bounds(net=i_net)

        self.assertEqual(lay, lay)
        self.assertNotEqual(lay, "")

        lay.freeze()
        with self.assertRaises(ValueError):
            # Adding to frozen layout
            lay += lay

        with self.assertRaises(ValueError):
            # wrong primitive
            lay.add_primitive(_prm.Auxiliary(name="error"))

        bnd1 = lay2.boundary
        lay2.move(dxy=dxy)
        lay2.rotate(rotation=rot)
        self.assertEqual(lay2.boundary, rot*(bnd1 + dxy))

        lay._hier_str_

        # code coverage
        dummy_layoutfab.new_layout(sublayouts=lay._sublayouts[0])

        ###

        cell2 = dummy_lib.cells.cell2

        ckt = cell2.circuit
        lay = cell2.layout

        self.assertEqual(len(lay._sublayouts), 1)
        sl = lay._sublayouts[0]
        self.assertIsInstance(sl, _laylay._InstanceSubLayout)

        subckt = sl.inst.cell.circuit
        sublay = sl.inst.cell.layout

        shapes1 = tuple(sublay.filter_polygons(net=subckt.nets.i, mask=prims.metal.mask))
        self.assertEqual(len(shapes1), 1)

        shapes2 = tuple(lay.filter_polygons(net=ckt.nets.i, mask=prims.metal.mask))
        self.assertEqual(len(shapes2), 1)

        shapes3 = tuple(lay.filter_polygons(net=None, mask=prims.metal.mask))
        self.assertEqual(len(shapes3), 1)

        self.assertEqual(shapes2[0], shapes1[0] + sl.origin)
        self.assertEqual(shapes3[0], shapes1[0] + sl.origin)

        ###

        cell4 = dummy_lib.cells.cell4 # no boundary

        lay = cell4.layout.dup()
        lay2 = lay.moved(dxy=dxy).rotated(rotation=rot)
        lay.move(dxy=dxy)

        self.assertIs(lay.boundary, None)


class PrimitiveLayouterTest(unittest.TestCase):
    def test__primitivelayouter(self):
        inprim = None
        def create_cb(*, layout, prim, **prim_args):
            if inprim is not None:
                self.assertEqual(inprim, prim)
        layouter = _layprim._PrimitiveLayouter(fab=dummy_layoutfab, create_cb=create_cb)

        enc = _prp.Enclosure(0.2)
        enc2 = _prp.Enclosure(1.0)
        rect = _geo.Rect.from_size(width=1.0, height=1.0)
        rect_enc = _geo.Rect.from_rect(rect=rect, bias=enc)
        rect_enc2 = _geo.Rect.from_rect(rect=rect, bias=enc2)

        with self.assertRaises(NotImplementedError):
            layouter(prims.anything_goes)

        with self.assertRaises(NotImplementedError):
            # Marker without width/height
            layouter(prims.metalpin)

        inprim = prims.metalpin
        lay = layouter(prims.metalpin, width=1.0, height=1.0)
        inprim = None
        self.assertEqual(len(lay._sublayouts), 1)
        sl = lay._sublayouts[0]
        self.assertIs(sl.net, None)
        self.assertEqual(len(sl.shapes), 1)
        ms = sl.shapes[0]
        self.assertEqual(
            ms,
            _geo.MaskShape(mask=prims.metalpin.mask, shape=rect),
        )

        # _WidthSpaceConductor without portnets
        lay = layouter(prims.metal, width=1.0, height=1.0)
        self.assertEqual(len(lay._sublayouts), 1)
        sl = lay._sublayouts[0]
        self.assertIs(sl.net, prims.metal.ports.conn)
        self.assertEqual(len(sl.shapes), 1)
        ms = sl.shapes[0]
        self.assertEqual(
            ms,
            _geo.MaskShape(mask=prims.metal.mask, shape=rect),
        )

        # WaferWire without well
        lay = layouter(
            prims.active, width=1.0, height=1.0,
            implant=prims.nplus, implant_enclosure=enc,
            extra=prims.substrate,
        )
        self.assertEqual(
            lay._sublayouts,
            _laylay._SubLayouts((
                _laylay._MaskShapesSubLayout(
                    net=prims.active.ports.conn,
                    shapes=_geo.MaskShapes(_geo.MaskShape(
                        mask=prims.active.mask, shape=rect,
                    ))
                ),
                _laylay._MaskShapesSubLayout(
                    net=None,
                    shapes=_geo.MaskShapes((
                        _geo.MaskShape(mask=prims.nplus.mask, shape=rect_enc),
                        _geo.MaskShape(mask=prims.substrate.mask, shape=rect),
                    )),
                ),
            )),
        )

        # WaferWire with well and oxide
        lay = layouter(
            prims.active, width=1.0, height=1.0,
            implant=prims.nplus, implant_enclosure=enc,
            oxide=prims.hvox, oxide_enclosure=enc,
            well=prims.nwell, well_enclosure=enc2,
            well_net=prims.active.ports.conn,
        )
        self.assertEqual(
            lay._sublayouts,
            _laylay._SubLayouts((
                _laylay._MaskShapesSubLayout(
                    net=prims.active.ports.conn,
                    shapes=_geo.MaskShapes((
                        _geo.MaskShape(mask=prims.active.mask, shape=rect),
                        _geo.MaskShape(mask=prims.nwell.mask, shape=rect_enc2),
                    ))
                ),
                _laylay._MaskShapesSubLayout(
                    net=None,
                    shapes=_geo.MaskShapes((
                        _geo.MaskShape(mask=prims.nplus.mask, shape=rect_enc),
                        _geo.MaskShape(mask=prims.hvox.mask, shape=rect_enc),
                    ))
                ),
            )),
        )

        # WaferWire with well but no well_net
        with self.assertRaises(TypeError):
            lay = layouter(
                prims.active, width=1.0, height=1.0,
                implant=prims.pplus, implant_enclosure=_prp.Enclosure(0.2),
                well=prims.nwell, well_enclosure=_prp.Enclosure(1.0),
            )

        # Via with bottom/top_enclosure as value
        lay = layouter(
            prims.via, space=0.35, rows=1, columns=1,
            bottom=prims.metal, bottom_enclosure=enc, bottom_extra=prims.substrate,
            bottom_width=None, bottom_height=None,
            top=prims.metal2, top_enclosure=enc,
            top_width=None, top_height=None,
        )
        viarect = _geo.Rect.from_size(width=prims.via.width, height=prims.via.width)
        mrect = _geo.Rect.from_rect(rect=viarect, bias=enc)
        mwidth = mrect.bounds.width
        self.assertEqual(
            lay._sublayouts,
            _laylay._SubLayouts((
                _laylay._MaskShapesSubLayout(
                    net=prims.via.ports.conn,
                    shapes=_geo.MaskShapes((
                        _geo.MaskShape(mask=prims.via.mask, shape=viarect),
                        _geo.MaskShape(mask=prims.metal.mask, shape=mrect),
                        _geo.MaskShape(mask=prims.metal2.mask, shape=mrect),
                    )),
                ),
                _laylay._MaskShapesSubLayout(
                    net=None,
                    shapes=_geo.MaskShapes((
                        _geo.MaskShape(mask=prims.substrate.mask, shape=mrect),
                    )),
                ),
            ))
        )

        self.assertEqual(
            layouter(
                prims.via, space=0.35, rows=None, columns=1,
                bottom=prims.metal, bottom_enclosure=enc,
                bottom_width=None, bottom_height=mwidth,
                top=prims.metal2, top_enclosure=enc,
                top_width=None, top_height=mwidth,
            ),
            layouter(
                prims.via, space=0.35, rows=1, columns=None,
                bottom=prims.metal, bottom_enclosure=enc,
                bottom_width=mwidth, bottom_height=None,
                top=prims.metal2, top_enclosure=enc,
                top_width=mwidth, top_height=None,
            ),
        )

        # Via with bottom_implant_enclosure but without bottom_implant
        with self.assertRaises(TypeError):
            layouter(
                prims.contact, bottom=prims.active, bottom_implant_enclosure=_prp.Enclosure(1.0),
            )

        # Code coverage for bottom_width/bottom_height/top_width/top_width None/float
        # combinations
        layouter(
            prims.via, space=0.35, rows=None, columns=1,
            bottom=prims.metal, bottom_enclosure=enc,
            bottom_width=None, bottom_height=None,
            top=prims.metal2, top_enclosure=enc,
            top_width=None, top_height=mwidth,
        )
        layouter(
            prims.via, space=0.35, rows=None, columns=1,
            bottom=prims.metal, bottom_enclosure=enc,
            bottom_width=None, bottom_height=mwidth,
            top=prims.metal2, top_enclosure=enc,
            top_width=None, top_height=None,
        )
        layouter(
            prims.via, space=0.35, rows=1, columns=None,
            bottom=prims.metal, bottom_enclosure=enc,
            bottom_width=None, bottom_height=None,
            top=prims.metal2, top_enclosure=enc,
            top_width=mwidth, top_height=None,
        )
        layouter(
            prims.via, space=0.35, rows=1, columns=None,
            bottom=prims.metal, bottom_enclosure=enc,
            bottom_width=mwidth, bottom_height=None,
            top=prims.metal2, top_enclosure=enc,
            top_width=None, top_height=None,
        )

        # Via with bottom/top_enclosure as str
        # enclosures are symmetric so "wide" and "tall" should give same layout
        self.assertEqual(
            layouter(
                prims.via, space=0.35, rows=1, columns=1,
                bottom=prims.metal, bottom_enclosure="wide",
                bottom_width=None, bottom_height=None,
                top=prims.metal2, top_enclosure="wide",
                top_width=None, top_height=None,
            ),
            layouter(
                prims.via, space=0.35, rows=1, columns=1,
                bottom=prims.metal, bottom_enclosure="tall",
                bottom_width=None, bottom_height=None,
                top=prims.metal2, top_enclosure="tall",
                top_width=None, top_height=None,
            ),
        )

        # Via with bottom_implant_enclosure as str
        # enclosure is symmetric so "wide" and "tall" should give same layout
        self.assertEqual(
            layouter(
                prims.contact, space=0.3, rows=1, columns=1,
                bottom=prims.active, bottom_enclosure="tall",
                bottom_implant=prims.nplus, bottom_implant_enclosure="wide",
                top_enclosure="tall",
            ),
            layouter(
                prims.contact, space=0.3, rows=1, columns=1,
                bottom=prims.active, bottom_enclosure="tall",
                bottom_implant=prims.nplus, bottom_implant_enclosure="tall",
                top_enclosure="tall",
            ),
        )

        # Via with wrong portnets
        with self.assertRaises(ValueError):
            lay = layouter(prims.via, portnets={"error": prims.via.ports.conn})

        # Via with WaferWire as bottom
        # code coverage for
        # bottom_(implant|implante_enclosre|oxide|oxide_enclosure|well|well_enclosure)
        layouter(
            prims.contact, space=0.35, rows=1, columns=1,
            bottom=prims.active, bottom_enclosure=enc,
            bottom_implant=prims.pplus, bottom_implant_enclosure=enc,
            bottom_oxide=prims.hvox, bottom_oxide_enclosure=enc,
            bottom_well=prims.nwell, well_net=prims.active.ports.conn,
            bottom_well_enclosure=enc,
            top_enclosure=enc,
        )
        layouter(
            prims.contact, space=0.35, rows=1, columns=1,
            bottom=prims.active, bottom_enclosure=enc,
            bottom_implant=prims.nplus, bottom_implant_enclosure=enc,
            bottom_oxide=prims.hvox, bottom_oxide_enclosure=None,
            bottom_well=prims.nwell, well_net=prims.contact.ports.conn,
            bottom_well_enclosure=enc,
            top_enclosure=enc,
        )
        # well_net not given
        with self.assertRaises(TypeError):
            layouter(
                prims.contact, space=0.35, rows=1, columns=1,
                bottom=prims.active, bottom_enclosure=enc,
                bottom_implant=prims.pplus, bottom_implant_enclosure=enc,
                bottom_oxide=prims.hvox, bottom_oxide_enclosure=enc,
                bottom_well=prims.nwell,
                bottom_well_enclosure=enc,
                top_enclosure=enc,
            )
        # bottom_well type is bottom_implant type but net is different
        with self.assertRaises(ValueError):
            layouter(
                prims.contact, space=0.35, rows=1, columns=1,
                bottom=prims.active, bottom_enclosure=enc,
                bottom_implant=prims.nplus, bottom_implant_enclosure=enc,
                bottom_oxide=prims.hvox,
                bottom_well=prims.nwell, well_net=prims.poly.ports.conn,
                bottom_well_enclosure=enc,
                top_enclosure=enc,
            )
        # bottom_well type == implant type; same well
        lay = layouter(
            prims.contact, space=0.35, rows=1, columns=1,
            bottom=prims.active, bottom_enclosure=enc,
            bottom_implant=prims.nplus, bottom_implant_enclosure=enc,
            bottom_oxide=prims.hvox,
            bottom_well=prims.nwell,
            bottom_well_enclosure=enc,
            top_enclosure=enc,
        )
        self.assertEqual(len(lay._sublayouts), 2)

        # DeppWell
        with self.assertRaises(NotImplementedError):
            layouter(prims.deepwell)

        # Resistor
        # resistor without contact layer
        with self.assertRaises(NotImplementedError):
            layouter(prims.metal2res)
        self.assertEqual(
            layouter(prims.resistor, width=1.0, length=1.0),
            layouter(
                prims.resistor, portnets={
                    "port1": prims.resistor.ports.port1,
                    "port2": prims.resistor.ports.port2,
                },
                width=1.0, length=1.0,
            ),
        )
        # wrong ports
        with self.assertRaises(ValueError):
            layouter(prims.resistor, portnets={}, width=1.0, height=1.0),

        # MIMCapacitor
        self.assertEqual(
            layouter(
                prims.MIMCap, width=1.0, height=1.0, bottom_connect_up=True,
            ),
            layouter(
                prims.MIMCap, portnets={
                    "top": prims.MIMCap.ports.top,
                    "bottom": prims.MIMCap.ports.bottom,
                },
                width=1.0, height=1.0, bottom_connect_up=True,
            ),
        )
        # code coverage for bottom_connect_up == False
        layouter(
            prims.MIMCap, width=1.0, height=1.0, bottom_connect_up=False,
        )
        # wrong ports
        with self.assertRaises(ValueError):
            layouter(
                prims.MIMCap, portnets={}, width=1.0, height=1.0,
                bottom_connect_up=True,
            )

        # Diode
        self.assertEqual(
            layouter(prims.ndiode),
            layouter(prims.ndiode, portnets={
                "anode": prims.ndiode.ports.anode,
                "cathode": prims.ndiode.ports.cathode,
            }),
        )
        self.assertNotEqual(layouter(prims.ndiode), layouter(prims.pdiode))
        # wrong portnets
        with self.assertRaises(ValueError):
            layouter(prims.ndiode, portnets={})

        # MOSFET
        self.assertNotEqual(
            layouter(
                prims.nmos, l=0.3, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
            layouter(
                prims.nmos, l=0.4, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
        )
        self.assertNotEqual(
            layouter(
                prims.nmos, l=0.3, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
            layouter(
                prims.pmos, l=0.3, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
        )
        self.assertNotEqual(
            layouter(
                prims.hvnmos, l=0.3, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
            layouter(
                prims.hvnmos, l=0.4, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
        )
        self.assertNotEqual(
            layouter(
                prims.esdnmos, l=0.3, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
            layouter(
                prims.esdnmos, l=0.4, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
        )

        # Bipolar
        # not implmented
        with self.assertRaises(NotImplementedError):
            layouter(prims.npn)

class CircuitLayouterTest(unittest.TestCase):
    def test_addwire(self):
        # MetalWire
        wire = prims.metal

        ckt = dummy_cktfab.new_circuit(name="test")
        net = ckt.new_net(name="net", external=False)

        shape = _geo.Rect(left=1.0, bottom=-1.0, right=2.0, top=1.0)

        layouter = dummy_layoutfab.new_circuitlayouter(circuit=ckt, boundary=None)
        layouter.add_wire(net=net, wire=wire, shape=shape)

        layout = dummy_layoutfab.new_layout()
        layout.add_shape(net=net, layer=wire, shape=shape)

        self.assertEqual(layouter.layout, layout)

        # Via
        wire = prims.contact
        bottom = prims.poly

        ckt = dummy_cktfab.new_circuit(name="test")
        net = ckt.new_net(name="net", external=False)

        p = _geo.Point(x=-2.0, y=3.0)

        layouter = dummy_layoutfab.new_circuitlayouter(circuit=ckt, boundary=None)
        layouter.add_wire(net=net, wire=wire, origin=p, bottom=bottom)

        layout = dummy_layoutfab.new_layout()
        layout.add_primitive(portnets={"conn": net}, prim=wire, x=p.x, y=p.y, bottom=bottom)

        self.assertEqual(layouter.layout, layout)

    def test_place_layout_1(self):
        # Place layout with two parts from a _MultiPartShape
        mask = prims.metal.mask

        ckt = dummy_cktfab.new_circuit(name="ckt")
        net = ckt.new_net(name="net", external=False)
        net2 = ckt.new_net(name="net2", external=False)
        layouter = dummy_layoutfab.new_circuitlayouter(circuit=ckt, boundary=None)

        r1 = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        r2 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))
        r12 = _geo.Rect.from_floats(values=(0.0, 0.0, 2.0, 1.0))

        mps = _geo.MultiPartShape(fullshape=r12, parts=(r1, r2))

        ms1 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[0]))
        ms2 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[1]))

        sl1 = _laylay._MaskShapesSubLayout(net=net, shapes=ms1)
        sl2 = _laylay._MaskShapesSubLayout(net=net2, shapes=ms2)

        lay = dummy_layoutfab.new_layout()
        lay += sl1
        lay += sl2
        layouter.place(lay, origin=_geo.origin)

        def get_parts(l: _lay.LayoutT):
            for sl in l._sublayouts.__iter_type__(_laylay._MaskShapesSubLayout):
                for ms in sl.shapes:
                    s = ms.shape
                    if isinstance(s, _geo.MultiPartShape._Part):
                        yield s
                    elif isinstance(s, _geo.MultiShape):
                        yield from filter(
                            lambda s2: isinstance(s2, _geo.MultiPartShape._Part),
                            s.shapes,
                        )
        parts = tuple(get_parts(layouter.layout))

        self.assertEqual(len(parts), 2)
        self.assertIn(mps.parts[0], parts)
        self.assertIn(mps.parts[1], parts)

    def test_place_layout_2(self):
        # Place layout with two parts from a _MultiPartShape
        # Difference to test_place_layout_1 is that here the two parts
        # are put on the same net.
        mask = prims.metal.mask

        ckt = dummy_cktfab.new_circuit(name="ckt")
        net = ckt.new_net(name="net", external=False)
        layouter = dummy_layoutfab.new_circuitlayouter(circuit=ckt, boundary=None)

        r1 = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        r2 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))
        r12 = _geo.Rect.from_floats(values=(0.0, 0.0, 2.0, 1.0))

        mps = _geo.MultiPartShape(fullshape=r12, parts=(r1, r2))

        ms1 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[0]))
        ms2 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[1]))

        sl1 = _laylay._MaskShapesSubLayout(net=net, shapes=ms1)
        sl2 = _laylay._MaskShapesSubLayout(net=net, shapes=ms2)

        lay = dummy_layoutfab.new_layout()
        lay += sl1
        lay += sl2
        layouter.place(lay, origin=_geo.origin)

        def get_parts(l: _lay.LayoutT):
            for sl in l._sublayouts.__iter_type__(_laylay._MaskShapesSubLayout):
                for ms in sl.shapes:
                    s = ms.shape
                    if isinstance(s, _geo.MultiPartShape._Part):
                        yield s
                    elif isinstance(s, _geo.MultiShape):
                        yield from filter(
                            lambda s2: isinstance(s2, _geo.MultiPartShape._Part),
                            s.shapes,
                        )
        parts = tuple(get_parts(layouter.layout))

        self.assertEqual(len(parts), 2)
        self.assertIn(mps.parts[0], parts)
        self.assertIn(mps.parts[1], parts)
