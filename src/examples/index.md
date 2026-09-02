1MatCalc examples [MatCalc Documentation]



### Table of Contents

* [1MatCalc examples](#matcalc_examples)

  + [Equilibrium and non-equilibrium analysis](#equilibrium_and_non-equilibrium_analysis)
  + [Multi-component multi-phase precipitation](#multi-component_multi-phase_precipitation)
  + [Microstructure - property relationship](#microstructure_-_property_relationship)
  + [Long-range diffusion, and diffusion coupled with precipitation](#long-range_diffusion_and_diffusion_coupled_with_precipitation)

    - [Single-phase problems](#single-phase_problems)
    - [Diffusion in dispersed systems - Local equilibrium approach](#diffusion_in_dispersed_systems_-_local_equilibrium_approach)
    - [Simultaneous long-range diffusion and precipitation](#simultaneous_long-range_diffusion_and_precipitation)
  + [Moving phase boundary problems](#moving_phase_boundary_problems)
  + [Thermal simulations](#thermal_simulations)

1MatCalc examples
=================

The example documents of this sections are aimed at *introducing you to typical simulation problems* that can be solved with MatCalc. The examples demonstrate how these problems can be treated and which issues need to be accounted for to obtain reasonable simulation results.

If you are a newbie to MatCalc, you can benefit from this section because it also demonstrated the various simulation approaches that are implemented in MatCalc and how these are utilized to solve your problems. For practical use, we recommend, however, that you make yourself familiar also with the software using the [tutorials](/tutorials "tutorials").

The MatCalc examples provide complementary material to the How-To Manual. Typical examples of thermodynamic analysis, precipitation kinetics, long-range diffusion analysis, as well as Monte Carlo simulations are listed below. The following links will bring you to the example documents.

Equilibrium and non-equilibrium analysis
----------------------------------------

The examples provided in this section demonstrate the functionality of MatCalc for thermodynamic equilibrium analysis. The first examples demonstrate basic features and give instructions on how to perform typical calculations. These are the generation of stable and metastable phase fraction diagrams, as well as chemical driving forces. The later examples show how to use this module of MatCalc to retrieve estimates of how the microstructure of a material could look like and which precipitates one can expect to see in experiments. This type of analysis is often applied for temperature cycles with low to moderate temperature gradients.

* **E1** -  [Stable and meta-stable phase fraction diagram of Fe-C-Mn](/examples/e1 "examples/e1") - Evaluate ortho-equilibrium and para-equilibrium phase fraction diagrams.
* **E20** - Thermodynamic equilibrium analysis for continuous casting simulation of micro-alloyed Fe-Al-C-N-Nb-Ti steel. This analysis is a recommended step before carrying out precipitation kinetics simulations in inhomogeneous, segregated primary solidification microstructure.

Multi-component multi-phase precipitation
-----------------------------------------

The precipitation kinetics module of MatCalc provides a powerful means of evaluating the evolution of precipitates during thermal and thermo-mechanical treatment.

* **P1** -  [Precipitation of XXX in YYY](/examples/p1 "examples/p1") - asf asdf asdf
* **P2** -  [???](/examples/p2 "examples/p2") - asdf asdf asdf adfssdfds
* **P10** -  [AlN precipitation in steel](/examples/p10 "examples/p10") - Heterogeneous precipitation of AlN at dislocations and grain boundaries. Simulation and experimental verification.
* **P11** -  [Concurrent precipitation of AlN and VN in steel](/examples/p11 "examples/p11") - A computational study and comparison with experiment
* **P12** -  [NbC precipitation in steel](/examples/p12 "examples/p12") - Interaction between precipitation and deformation
* **P20** -  [Precipitation simulation during continuous casting](/examples/p20 "examples/p20") - Precipitation in primary solidification microstructure
* **P30** -  [TTP-plot of micro-alloying precipitates in Fe-Al-Nb-Ti-C-N](/examples/p30 "examples/p30") - Isothermal conditions.
* **P31** -  [TTP-plot of micro-alloying precipitates in Fe-Al-Nb-Ti-C-N](/examples/p31 "examples/p31") - Advanced programming including primary precipitates and deformation

Microstructure - property relationship
--------------------------------------

In the following examples, the results of the precipitation kinetics simulations within MatCalc are used for predictions of mechanical properties of materials.

* **P100** -  [Precipitation strengthening in Fe-Cu](/examples/p100 "examples/p100")
* **P110** -  [Yield strength prediction in 6xxx alloys](/examples/p110 "examples/p110")
* bla bla bla

Long-range diffusion, and diffusion coupled with precipitation
--------------------------------------------------------------

These simulations provide some examples of the long-range diffusion and precipitation module of Matcalc (mc\_sim). Try it out…

### Single-phase problems

* **D1** -  [Fe-C diffusion couple](/diffusion/d1 "diffusion/d1") - Carbon diffusion in austenite
* **D2** -  [Simple carburization treatment](/diffusion/d2 "diffusion/d2") - Diffusion of C into austenite
* **D3** -  [Fe-C-Mn-Si diffusion couple](/diffusion/d3 "diffusion/d3") - The famous Darken uphill diffusion experiment

### Diffusion in dispersed systems - Local equilibrium approach

* **D10** -  [Simultaneous long-range diffusion and second-phase formation](/diffusion/d10 "diffusion/d10") - XXXXX

### Simultaneous long-range diffusion and precipitation

* **D20** -  [Simultaneous long-range diffusion and precipitation](/diffusion/d20 "diffusion/d20") - XXXXX

Moving phase boundary problems
------------------------------

These simulations use the moving phase boundary capabilities of MatCalc. They are presently limited to binary systems and local equilibrium at the phase boundary. It is more or less still research in progress in a rather early stage. Still, if you feel like, try it out…

* **M1** - Austenite to ferrite transformation during continuous cooling (Fe-C). Makes use of Local Equilibrium (LE) hypothesis.
* **M2** - Peritectic transformation in Fe-C. Makes use of Local Equilibrium (LE) hypothesis.
* **M5** - Austenite to ferrite transformation during continuous cooling (Fe-C-Mn). Makes use of Thermodynamic Extremal Principle (TEP).
* **M6** - Peritectic transformation in Fe-C-Mn. Makes use of Thermodynamic Extremal Principle (TEP).

Thermal simulations
-------------------

'Thermal simulations' help files contain some examples of the thermal treatment module of Matcalc. Try it out…

* **H1** -  [Heating a block of metal](/thermal/t1 "thermal/t1")
* **H2** -  [Quenching a block of metal](/thermal/t2 "thermal/t2")
* **H3** -  [Temperature profile in the Gleeble thermo-dynamical-testing machine](/thermal/t3 "thermal/t3")

bla bla bla

![](/wiki/lib/exe/taskrunner.php?id=examples%3Aindex&1788352980)