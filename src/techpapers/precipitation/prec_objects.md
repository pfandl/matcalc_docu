TechPaper #2011001: Object hierarchy and interconnectivity in precipitation kinetics simulations [MatCalc Documentation]



### Table of Contents

* [TechPaper #2011001: Object hierarchy and interconnectivity in precipitation kinetics simulations](#techpaper_2011001object_hierarchy_and_interconnectivity_in_precipitation_kinetics_simulations)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Object hierarchy](#object_hierarchy)
  + [Equilibrium phases](#equilibrium_phases)
  + [Precipitation domains](#precipitation_domains)
  + [Precipitate phases](#precipitate_phases)

TechPaper #2011001: Object hierarchy and interconnectivity in precipitation kinetics simulations
================================================================================================

Compatibility
-------------

MatCalc version: 4.0 - …   
Author: E. Kozeschnik   
Created: 2011-06-23   
Revisions:

Objectives
----------

This paper describes the object hierarchy implemented in MatCalc for precipitation kinetics simulations. It sketches the interconnections between the simulation control module, the equilibrium phases with precipitation domains and precipitate parent phases, as well as the precipitate phase objects.

Related documents
-----------------

None

Main document
=============

The precipitation simulations in MatCalc are controlled by the kinetic calculation algorithms of the mc\_core module. The foundation of the object structure is given by the setup of the thermodynamic equilibrium system, which defines the possible thermodynamic matrix phase(s) as well as the parent phases for the precipitate(s).

Object hierarchy
----------------

Based on the selection of equilibrium phases, the user defines precipitation domains, which are the containers for the precipitates, as well as the precipitate phase objects. Each precipitate must be created manually by the user, based on a particular precipitate parent phase, to which the precipitate remains connected to. The following figure illustrates these interconnections.

[![ Object hierarchy for precipitation kinetics simulations](/matcalc_docu/techpapers/precipitation/img/precipitation_object_hierarchy.png " Object hierarchy for precipitation kinetics simulations")](/matcalc_docu/techpapers/precipitation/img/precipitation_object_hierarchy.png "techpapers:precipitation:img:precipitation_object_hierarchy.png")
Figure 1: Object hierarchy for precipitation kinetics simulations in *MatCalc*

The figure shows the two major controlling objects for calculations in the top row, connected with a line to indicate the direct link between the two. The first object is the 'Gibbs' class from within the 'mc\_core' module, which is the class that handles thermodynamic calculations, evaluation of chemical potentials and driving forces, etc., and manages the phase objects. The second class is the 'kinetic control' class, also in the 'mc\_core' module of MatCalc. This class is responsible for all kinetic simulations related to the precipitation kinetics functionality. It manages the precipitation domain functions and the link between the parent phase and precipitate phase objects.

Below the 'Gibbs' class, directly linked to this object, are the equilibrium phases. This is the list of phases just as they are created when the user reads the thermodynamic database. In the precipitation kinetics simulations, these phases act as parent objects to the precipitate phases. This link is indicated by the lines between the equilibrium phases and the precipitates.

The last group of objects relates to the precipitation domains. These are linked to the 'kinetic control' class, which handles all kinetic calculations and finally links the precipitates to the corresponding precipitation domains.

Equilibrium phases
------------------

The equilibrium phases in precipitation kinetics simulations play the important role of handling the *nucleation* properties of the precipitate. Depending on the choice of nucleation model, these phases always contain the selected (or calculated) chemical composition of the precipitate nucleus.

These phases are denoted as *precipitate parent phases* and they are initialized with a 'fixed' phase flag [1)](#fn__1) and a phase amount set to zero. This phase flag setting allows for the calculation of the appropriate chemical composition for the ortho- or para-equilibrium nucleus. These settings also ensure that the precipitate parent phases do not participate in any kind of equilibrium calculation or evaluation of mass balances, since they have zero phase fraction and, thus, contain no actual mass. Still, they are very closely linked to the precipitates and must not be suspended, made dormant or changed in any other way.

**Important note:** The precipitate parent phases contain all information that are needed to evaluate the nucleation rate for the precipitate. This includes the nucleus composition, but also the chemical driving force, chemical potentials or sublattice site fractions. The properties of the precipitate parent phase can be evaluated in addition to the corresponding variables for nucleation provided for the precipitate phase.

In the equilibrium phases group of Figure 1, the phases named A and B are phases that are attached to the two precipitation domains. The phases named a, b and c are precipitate parent phases. Phase c#01 is a *composition set*, which is a phase with the identical phase description and identical thermodynamic parameters as phase c, however, it usually has different major constituents defined. Since this phase is the *first* composition set of phase c, it has the index 1 given after a hash '#' sign to indicate composition sets. In all other aspects, this phase behaves like any other equilibrium phase.

Precipitation domains
---------------------

A precipitation domain represents a *container*, in which precipitates can nucleate and grow. The most important property of a precipitation domain is the attached *thermodynamic matrix phase*. The type of equilibrium phase uniquely *determines the thermodynamic properties of the precipitation domain*. For instance, in steel, the 'ferrite' precipitation domain is usually linked to the BCC\_A2 phase. In Al or Ni alloys, the precipitation domain commonly links to the FCC\_A1 phase.

In figure 1, each of the two precipitation domains I and II are linked to one single equilibrium phase A or B. This is indicated by thin solid lines connecting the precipitation domains with the matrix phases. Note that it is not possible that two precipitation domains share the same matrix phase, since the equilibrium phase object holds many of the properties of the precipitation domain.

In the precipitation kinetics simulation, one of the existing precipitation domains is made active. The existing precipitates are automatically assigned to this domain. In practice, this is a representation of the situation that the precipitation domain acts as a representative volume element. The available precipitates can, thus, only be within this RVE, or not exist at all [2)](#fn__2).

It is not possible that one precipitate shares multiple precipitation domains. It is, however, possible that a precipitate nucleates in one precipitation domain and continues to grow in another one after the active domain has been switched from one to the other precipitation domain. This situation corresponds, for instance, to cases, where the matrix phase of the RVE changes due to a matrix phase transformation in the course of a complex heat treatment.

**Important note:** The precipitation domain contains all information about the microstructure of your precipitation system, including dislocation density and grain size (determining the number of potential nucleation sites for heterogeneous nucleation), grain boundary energies, settings for the treatment of excess vacancies, and many more. The properties of the precipitation domain thus strongly affect the precipitation process.

Precipitate phases
------------------

In the bottom right group box of figure 1, an ensemble of precipitate phases is displayed. Each precipitate phase object must be created manually by the user and linked to a precipitate parent phase. The precipitate phases generally carry the suffix '\_Pn', where *n* stands for a number >= 0. The letter 'P' indicates that this phase is a precipitate. The index n refers to the index of the precipitate population, which is assigned to the precipitate parent phase.

The precipitate phase contains all information of the precipitate, including the distribution of size classes and each corresponding chemical composition, the mean driving force for precipitation, the number density, etc., etc. The precipitate phase object also *contains all settings that control the nucleation and growth* characteristics of the precipitate.

**Note:** Each precipitate is linked to one single precipitate parent phase. The precipitate phase contains all information on the constitution of the precipitate, the parent phase all properties related to nucleation.

Figure 1 shows this requirement clearly on a few examples. The precipitates a and b
are linked to one parent phase each and the phase names are a\_p0 and b\_p0. Phase c has three precipitate populations defined and linked to one single parent phase. This is possible (and reasonable), if all three precipitate populations rely on the same model for the nucleus composition. In this case, the composition of the nucleus, and, thus, all nucleation properties, are identical for all three populations and one can rely on only one parent phase. The three precipitate populations are named c\_p0, c\_p1 and c\_p2.

Multiple precipitate populations are useful if you analyze, for instance, simultaneous nucleation of precipitates on either dislocations and grain boundaries. In this case, the nucleation model is the same, and the same parent phase can be used.

Another example, where selection of only one parent phase is incorrect, is the analysis of simultaneous precipitation of para-equilibrium and ortho-equilibrium precipitates. In this case, each of the two precipitates has different settings for the nucleus composition and ,thus, two separate composition sets of the same thermodynamic phase are required for a correct simulations. This situation applies, for instance, to the last two precipitates in figure 1. These are attached to the composition set phase c#01 with the names c#01\_p0 and c#01\_p1. The precipitates based on the two different parent phases can have different settings for the nucleus composition, without causing a conflict in the simulation. The two precipitate populations of the c#01 phase, i.e. c#01\_p0 and c#01\_p1, could, for instance, represent precipitate populations nucleating with para-equilibrium composition on dislocations or grain boundaries. The three phases belonging to the c phase could represent precipitates with ortho-equilibrium nucleus composition nucleating in the bulk, on dislocations and on grain boundaries, respectively.

[1)](#fnt__1)

flags |= FLAG\_PHASEISFIXED

[2)](#fnt__2)

If you want to suppress a precipitate from being formed in your simulation, uncheck all possible nucleation sites. This is the safest way of ignoring a certain phase

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Aprecipitation%3Aprec_objects&1788353011)