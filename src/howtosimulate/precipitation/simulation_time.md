How to reduce the duration time of long simulations [MatCalc Documentation]



### Table of Contents

* [How to reduce the duration time of long simulations](#how_to_reduce_the_duration_time_of_long_simulations)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Many active output windows](#many_active_output_windows)
  + [System complexity](#system_complexity)
  + [Tight numerical constraints](#tight_numerical_constraints)

How to reduce the duration time of long simulations
===================================================

Compatibility
-------------

MatCalc version: 6.02 - …   
Author: P. Warczok   
Created: 2020-08-11   
Revisions:

Objectives
----------

In this document, various reasons behind the lengthy simulation time are examined. For each reason, the possible speed up the calculations are discussed.

Related documents
-----------------

None

Main document
=============

On some occasions microstructure kinetics simulation happen to take a lot of time. Generally speaking, two reasons behind can be distinguished:

* Many active output windows
* System complexity
* Tight numerical constraints

These are to be discussed below.

Many active output windows
--------------------------

There is plenty of GUI windows in MatCalc which provide useful information on the system state during the simulation. Probably most popular are the xy-plots containing series describing the evolution of various variables. Also the histograms containing bars describing the parameters of various precipitate phase or grain classes are frequently used. MatCalc GUI windows have a convenient feature of the interactive content update as the simulation progresses. On some occasions, the strange window output allows to recognize the wrong setup of the simulation so that the calculation can be interrupted to avoid the further loss of computation time. On the other hand, one needs to keep in mind that an iterative update of GUI windows also requires some computation time. This cost increases with the number of displayed elements (e.g. plots) in GUI windows. In extreme cases (few hundreds of displayed variables/classes), the computation time required for a simulation might double.

Several solutions can be implemented to overcome this problem. The simplest one would be to create the needed output windows after the simulation is completed. Another possibility exist with increasing the buffer storage period, which can be set in **'Precipitation kinetics'** window or with script/console command ***'set-simulation-parameter store-every …'***.

[![ 'Store results every…' entry](/howtosimulate/precipitation/img/store_results_interval.png " 'Store results every…' entry")](/howtosimulate/precipitation/img/store_results_interval.png "howtosimulate/precipitation/img/store_results_interval.png")

There exists also the possibility to freeze the window content update. This can be done with clicking on the icon [![ 'Freeze all window update' icon](/howtosimulate/precipitation/img/icon_freeze_update.png " 'Freeze all window update' icon")](/howtosimulate/precipitation/img/icon_freeze_update.png "howtosimulate/precipitation/img/icon_freeze_update.png") in Toolbar or on the entry **'Freeze Update'** in menu **'View'** (this places the checkmark next to it).

[![ 'Freeze update' menu entry](/howtosimulate/precipitation/img/menu_freeze_update.png " 'Freeze update' menu entry")](/howtosimulate/precipitation/img/menu_freeze_update.png "howtosimulate/precipitation/img/menu_freeze_update.png")

System complexity
-----------------

MatCalc is capable to perform the kinetic simulations in multi-component multi-phase systems. However, the with the increasing number of the elements, phases or grain-/precipitate-size classes, the number of the computed equations for one time iteration increase during the simulation increase as well. Moreover, more equations enhance the chance of crossing one of the numerical limits, which will be described in the next section. Hence, in order to obtain a simulation with a reasonable duration time, it is recommended to take a while for the consideration of the simulation goals and the factors which might affect its outcome.

Let us name an example here (***Disclaimer/** the following is used in the fictitious manner - any resemblance to a real user or simulation is purely coincidental*): a MatCalc user wants to simulate the precipitation kinetics in the microalloyed steel – a “classic” task for MatCalc. Here, the precipitates consist of carbonitrides of vanadium, niobium and tantalum. The user sets up the simulation with the system composition of the commercial steel, specifying, among others, also the contents for phosphorus and sulphur. While the latter are definitely included in the system (both P and S are usually present in the steel compositions), these are not relevant for the problem that is to be considered in the simulation - Phosphorus and sulphur do not constitute the precipitates that are to be investigated in this simulation, which can be checked by the literature study supported with the thermodynamic equilibrium calculations in MatCalc. In effect, their presence does not have an effect on the result of the kinetic simulation, but will elongate its duration, as the mass balance checks need to be performed for these elements.

While for simple calculations (short thermo-mechanical treatments, small amount of constituents), the inclusion of one more species in the simulation might have a hardly noticeable effect (in range of few seconds), it might still result in the considerable extension of the duration time for complex treatments in multi-component systems, making a difference of few hours at the end. Of course, very often the users are not aware of the factors affecting the simulation outcome, and it is not until the simulation results are available that these factors are revealed to them. Still, the point presented here is that a reflection of any prior knowledge of the system/process on the simulation setup might be beneficial on the simulation duration time. After all, it is very easy to introduce more complexity into the oversimplified system setup and observe the effect of the modification. On the other hand, once the simulation seem to be stuck, it might be a good idea to have a look on the results in scope of the factors (elements, phases, models) that seem to be neutral on its outcome so far and eliminate these from the next try.

Tight numerical constraints
---------------------------

Kinetic simulations in MatCalc are performed in terms of iterations during which the time variable is incremented. During each iteration, the state parameters (e.g. size class radius, matrix composition, grain size) evolve according to the evolution equations from the models involved in the simulation. While the user has a possibility to define the magnitude of the time increments, MatCalc has a management algorithm which usually works fine and is used by default. Within this algorithm, some constraints are imposed on the magnitude of the system parameter difference obtained within one iteration in order to assure the convergence of the calculation result. At any time instance, the time increment is evaluated which is needed to reach each these limit values. The shortest increment value found is used for the next iteration.

On several occasions, a specific constraint is found to be limiting the time increment of one iteration. Hence, more iterations are evaluated till the simulated end time point is reached which finally results in the longer simulation duration time. In extreme cases, one iteration could cover a tiny fraction of a second of simulated time, which practically freezes a simulation, even on the computers with fastest CPU.

Once the command “list-simulation-parameter” is executed, the list of these constraints, together with their values, can be seen in the console in the “convergence control” section.

[![ "list-simulation-parameter" output](/howtosimulate/precipitation/img/convergence_control_parameters.png " \"list-simulation-parameter\" output")](/howtosimulate/precipitation/img/convergence_control_parameters.png "howtosimulate/precipitation/img/convergence_control_parameters.png")

The numerical constraint which determines the actual time interval in the given iteration can be recognized in two ways:

* The kinetic simulation output displayed in the console window includes information on the state of the actual matrix phase and precipitate phases during the simulation. Among others, the numerical limits which return the shortest time interval, together with this interval value is also included, as shown in the picture (zero values mean no interaction from this entity). The lowest value is then applied for the last time interval.

[![ Iteration limits displayed in console window](/howtosimulate/precipitation/img/console_limit_display.png " Iteration limits displayed in console window")](/howtosimulate/precipitation/img/console_limit_display.png "howtosimulate/precipitation/img/console_limit_display.png")

* Once “kinetic-accelarator” option is activated (with “set-simulation-parameter kinetic-accelerator=yes” command), the active constraints of few last iterations are stored in the buffer and can be displayed in the GUI window “Kinetic accelerator: summary” (window type “u2”). In each row, a system entity (precipitate or domain phase) and the name of the limiting constraint is displayed. A broader overview can be obtained with an investigation of the “Kinetic accelerator: phase details” GUI window (window type “u1”), where the active limits for the selected phases can be examined.

[![ "Kinetic accelerator summary" window](/howtosimulate/precipitation/img/kinetic_accelerator_summary.png " \"Kinetic accelerator summary\" window")](/howtosimulate/precipitation/img/kinetic_accelerator_summary.png "howtosimulate/precipitation/img/kinetic_accelerator_summary.png")

Hence, a review of the last iteration data with the scope of the occurring limiting constraints and the related system component (precipitate or domain phase) usually yields a useful information. Once one of these seems to be dominating the output, the following should be considered (in this order):

1. Are the settings for this entity correct?
2. Is this entity essential for the simulation goal? (in the spirit of the system complexity analysis mentioned in the previous point)
3. Cautious modification of the numerical constraint.

While the numerical constraints set within MatCalc algorithm are intended to assure the simulation result convergence, a cautious modification of these can have little effect on the result quality but a profound one on the simulation length. The changes can be performed in the console with the “set-simulation-parameter convergence-control numerical-limits-precipitation #constraint=” or “set-simulation-parameter convergence-control numerical-limits-microstructure-evolution #constraint=” command. Once such a modification is performed, some test runs for various modification magnitudes are recommended to recognize the effect on the simulation result.

![](/wiki/lib/exe/taskrunner.php?id=howtosimulate%3Aprecipitation%3Asimulation_time&1788352863)