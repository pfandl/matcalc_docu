General considerations [MatCalc Documentation]



### Table of Contents

* [General considerations](#general_considerations)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Before you start ...](#before_you_start)
* [Setting up a thermodynamic simulation](#setting_up_a_thermodynamic_simulation)

  + [Create a new workspace](#create_a_new_workspace)
  + [Define thermodynamic system](#define_thermodynamic_system)
  + [Enter chemical composition](#enter_chemical_composition)
  + [Set simulation start values](#set_simulation_start_values)
  + [Run your simulation](#run_your_simulation)
* [Further information](#further_information)

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

In this document, general considerations for *equilibrium and non-equilibrium thermodynamic simulations …* are discussed.

Related documents
-----------------

```
none
```

Main document
=============

Before you start ...
--------------------

Before actually going into the software to perform the simulation, do make sure you clearly know which problem you want to solve. Setup a thermodynamic simulation as simple as possible in order to avoid unnecessary computational effort and artifacts that might come from incomplete or missing thermodynamic data. But do not make the system too simple, otherwise you run into danger of missing the answers that you are seeking.

Setting up a thermodynamic simulation
=====================================

When setting up a thermodynamic simulation in *MatCalc*, you commonly proceed with the following steps:

Create a new workspace
----------------------

In the GUI version of *MatCalc*, all information about the thermodynamic system, all simulation results, and also the position and order of windows is stored in a ***MatCalc* workspace**. The file extension is **'\*.mcw'**. Alternatively, you can store your results in a **binary file**, which avoids all GUI relevant information and only stores the simulation setup and all results. The binary file extension is **'\*.mcb'**.

Define thermodynamic system
---------------------------

The definition of the thermodynamic system in *MatCalc* is a most relevant step in the simulation setup. This step defines the possible elements that take part in any kind of simulation, as well as the possible phases. Any element or phase that you miss to define in this step cannot be added or included later on without destroying all simulation results.

* *Open the thermodynamic database* that you want to work with.
* *Select elements*.

  + Consider in detail, which elements you want to include in your simulation. It is important that you do not miss the relevant element that is responsible for the effect that you want to investigate. It is also not advisable to simply select all elements that are available in the database. This increases your computational effort and it increases the possibility of unwanted artifacts or invalid calculation results. It might also impair the numerical convergence behavior.
  + Make sure that the relevant phases exist for all elements that you include in your calculation. It is not advisable to select, for instance, element A from the list, without also including the relevant phases, where this element can partition (go to) during the simulation. Selecting C as an element but ignoring the carbide phases will definitely deliver erroneous and unexpected results.
* *Select phases*.

  + Selecting the appropriate phases is of utmost importance for delivering useful results from a thermodynamic equilibrium simulation. Make sure that you include *all stable phases* that might possibly appear in your system within the given limits of temperature, pressure and chemical composition. In case of analyses of metastable phase formation, as usually the case in precipitation kinetics simulations, make sure that you also include all relevant *metastable phases*.
  + In the phase list, the order of phases is such that

    - only phases are listed, where all elements that are required to define at least one element on each sublattice, are shown.
    - the relevance of the individual phases is accounted for according to its setting in the corresponding column of the phases list box. The lower the relevance number, the more likely you do not have to account it in simulations with standard materials.
* *Read the database*.

Enter chemical composition
--------------------------

After definition of elements and phases of the database, the chemical composition of the thermodynamic system must be set. In the 'Nominal composition' dialog, the amount of elements can be entered in

* mole fraction (sum of all $X\_i$ is one)
* u-fraction (sum of all substitutional $X\_i$ is one)
* weight fraction (sum of all $w\_i$ is one)
* weight percent (sum of all $wp\_i$ is 100)

By default, one of the elements is set as the **reference element**. This definition is usually done in the database with the command REFERENCE\_ELEMENT.

Set simulation start values
---------------------------

The last step before actually performing the equilibrium simulation is to initialize the *MatCalc* variables and parameters with some reasonable starting values. This is done with the 'Set start values' command in the 'Calc' menu.

It is possible, to leave out this step, however, the simulation sometimes does not converge and will deliver undefined results.

You can use this command multiple times to improve the initial estimates.

The 'Set start values' command is used whenever the simulation state is undefined, such as, for instance, after reading the thermodynamic database. You can also use it in case you have trouble with convergence of equilibrium simulations. Several calls of this function (and eventually a change of temperature to higher values) can be beneficial for convergence.

Run your simulation
-------------------

Perform the equilibrium simulation with the 'Equilibrium …' command from the 'Calc' menu. Enter the desired temperature and pressure[1)](#fn__1) and start the simulation with the 'Go' button.

***Important …***

When the simulation is finished, *MatCalc* provides information on the simulation results in the output window. You **MUST** check the results for possible errors in the calculation before you continue. *MatCalc* will report with **`- OK -`** if the simulation was successful, report a **`* Warning *`**, if you should recheck the result, and report **`* ERROR *`**, if no solution was found.

If you do not check the status of your simulation results, you are running danger of using *undefined* results.

Further information
===================

[1)](#fnt__1)

In the present MatCalc databases, no pressure-dependent data are included. This parameter is thus ignored.

![](/wiki/lib/exe/taskrunner.php?id=howtosimulate%3Aequilib%3Ageneral&1788352862)