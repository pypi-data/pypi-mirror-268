# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest
from typing import cast

from pdkmaster.technology import primitive as _prm
from pdkmaster.design import cell as _cell

from pdkmaster.io import spice as _sp

from ...dummy import dummy_tech, dummy_cktfab, dummy_layoutfab, dummy_prims_spiceparams
dummy_prims = dummy_tech.primitives

class PySpiceFactoryTest(unittest.TestCase):
    def test_error(self):
        fab = _sp.PySpiceFactory(
            libfile="test.lib", corners=("fast", "typ", "slow"), conflicts={
                "fast": ("typ", "slow"),
                "typ": ("fast", "slow"),
                "slow": ("fast", "typ"),
            },
            prims_params=dummy_prims_spiceparams,
        )

        #----
        # instance ports on net checking
        ckt = dummy_cktfab.new_circuit(name="test")

        res = ckt.instantiate(
            cast(_prm.Resistor, dummy_prims.resistor), name="res",
            width=1.0, height=3.0,
        )
        ckt.new_net(name="res_p1", external=True, childports=res.ports.port1)

        # res.ports.port2 not on a net
        with self.assertRaises(ValueError):
            fab.new_pyspicesubcircuit(circuit=ckt)

        ckt.new_net(name="res_p1b", external=True, childports=res.ports.port1)

        # res.ports.port1 on two nets
        with self.assertRaises(ValueError):
            fab.new_pyspicesubcircuit(circuit=ckt)

        #----
        # wrong corner spec
        ckt = dummy_cktfab.new_circuit(name="test")

        # wrong corner
        with self.assertRaises(ValueError):
            fab.new_pyspicecircuit(corner="error", top=ckt)
        # conflicting corner
        with self.assertRaises(ValueError):
            fab.new_pyspicecircuit(corner=("slow", "fast"), top=ckt)

        #----
        # MIMCapacitor in lvs
        ckt = dummy_cktfab.new_circuit(name="test")

        mim = ckt.instantiate(
            cast(_prm.MIMCapacitor, dummy_prims.MIMCap), name="mim",
            width=0.5, height=0.5,
        )
        ckt.new_net(name="mim_bot", external=True, childports=mim.ports.bottom)
        ckt.new_net(name="mim_top", external=True, childports=mim.ports.top)

        with self.assertRaises(NotImplementedError):
            fab.new_pyspicesubcircuit(circuit=ckt, lvs=True)

        #----
        # MIMCapacitor not a subcircuit model
        params = _sp.SpicePrimsParamSpec()
        params.add_device_params(
            prim=cast(_prm.MIMCapacitor, dummy_prims.MIMCap), is_subcircuit=False,
        )
        fab = _sp.PySpiceFactory(
            libfile="test.lib", corners=("typ",), conflicts={}, prims_params=params,
        )

        ckt = dummy_cktfab.new_circuit(name="test")

        mim = ckt.instantiate(
            cast(_prm.MIMCapacitor, dummy_prims.MIMCap), name="mim",
            width=0.5, height=0.5,
        )
        ckt.new_net(name="mim_bot", external=True, childports=mim.ports.bottom)
        ckt.new_net(name="mim_top", external=True, childports=mim.ports.top)

        with self.assertRaises(NotImplementedError):
            fab.new_pyspicesubcircuit(circuit=ckt)

    def test_pyspicecircuit(self):
        # Wrong corner in conflicts
        with self.assertRaises(ValueError):
            _sp.PySpiceFactory(
                libfile="test.lib", corners=("typ",), conflicts={"error": "error2"},
                prims_params=dummy_prims_spiceparams,
            )

        # Currently only run some code for code coverage.
        # No checking done ATM.
        fab = _sp.PySpiceFactory(
            libfile="test.lib", corners=("typ",), conflicts={},
            prims_params=dummy_prims_spiceparams,
        )

        mos_cell = _cell.Cell(
            name="mytest",
            tech=dummy_tech, cktfab=dummy_cktfab, layoutfab=dummy_layoutfab,
        )
        mos_ckt = mos_cell.new_circuit()
        mos = mos_ckt.instantiate(cast(_prm.MOSFET, dummy_prims.nmos), name="mos")
        mos_ckt.new_net(name="s", external=True, childports=mos.ports.sourcedrain1)
        mos_ckt.new_net(name="g", external=True, childports=mos.ports.gate)
        mos_ckt.new_net(name="d", external=True, childports=mos.ports.sourcedrain2)
        mos_ckt.new_net(name="b", external=True, childports=mos.ports.bulk)


        ckt = dummy_cktfab.new_circuit(name="test")

        res = ckt.instantiate(
            cast(_prm.Resistor, dummy_prims.resistor), name="res",
            width=1.0, height=3.0,
        )
        ckt.new_net(name="res_p1", external=True, childports=res.ports.port1)
        ckt.new_net(name="res_p2", external=True, childports=res.ports.port2)

        res2 = ckt.instantiate(
            cast(_prm.Resistor, dummy_prims.metal2res), name="res2",
        )
        ckt.new_net(name="res2_p1", external=True, childports=res2.ports.port1)
        ckt.new_net(name="res2_p2", external=True, childports=res2.ports.port2)

        ndio = ckt.instantiate(
            cast(_prm.Diode, dummy_prims.ndiode), name="ndio",
        )
        ckt.new_net(name="ndio_ano", external=True, childports=ndio.ports.anode)
        ckt.new_net(name="ndio_cath", external=True, childports=ndio.ports.cathode)

        pdio = ckt.instantiate(
            cast(_prm.Diode, dummy_prims.pdiode), name="pdio",
        )
        ckt.new_net(name="pdio_ano", external=True, childports=pdio.ports.anode)
        ckt.new_net(name="pdio_cath", external=True, childports=pdio.ports.cathode)

        nmos = ckt.instantiate(mos_cell, name="nmos")
        ckt.new_net(name="nmos_s", external=True, childports=nmos.ports.s)
        ckt.new_net(name="nmos_g", external=True, childports=nmos.ports.g)
        ckt.new_net(name="nmos_d", external=True, childports=nmos.ports.d)
        ckt.new_net(name="nmos_b", external=True, childports=nmos.ports.b)

        pmos = ckt.instantiate(
            cast(_prm.MOSFET, dummy_prims.pmos), name="pmos",
        )
        ckt.new_net(name="pmos_s", external=True, childports=pmos.ports.sourcedrain1)
        ckt.new_net(name="pmos_g", external=True, childports=pmos.ports.gate)
        ckt.new_net(name="pmos_d", external=True, childports=pmos.ports.sourcedrain2)
        ckt.new_net(name="pmos_b", external=True, childports=pmos.ports.bulk)

        mim = ckt.instantiate(
            cast(_prm.MIMCapacitor, dummy_prims.MIMCap), name="mim",
            width=0.5, height=0.5,
        )
        ckt.new_net(name="mim_bot", external=True, childports=mim.ports.bottom)
        ckt.new_net(name="mim_top", external=True, childports=mim.ports.top)

        mim2 = ckt.instantiate(
            cast(_prm.MIMCapacitor, dummy_prims.MIMCap2), name="mim2",
        )
        ckt.new_net(name="mim2_bot", external=True, childports=mim2.ports.bottom)
        ckt.new_net(name="mim2_top", external=True, childports=mim2.ports.top)

        npn = ckt.instantiate(cast(_prm.Bipolar, dummy_prims.npn), name="npn")
        ckt.new_net(name="npn_c", external=True, childports=npn.ports.collector)
        ckt.new_net(name="npn_b", external=True, childports=npn.ports.base)
        ckt.new_net(name="npn_e", external=True, childports=npn.ports.emitter)

        pnp = ckt.instantiate(cast(_prm.Bipolar, dummy_prims.pnp), name="pnp")
        ckt.new_net(name="pnp_c", external=True, childports=pnp.ports.collector)
        ckt.new_net(name="pnp_b", external=True, childports=pnp.ports.base)
        ckt.new_net(name="pnp_e", external=True, childports=pnp.ports.emitter)

        fab.new_pyspicecircuit(corner="typ", top=ckt)


        ckt = dummy_cktfab.new_circuit(name="test")

        res = ckt.instantiate(
            cast(_prm.Resistor, dummy_prims.metal2res), name="res",
            width=1.0, height=3.0,
        )
        ckt.new_net(name="res_p1", external=True, childports=res.ports.port1)
        ckt.new_net(name="res_p2", external=True, childports=res.ports.port2)

        fab.new_pyspicesubcircuit(circuit=ckt, lvs=True)
