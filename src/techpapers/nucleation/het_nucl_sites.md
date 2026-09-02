TechPaper #2011002: Treatment of heterogeneous nucleation [MatCalc Documentation]



### Table of Contents

* [TechPaper #2011002: Treatment of heterogeneous nucleation](#techpaper_2011002treatment_of_heterogeneous_nucleation)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Homogeneous nucleation](#homogeneous_nucleation)

    - [Potential nucleation sites](#potential_nucleation_sites)
    - [Misfit strain effect](#misfit_strain_effect)
  + [Dislocations](#dislocations)

    - [Potential nucleation sites](#potential_nucleation_sites1)
    - [Misfit strain effect](#misfit_strain_effect1)
    - [Removal of a dislocation line segment](#removal_of_a_dislocation_line_segment)
  + [Grain boundaries, edges and corners](#grain_boundaries_edges_and_corners)

    - [Potential nucleation sites](#potential_nucleation_sites2)
    - [Misfit strain effect](#misfit_strain_effect2)
    - [Removal of grain boundary area](#removal_of_grain_boundary_area)
    - [Chemical driving force for grain boundary nucleation](#chemical_driving_force_for_grain_boundary_nucleation)
  + [Subgrain boundaries, edges and corners](#subgrain_boundaries_edges_and_corners)

    - [Potential nucleation sites](#potential_nucleation_sites3)
    - [Misfit strain effect](#misfit_strain_effect3)
    - [Removal of subgrain boundary area](#removal_of_subgrain_boundary_area)
  + [Other precipitates](#other_precipitates)

    - [Nucleate at precipitate surface](#nucleate_at_precipitate_surface)
    - [Nucleate with equivalent interfacial energy](#nucleate_with_equivalent_interfacial_energy)
    - [Nucleate within range of transformation radius](#nucleate_within_range_of_transformation_radius)
  + [Multiple selection of heterogeneous nucleation sites](#multiple_selection_of_heterogeneous_nucleation_sites)

TechPaper #2011002: Treatment of heterogeneous nucleation
=========================================================

Compatibility
-------------

MatCalc version: 5.44 - …   
Author: E. Kozeschnik   
Created: 2011-06-23   
Revisions: 2011-06-28 (koze), 2011-08-22 (koze), 2011-09-06 (koze), 2023-06-23 (warp)

Objectives
----------

This paper discusses the implementation of heterogenous nucleation in the *MatCalc* precipitation kinetics framework.

Related documents
-----------------

1. [The multi-component transient nucleation rate](/matcalc_docu/techpapers/nucleation/nucleation_rate "techpapers:nucleation:nucleation_rate")
2. [Diffusion in heterogenous precipitation](/matcalc_docu/techpapers/precipitation/diffusion "techpapers:precipitation:diffusion")

Main document
=============

The *MatCalc* multi-component precipitate nucleation model is described in  [The multi-component transient nucleation rate](/matcalc_docu/techpapers/nucleation/nucleation_rate "techpapers:nucleation:nucleation_rate"). In addition to homogeneous nucleation in the undisturbed crystal bulk volume, in *MatCalc*, nucleation can occur on different types of heterogenous nucleation sites (HNS), which are

* dislocations
* grain boundaries (2-grain junctions)
* grain boundary edges (3-grain junctions)
* grain boundary corners (4-grain junctions)
* subgrain boundaries
* subgrain boundary edges
* subgrain boundary corners
* other precipitates

The choice of nucleation site has various important consequences in the treatment of nucleation. These are

| parameter | comment |
| --- | --- |
| $N\_0$ | Potential number of nucleation sites. For each HNS, the number of activated sites is evaluated. It is assumed that each single atom located on the particular HNS acts as a potential site. In homogeneous nucleation, all atoms of the unit volume are assumed to be potential sites, for nucleation on dislocations, only atoms located in the dislocation core are active nucleation sites. Similar applies for nucleation on grain boundaries and subgrain boundaries. Details on this are given in the sections below. |
| $G^\*$ | The nucleation barrier $G^\*$ is *reduced* due to removal of a part of the heterogeneous nucleation site area, which is either a dislocation line section or grain boundary area. In the present *MatCalc* version, this effect is implemented only for nucleation at grain boundaries in the form of the Clemm-Fisher model[1)](#fn__1), where a (reduced) $G^\*$ is calculated. In *MatCalc*, this quantity is transformed into an effective (reduced) interfacial energy. |
| $G^\*$ | The nucleation barrier $G^\*$ is *increased*, since the driving force for precipitation is reduced by elastic misfit stress (See the document on  [The multi-component transient nucleation rate](/matcalc_docu/techpapers/nucleation/nucleation_rate "techpapers:nucleation:nucleation_rate") for details on the mathematical expression). This effect can be activated by making the appropriate settings for the Young's modulus and volumetric misfit in precipitation domain and precipitate, and by checking the “account for coherent misfit stress” option in the phase status dialog. |

In practical calculation, the first parameter, $N\_0$, is controlled in the 'nucleation' tab of the 'phase status' dialog, as well as the 'structure' tab of the 'precipitation domain' dialog. In the 'phase status' dialog, the selection of HNS is used to evaluate the correct number of potential nucleation sites. In the 'precipitation domain' dialog, the microstructure parameters controlling $N\_0$ are defined, which is the dislocation density, grain size and subgrain size. In addition, one of the three models for on-particle nucleation can be selected.

Further details on the implementation are discussed below.

Homogeneous nucleation
----------------------

Homogeneous nucleation is treated in the framework of homogeneous multi-component Classical Nucleation Theory. This topic is discussed in detail in the technical paper on  [The multi-component transient nucleation rate](/matcalc_docu/techpapers/nucleation/nucleation_rate "techpapers:nucleation:nucleation_rate").

### Potential nucleation sites

For homogeneous nucleation, each atom in the bulk volume is assumed to be a potential nucleation site. The number of sites $N\_0$ is simply evaluated from

\[N\_0=\frac{N\_{\text{A}}}{v\_m}\]

where $N\_\text{A}$ is Avogadro's number and $v\_m$ is the molar volume.

### Misfit strain effect

The major factor influencing the nucleation barrier in homogeneous coherent nucleation is the elastic misfit stress. In practical simulation, this effect can be activated by making the appropriate settings for the Young's modulus $E$ and volumetric misfit $v^\*$ in precipitation domain and precipitate, and by checking the “account for coherent misfit stress” option in the phase status dialog.

The nucleation barrier $G^\*$ is then evaluated as

\[G^\* = \frac{16 \pi}{3} \frac{\gamma^3}{\left({\Delta G\_\text{vol} + \Delta G\_\text{el}}\right)^2}\]

where $\gamma$ is the interfacial energy, $\Delta G\_\text{vol}$ is the volume free energy change on nucleation and $\Delta G\_\text{el}$ is the elastic energy of the stress field accompanying the nucleateion process.

**Note:** $G^\*$ in the elastically strained state is always larger than $G^\*$ in the unstrained state.

The elastic energy $\Delta G\_\text{el}$ of a spherical inclusion can be calculated with the help Eshelby's concept, which delivers

\[\Delta G\_\text{el} = \frac{E}{1-\nu} \cdot (\epsilon^\*)^2 = \frac{E}{9(1-\nu)} \cdot (v^\*)^2\]

where $\nu$ is Poisson's ratio, $\epsilon^\*$ is the linear misfit strain and the relation hold $\epsilon^\*=v^\*/3$.

In most situations, homogeneous nucleation occurs with a coherent interface between matrix and precipitate. In some cases, however, homogeneous nucleation might occur also with incoherent interfaces. This is claimed, for instance, to be the case for NbC precipitation in austenite (steel), where NbC has a large volumetric misfit to the fcc matrix.

Dislocations
------------

### Potential nucleation sites

For heterogeneous nucleation at dislocations, each atom located in the dislocation core is assumed to be a potential nucleation site. The corresponding number is evaluated from the dislocation density (set in the 'structure' tab of the 'precipitation domain' dialog) according to

\[N\_0=\rho {\left ( \frac{N\_\text{A}}{v\_\text{m}}\right )}^{\frac{1}{3}}\]

where $\rho$ is the dislocation density, $N\_\text{A}$ is Avogadro's number and $v\_\text{m}$ is the molar volume.

### Misfit strain effect

When a precipitate nucleates coherently on a dislocation, the elastic misfit stress field of the precipitate interacts with the stress field of the dislocation. Since dislocations are surrounded by both, a compressive and a tensile stress field, a misfitting precipitate will always benefit from nucleation on a dislocation, irrespective of whether the misfit is positive or negative.

Still, there is an important difference to the homogeneous nucleation case, which must be considered. In homogeneous coherent nucleation, the entire volumetric misfit stress is operative and should be used in the calculation. At dislocations, the compressive or tensile strain field compensates some part of the misfit and a **reduced misfit value** should be used in the simulation.

In a study of AlN precipitation in unalloyed steel[2)](#fn__2), a volumetric misfit of 75% has been used for homogeneous nucleation. This value effectively suppresses *homogeneous* nucleation due to the high volumetric misfit stress energy. For nucleation on dislocations, an *effective* misfit strain of 27%[3)](#fn__3) is capable of reproducing a large variety of experimental data correctly. For nucleation at grain boundaries, typically, the volumetric misfit is set to zero, since condensation and evaporation of vacancies is assumed to rapidly relax the entire misfit strain.

### Removal of a dislocation line segment

Nuclei appearing on dislocations are assumed to replace the segment of the dislocation line corresponding to the nucleus size. In consequence, the system energy decreases by the amount of replaced dislocation line energy. This effect is taken into account by the reduction of nucleation energy barrier $\Delta G\_{nucl}$ by a heterogenous nucleation site energy term of

\[\Delta G\_{het,disl}=\eta rGb^2\]

where $r$ is the nucleus radius, $G$ is the shear modulus, $b$ is the Burgers vector and $\eta$ is a scaling factor (with values expected in range 0-1)[4)](#fn__4).

Grain boundaries, edges and corners
-----------------------------------

In *MatCalc*, the polycrystalline grain microstructure is modelled as an ensemble of space-filling *tetrakaidecahedra*, objects which have been introduced by Lord Kelvin (Sir William Tompson) in 1887[5)](#fn__5). The tetrakaidecahedron is

1. space filling
2. has minimum separating area
3. has 120° angles between the faces

The tetrakaidecahedron is a body with eight hexagons and six quadrilaterals.

### Potential nucleation sites

In *MatCalc*, a slightly simplified version of tetrakaidecahedron is used, with a geometrical form sketched in the following diagram. The simplified version slightly deviates from the three properties above, however, it has planar faces, which makes it easier to evaluate its geometrical features.

[![ Tetrakaidecahedron used in //MatCalc// to represent polycrystalline microstructure](/matcalc_docu/techpapers/nucleation/img/fig_nucleation_tetrakaidecahedron_1.png " Tetrakaidecahedron used in //MatCalc// to represent polycrystalline microstructure")](/matcalc_docu/techpapers/nucleation/img/fig_nucleation_tetrakaidecahedron_1.png "techpapers:nucleation:img:fig_nucleation_tetrakaidecahedron_1.png")
[![ Tetrakaidecahedron used in //MatCalc// to represent polycrystalline microstructure](/matcalc_docu/techpapers/nucleation/img/fig_nucleation_tetrakaidecahedron_2.png " Tetrakaidecahedron used in //MatCalc// to represent polycrystalline microstructure")](/matcalc_docu/techpapers/nucleation/img/fig_nucleation_tetrakaidecahedron_2.png "techpapers:nucleation:img:fig_nucleation_tetrakaidecahedron_2.png")

From these objects, the total area, line length and number density of 2-grain, 3-grain and 4-grain junctions (grain boundaries, grain boundary edges and grain corners) can be evaluated straightforwardly. From these quantities, finally, the density of potential nucleation sites is calculated by evaluating the number of atoms located on the junctions. For a detailed description of the mathematical expression see, for instance, the PhD thesis by J. Rajek[6)](#fn__6). For selection of either of these potential nucleation sites, the corresponding choice in the 'nucleation' tab of the 'phase status' dialog must be made.

***Important note…***

If only 'grain boundary' is chosen as potential nucleation site, *MatCalc* evaluates nucleation and growth in a special treatment of precipitation in *grain boundary diffusion geometry*. Any other choice of nucleation site, as well as any combination of nucleation sites, will utilize the 'random nucleation' approach, where all precipitates are assumed to be randomly distributed in the bulk volume. See the section 'Multiple selection of nucleation sites' below.

### Misfit strain effect

When a precipitate nucleates on a grain boundary site, it is assumed that the elastic misfit stress field of the precipitate is instantaneously relaxed by condensation or annihilation of structural vacancies. A corresponding theoretical model has been developed by F.D. Fischer et al.[7)](#fn__7) and has been implemented in an older version of Matcalc[8)](#fn__8). A simulation study performed with this model has confirmed this assumption.

In practical simulation, the volumetric misfit value for grain boundary precipitates is commonly set to a value of zero. This setting reflects the fast strain relaxation potential of these heterogeneous nucleation sites.

### Removal of grain boundary area

When a precipitate nucleates, a certain amount of new interfacial area between the nucleus and the matrix must be created. On one hand, this process is energy-expensive up to the critical size of the nucleus, thus rendering this energy contribution an important ingredient of Classical Nucleation Theory. On the other hand, when a precipitate nucleates on a grain boundary site, part of the grain boundary is removed by the new precipitate, which adds an energy-supporting contribution to the energy balance.

*Starting with MatCalc version 6.04.1000*, the amounts of grain boundary energy consumed by the emerging nucleus (equal to heterogeneous nucleation site energy) are given as:

* for the grain boundariy surface (nucleation sites set to “grain boundaries”) \[\Delta G\_{het,gb}=\pi r^2\gamma\_{gb}\]
* for the grain boundary edges \[\Delta G\_{het,gbe}=\frac{3}{2} \pi r^2\gamma\_{gb}\]
* for the grain boundary corners \[\Delta G\_{het,gbc}=6arctan(\sqrt{2})r^2\gamma\_{gb}\]

where $r$ is the nucleus radius, and $\gamma\_{gb}$ is the grain boundary energy[9)](#fn__9).

*In the MatCalc version 6.03.1000 and older*, the balance between expensive and supporting contributions to the nucleation process has been treated quantitatively by Clemm and Fisher[10)](#fn__10). These authors evaluate geometrically the ratio between newly formed grain junctions to removed grain boundary area and express the results in terms of a modified nucleation barrier $G^\*$. Basically, they express this quantity in terms of three geometrical parameters *a*, *b*, *c*, the interfacial energy $\gamma\_{\alpha \beta}$ and the grain boundary energy $\gamma\_{\alpha \alpha}$

\[G^\* = \frac{4}{27} \frac{{ \left ( b \gamma\_{\alpha \beta} - a \gamma\_{\alpha \alpha} \right )}^3}{{\left ( c \Delta G\_\text{vol} \right )}^2}\]

Clemm and Fisher then evaluate *a*, *b* and *c* for the 2-grain, 3-grain and 4-grain junctions. In *MatCalc*, this treatment was slightly extended by summing up the change in the nucleation barrier into an effective interfacial energy $\gamma'$ with

\[\gamma ' = \left(\frac{1}{36 \pi}\right)^{\frac{1}{3}} \left( \frac {b \gamma\_{\alpha\beta} - a \gamma\_{\alpha\alpha}}{c^{\frac{2}{3}}} \right)\]

This quantity was accessible via the *MatCalc* variable **EIE$phase\_Pnn** for the *effective interfacial energy*, which was determined as the calculated interfacial energy of the planar sharp interface minus the contribution from removal of grain boundary area.

**Note:** For a proper evaluation of the effective interfacial energies, the correct settings for the grain boundary energy must be made in the 'special' tab of the 'precipitation domain' dialog. Typical values for this quantity are around 0.3 J/m2.

In both treatments, the employed values of precipitate interface energy and grain boundary energy can sometimes result in the absence of nucleation energy barrier. The evolution of the precipitate is then given only by its growth rate. A typical example for such behavior is the nucleation of bcc ferrite from fcc austenite in ultra-low carbon unalloyed steel, where the ferrite grains (precipitates) nucleate instantaneously after crossing the phase boundary. This effect is described, for instance, by Kozeschnik and Gamsjäger[11)](#fn__11).

### Chemical driving force for grain boundary nucleation

If precipitates nucleate and grow on grain boundaries, the so-called 'collector plate' mechanism is assumed to be operative for the diffusive transport of atoms to the precipitate. In this approach, commonly, an infinitely fast diffusion inside the grain boundary is assumed, and slow transport in the bulk volume. In *MatCalc*, diffusion during grain boundary nucleation is treated according to the settings made for 'diffusion in grain boundary' in the 'special' tab of the 'precipitation domain' dialog. Typical values for these quantities are summarizes in the article  [Diffusion in heterogenous precipitation](/matcalc_docu/techpapers/precipitation/diffusion "techpapers:precipitation:diffusion").

**Note:** In the nucleation stage, the effective region supporting solute atoms for nucleation is assumed to be 1 nm wide, that is, 0.5 nm to each of the two sides of the grain boundary. This assumption is essentially reproducing the observation that nucleation in grain boundaries will be extremely fast due to the fast diffusion kinetics along the grain boundary. However, once the solute atoms available in this restricted region have formed the first nuclei, any additional solute atom arriving at the grain boundary later will diffuse towards existing precipitates and attach there rather than nucleating additional particles. This assumption is the reason that you will observe decreasing and, finally, zero nucleation rate for grain boundary precipitates even if the driving force inside the grain would still support nucleation.

Subgrain boundaries, edges and corners
--------------------------------------

In *MatCalc*, subgrain boundaries (SGB) represent special objects, which are different from grain boundaries in a few aspects. SGB are

* low-angle boundaries inside the high-angle grain structure
* faster diffusion paths than within the bulk volume, but still significantly slower than high-angle grain boundaries

SGBs have been introduced into *MatCalc* originally to mimic the martensitic substructure of materials. This is sketched in the figure below showing a prior austenite grain with a few martensite laths.

[![ Subgrains representing the martensitic microstructure of materials](/matcalc_docu/techpapers/nucleation/img/fig_nucleation_tetrakaidecahedron_mart.png " Subgrains representing the martensitic microstructure of materials")](/matcalc_docu/techpapers/nucleation/img/fig_nucleation_tetrakaidecahedron_mart.png "techpapers:nucleation:img:fig_nucleation_tetrakaidecahedron_mart.png")

### Potential nucleation sites

For SGB nucleation, each atom located on the SGB is assumed to be a potential nucleation site. Just like for grain boundaries, the number of potential sites is evaluated from the geometrical properties of the (elongated) tetrakaidecahedron as described in J. Rajeks thesis.[12)](#fn__12)

For the choice of subgrain boundary edges and corners, each atom located at these sites is considered to be a potential nucleation site. Evaluation of $N\_0$ is performed in analogy to grain boundaries.

### Misfit strain effect

At subgrain boundaries, the misfit stress is assumed to be compensated easily by structural rearrangement of dislocations and generation or annihilation of excess vacancies. These processes can rapidly relax the volumetric misfit stress of the coherent precipitate.

In practical simulation, it is recommended that the volumetric misfit value for subgrain boundary precipitates is set to a value of zero, therefore.

### Removal of subgrain boundary area

The nucleation of precipitates at subgrain boundaries resembles very much the situation at grain boundaries. For this reason, the model described above for nucleation at 2-grain junctions has also been adopted for nucleation at 2-subgrain junctions. Instead of the grain boundary energy, the value for the subgrain boundary energy is utilized in the evaluation.

For details, see treatment above for 2-grain junctions.

**Note:** For a proper evaluation of the effective interfacial energies, the correct settings for the subgrain boundary energy must be made in the 'special' tab of the 'precipitation domain' dialog. Typical values for this quantity are around 0.1-0.2 J/m2. In any case, the choice of value should be less than in the grain boundary case.

Other precipitates
------------------

In *MatCalc*, three different models are presently implemented that take into account the possibility that existing precipitates can act as heterogeneous nucleation sites for other precipitates. These models can be used for two different cases where either

* One precipitate type acts as a *catalyst* for the nucleation of another precipitate type. Nucleation occurs on the phase boundary between the parent precipitate and the matrix by random compositional fluctuations within the matrix. This type of transformation is denoted as **on-particle nucleation**.
* The parent precipitate *directly transforms* into the new precipitate type by structural and/or compositional transformation. For this type of transformation, two models are implemented, with different physical foundation and transformation mechanism. This type of transformation is denoted as **inner-particle nucleation**.

The selection of **'other precipitates'** cannot be combined with other nucleation sites, such as dislocations or grain boundaries.

The models available in *MatCalc* for on-particle and inner-particle nucleation are described below.

### Nucleate at precipitate surface

In choosing the **on-particle nucleation** model, *MatCalc* assumes that the surface of the parent precipitates acts as a catalytic region where nucleation of the product phase is facilitated. Each atom located on the parent precipitate surface is assumed to represent a potential nucleation site.

In evaluation of the total number of potential nucleation sites $N\_0$ for *on-particle* nucleation, MatCalc evaluates the total interfacial area spanned by the parent precipitates. This value is divided by the mean area that one single atom needs in a mono-atomic layer. The latter quantity is evaluated on basis of the precipitate molar volume to the power of 2/3. If more than one parent precipitate phase is selected, the total surface area of all selected precipitates is considered in the evaluation of $N\_0$.

The *nucleation rate* $J$ for on-particle nucleation is otherwise evaluated identical to the treatment for homogeneous nucleation. During nucleation of the new phase, the parent precipitate population remains entirely unaffected.

**Note:** This type of nucleation must be combined with a selection of 'nucleation model' of **'Becker-Döring time-dependent'**, since nucleation is governed by the diffusional transport of atoms in the parent matrix and the corresponding compositional and structural fluctuations. Application of the standard Classical Nucleation Theory implementation of *MatCalc* seems thus sufficiently justified.

### Nucleate with equivalent interfacial energy

This first variant of **inner-particle nucleation** model has been developed and implemented[13)](#fn__13) to allow for the simulation of nucleation in cases, where the nucleation process of the new phase occurs **within** the volume of the parent precipitate and the probability of transformation does not scale with the total volume of the precipitate or the precipitate radius.

A typical example for this (very rare) type of transformation is found in the ferritic-martensitic 9%-Cr steel group, where Z-phase precipitates nucleate within VN precipitates, and consume the entire VN population after long time exposure at temperatures around 600°C. From a practical viewpoint, this transformation has considerable impact, since these steels then lose their precipitation strengthening potential because a single Z-phase particle can dissolve a large number of smaller and densely distributed VN precipitates.

The transformation itself is only possible if the product phase is thermodynamically more stable than the parent phase. This condition is implemented in *MatCalc* in the form that the stability of parent and product phases is continuously compared based on their thermodynamic driving force. Transformation occurs only if the driving force for precipitation of the product phase is larger than the driving force evaluated for the parent phase. The difference between the two driving force values is considered to be the *effective driving force for nucleation* of the product phase.

In evaluation of the nucleation rate $J$, this *effective driving force* is used together with the ***equivalent interfacial energy*** value entered for this transformation type in the conventional nucleation rate expression. The total number of potential nucleation sites, $N\_0$, is evaluated as the number of atoms on the surface area of the parent precipitates, the Zeldovich factor *Z* is calculated identical to the homogeneous nucleation case and the atomic attachment rate $\beta^\*$ is set to unity.

After nucleation of $J.dt$ precipitates of the product phase, the equivalent number of precipitates of the parent phase is removed. The critical nucleation radius of the new precipitates is assumed to be given by the mean radius of the parent precipitates.

This choice of inner-particle nucleation model must be combined with the **'direct particle transformation'** option for the 'nucleation model'.

***Important note…***

The model used for nucleation within a parent precipitate using the *equivalent interfacial energy* must be considered as a ***semi-phenomenological approach***. It is *not* rigorously derived and represents only a work-around for the lack of a fundamental physical model of inner-particle nucleation.

**Note:** In this nucleation model, it is not possible to select more than one parent phase for this type of transformation, otherwise the transformation would not be unambiguous.

***Important note…***

In this type of approach, the nucleation rate evaluated on basis of the effective driving force and the equivalent interfacial energy is very sensitive to numerical oscillations during integration of the evolution equations. Particular care must be taken in the simulations to avoid numerical oscillations with strict settings of the numerical parameters controlling the integration process. Oscillations in the effective driving force can lead to **unrealistic nucleation bursts** that might impair the significance of the simulation results.

### Nucleate within range of transformation radius

The second variant of **inner-particle nucleation** model has been developed for cases, where the nucleation process of the new phase occurs **within** the volume of the parent precipitate ***and*** the probability of transformation scales with the precipitate radius.

Situations of this kind occur typically in precipitation of particles that show a transition from fully coherent to semi-coherent or incoherent interfacial structure. In the very early stages of precipitation, precipitates with volumetric misfit to the matrix are often constrained and forced into metastable crystal structures due to the coherency stress exerted by the matrix structure. While growing, the misfit stress becomes so large that the interfacial structure becomes incoherent, with the effect that the elastic misfit stress is substantially reduced. The coherency stress from the matrix is reduced and the precipitate can adopt crystal structures and/or chemical compositions with higher thermodynamic stability.

An example of this type of transformation is found, for instance, in the transition of beta” to beta' precipitates in the Al-Mg-Si system. The coherent beta“ precipitates start losing coherency after reaching a certain critical size, which is denoted as the **'transformation radius'** in the 'nucleation' tab of the 'phase status' dialog. In the actual nucleation procedure, two values for the transformation radius must be defined, spanning a range within which the transformation from parent to product phase occurs. The two values, minimum and maximum transformation radius, $r\_{t,min}$ and $r\_{t,max}$, reflect the observation that the transformation process will not instantaneously start at the minimum critical value, but proceed smoothly over a certain range.

When a precipitate size class of the parent phase reaches the minimum critical size $r\_{t,min}$, in each time integration step, a certain number of precipitates of this size class transforms into the product phase given by the actual location of the radius within the transformation interval. Close to the minimum size, the transformation probability is rather low, such that only a small number of the precipitates in the size class transform. In contrast, the probability is very high close to the maximum transformation radius and a large number of precipitates will transform in each step. Above the maximum, the transformation probability becomes unity and all particles exceeding this size are transformed immediately. This situation is schematically shown in the following graph.

[![ Transformation probability for inner-particle nucleation with transformation radius](/matcalc_docu/techpapers/nucleation/img/fig_nucleation_direct_particle_radius.png " Transformation probability for inner-particle nucleation with transformation radius")](/matcalc_docu/techpapers/nucleation/img/fig_nucleation_direct_particle_radius.png "techpapers:nucleation:img:fig_nucleation_direct_particle_radius.png")

After a certain number of new precipitates have nucleated, the same number of precipitates of the parent phase are removed from the system. The critical radius of the new precipitates is taken as the value of the parent precipitates.

**Note:** Similar to the nucleation model based on the equivalent interfacial energy, this type of inner-particle transformation only occurs, if the relative thermodynamic stability of the product phase is above the stability of the parent phase. This condition is always evaluated before any kind of inner-particle transformation is performed by *MatCalc*.

**Practical note:** If you define this type of nucleation model in your simulations, and you do not observe any transformation although the parent phase precipitates have already exceeded the maximum transformation radius, check the chemical driving force of the two phases.

Multiple selection of heterogeneous nucleation sites
----------------------------------------------------

The selection of only a single nucleation site for the new phase has been outlined in some detail above. Combination of multiple nucleation sites for one precipitates has different effects, depending on the choices.

If either

* homogeneous (bulk)
* dislocations
* grain boundary edge
* grain boundary corner
* subgrain boundary
* subgrain boundary edge
* subgrain boundary corner

is selected as nucleation site, the **random distribution** diffusion geometry is used in evaluation of the growth conditions for the precipitate, and the potential number of nucleation sites $N\_0$ is evaluated as the number of atoms located at the homogeneous or heterogeneous nucleation sites. It is possible to combine selections, with the effect that the number of potential nucleation sites are then evaluated as the superposition of all selected options.

If only

* grain boundary

is selected, nucleation is evaluated as described above in the section on grain boundary nucleation. Growth is evaluated according to the model for **grain boundary** diffusion geometry. Combination of grain boundary nucleation with any of the above choices will tell *MatCalc* to use the **random distribution** model in combination with a superposition of values for $N\_0$.

**Important Note:** *MatCalc* will utilize the 'grain boundary' diffusion model for growth **only** for the single choice of nucleation site as 'grain boundary'. Any combination of nucleation sites, will utilize the 'random distribution' approach, where all precipitates are assumed to be randomly distributed in the bulk volume.

The choice of

* other precipitates

cannot be combined with the above options and must be used separately.

With the selection of

* nucleate at precipitate surface

you can use multiple phases as parent precipitates. The number of potential nucleation sites is evaluated from the total surface area of all precipitate types.

Selections of

* equivalent interfacial energy
* transformation radius

allows for selection of only one parent precipitate. These two options must be combined with the 'direct particle transformation' option for the 'nucleation model'.

[1)](#fnt__1)

See references below

[2)](#fnt__2)

R. Radis and E. Kozeschnik, “Kinetics of AlN precipitation in microalloyed steel”, Model. Simul. Mater. Sci. Eng. 18 (2010) 055003 (16pp)

[3)](#fnt__3)

Erroneously, a value of 19% has been reported in the publication

[4)](#fnt__4)

B. Miesenberger et al., “Computational analysis of heterogeneous nucleation and precipitation in
AA6005 Al-alloy during continuous cooling DSC experiments”, Materialia 25 (2022) 101538

[5)](#fnt__5)

Sir W. Thomson, „On the division of space with minimum partitional area“ Philos. Mag. 24 (1887) 503-514

[6)](#fnt__6)

[list of MatCalc-relevant publications](https://www.matcalc.at/index.php/about/publications "https://www.matcalc.at/index.php/about/publications")

[7)](#fnt__7)

F.D. Fischer, J. Svoboda, E. Gamsjäger, E. Kozeschnik and B. Sonderegger, “Modelling of Precipitation Kinetics with Simultanous Stress Relaxation”, Mater. Res. Soc. Symp. Proc., 979, 2007, pp. 0979-HH11-04.

[8)](#fnt__8)

In the present versions of *MatCalc*, this model is no longer available due to numerical shortcomings and very low computation efficiency of this approach

[9)](#fnt__9)

B. Miesenberger et al., “Computational analysis of heterogeneous nucleation and precipitation in AA6005 Al-alloy during continuous cooling DSC experiments”, Materialia 25 (2022) 101538

[10)](#fnt__10)

P.J. Clemm and J.C. Fisher, “The influence of grain boundaries on the nucleation of secondary phases, Acta Metall. 3 (1955) 70-73

[11)](#fnt__11)

E. Kozeschnik and E. Gamsjäger, „High-Speed Quenching Dilatometer Investigation of the Austenite to Ferrite Transformation in Fe-C”, Met. Mater. Trans. 37A, 2006, 1791-1797.

[12)](#fnt__12)

[list of MatCalc-relevant publications](https://www.matcalc.at/index.php/about/publications "https://www.matcalc.at/index.php/about/publications")

[13)](#fnt__13)

E. Kozeschnik, B. Sonderegger and H. Danielsen, unpublished research (2005).

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Anucleation%3Ahet_nucl_sites&1788352981)