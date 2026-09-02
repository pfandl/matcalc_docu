Introduction of precipitates into the initial state of the simulation [MatCalc Documentation]



### Table of Contents

* [Introduction of precipitates into the initial state of the simulation](#introduction_of_precipitates_into_the_initial_state_of_the_simulation)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Definition of size distribution of the initial precipitates](#definition_of_size_distribution_of_the_initial_precipitates)

    - [Type in the required values](#type_in_the_required_values)
    - [Read the required values from a text file](#read_the_required_values_from_a_text_file)
    - [Generate the required values](#generate_the_required_values)
  + [Selection of initial state condition](#selection_of_initial_state_condition)

Introduction of precipitates into the initial state of the simulation
=====================================================================

Compatibility
-------------

MatCalc version: 6.02 - …   
Author: P. Warczok   
Created: 2019-09-17   
Revisions:

Objectives
----------

On several occasions, simulated microstructure contains some precipitates already in the initial state of kinetic calculation. This section describes the way to introduce these precipitates before the simulation.

Related documents
-----------------

1. [Primary precipitates](/matcalc_docu/howtosimulate/precipitation/primary_prec "howtosimulate:precipitation:primary_prec") - Treatment of primary precipitates in precipitation kinetics simulations
2. [Treatment of primary precipitates](/matcalc_docu/examples/precipitation/p20/p20_1 "examples:precipitation:p20:p20_1")

Main document
=============

There are 2 points that are to be considered in this kind of simulation:

* Definition of size distribution for the initial precipitates
* Selection of initial state condition

Note that this procedure can be applied also for the introduction of the primary precipitates into the kinetic simulation. In this case, the input data (phase fraction, chemical composition) can be taken from the Scheil-Gulliver simulation results.

Definition of size distribution of the initial precipitates
-----------------------------------------------------------

MatCalc treats the precipitates as objects consisting of size classes, where each size class is characterized with the radius, number density and chemical composition (expressed with the site fractions for each sublattice). The set of these parameters is referred to as *precipitate size distribution*. The size distribution of the precipitates in the initial state needs to be defined by the user. Once a precipitate phase representing the phase in question is created and the number of size classes is set (by default 25 size classes are used), the definition of precipitate size distribution can be performed in **“Phase status”** window → **“Precipitate”** tab, by clicking on **“Edit precipitate distribution”** (once the relevant precipitate phase is selected).

[![ Edit precipitate distribution button](/matcalc_docu/howtosimulate/precipitation/img/edit_precipitate_distribution_1_6021003.png " Edit precipitate distribution button")](/matcalc_docu/howtosimulate/precipitation/img/edit_precipitate_distribution_1_6021003.png "howtosimulate:precipitation:img:edit_precipitate_distribution_1_6021003.png")

A new window **“Edit…”** appears which consist of a table and has some buttons and text boxes located on the right side. The number of table rows corresponds to the number of size classes used for this precipitate phase. The column headers describe the parameters, the values of which are stored for each size class. The radius and the number are placed in the first and second column accordingly. Next columns describe the site fractions of elements on the sublattices, as specified by the sublattice description used for this phase, eg. *“yx\_TI(0)”* describes the site fraction of titanium on sublattice “0”. Initially, the table cells are empty – the precipitate is not present in the microstructure. It is necessary to fill these cells with the relevant information for the precipitates that are to be present in the initial state of the simulation.

[![ Edit precipitate distribution table](/matcalc_docu/howtosimulate/precipitation/img/edit_precipitate_distribution_2_6021003.png " Edit precipitate distribution table")](/matcalc_docu/howtosimulate/precipitation/img/edit_precipitate_distribution_2_6021003.png "howtosimulate:precipitation:img:edit_precipitate_distribution_2_6021003.png")

There are 3 ways to define the precipitate size distributions:

* Type in the required values
* Read the required values from a text file
* Generate the required values

Regardless of the input method, it is recommended to create a calculation state in which the defined size distributions will be stored.

### Type in the required values

The values for radius, number density and relevant site fractions for each size class can be simply typed (or “copy-pasted”) in by the user. Using this straightforward method, one has to keep in mind that the radius values are to be expressed in meters and the number density values are to be relevant for a cubic meter of the system. Moreover, the sum of the site fractions at the given sublattice needs to equal the stoichiometric contribution of this sublattice.

Example: M23C6 carbide is described in mc\_fe.tdb database with 3 sublattices with the stoichiometric ratio of 20:3:6. Hence:

* the sum of site fractions on sublattice “0” needs to equal 20/29
* the sum of site fractions on sublattice “1” needs to equal 3/29
* the sum of site fractions on sublattice “2” needs to equal 6/29

This method is a convenient way to transfer the MatCalc results from one workspace to the other.

### Read the required values from a text file

Size distribution can be read from the text file. [Here](/matcalc_docu/howtosimulate/precipitation/script/size_dist_tin_primary.txt "howtosimulate:precipitation:script:size_dist_tin_primary.txt (3.3 KB)") you will find the file with sample distribution of M23C6 phase which can be used as a template. The column order in the file relates to the column order in the MatCalc table. The first column in text file contains always the radius values (expressed in meters), the second column contains always the number density values (expressed in m-3) and the next columns contain the respective site fractions according to the sublattice description of the relevant phase. So be sure, that the order in the columns in the file correlates with the order of the columns in MatCalc! Moreover, keep in mind that the sum of the site fractions at the given sublattice needs to equal the stoichiometric contribution of this sublattice.

In order to read the size distribution data from a file, klick on **“Read”** button and select the relevant data.

[![ Read precipitate distribution from file](/matcalc_docu/howtosimulate/precipitation/img/read_precipitate_distribution_6021003.png " Read precipitate distribution from file")](/matcalc_docu/howtosimulate/precipitation/img/read_precipitate_distribution_6021003.png "howtosimulate:precipitation:img:read_precipitate_distribution_6021003.png")

### Generate the required values

In order to use the functionality of size distribution generation, the user needs to define:

* Total phase fraction of the precipitate at the given instant
* Size distribution type. Available types are: Normal, Log-normal, LSW and Rayleigh distributions
* Values of minimal, mean and maximal radius of the size distribution
* Relative standard deviation (coefficient of variation)

The total phase fraction is to be set for the parent equilibrium phase. In order to do that:

1. Select parent equilibrium phase in the phase list
2. Select **“General tab”**
3. Click on **“Set amount”** button
4. In the **“Input…”** window type in the phase fraction value and click on **“OK”** button

[![ Set phase fraction button](/matcalc_docu/howtosimulate/precipitation/img/set_phase_fraction_1_6021003.png " Set phase fraction button")](/matcalc_docu/howtosimulate/precipitation/img/set_phase_fraction_1_6021003.png "howtosimulate:precipitation:img:set_phase_fraction_1_6021003.png")

[![ Set phase fraction window](/matcalc_docu/howtosimulate/precipitation/img/set_phase_fraction_2_6021003.png " Set phase fraction window")](/matcalc_docu/howtosimulate/precipitation/img/set_phase_fraction_2_6021003.png "howtosimulate:precipitation:img:set_phase_fraction_2_6021003.png")

Other parameters are to be set in the **“Edit…”** window. Afterwards, click on **“Generate”** button. The relevant values will be introduced into the table cells. Note that the provided information allows to calculate the number density for each individual size class. On the other side, the chemical composition of each size class is identical and equal to the one of the parent equilibrium phase.

[![ Generate precipitate distribution](/matcalc_docu/howtosimulate/precipitation/img/generate_precipitate_distribution_6021003.png " Generate precipitate distribution")](/matcalc_docu/howtosimulate/precipitation/img/generate_precipitate_distribution_6021003.png "howtosimulate:precipitation:img:generate_precipitate_distribution_6021003.png")

Selection of initial state condition
------------------------------------

There 3 different options for the specification of the microstructure kinetics simulation initial state (Menu **“Calc”** → **“Precipitation kinetics”**). These are:

* Taking no action
* Resetting precipitates and microstructure
* Loading the previously defined calculation state as starting condition

[![ Starting conditions for kinetic simulation](/matcalc_docu/howtosimulate/precipitation/img/starting_conditions_kinetics_6021003.png " Starting conditions for kinetic simulation")](/matcalc_docu/howtosimulate/precipitation/img/starting_conditions_kinetics_6021003.png "howtosimulate:precipitation:img:starting_conditions_kinetics_6021003.png")

In principle, the default option of resetting the precipitates precludes the usage precipitates in the initial state. One possibility is to switch it to **“no action”** which just takes the current MatCalc state as the initial state for the upcoming simulation. However, it works only for the very first calculation, as every consecutive simulation starts with the final state of the previous one. In other words, the introduced size distribution is lost after the first simulation with this option selected.

A recommended course of action is to create a calculation state right after the size distribution are introduced. This calculation state can be used next as the starting condition for the all the simulations (as long as this calculation state will not be overwritten by the user).

![](/wiki/lib/exe/taskrunner.php?id=howtosimulate%3Aprecipitation%3Ainitial_precipitates&1788352862)