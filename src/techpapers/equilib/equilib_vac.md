TechPaper #2014002: Equilibrium vacancy concentration [MatCalc Documentation]



### Table of Contents

* [TechPaper #2014002: Equilibrium vacancy concentration](#techpaper_2014002equilibrium_vacancy_concentration)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Thermodynamics](#thermodynamics)
  + [Literatur Results](#literatur_results)

TechPaper #2014002: Equilibrium vacancy concentration
=====================================================

Compatibility
-------------

MatCalc version: 5.60 - …   
Author: W. Mayer   
Created: 2014-04-09   
Revisions:

Objectives
----------

This paper describes how the vacancy concentration at equilibrium condition is evaluated in *MatCalc*. It serves as a basis for the discussion of the vacancy concentration evolution models.

Related documents
-----------------

* [Excess vacancies](/matcalc_docu/techpapers/precipitation/excess_va "techpapers:precipitation:excess_va")

Main document
=============

A knowledge of the equilibrium and excess vacancy concentration in metals, and their temperature dependence, is necessary for the fundamental understanding of the atomic processes of mass transport and the more complex diffusion related phenomena important to the technological applications of metals.
This motivated many people to define thermodynamics properties by measuring and calculating material properties, e.g. the formation energy, $E^f$, and the formation entropy, $ S^f $, which we will deal here with.
This topic is continued in the discussion of  [the influence of the excess vacancies on the precipitation kinetics](/matcalc_docu/techpapers/precipitation/excess_va "techpapers:precipitation:excess_va").

Thermodynamics
--------------

In a crystal lattice, one can always find vacant sites (i.e. vacancies) for the pure thermodynamical reason of minimizing the Gibbs free energy of the system. When lattice defects are introduced in a crystal, the free energy of the crystal is changed. A change due to a single defect is called the Gibbs free energy of formation, $ G\_i^f $, of the defect (i…mono-vacancy, di-vacancy, interstitial,…). The free energy is decomposed into an enthalpy term and an entropy term according
to the thermodynamic relation

\[ G\_i^f = H\_i^f - TS\_i^f , \]

where T is the absolute temperature (Kelvin). Here $ H\_i^f $, the formation
enthalpy of a certain defect, represents the work done when a defect
is created and $ S\_i^f $ is the formation entropy of the defect. The enthalpy
term can be expressed as

\[H\_i^f = E\_i^f - pV\_i^f , \]

where $ E\_i^f $ and $ V\_i^f $ are formation energy and formation
volume, respectively, and $p$ is the pressure. The term $ pV\_i^f $
is negligible at atmospheric pressure as the volume $ V\_i^f $ is
usually of the order of the volume of a unit cell in the
crystal.  
Therefore in literature the formation enthalpy is often replaced by the formation energy when the vacancy concentration is under consideration. The equilibrium mono-vacancy (i = ${Va}$) concentration [1)](#fn__1), $c\_{Va}^{eq}$, can be calculated by

\[
c\_{Va}^{eq} =\exp\left[- \frac{G\_{Va}^f}{k\_BT}\right] = \exp\left[- \frac{E\_{Va}^f + pV^f}{k\_BT}\right]\ \exp\left[\frac{S\_{Va}^f}{k\_B}\right]
\]
\[
\qquad \approx \exp\left[- \frac{E\_{Va}^f}{k\_BT}\right]\ \exp\left[\frac{S\_{Va}^f}{k\_B}\right]
\]

where we inserted the equations above neglecting the $pV\_i^f$ term (as usual in literature).

$S\_{Va}^f$ is a property of a single vacancy resulting
from the disorder introduced into the crystal by changing the vibrational properties of the neighbouring atoms. It can be calculated in the high temperature (Einstein) and harmonic approximation as

\[
S^f\_{Va} = k\_B \sum\limits\_{n} \ln \left( \frac{\omega\_{0n}}{\omega\_n}\right)
\]

where $\omega\_{0n}$ and $\omega\_{n}$ are the eigenfrequencies of the crystal without and with vacancies, respectively.
Atoms with a vacancy as a neighbour tend to vibrate with lower frequencies because some bonds ('springs') are missing. These atoms are therefore less well localized than the others and thus more unordered than regular atoms.  
The formation entropy measures the spatial extension of a vacancy, or, more generally, of a zero-dimensional defect. The larger $S^f$ is, the more extended the defect will be, because more atoms had to change their
vibration frequency ($1k\_B \sim $ atomic defect).

Literatur Results
-----------------

The following statements are generally accepted:

* Compression of the solid increases the vacancy-formation entropy;
* vacancy entropies can vary widely within one lattice structure;
* vacancy entropies are somewhat higher in bcc solids than in fcc solids.

The first conclusion is directly related to the vacancy relaxation as already mentioned above. The second one shows that there are other material properties which influence the formation entropy, e.g. atomic potentials and the existence of vacancy clusters. The reason for higher entropies in bcc solids can be found in the atomic packing factor which is 68% for bcc and 74% for fcc. This means it is easier for atoms in a bcc structure to relax and the conclusions drawn in connection with the relaxation can be used to explain the literature data.

|  |  |  |  |
| --- | --- | --- | --- |
| **Element (Structure)** | $E^f\_{Va}$ [kJ/mol] | $S^f\_{Va}$ [$k\_B$] | Reference |
| Al (fcc) | 63.68 | 0.7 | Siegel[2)](#fn__2) |
| Cr (bcc) | 190 $\pm$ 1.9 | 2.25 | Cahn[3)](#fn__3) / Burton[4)](#fn__4) |
| Fe (fcc) | 173.7 - 178.5 | - | Cahn |
| Fe (bcc) | 154.4 - 166.92 | 2.17 (?) | Cahn / Burton |
| Mg (hcp) | 76.23 | 0 $\pm$ 0.3 | Cahn |
| Mo (bcc) | 290 $\pm$ 1.9 | 1.6 | Cahn |
| Ni (fcc) | 172 $\pm$ 4.8 | 1.96 | Cahn / Burton |
| Ti (hcp) | 122.54 | 5.15 | Landolt[5)](#fn__5) / Kraftmakher[6)](#fn__6)(high T) |

The equilibrium vacancy concentration can be seen in the figure below for different assumptions on $E^f\_{Va}$ and $S^f\_{Va}$ for aluminium.

[![  
The equilibrium vacancy concentration in aluminium ](/matcalc_docu/techpapers/equilib/img/arrheniusformationentropy300-930.png "  
The equilibrium vacancy concentration in aluminium ")](/matcalc_docu/techpapers/equilib/img/arrheniusformationentropy300-930.png "techpapers:equilib:img:arrheniusformationentropy300-930.png")

Figure: The equilibrium vacancy concentration in aluminium

[1)](#fnt__1)

The total equilibrium vacancy concentration, $c\_{tot}^{eq}$, takes also di-, tri- and clusters of vacancies into account.

[2)](#fnt__2)

R.W. Siegel. Vacancy concentrations in metals. J.Nucl.Mater., 69-70(117-146), February
1978.

[3)](#fnt__3)

R. Cahn and P. Haasen.
Physical metallurgy: Ed. by R. W. Cahn. 4th rev. ed, volume 2.
1996.

[4)](#fnt__4)

J.J. Burton. Vacancy formation entropy in cubic metals. Phys.Rev.B, 5(8):2948, April 1972.

[5)](#fnt__5)

H. Ullmaier. Atomic defects in metals. In Landolt-Börnstein, New Series, volume 25.
Springer-Verlag, Heidelberg, 1991.

[6)](#fnt__6)

Y. Kraftmakher.
Equilibrium vacancies and thermophysical properties of metals.
Physics reports. North-Holland, 1998.

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Aequilib%3Aequilib_vac&1788353010)