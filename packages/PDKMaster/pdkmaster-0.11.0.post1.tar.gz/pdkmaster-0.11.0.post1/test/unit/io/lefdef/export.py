# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

from pdkmaster.technology import primitive as _prm
from pdkmaster.io import lefdef as _ld

from ...dummy import dummy_tech


class LEFExporterTest(unittest.TestCase):
    def test_tlef(self):
        _ld.LEFExporter(
            tech=dummy_tech,
            site_width=1.0,
            site_height=1.0,
            use_nwell=True,
        )()


        metals = tuple(filter(
            lambda p: not isinstance(p, _prm.MIMTop),
            dummy_tech.primitives.__iter_type__(_prm.MetalWire),
        ))
        vias = tuple(dummy_tech.primitives.__iter_type__(_prm.Via))
        pitches = (
            *(
                max(
                    vias[i].width/2 + vias[i].min_top_enclosure[0].max()
                    + metals[i].min_space + metals[i].min_width,
                    vias[i+1].width/2 + vias[i+1].min_bottom_enclosure[0].max()
                    + metals[i].min_space + metals[i].min_width,
                ) for i in range(len(metals)-1)
            ),
            vias[-1].width/2 + vias[-1].min_top_enclosure[0].max()
              + metals[-1].min_space + metals[-1].min_width,
        )
        metals_sheetres = tuple(20.0 for _ in metals)
        _ld.LEFExporter(
            tech=dummy_tech,
            site_width=1.0,
            site_height=1.0,
            use_pwell=True,
            metals=metals,
            vias=vias,
            pitches=pitches,
            metals_sheetres=metals_sheetres,
        )()
