TechPaper #2014003: Excess vacancies [MatCalc Documentation]



### Table of Contents

* [TechPaper #2014003: Excess vacancies](#techpaper_2014003excess_vacancies)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Influence of the excess vacancies on the precipitation kinetics](#influence_of_the_excess_vacancies_on_the_precipitation_kinetics)

    - [Diffusion](#diffusion)
    - [Nucleation](#nucleation)
  + [Excess Vacancies](#excess_vacancies)

TechPaper #2014003: Excess vacancies
====================================

Compatibility
-------------

MatCalc version: 5.43 - …   
Author: E. Kozeschnik   
Created: 2014-04-25   
Revisions:

Objectives
----------

This paper describes the effects of the excess vacancies on the precipitation kinetics. Next, the models of the vacancy concentration evolution used in the kinetic simulation are presented. At the end, the approach for modeling of the vacancy trapping effects is discussed.

Related documents
-----------------

* [Equilibrium vacancy concentration](/techpapers/equilib/equilib_vac "techpapers/equilib/equilib_vac")
* [Example P2: Precipitation sequence in Al-Cu](/examples/precipitation/p2 "examples/precipitation/p2")

Main document
=============

The vacancies play a crucial role in the diffusion processes in the solid state. Other than for the most elements, the vacancy concentration in the alloy may vary during the temperature cycles. Clearly, the magnitude of the effects attributed to the vacancy presence will vary with the concentration of those. There are 2 models in MatCalc implemented which describe the dynamics of the vacancy generation and anihilation. Additionally, there is a possibility to account for the trapping of the vacancies which impedes the anihilation rate.

Influence of the excess vacancies on the precipitation kinetics
---------------------------------------------------------------

As already mentioned, the vacancies influence the diffusion process in the solids. There is also another effect of the vacancy concentration connected with the nucleation of the precipitates. Both topics are shortly presented below.

### Diffusion

Atoms diffuse by the position exchange with the neighbor vacancies. Clearly, the magnitude of this process depends on the ratio of the vacancies to the atoms - the higher the ratio, the higher the probability of an atom to have an empty space to jump in. Diffusion coefficients found in the literature usually refer to the condition with the equilibrium vacancy concentration $y\_{Va,eq}$. For the evaluation of the actual diffusion coefficient $D$, the following equation is used:

\[ D = D\_{eq} \frac{y\_{Va}}{y\_{Va,eq}} \]

with:

$D\_{eq}$ - Diffusion coefficient for the system with vacancy concentration $y\_{Va,eq}$

$y\_{Va}$ - Actual vacancy concentration

Obviously, $D$ impacts the nucelation and growth of the precipitates.

### Nucleation

Except of the above mentioned diffusion modification, there is antoher effect which impacts the nucleation stage of the precipitation process. As mentioned elsewhere, the nucleation barrier $G^\*$ is given as:

The following statements are generally accepted:

* Compression of the solid increases the vacancy-formation entropy;
* vacancy entropies can vary widely within one lattice structure;
* vacancy entropies are somewhat higher in bcc solids than in fcc solids.

The first conclusion is directly related to the vacancy relaxation as already mentioned above. The second one shows that there are other material properties which influence the formation entropy, e.g. atomic potentials and the existence of vacancy clusters. The reason for higher entropies in bcc solids can be found in the atomic packing factor which is 68% for bcc and 74% for fcc. This means it is easier for atoms in a bcc structure to relax and the conclusions drawn in connection with the relaxation can be used to explain the literature data.

|  |  |  |  |
| --- | --- | --- | --- |
| **Element (Structure)** | $E^f\_{Va}$ [kJ/mol] | $S^f\_{Va}$ [$k\_B$] | Reference |
| Al (fcc) | 63.68 | 0.7 | Siegel[1)](#fn__1) |
| Cr (bcc) | 190 $\pm$ 1.9 | 2.25 | Cahn[2)](#fn__2) / Burton[3)](#fn__3) |
| Fe (fcc) | 173.7 - 178.5 | - | Cahn |
| Fe (bcc) | 154.4 - 166.92 | 2.17 (?) | Cahn / Burton |
| Mg (hcp) | 76.23 | 0 $\pm$ 0.3 | Cahn |
| Mo (bcc) | 290 $\pm$ 1.9 | 1.6 | Cahn |
| Ni (fcc) | 172 $\pm$ 4.8 | 1.96 | Cahn / Burton |
| Ti (hcp) | 122.54 | 5.15 | Landolt[4)](#fn__4) / Kraftmakher[5)](#fn__5)(high T) |

Excess Vacancies
----------------

Excess vacancies can be inserted in a solid by different methods:

* Quenching from high temperatures
* Plastic deformation
* Irridation

This excess vacancies will annihilate at jogs, dislocations, and surfaces (e.g. grain boundaries). How fast depends mainly on the temperature of the solid and on the number of the mentioned traps.

[1)](#fnt__1)

R.W. Siegel. Vacancy concentrations in metals. J.Nucl.Mater., 69-70(117-146), February
1978.

[2)](#fnt__2)

R. Cahn and P. Haasen.
Physical metallurgy: Ed. by R. W. Cahn. 4th rev. ed, volume 2.
1996.

[3)](#fnt__3)

J.J. Burton. Vacancy formation entropy in cubic metals. Phys.Rev.B, 5(8):2948, April 1972.

[4)](#fnt__4)

H. Ullmaier. Atomic defects in metals. In Landolt-Börnstein, New Series, volume 25.
Springer-Verlag, Heidelberg, 1991.

[5)](#fnt__5)

Y. Kraftmakher.
Equilibrium vacancies and thermophysical properties of metals.
Physics reports. North-Holland, 1998.

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Aprecipitation%3Aexcess_va&1788353011)