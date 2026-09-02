TechPaper #2015001: Solid solution strengthening [MatCalc Documentation]



### Table of Contents

* [TechPaper #2015001: Solid solution strengthening](#techpaper_2015001solid_solution_strengthening)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [MatCalc model](#matcalc_model)
  + [Unit conversion](#unit_conversion)

TechPaper #2015001: Solid solution strengthening
================================================

Compatibility
-------------

MatCalc version: 5.60 - …   
Author: P. Warczok   
Created: 2015-05-06   
Revisions:

Objectives
----------

This paper describes how the contribution of the solid solution to the material strength is evaluated in MatCalc.

Related documents
-----------------

None

Main document
=============

Solid solutions are obtained when the solute atoms are introduced into the crystal lattice of the host atom. The solute atoms will substitute the host atoms on its crystal sites when the sizes of these atoms are comparable. Another possibility for the solute atoms is to occupy the interstitial sites of the host lattice, but this happens when the solute atoms are of a very small size compared to the host atom (e.g. carbon atoms in Fe-bcc or Fe-fcc lattice).

The size difference between the solute and host atoms results in tensile or compressive strains around the solutes present on the host lattice. These strains will interact with strains produced by the dislocations. Hence, the movement of the dislocation will require an application of the extra stress amount. This critical stress value $\sigma\_{ss}$ is found to be dependent on the solute atom concentration in the solid solution (matrix phase) $c\_i$ in the form of:  
  
\[ \sigma\_{ss}=\sum\limits\_{i} k\_i\*c\_i^{n\_i}\]

with

$k\_i$ - strengthening coefficient of element i

$n\_i$ - exponent relevant for element i (values in range of 0.5-1)

MatCalc model
-------------

In MatCalc, a similar formula is applied. The only difference is the presence of the exponents used for the summation, as shown below:  
  
\[ \sigma\_{ss}=\bigg[\Big(\sum\limits\_{i} (k\_i\*c\_{i}^{n\_i})^{m\_{sub}}\Big)\_{sub}^{\frac {m\_{tot}}{m\_{sub}}}+\Big(\sum\limits\_{i} (k\_i\*c\_{i}^{n\_i})^{m\_{int}}\Big)\_{int}^{\frac {m\_{tot}}{m\_{int}}}\bigg]^{1/m\_{tot}}\]

with

$m\_{sub}$ - coupling exponent applied for functions relevant for substitutional elements

$m\_{int}$ - coupling exponent applied for functions relevant for interstitial elements

$m\_{tot}$ - global exponent

In MatCalc, $c\_i$ is expressed with mole fraction in the above equation. $\sigma\_{ss}$ and $k\_i$ are expressed with pascal (Pa).

Unit conversion
---------------

It must be noted, that $c\_i$ can be expressed in various units (e.g. at.%, wt.%) in the functions for $\sigma\_{ss}$ found in the literature. Hence, some care in this regard must be taken when the values of $k\_i$, taken from a publication, are to be applied in MatCalc. The formula given below can be used for the adaptation of the $k\_i,wt%$ coefficient from the function of $c\_i$ expressed in wt.%  
  
\[ k\_{i,MatCalc}=k\_{i,wt\%}\*(100\*M\_i/M\_{mx})^{n\_i} \]

with

$k\_{i,MatCalc}$ - strengthening coefficient for MatCalc (relevant for $c\_i$ expressed in mole fraction

$k\_{i,wt\%}$ - strengthening coefficient for $c\_i$ expressed in wt.%

$M\_i$ - Molar mass of the element i

$M\_{mx}$ - Molar mass of the matrix host element

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Amprops%3Assol_strength&1788353012)