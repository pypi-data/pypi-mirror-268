# Description

PDK Master is a tool to manage [PDK](https://en.wikipedia.org/wiki/Process_design_kit)s for ASIC design and a framework for designing circuits and layouts in those technologies.
It is a Python framework under heavy development and with an unstable API.

# Release history

* [v0.11.0](https://gitlab.com/Chips4Makers/PDKMaster/-/commits/v0.11.0): split off
  pdkmaster.io.klayout module
* [v0.10.2](https://gitlab.com/Chips4Makers/PDKMaster/-/commits/v0.10.2): includes support for
  IHP SG13G2 IO cells in [c4m-pdk-ihpsg13g2](https://gitlab.com/Chips4Makers/c4m-pdk-ihpsg13g2)
* v0.10.1: Smaller layout and DRC improvements guided by work on the IHP
  sg13g2 IO cells. Please refer to individual git commit for the details.
* v0.10.0: Start newer minor version by merging API breaking changes.
  I will backwards compatibility for code using deprecated *T types and for Resistor and Diode
  primitive creation that explicitly specify None for implant or min_implant_enclosure property.
  Technology.substrate() property has been removed and wafer_.outside() function.  
  For the rest no code difference with v0.9.6.  
  Originally it was planned to have v1.0 to be released after the v0.9.x releases. For the
  layout code in PDKMaster still major reworks and API breakage is expected and v1.0 is delayed
  until this has stabilized more.
* v0.9.6: Release of several changes used in improved version of c4m-flexcell and c4m-flexio
  Mostly small changes or bug fixes. One bigger change is that now more than one implant layer
  can be drawn around a WaferWire interconnect. Resistor and Diode primitives now allow to
  define them with multiple implant layers and generate the layout for these multiple implant
  layers.
  After this release some API breaking changes will be merged.
* v0.9.5: allow use of MOSFET.gate4mosfet attribute before MOSFET is added to Technology.
  This allows having rules added to the technology that are using the gate of a specific
  MOSFET.
* v0.9.4:
  * Support for WaferWire without an implant for diode, MOSFET etc.
  * Roadworks on layer manipulation
  * API improvements, unification and deprecation
* v0.9.3:
  * First LEF/DEF support: support exporting tech.lef file
  * Bug fixing
* v0.9.2: support new namespace in coriolis export
* v0.9.1: fix coriolis export, primitive type values are not python types.
* v0.9.0: [release notes](https://gitlab.com/Chips4Makers/PDKMaster/-/blob/v0.9.0/ReleaseNotes/v0.9.0.md)
* v0.3.0: [release notes](https://gitlab.com/Chips4Makers/PDKMaster/-/blob/v0.3.0/ReleaseNotes/v0.3.0.md)
* v0.2.1: add klayout dependency
* v0.2.0: [release notes](https://gitlab.com/Chips4Makers/PDKMaster/-/blob/v0.2.0/ReleaseNotes/v0.2.0.md)
* v0.1: [release notes](https://gitlab.com/Chips4Makers/PDKMaster/-/blob/v0.2.0/ReleaseNotes/v0.1.md)

# Overview

Currently no documentation is available, the documentation is planned to be added as part of the stabilization of the PDKMaster API. To show the things PDKMaster wants to solve here an overview of the different parts of the current PDKMaster code base:

* __pdkmaster__: the top python module
  * __`_util.py`__: some helper functions and classes
  * __technology__:
  this submodule handles the description of an ASIC technology with final target to allow describe that in one python file.
    * __`property_.py`__: base class to represent properties on operations that can be done on them.
    * __`rule.py`__: abstract base class to represent a rule object, e.g. a condition on properties that has to be fulfilled to be manufacturable.
    * __`mask.py`__: class to represent the photolithography masks used in ASIC production and the properties on them. The latter are then used to define design rules.
    * __`edge.py`__: class representing mask edges and it's properties to be used in design rules.
    * __`wafer.py`__: object to represent a (silicon) wafer that is the start of processing and that is auto-connected to some device ports.
    * __`net.py`__: class representing a net, e.g. o group of conductors in a circuit that are connected together.
    * __`primitive.py`__: classes for all possible device primitives available in a technology. This goes from low-level interconnect to transistors. As indication of the content here the exported classes are given:
      ```python
      __all__ = ["Marker", "Auxiliary", "ExtraProcess",
                 "Implant", "Well",
                 "Insulator", "WaferWire", "GateWire", "MetalWire", "TopMetalWire",
                 "Via", "PadOpening",
                 "Resistor", "Diode",
                 "MOSFETGate", "MOSFET", "Bipolar",
                 "Spacing",
                 "UnusedPrimitiveError", "UnconnectedPrimitiveError"]
      ```
      The object attibutes defined by these classes are used to derive mask design rules.

    * __`technology_.py`__: class to define the capability of a certain technology: all support devices, the masks needed to define them and the rules for making circuit in this technology.
  * __dispatch__: helper classes inspired by the [Visitor design pattern](https://en.wikipedia.org/wiki/Visitor_pattern).
  * __design__: support code for making circuits compliant with a given technology.
    * __`circuit.py`__: defines a factory that allows to generate objects of the Circuit class using devices from a given technology.
    * __`layout.py`__: classes to define layout compliant with a given technology and a factory to generate layouts for a given circuit that are technology design rule compliant.
    * __`library.py`__: contains:
      * __Cell class__: representing several possible circuit representations and layouts of a block with the same function
      * __Library class__: represent a collections of cells
  * __io__: submodule to import and export technology data, circuit and layouts. It also allows
    to interface with external tools.
    * __parsing__: submodule to parse setup files for other EDA tools and extract data to build a PDKMaster technology object based on this data.
      * __`skill_grammar.py`__: modgrammar based parser for [SKILL](https://en.wikipedia.org/wiki/Cadence_SKILL)(-like) files. [SKILL](https://en.wikipedia.org/wiki/Cadence_SKILL) is the Cadence bastardized version of [Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language)).
      * __`tf.py`, `display.py`, `layermap.py`, `assura.py`__: classes for representing Cadence EDA files based on the [SKILL](https://en.wikipedia.org/wiki/Cadence_SKILL) grammar.
    * __pdkmaster__: support code to export a PDKMaster technology as Python souce code; main targeted use case to use the parsing submodule to extract data from NDA covered PDK and generate PDKMaster Technology object without needing to disctribute NDA covered data.
    * __coriolis__: support code to generate Coriolis technology setup, cells and libraries from PDKMaster objects.
    * __klayout__: support code to generate klayout Technology setup for PDKMaster Technology object including DRC and LVS scripts.
    * __spice__: support code to convert PDKMaster Circuit to use in SPICE simulations;
    currently PySpice is used to interface with SPICE.

The current code base has been gradually grown to allow to do a 0.18µm prototype layout of the NLNet sponsored Libre-SOC project. It has known (and unknown) inconsistencies and shortcomings. A full revision of the current API is planned without any backwards guarantees whatsoever. As this is an open source project it is meant to be used by other people but one should be aware that user code using PDKMaster has a high chance of breaking with each commit done to the repository in the near future.

# Installation

All dependencies for installation should be available so PDKMaster should be able to installed by a simple pip command.

```console
% pip install PDKMaster
```

To install build dependencies:
```console
% pip install -r dev-requirements.txt
```

More in depth discussion of different `pip` use case scenarios is out of the scope of this document.

Run time dependencies:

- [modgrammar](https://pythonhosted.org/modgrammar/)
- [shapely](https://shapely.readthedocs.io/en/latest/manual.html), [descartes](https://pypi.org/project/descartes/) (deprecated way of plotting in notebooks)
- [PySpice](https://pyspice.fabrice-salvaire.fr/pages/documentation.html) >= 1.5
- klayout ([pypi](https://pypi.org/project/klayout/), [home](https://www.klayout.de/)): for pdkmaster.io.klayout

# Licensing Rationale

Open source projects and it's surrounding community can only strive when improvements to the
code or application of the code itself are released to the public and allowed to be used by
them. Copyleft type license are using the licensing terms to guarantee this actually happens
and no party uses a 'take-but-don't-give-back' approach. The
[GNU Aferro General Public License V3.0](LICENSES/agpl-3.0.txt) is used as main license for
the code in this project as it is a copyleft type license that is also applicable to cloud
services without binary distribution of the code.

One of the problems with a strict copyleft license is that it can introduce incompatibilities
with code released under other open source licenses. In order to improve compatibility and
thus also reusablity the code in this repo is multi-licensed. Multi-licensing under
established open source licenses was preferred over custom extension of licenses.

The [GNU General Public License V2.0](LICENSES/gpl-2.0.txt) was added as optional license in
order to allow derived code not to be bound by the anti-[tivoization](
  https://en.wikipedia.org/wiki/Tivoization
) clauses introduced in the [GNU General Public License Version 3](
  https://www.gnu.org/licenses/gpl-3.0-standalone.html
). The latter was not deemed necessary for this project and the addition was done to increase
compatibility with some corporate policies.

The [CERN Open Hardware Licence Version 2 - Strongly Reciprocal](LICENSES/cern_ohl_s_v2.txt) is included as it is a copyleft license specifically targeted for hardware but incompatible
with the GPL licenses.

The [Apache License Version 2.0](LICENSES/apache-2.0.txt) is included to maximize compatiblity
with existing open source code. One is supposed to not use it to avoid having to release one's
own derived code to the public. If you plan development of a project in a proprietary way, one
is kindly asked to not derive one's code from this project's code.

In future the list of allowed licenses may be reduced. A reason could be that such an action
is deemed necessary by the project maintainers to encourage open sourcing of derived code.

Analog to how the object files and the executables generated by the gcc compiler are not
necessarily goverened by the GPL license, the multi-licensing applies only to code derived
from code in this repository. Output files generated through the use of the code in this
repository are not by default bound to the multi-licensing requirements of this project's
code.

# Copyright

The code in this repo is copyrighted by all the contributors to it; git is
used to track this copyright.
