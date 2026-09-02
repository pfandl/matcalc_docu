TechPaper #2016001: Equilibrium trapping [MatCalc Documentation]



### Table of Contents

* [TechPaper #2016001: Equilibrium trapping](#techpaper_2016001equilibrium_trapping)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Thermodynamics](#thermodynamics)
  + [References](#references)

TechPaper #2016001: Equilibrium trapping
========================================

Compatibility
-------------

MatCalc version: 6.0100 - …   
Author: Y. Shan   
Created: 2016-08-01   
Revisions:

Objectives
----------

This paper describes how trapping at equilibrium condition is evaluated in *MatCalc*. It serves as a basis for the discussion for the trapping model.

Related documents
-----------------

* [Trapping kinetics](/techpapers/precipitation/trapping "techpapers/precipitation/trapping")
* [Example E30: Trapping in Fe-C](/examples/equilib/e30 "examples/equilib/e30")
* [Example E31: Segregation kinetics of P and S at grain boundaries](/examples/equilib/e31 "examples/equilib/e31")
* [Presentation of trapping model](/techpapers/spec_top_present/trapping.pptx "techpapers/spec_top_present/trapping.pptx (1.9 MB)")

Main document
=============

Thermodynamics
--------------

Trapping of an element $i$ on a trap $k$ reduces the system energy by an amount of $\Delta E$. Traps are usually system defects such as solute elements, dislocations or grain boundaries. The molar concentration $c\_i$ of the trapped element $i$ can be divided into a lattice (free) part, denoted by indices $Li$, and into trapped parts by traps $k$, denoted by indices $Tki$

\[
c\_i = c\_{Li} + \sum\_{k}c\_{Tki} .
\]

The occupancy of all lattice positions by an element $i$ is given by $y\_{Li}$ and vice versa for trap positions of a trap $k$ by $y\_{Tki}$. These are the product of the molar concentrations $c\_{Li}$, $c\_{Tki}$ and the molar volumes $V\_{L}$, $V\_{Tk}$

\[
y\_{Li} = c\_{Li} V\_{L}, \quad y\_{Tki} = c\_{Tki} V\_{Tk} .
\]

The molar volume $V\_{L}$ corresponds to the volume of 1 mole of lattice positions, whereas the molar volume $V\_{Tk}$ corresponds to the volume of 1 mole of trap positions of a trap $k$. The sum of the inverse molar volumes gives the inverse molar volume of the system $\Omega$

\[
\frac{1}{\Omega} = \frac{1}{V\_L}+\sum\_{k}\frac{1}{V\_{Tk}} .
\]

As for the molar volume of trapping sites $V\_{Tk}$, the value is given by the amount of trapping sources, expressed by a molar concentration $c\_k$, and their range, given by the coordination number $Z\_k$

\[
V\_{Tk} = \frac{1}{Z\_k c\_k} .
\]

Now the Gibbs Energy can be expressed by

\[G = G\_0 +
R\_gT \left[ \frac{\Omega}{V\_L}\left( \sum\limits\_{i} y\_{Li} \ln y\_{Li} + (1- \sum\limits\_{i} y\_{Li}) \ln (1-\sum\limits\_{i} y\_{Li})\right) + \\
\sum\limits\_{k} \frac{\Omega}{V\_{Tk}} \left(\sum\limits\_{i} y\_{Tki} \ln y\_{Tki} + (1- \sum\limits\_{i} y\_{Tki}) \ln (1-\sum\limits\_{i} y\_{Tki} \right)\right] - \sum\limits\_{k}\sum\limits\_{i}\frac{\Omega}{V\_{Tk}}y\_{Tki}\Delta E\_{ki}. \]

The equilibrium case for element $j$ trapped on a trap $l$ can be calculated by $\dot{G}=0$

\[ \frac{y\_{Lj}}{1-\sum\limits\_{i}y\_{Li}} \frac{1-\sum\limits\_{k}\sum\limits\_{i}y\_{Tki}}{y\_{Tlj}} = \exp\left(\frac{\Delta E\_{lj}}{R\_gT}\right) .
\]

References
----------

[1] J. Svoboda, F. D. Fischer, Modelling for hydrogen diffusion in metals with traps revisited, Acta Mater. 60 (2012) 1211-1220.

[2] F. D. Fischer, J. Svoboda, E. Kozeschnik, Interstitial diffusion in systems with multiple sorts of traps, Model. Simul. Mater. Sci. Eng. 21 (2013) 025008/1-13.

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Aequilib%3Atrapping&1788353010)