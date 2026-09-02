TechPaper #2014001: Evaluation of interfacial energies [MatCalc Documentation]



### Table of Contents

* [TechPaper #2014001: Evaluation of interfacial energies](#techpaper_2014001evaluation_of_interfacial_energies)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [The planar sharp interface](#the_planar_sharp_interface)
  + [The size correction factor](#the_size_correction_factor)
  + [The diffuse interface correction factor](#the_diffuse_interface_correction_factor)

TechPaper #2014001: Evaluation of interfacial energies
======================================================

Compatibility
-------------

MatCalc version: 5.60 - …   
Author: P. Warczok   
Created: 2014-04-09   
Revisions:

Objectives
----------

This paper describes how the energy of the precipitate/matrix interface is evaluated in *MatCalc*. The simple case of the planar shape interface is discussed. The correction factor which allows to extend this model for the more complex situations (curved interface, diffuse interface) are also presented.

Related documents
-----------------

None

Main document
=============

The energy of the precipitate/matrix interface (later referred to simply as “interfacial energy”) is an important parameter in the precipitate kinetics simulations. Its value determines the height of the nucleation energy barrier which the solute clusters have to overcome in order to create a separate precipitation phase. Furthermore, it affects the coarsening dynamics, when the system strives to minimize the total area of precipitate/matrix interfaces.

Unfortunately, the interface energy is not directly measurable in experiments. While its value can be indirectly extracted from the models applied on the nucleation or coarsening experimental results, the obtained scatter is considerably large. On the other hand, the atomistic calculation can deliver more precise values but its computational cost makes it hardly applicable to the multi-component systems with several precipitates present at a time.

The nearest-neighbor broken bond (*NNBB*) model offers a reliable physical basis and an easy-to-implement structure for the complex systems. Reformulation to generalized broken bond (*GBB*) model allowed to overcome the NNBB model dependence on the crystal structure and the interface orientation[1)](#fn__1). Because of the idealized case of the planar sharp interface, the correction factors to the GBB model were proposed accounting for the interface curvature for the spherical precipitate[2)](#fn__2) and for the diffuse composition gradient across extending the interface[3)](#fn__3).

The planar sharp interface
--------------------------

The energy of the planar sharp interface is calculated according to GBB model with the following formula:

\[\gamma\_{pl,sh}=\frac{n\_s z\_s}{n\_l z\_l}\Delta H\_{sol}\]

with:

$n\_s$ - number of atoms per unit interface area. It is set as $n\_s=({N\_A}/{V\_m})^{2/3}$, where $N\_A$ stands for Avogadro number and $V\_m$ stands for the molar volume of the system.

$n\_l$ - number of atoms in one mole, thus being equal to $N\_A$

$z\_s/z\_l$ - is the ratio of number of the bonds broken by the interface to the total number of bonds. It refers only to the bonds of the atoms on the interface. As shown in Ref. 1, this ratio converges to the value of $\sim0.329$ for both bcc and fcc structures, when the bonds to the atoms beyond the nearest neighborhood are considered.

$\Delta H\_{sol}$ - Solution enthalpy of 1 mole of precipitate atoms in the reference phase (reference phase is marked with asterisk in the *Phase summary* window). This value is stored as a variable **`DHM_DFP$EP`** (**“state variables GBB”** variables group), where **`“EP”`** stands for the name of the equilibrium parent phase for the precipitate (the creation of the precipitate phase itself is not required).

Considering the above, the formula for the planar sharp interface energy can be eventually given, as:

\[\gamma\_{pl,sh}=0.329({N\_A}{V\_m}^2)^{-1/3}\Delta H\_{sol}\]

The values of $\gamma\_{pl,sh}$ are evaluated by MatCalc for every phase (other than the reference phase) relative to the reference phase. These are stored in the variable **`CIE$EP`** (**“state variables GBB”** variables group; **`“EP”`** - equilibrium phase name). Once the precipitate phases are defined, the values for those are also found in the variable **`NUCL_CIE$PP`** (**“kinetics/ nucleation”** variables group; **`“PP”`** - precipitate phase name).

The size correction factor
--------------------------

The spherical precipitates possess a curved interface, instead of a planar one. This results in a different number of bonds broken by the interface per unit interface area. Hence, a size correction factor $\alpha\_{SCF}$ needs to be applied on the value relevant for the planar interface. As the curvature of the interface depends on the radius of the spherical precipitate $\rho$, $\alpha\_{SCF}$ needs to be a function of this parameter as well. A mathematical analysis presented in Ref.2 yields the following form:

\[\alpha\_{SCF}(\rho)=1-1.353\*10^{-10} \rho^{-1}+2.768\*10^{-21} \rho^{-2} (ln(\rho)+23.322)\]

Additionally, a lower limit value of $0.743$ is set for $\alpha\_{SCF}(\rho)$. The interfacial energy of the spherical precipitate is thus given as:

\[\gamma\_{sp}=\gamma\_{pl,sh}\alpha\_{SCF}(\rho)\]

Clearly, this crrection factor plays an important role during the nucleation stage, when the nuclei radii are small. The value of $\alpha\_{SCF}$ used for the modeling of the nucleation rate is stored in the variable **`NUCL_CIE_S_CORR$Phasename`** (**“kinetics/ nucleation”** variables group) and is evaluated for the calculated value of the critical radius. Once the precipitate is formed, $\alpha\_{SCF}$ is evaluated for every precipitate size class separately so that the proper size evolution is assured (e.g. coarsening).

The diffuse interface correction factor
---------------------------------------

When two phases are brought in contact together, some mixing is expected on the interface which increases the entropy. In result, some boundary width might be specified where a concentration gradient is observed, rather than a sudden (sharp) composition change. Again, the number of broken bonds in the diffuse interface is different than in the case of the sharp interface and this effect is accounted by the introduction of the correction factor $\beta\_{diff}$.

As the diffuse interface is entropically favorable, its presence will be more pronounced with the increasing temperatures. In Ref.3, this effect was analyzed using a regular solution approximation. This approach uses the concept of the critical temperature $T\_{crit}$ which is the highest temperature at which two phases are present in the system, regardless of the composition. At $T\_{crit}$ the composition of both phases is the same (the interface energy equals zero) whereas, at $T=0 K$ an ideal sharp interface is present. The numerical solution for the range $0 \div T\_{crit}$ allowed the formulation of the analytical expression for $\beta\_{diff}$ as a function of $T/T\_{crit}$ in the form of:

\[\beta\_{diff}(T/T\_{crit})=8.4729(\frac{T}{T\_{crit}})^6-26.691(\frac{T}{T\_{crit}})^5+32.717(\frac{T}{T\_{crit}})^4-17.674(\frac{T}{T\_{crit}})^3+\]
\[+2.2673(\frac{T}{T\_{crit}})^2-0.09(\frac{T}{T\_{crit}})+1.00047632\]

$T\_{crit}$ needs to be provided by the user. The values can be specified in the **“Precipitate”** tab of the **“Phase status”** window when a precipitate is selected. For the few cases, the following values can be recommended:

| System | Precipitate | $T\_{crit}$ [K] |
| --- | --- | --- |
| Fe | Cu(bcc) | 1700 |
| Fe | MnS | 2400 |
| Fe | NbC | 3300 |
| Fe | NbN | 3200 |
| Fe | TiN | 4200 |
| Fe | VC | 2100 |
| Fe | VN | 3300 |
| Ni | $\gamma$' (“gamma prime”) | 2500 |
| Al | $\beta$ (“Mg2Si”) | 2000 |
| Al | $\beta$' (“beta prime”) | 2200 |

The value of $\beta\_{diff}$ used by MatCalc is stored in the variable **`CIE_DI_CORR$Phasename`** (**“kinetics/ precipitates”** variables group). The value of the diffuse interface energy $\gamma\_{diff}$ is stored in the variable **`EIE$Phasename`** (**“kinetics/ precipitates”** variables group), with

\[\gamma\_{diff}=\gamma\_{pl,sh}\beta\_{diff}(T/T\_{crit})\]

[1)](#fnt__1)

B. Sonderegger, E. Kozeschnik, “Generalized nearest-neighbor broken-bond analysis of randomly oriented coherent interfaces in multicomponent fcc and bcc structures”, Metall. Mater. Trans. A, 2009, 40 (3) 499-510

[2)](#fnt__2)

B. Sonderegger, E. Kozeschnik, “Size dependence of the interfacial energy in the generalized nearest-neighbor broken-bond approach”, Scripta Mater., 2009, 60 (8) 635-638

[3)](#fnt__3)

B. Sonderegger, E. Kozeschnik, “Interfacial energy of diffuse phase boundaries in the generalized broken-bond approach”, Metall. Mater. Trans. A, 2010, 41 (12) 3262-3269

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Anucleation%3Ainterfacial_energy&1788353012)