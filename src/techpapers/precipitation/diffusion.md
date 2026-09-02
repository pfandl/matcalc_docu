TechPaper #2011004: Diffusion in heterogeneous precipitation [MatCalc Documentation]



### Table of Contents

* [TechPaper #2011004: Diffusion in heterogeneous precipitation](#techpaper_2011004diffusion_in_heterogeneous_precipitation)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Diffusion in the undisturbed crystal](#diffusion_in_the_undisturbed_crystal)
  + [Diffusion along dislocations](#diffusion_along_dislocations)

    - [Recommended values for the dislocation core diffusivity](#recommended_values_for_the_dislocation_core_diffusivity)
  + [Diffusion along grain boundaries](#diffusion_along_grain_boundaries)

    - [Recommended values for the grain boundary diffusivity](#recommended_values_for_the_grain_boundary_diffusivity)
  + [Tuning diffusivities for special cases](#tuning_diffusivities_for_special_cases)

    - [Recommended values for MDEF](#recommended_values_for_mdef)

TechPaper #2011004: Diffusion in heterogeneous precipitation
============================================================

Compatibility
-------------

MatCalc version: 5.42 - …   
Author: E. Kozeschnik   
Created: 2011-06-29   
Revisions:

Objectives
----------

In this paper, the implementation of diffusion during heterogenous precipitation in the *MatCalc* precipitation kinetics framework is discussed.

Related documents
-----------------

1. [Heterogenous nucleation](/techpapers/nucleation/het_nucl_sites "techpapers/nucleation/het_nucl_sites")
2. [Excess vacancies](/techpapers/precipitation/excess_va "techpapers/precipitation/excess_va")

Main document
=============

Diffusion in the undisturbed crystal
------------------------------------

The *MatCalc* multi-component diffusion model is based on the treatment developed at KTH Stockholm for the DICTRA software. Accordingly, the diffusional mobility $M\_i$ of component *i* and the tracer diffusion coefficient $D^\*\_i$ are related by the equation

\[D^\*\_i = RTM\_i\]

with $R$ being the Universal Gas Constant and $T$ being temperature. The values of $M\_i$ and $D^\*\_i$ are accessible through the *MatCalc* variables **MO$phase\_name$element** and **DT$phase\_name$element** in the 'diffusion' category of the variables list.

In the *MatCalc* mobility databases, only the value of $M\_i$ is stored, since the thermodynamic factor can be calculated from the thermodynamic information and $D^\*\_i$ is then uniquely given as a function of composition and temperature only.

**Note:** The diffusion coefficient used in the precipitation kinetics framework is the tracer diffusivity given above. In the microstructure simulation framework for long-range diffusion, the chemical diffusivity is used in the form of a diffusion matrix, which accounts for all the non-diagonal cross-terms also. In the precipitation kinetics framework, the cross-terms come into play directly in the evolution equations described in the corresponding publication[1)](#fn__1).

If you want to investigate the influence of the alloy chemistry on the diffusion coefficient, use the chemical diffusion coefficient $D^c\_i$, which is defined as

\[D^c\_i = RTM\_i \cdot \phi\]

with $\phi$ being the thermodynamic factor. The corresponding *MatCalc* variable is denoted **D$phasename$element**. This version of diffusion coefficient is *not* used in the precipitation kinetics framework, since the *MatCalc* evolution equations for precipitation are based on the explicit us of chemical potentials, which takes the effect of alloy composition into account directly.

Diffusion along dislocations
----------------------------

Dislocations are linear lattice defects, which provide a network of linear high-speed diffusion paths. In the core of a dislocation, the lattice is expanded, thus supporting the possibility for solute atoms to move considerably faster than in the undisturbed bulk crystal.

**Note:** The mobilities saved in the database are assessed for equilibrium conditions, which means that some given mean grain size and a dislocation density (most likely) close to its equilibrium value have been present during the experiment. The diffusivities of the database do *not* represent values for defect-free single crystals, but poly-crystalline microstructures.

The diffusion carried along by dislocations can be taken into account rigorously in the diffusivities used in the precipitation kinetics simulations by simply estimating the ratio between undisturbed crystal volume and the volume consumed by the dislocation cores. In *MatCalc*, the following relation is used to define a *diffusion correction factor for pipe diffusion* along dislocations

\[D\_i=D^\*\_i \cdot \alpha\_\text{PD}\],

with $D\_i$ being the effective diffusion coefficient of component $i$. The correction factor $\alpha\_\text{PD}$ is given as

\[\alpha\_\text{PD} = \frac{D\_i}{D^\*\_i} = \frac{1}{D^\*\_i} \left( {\pi R^2\_\text{core}\rho \cdot D^\*\_{di} + \left( 1-\pi R^2\_\text{core}\rho \right)\cdot D^\*\_{i}} \right)\].

where $D^\*\_{di}$ is the diffusivity in the dislocation core.

The value of $\alpha\_\text{PD}$ is accessible through the *MatCalc* variable **PIPE\_DCF$prec\_domain$element** in the 'kinetics: prec\_domain special' category.

### Recommended values for the dislocation core diffusivity

In the above equations, a key parameter for evaluation of the effective diffusivity $D\_i$ is the diffusivity of element $i$ in the dislocation core $D^\*\_{di}$. In MatCalc, the dislocation core diffusivity is coupled to the bulk diffusivity via a factor $\alpha\_{di}$, which reads

\[D^\*\_{di}=\alpha\_{di}\cdot D^\*\_i\]

$\alpha\_{di}$ can be defined as a user-function in the 'subst. disl. diffusion as ratio from matrix' and 'interst. disl. diffusion as ratio from matrix' fields of the 'special' tab of the 'precipitation domain' dialog. Note that you can set the ratios separately for substitutional and interstitial elements.

**Note:** The values for $\alpha\_{di}$ that are evaluated with the above equation are used in all *MatCalc* expressions, where the tracer diffusion The following values are recommended for different alloy systems:

| system | Temperature [K] | $\alpha\_{di}$ | MatCalc syntax | source |
| --- | --- | --- | --- | --- |
| Al (fcc) | 298 - 933 | \[ 1.07\cdot10^{-1} \cdot exp \left( \frac{43900}{RT} \right) \] | `1.07e3*exp(43900/(R*T))` | unpublished research |
| Fe (fcc) | 298 - 1811 | \[ 6.43\cdot10^{-1} \cdot exp \left( \frac{118700}{RT} \right) \] | `6.43e-1*exp(118700/(R*T))` |
| Fe (bcc) | 298 - 693 | \[ 3.33\cdot10^{1} \cdot exp \left( \frac{70000}{RT} \right) \] | `3.33e1*exp(70000/(R*T))` |
| Fe (bcc) | 693 - 1214 | \[ 1.33\cdot10^{-2} \cdot exp \left( \frac{115000}{RT} \right) \] | `1.33e-2*exp(115000/(R*T))` |
| Fe (bcc) | 1214 - 1811 | \[ 1.00\cdot10^{2} \cdot exp \left( \frac{25000}{RT} \right) \] | `1.00e2*exp(25000/(R*T))` |
| Ni (fcc) | 298 - 1728 | \[ 1.74\cdot10^{-1} \cdot exp \left( \frac{116100}{RT} \right) \] | `1.74e-1*exp(116100/(R*T))` |

coefficient $D^\*\_i$ enters. The pipe diffusion correction factor thus represents a **prefactor to the diffusivity value** that is calculated from the mobility database.

In general, the value of $\alpha\_{di} \approx 1$ for typical dislocation densities of well-annealed metallic materials, i.e. $10^{11} m/m^3$ for fcc metals and $10^{12} m/m^3$ for bcc metals. However, in the case of dislocation densities exceeding approximately $10^{13}$ or $10^{14} m/m^3$, the influence of $\alpha\_{di}$ becomes significant. At dislocation densities of $10^{15}$ or $10^{16} m/m^3$, which are typical for martensitic microstructures, the pipe diffusion correction factor adopts values of several orders of magnitude.

***Important note …***

For **predictive simulations** in deformed metals and/or martensitic or bainitic microstructures, it is absolutely necessary to **account for the influence of pipe diffusion**! This effect often accelerates the precipitation kinetics by several orders of magnitude.

Diffusion along grain boundaries
--------------------------------

In *MatCalc*, grain boundaries are assumed to be high-angle boundaries, which provide a network of two-dimensional high-speed diffusion paths. In contrast to the pipe diffusion effect, the influence of grain boundary diffusion is *not* explicitely taken into account as a prefactor to the tracer diffusion coefficient. Instead, the influence of grain boundary diffusion on the overall precipitation kinetics must be included manually. See the corresponding section below.

The grain boundary diffusion coefficient is, however, used in the kinetic framework for grain boundary precipitation[2)](#fn__2). The grain boundary diffusivity is explicitely integrated in the evolution equations and must be correctly set, if this type of precipitation geometry is used. For the correct definition of grain boundary nucleation and growth see also the technical paper on  [Heterogenous nucleation](/techpapers/nucleation/het_nucl_sites "techpapers/nucleation/het_nucl_sites").

### Recommended values for the grain boundary diffusivity

In the treatment of grain boundary precipitation, the grain boundary diffusivity $D\_{gi}$ is a key parameter. In MatCalc, the grain boundary diffusivity is coupled to the bulk diffusivity via a factor $\alpha\_{gi}$, which reads

\[D^\*\_{gi}=\alpha\_{gi}\cdot D^\*\_i\]

$\alpha\_{gi}$ can be defined as a user-function in the 'subst. gb diffusion as ratio from matrix' and 'interst. gb diffusion as ratio from matrix' fields of the 'special' tab of the 'precipitation domain' dialog. Note that you can set the ratios separately for substitutional and interstitial elements.

The following values are recommended for different alloy systems:

| system | Temperature [K] | $\alpha\_{gi}$ | MatCalc syntax | source |
| --- | --- | --- | --- | --- |
| Al (fcc) | 298 - 933 | \[ 1.36\cdot10^{0} \cdot exp \left( \frac{67000}{RT} \right) \] | `1.36*exp(67000/(R*T))` | unpublished research |
| Fe (fcc) | 298 - 1811 | \[ 7.86\cdot10^{-1} \cdot exp \left( \frac{141400}{RT} \right) \] | `7.86e-1*exp(141400/(R*T))` |
| Fe (bcc) | 298 - 693 | \[ 6.33\cdot10^{1} \cdot exp \left( \frac{87700}{RT} \right) \] | `6.33e1*exp(87700/(R*T))` |
| Fe (bcc) | 693 - 1214 | \[ 2.53\cdot10^{-2} \cdot exp \left( \frac{132700}{RT} \right) \] | `2.53e-2*exp(132700/(R*T))` |
| Fe (bcc) | 1214 - 1811 | \[ 1.90\cdot10^{2} \cdot exp \left( \frac{42700}{RT} \right) \] | `1.90e2*exp(42700/(R*T))` |
| Ni (fcc) | 298 - 1728 | \[ 5.22\cdot10^{-3} \cdot exp \left( \frac{184700}{RT} \right) \] | `5.22e-3*exp(184700/(R*T))` |

Tuning diffusivities for special cases
--------------------------------------

In some cases of precipitation kinetics simulations, the diffusion coefficient stored in the mobility database needs some adjustment, since the actual microstructure of the system does not represent the conditions for which the diffusivity has been experimentally assessed. For these situations, the so-called 'matrix diffusion enhancement factor' (MDEF) can be utilized to 'tune' the diffusion coefficients used in the simiulations toi values that better represent the experimental conditions.

The MDEF is accessible through the 'substitutional matrix diffusion enhancement' and the 'interstitial matrix diffusion enhancement' in the 'special' tab of the 'precipitation domains' dialog.

### Recommended values for MDEF

In most practical situations, it will *not* be necessary to modify the MDEF value. Sometimes, this parameter value is set between 0.2 to 5, in order to achieve 'perfekt' agreement between simulation and experiment.

**Note:** In the viewpoint of a general simulation strategy, it is not recommended , however, to change this value away from the default value of 1.0, since any change of these parameters does impair the predictive capabilities of your simulations.

In some cases, however, a modification of the experimental diffusivities can be justified. One example, for instance, is precipitation at martensite subgrain boundaries. It is well known that diffusion along the subgrain boundary network is significantly faster than diffusion in the bulk crystal. For this type of precipitate, an MDEF of 5 has shown to be a reasonable diffusion enhancement, which seems to reproduce the real diffusion conditions reasonably well. For any other 'artifical' modification of the diffusion coefficients make sure that you can justify it on physical grounds.

The following values are recommended for selected cases:

| case | MDEF | comment |
| --- | --- | --- |
| Typical precipitation simulation | 1.0 | **default value is recommended** |
| Grain boundary precpitation | 1.0 | Fast GB diffusion is accounted for in the gb precipitation model and the gb diffusion coefficient $D\_{gi}$. |
| Grain boundary edges and corners | 1.0 - 3.0 | Fast gb diffusion not accounted for in the model. Slight acceleration plausible |
| Subgrain boundaries | 1.0 - 5.0 | Fast sgb diffusion not accounted for in the model. Slight acceleration plausible |

**Note:** In addition to the acceleration of diffusion along grain boundaries and subgrain boundaries, significantly higher diffusion knietics can also be stimulated by the presence of **quenched-in** or **deformation-induced excess vacancies**. See the corresponding article  [Excess vacancies](/techpapers/precipitation/excess_va "techpapers/precipitation/excess_va") for a description of this effect and how to take it into account in your simulations.

[1)](#fnt__1)

J. Svoboda, F. D. Fischer, P. Fratzl and E. Kozeschnik, „Modelling of kinetics in multi-component multi-phase systems with spherical precipitates I. – Theory“, Mater. Sci. Eng. A, 2004, 385 (1-2) 166-174.

[2)](#fnt__2)

E. Kozeschnik, J. Svoboda, R. Radis and F.D. Fischer, “Mean-field model for the growth and coarsening of stoichiometric precipitates at grain boundaries”, Model. Simul. Mater. Sci. Eng. 18 (2010) 015011 (19pp).

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Aprecipitation%3Adiffusion&1788352980)