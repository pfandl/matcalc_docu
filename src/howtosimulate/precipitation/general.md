General considerations [MatCalc Documentation]



### Table of Contents

* [General considerations](#general_considerations)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Before you start ...](#before_you_start)
* [The representative volume element (RVE)](#the_representative_volume_element_rve)
* [Setting up a precipitation simulation](#setting_up_a_precipitation_simulation)

  + [Setup the thermodynamic system](#setup_the_thermodynamic_system)
  + [Create precipitation domain(s)](#create_precipitation_domain_s)
  + [Create precipitates](#create_precipitates)

General considerations
======================

Compatibility
-------------

MatCalc version: 5.0 - …   
Author: E. Kozeschnik   
Created: 2011-07-05   
Revisions:

Objectives
----------

In this document, general considerations for *precipitation kinetics simulations …* are discussed.

Related documents
-----------------

none

Main document
=============

Before you start ...
--------------------

Before actually going into the software to perform the simulation, do **make sure you clearly know, which problem you want to solve, and how you want to realize your task**. For precipitation simulations, this statement is of highest importance, because experience shows that (particularly unexperienced) users have sometimes tremendous problems to appropriately formulate their simulation task.

Setup your precipitation simulation as simple as possible in order to avoid unnecessary computational effort. This *is* an issue in kinetic simulations. Once you have successfully completed simulations in a simplified system, gradually increase the complexity until you arrive at the answer to the problem you are seeking. If you are new to MatCalc precipitation simulations, it is not advisableto start your simulations in all complexity. You will almost certainly be unable to find the correct interpretation of your results if you pack too many details into the simulations.**Use the scripting functionality!**. With this technique, it is easy and straightforward to gradually develop your simulations stepwise. And it makes it easy when you need to contact help desk with some unresolvable problem.

***And most important …***

*MatCalc* is a simulation tool that follows a *physically-based* concept. *MatCalc* builds upon models that rely on well-known input parameters and the simulations can, and should!, be carried out in a parameter-free manner.

***DO NOT use MatCalc as a fitting tool where you adjust the interfacial energy until the calculation fits your experiment!!!***

The vision of *MatCalc* is to provide a *predictive* framework for precipitation kinetics simulations. In your simulations, identify the relevant physical mechanisms that are responsible for the behavior of the system. Use *MatCalc* as the tool by which you can test your ideas and conceptions.

In the 'How to' manual section on alloy specific issues, you can find tips and tricks that are relevant for the particular system. This will certainly assist you in identifying the important processes that you have to account for. If you still have trouble, see whether you can find an appropriate [example](/examples/index "examples/index"), consult the  [MatCalc forum](http///matcalc.at/CustomerPortal "http///matcalc.at/CustomerPortal"), or contact  [help desk](http///matcalc.at/CustomerPortal "http///matcalc.at/CustomerPortal").

The representative volume element (RVE)
=======================================

When designing and performing precipitation kinetics simulations, it is important to understand the conceptual framework of the precipitation kinetics module.

*MatCalc* **precipitation kinetics simulations** are carried out within a ***representative volume element***, which means that one single simulation refers to

* a single, homogeneous matrix (precipitation domain) containing all existing precipitates. This is a consequence of the *mean-field approach* taken in the SFFK model[1)](#fn__1).
* all precipitates are assigned to one single precipitation domain only at one time. It is possible to swap precipitates from one precipitation domain into another, though, to mimic phase transformations of the matrix phase.
* temperature, pressure and overall chemical composition are homogeneous inside the entire precipitation domain. There exist no gradients in these quantities inside the RVE.

The following graphics shows a sketch of the RVE for precipitation kinetics simulations.

[![ //MatCalc// representative RVE](/howtosimulate/precipitation/img/matcalc_rve.png " //MatCalc// representative RVE")](/howtosimulate/precipitation/img/matcalc_rve.png "howtosimulate/precipitation/img/matcalc_rve.png")

The RVE in *MatCalc* contains unit volume of matter, with an arbitrary number of different atomic species. The atoms can form precipitates of different type and different chemical composition. The precipitates are considered to be spherical objects,[2)](#fn__2) with a homogenous chemical composition, just like the matrix.

Setting up a precipitation simulation
=====================================

When setting up a precipitation kinetics simulation, you commonly proceed with the following steps:

Setup the thermodynamic system
------------------------------

Create a new workspace. Then

* Open the desired database and *select elements and phases* that you want to work with. Read thermodynamic and mobility databases.
* Define nominal chemical composition.

Create precipitation domain(s)
------------------------------

If you want to simulation precipitation, you must provide at least one *container* for the precipitates, where they are allowed to nucleate and grow. This container is denoted as the *precipitation domain*.

* **Create precipitation domain**. Use 'Create' in the 'Precipitation domains…' dialog.
* Select the **thermodynamic matrix phase**. This is the phase, which defines the thermodynamic properties of the precipitation domain.
* Enter the microstructure information in the 'structure' tab of the precipitation domain dialog:

  + **Grain size** (important for grain boundary precipitates)
  + **Dislocation density** (important for dislocation precipitates as well as pipe diffusion)
  + **Subgrain size** (important for subgrain boundary precipitates, e.g., in martensitic microstructure)
* For dislocation density above the equilibrium values ($10^{11}-10^{12}$), enter the **dislocation diffusivity ratio** in the special tab. See article  [Diffusion in heterogenous precipitation](/techpapers/precipitation/diffusion "techpapers/precipitation/diffusion") for details.
* For grain boundary precipitates, enter the **grain boundary diffusivity ratio** in the special tab. See article  [Diffusion in heterogenous precipitation](/techpapers/precipitation/diffusion "techpapers/precipitation/diffusion") for details.

Create precipitates
-------------------

For each desired precipitate, select the **precipitate parent phase** and create a new precipitate with the 'Create' button. Select 'precipitate' as phase type.

* Define the desired **number of size classes** to use in the simulations. This quantity determines, which maximum number of size classes *MatCalc* will maintain during the simulations. Practically, values between 15 and 25 have proven to be reasonable values, if you are interested in the evolution of mean quantities, such as number density or mean radius. A value of 20 delivers a good compromise for calculation speed an accuracy.
* Attach the precipitate to a **precipitation domain**.
* Do *not* change the automatic setting for the interfacial energy. The estimates delivered by *MatCalc* have shown to be quite reasonable in the majority of cases, and no significant changes are usually necessary at this stage.
* On the 'nucleation' tab, select the desired homogeneous of heterogeneous **nucleation site**. See the article on  [Heterogeneous nucleation](/techpapers/nucleation/het_nucl_sites "techpapers/nucleation/het_nucl_sites") for additional information.

[1)](#fnt__1)

J. **S**voboda, F. D. **F**ischer, P. **F**ratzl and E. **K**ozeschnik, „Modelling of kinetics in multi-component multi-phase systems with spherical precipitates I. – Theory“, Mater. Sci. Eng. A, 2004, 385 (1-2) 166-174.

[2)](#fnt__2)

In reality, the precipitates in *MatCalc* can have non-spherical shapes also. This is described in the article about  [The precipitate shape](/techpapers/precipitation/prec_shape "techpapers/precipitation/prec_shape")

![](/wiki/lib/exe/taskrunner.php?id=howtosimulate%3Aprecipitation%3Ageneral&1788352862)