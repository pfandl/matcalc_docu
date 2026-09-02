TechPaper #2011003: The CNT multi-component transient nucleation rate [MatCalc Documentation]



### Table of Contents

* [TechPaper #2011003: The CNT multi-component transient nucleation rate](#techpaper_2011003the_cnt_multi-component_transient_nucleation_rate)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Energetics of nucleus formation](#energetics_of_nucleus_formation)
  + [Homogeneous nucleation](#homogeneous_nucleation)
  + [The transient nucleation rate](#the_transient_nucleation_rate)
  + [Multi-component CNT expressions](#multi-component_cnt_expressions)

TechPaper #2011003: The CNT multi-component transient nucleation rate
=====================================================================

Compatibility
-------------

MatCalc version: 5.40 - …   
Author: E. Kozeschnik   
Created: 2011-06-27   
Revisions: 2018-04-09 E. Kozeschnik for version 6.01; 2023-06-23 P. Warczok for version 6.04

Objectives
----------

This paper discusses the implementation of the multi-component transient nucleation rate expression in the *MatCalc* precipitation kinetics framework. The equations presented below are derived in the framework of **Classical Nucleation Theory** (CNT) and they are strictly valid only for the special case of size-independent interfacial energy and volume free energy as well as homogeneous nucleation. The *MatCalc*-specific extensions (size effect/diffuse interface effect/volume energy effect) and their implementation are described in seperate documents.

Related documents
-----------------

1. [Heterogeneous nucleation](/techpapers/nucleation/het_nucl_sites "techpapers/nucleation/het_nucl_sites")

Main document
=============

Nucleation in *MatCalc* is realized in an extended Classical Nucleation Theory framework, where all input quantities are either given from experimental information (microstructure parameters such as dislocation density and grain size) or from theory (such as chemical driving force and interfacial energy). For details on the theoretical models, see the corresponding section in the list of *MatCalc*-relevant  [publications](http///matcalc.tuwien.ac.at/index.php/about/publications "http///matcalc.tuwien.ac.at/index.php/about/publications").

Energetics of nucleus formation
-------------------------------

If a nucleus of a new phase forms, the total change in energy $\Delta G\_\text{nucl}$ accompanying this event can be expressed as

\[ \Delta G\_\text{nucl} = \frac{4\pi}{3} \rho^3 \cdot \Delta G\_\text{vol} + 4\pi \rho^2 \gamma + \Delta G\_{het}\]

where $\rho$ is the radius of the nucleus, $\Delta G\_\text{vol}$ is the volume free energy change on nucleation, $\gamma$ is the specific interfacial energy and $\Delta G\_{het}$ describes the energetical effects of crystal structure defects. $\Delta G\_\text{vol}$ has negative value if the phase to form is thermodynamically stable.

Homogeneous nucleation
----------------------

In case of homogeneous nucleation, the precipitate nuclei appear within regular crystal structure of matrix. Here, the nucleation process is not promoted by any structure defects, like dislocations or any boundaries (grain boundaries, subgrain boundaries, interfaces of pre-existing precipitates). Hence the homogeneous nucleation energy does not contain any energetic contribution of these effects and is represented with only

\[ \Delta G\_\text{nucl,hom} = \frac{4\pi}{3} \rho^3 \cdot \Delta G\_\text{vol} + 4\pi \rho^2 \gamma\]

The function $\Delta G\_\text{nucl,hom}$ is shown in the next figure as a function of the nucleus radius.

[![ Total energy change on nucleation](/techpapers/nucleation/img/fig_nucleation_delta_g_of_r.png " Total energy change on nucleation")](/techpapers/nucleation/img/fig_nucleation_delta_g_of_r.png "techpapers/nucleation/img/fig_nucleation_delta_g_of_r.png")

From this relation, the extremum value for the critical radius $\rho^\*$ can be evaluated after setting the first derivative of $\Delta G\_\text{nucl,hom}$ to zero with

\[ \frac{\partial}{\partial \rho}\Delta G\_\text{nucl,hom} = 0\]

The critical radius is then

\[ \rho^\* = -\frac{2\gamma}{\Delta G\_\text{vol}} \]

and the critical nucleation energy is

\[ G^\* = \frac{16\pi}{3} \frac{\gamma^3}{(\Delta G\_\text{vol})^2} \]

The transient nucleation rate
-----------------------------

The number of newly formed precipitates per unit volume and unit time is given by the transient nucleation rate $J$ as

\[J=N\_0Z\beta^\*\exp\left({-\frac{G^\*}{k\_\text{B}T}}\right)\exp\left({-\frac{\tau}{t}}\right)\]

where $N\_0$ is the number of potential nucleation sites, $Z$ is the Zeldovich factor, $\beta^\*$ is the atomic attachment rate, $G^\*$ is the critical nucleation energy, $k\_\text{B}$ is the Boltzmann constant, $T$ is the absolute temperature, $\tau$ is the incubation time and $t$ is time.

Multi-component CNT expressions
-------------------------------

It is important, now, to realize that all quantities in the nucleation rate expression are defined either from independent experimental information (e.g., diffusion coefficients) or given in terms of some theoretical model (e.g., chemical driving force and interfacial energy). The table below summarizes all the quantities entering the transient nucleation rate expression.

| Symbol | Expression | comment |
| --- | --- | --- |
| $N\_0$ | / | Number of potential nucleation sites |
| $Z$ | \[{\left[-\frac{1}{2\pi k\_\text{B}T}\left( \frac{\partial^2 \Delta G\_\text{nucl}}{\partial n^2} \right)\_{n^\*} \right]^{\frac{1}{2}}}\] | Zeldovich factor |
| $\beta^\*$ | \[ \frac{4\pi \left(\rho^\* \right)^2}{a^4 v^\alpha} \left[ \sum\_{i=1}^{n}{\frac{\left(c\_{ki}-c\_{0i}\right)^2}{c\_{0i}D\_{0i}}} \right]^{-1} \] | Atomic attachment rate |
| $\tau$ | \[\frac{1}{2\beta^\* Z^2} \] | Incubation time |
| $G^\*$ | \[\frac{16\pi}{3} \frac{\gamma^3}{\left(\Delta G\_\text{chem}+\Delta G\_\text{el} \right)^2} \] | Critical nucleation energy |
| $\rho^\*$ | \[ -\frac{2\gamma}{\left(\Delta G\_\text{chem}+\Delta G\_\text{el} \right)} \] | Critical nucleation radius |
| $\Delta G\_\text{nucl}$ | \[ \frac{4\pi}{3}\rho^3 \cdot {\left(\Delta G\_\text{chem}+\Delta G\_\text{el} \right)} + 4\pi \rho^2 \cdot \gamma\] | Total energy change on nucleation |
| $\Delta G\_\text{chem}$ | \[ \sum^n\_{i=1}{X^{\beta}\_i(\frac{\mu^{\beta}\_i}{v^\beta}-\frac{\mu^{\alpha}\_i}{v^\alpha})} \] | Volume free energy change on nucleation (=negative chemical driving force) |
| $\Delta G\_\text{el}$ | \[ \frac{E}{1-\nu\_\text{P}} \cdot \left( \epsilon^\* \right)^2\] | Elastic strain energy, see also document  [Heterogeneous nucleation](/techpapers/nucleation/het_nucl_sites "techpapers/nucleation/het_nucl_sites") |
| $\Delta G\_\text{het}$ | depends on structure defect considered | Heterigeneous site nucleation energy, see also document  [Heterogeneous nucleation](/techpapers/nucleation/het_nucl_sites "techpapers/nucleation/het_nucl_sites") |
| $\gamma$ | \[ \frac{n\_\text{S} \cdot z\_\text{S,eff}}{N\_\text{A} \cdot z\_\text{L,eff}} \cdot \Delta H\] | Interfacial energy, see document  [Evaluation of interfacial energies](/techpapers/nucleation/interfacial_energy "techpapers/nucleation/interfacial_energy") for details |

The expressions above are valid for spherical precipitates.

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Anucleation%3Anucleation_rate2023&1788353249)