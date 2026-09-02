TechPaper #2018001: Nucleus composition [MatCalc Documentation]



### Table of Contents

* [TechPaper #2018001: Nucleus composition](#techpaper_2018001nucleus_composition)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Ortho-equilibrium](#ortho-equilibrium)
  + [Para-equilibrium](#para-equilibrium)
  + [Constrained equilibrium](#constrained_equilibrium)
  + [Fixed molar site fractions](#fixed_molar_site_fractions)
  + [Minimum critical nucleation energy (G\*)](#minimum_critical_nucleation_energy_g)
  + [Maximum nucleation rate (J)](#maximum_nucleation_rate_j)

TechPaper #2018001: Nucleus composition
=======================================

Compatibility
-------------

MatCalc version: 6.01 - …   
Author: P. Warczok   
Created: 2018-12-19   
Revisions:

Objectives
----------

This paper describes the available options for the definition of the precipitate nucleus composition. Depending on the chosen option, the relevant nucleation rate is calculated by MatCalc.

Related documents
-----------------

[The multi-component transient nucleation rate (#2011003)](/techpapers/nucleation/nucleation_rate "techpapers/nucleation/nucleation_rate")

Main document
=============

Nucleus composition of the given precipitate phase is one of the parameters that determine the value of the nucleation driving force ($-\Delta G\_\text{chem}$) and the precipitate/matrix interface energy $\gamma$. Hence, various nucleus compositions will result in different critical nucleation energy $G^\*$ the nucleation rate $J$ values.  
  
\[J=N\_0Z\beta^\*\exp\left({-\frac{G^\*}{k\_\text{B}T}}\right)\exp\left({-\frac{\tau}{t}}\right)\]
\[ G^\*=-\frac{2\gamma}{\left(\Delta G\_\text{chem}+\Delta G\_\text{el} \right)} \]

MatCalc gives the following options for the nucleus composition assumption:

* Ortho-equilibrium
* Para-equilibrium
* Constrained equilibrium
* Fixed molar site fractions
* Minimum critical nucleation energy ($G^\*$)
* Maxmium nucleation rate ($J$)

In many cases, the “ortho-equilibrium”, “minimum critical nucleation energy” and “maximum nucleation rate” result in almost identical values of nucleus composition.

Ortho-equilibrium
-----------------

Nucleus composition is evaluated by MatCalc which results in the highest value of the nucleation driving force ($-\Delta G\_\text{chem}$) for the precipitate phase at the given system state.

Para-equilibrium
----------------

Nucleus composition is taken as close to the matrix composition as possible. This is realized with identical u-fraction values of substitutional elements for matrix and precipitate phase.

Constrained equilibrium
-----------------------

Nucleus composition resulting in the highest driving force is taken, considering the composition constraints defined for the parent equilibrium phase.

Fixed molar site fractions
--------------------------

The site fractions of various elements in the nucleus are to be defined by the user.

Minimum critical nucleation energy (G\*)
----------------------------------------

Nucleus composition which yields the minimal value of $G^\*$ is evaluated and taken for the nuclei.

Maximum nucleation rate (J)
---------------------------

Nucleus composition appears in the nucleation rate formula at the critical nucleation energy ($G^\*$) and atomic attachment rate ($ß^\*$). With this option, the composition which yields the maximal value of $J$ is evaluated and taken for the nucleus.

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Anucleation%3Anucleus_composition&1788353012)