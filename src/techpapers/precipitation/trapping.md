TechPaper #2016002: Trapping kinetics [MatCalc Documentation]



### Table of Contents

* [TechPaper #2016002: Trapping kinetics](#techpaper_2016002trapping_kinetics)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Thermodynamics](#thermodynamics)
  + [References](#references)

Section 'Trapping kinetics' is still under construction!!

[![](/matcalc_docu/wiki/under_construction_icon-yellow.svg.png)](/wiki/lib/exe/detail.php?id=techpapers%3Aprecipitation%3Atrapping&media=wiki/under_construction_icon-yellow.svg.png "wiki:under_construction_icon-yellow.svg.png")

TechPaper #2016002: Trapping kinetics
=====================================

Compatibility
-------------

MatCalc version: 6.0100 - …   
Author: Y. Shan   
Created: 2016-08-09   
Revisions:

Objectives
----------

This paper describes how trapping for kinetics is evaluated in *MatCalc*. It serves as a basis for the discussion for the trapping model.

Related documents
-----------------

* [Equilibrium trapping](/matcalc_docu/techpapers/equilib/trapping "techpapers:equilib:trapping")
* [Example E30: Trapping in Fe-C](/matcalc_docu/examples/equilib/e30 "examples:equilib:e30")
* [Presentation of trapping model](/matcalc_docu/techpapers/spec_top_present/trapping.pptx "techpapers:spec_top_present:trapping.pptx (1.9 MB)")

Main document
=============

Thermodynamics
--------------

The kinetics for trapped elements are obtained by the thermodynamic extremal principle [1]

\[
Q = -\dot{G} .
\]

The dissipation $Q$ at dislocations of an element $i$ due to diffusion can be approximated by [2]

\[
Q \approx \frac{ R\_g T a^2 V\_L }{2 D\_i \Omega y\_{Li} V\_{T,disl}} \dot{y}\_T^2 \left( \ln \left( \frac{R}{a} \right) - \frac{3}{4} \right) ,
\]

with $a$ being the acting radius of a dislocation (sites within this radius are considered as trap positions) in a cylindrical unit cell of radius $R$. $D\_i$ the diffusion coefficient of element $i$. $V\_{T,disl}$ is the molar volume for trap sites in dislocations and is given by

\[
V\_{T,disl} = \frac{1}{\rho \pi a^2},
\]

with $\rho$ being the dislocation density.

Using the thermodynamic extremal principle, this leads to the following evolution of trapped elements

\[
\dot{y\_T} = \frac{2D\_i}{a^2\left(\ln\frac{R}{a}-\frac{3}{4}\right)} y\_L \left( \ln\frac{y\_L(1-y\_T)}{y\_T(1-y\_L)} + \frac{\Delta E}{R\_gT} \right) .
\]

The dissipation $Q$ at grain boundaries due to diffusion is given by [2]

\[
Q = \frac{ R\_g T \delta V\_L}{10 D\_i \Omega y\_{Li} V\_{T,gb}} \dot{y}\_T^2 ,
\]

and the molar volume of trap positions for grain boundaries

\[
V\_{T,gb} = \frac{\left(2R\_G + \delta \right)^3}{12 R\_G^2 \delta} \approx \frac{2 R\_G}{3 \delta} ,
\]

with $R\_G$ being the grain radius in a unit cell and $\delta$ the grain boundary thickness, which is considered to be the positions for trapping.

The evolution of trapped elements at grain boundaries is finally given by
\[
\dot{y\_T} = \frac{10 D\_i}{R\_G \delta} y\_L \left( \ln\frac{y\_L(1-y\_T)}{y\_T(1-y\_L)} + \frac{\Delta E}{R\_gT} \right) .
\]

References
----------

[1] J. Svoboda, I. Turek, F.D. Fischer, Application of the thermodynamic extremal principle to modelling of thermodynamic processes in material science, Phil. Mag. 85 (2005) 3699-3707.

[2] J. Svoboda, G.A. Zickler, E. Kozeschnik, F.D. Fischer, Kinetics of interstitial segregation in Cottrell atmospheres and grain boundaries, Phil. Mag. Lett. 95 (2015) 458-465.

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Aprecipitation%3Atrapping&1788353011)