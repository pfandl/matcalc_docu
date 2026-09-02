How to... calculate min G\* and P-nucl array [MatCalc Documentation]



### Table of Contents

* [How to... calculate min G\* and P-nucl array](#how_to_calculate_min_g_and_p-nucl_array)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
  + [Complementary files](#complementary_files)
* [Main document](#main_document)

  + [Physical description of the example](#physical_description_of_the_example)
  + [Setup system](#setup_system)
  + [Loops and conditions](#loops_and_conditions)
  + [Detailed discussion of the loops](#detailed_discussion_of_the_loops)
* [Consecutive articles](#consecutive_articles)

How to... calculate min G\* and P-nucl array
============================================

Compatibility
-------------

MatCalc version: 5.50.1007   
Database: mc\_fe.tdb, mc\_sample\_fe.ddb  
Author: Georg Stechauner  
Created: 2013-02-28   
Revisions:

Objectives
----------

The minimum nucleation energy is of interest, whenever a nucleation event occurs and has to be calculated (i.e. to calculate P-nucl). It should be understood that the calculated energy, depends on various factors including chemical composition and temperature. Further, the composition which delivers the minimum G\* energy only gives a statistically 'most likely' composition, that is why the calculated nucleation probability is given in percent, depending on the likelihood of the event to occur. Other compositions, mostly close to the calculated one are also possible and have to be considered.

**Note:** This is an advanced example for interested users who want to gain a deep understanding of their material. The whole example will be given in script form, which will be discussed at length. If you feel uneasy about loops and conditions, you may want to check out our explanation on ['Syntax for Conditions, Loops and other commands'](/matcalc_docu/reference/syntax "reference:syntax") beforehand.

Related documents
-----------------

* [E10 - 'Most-likely' nucleus composition for bcc-Cu precipitation in bcc-Fe](/matcalc_docu/examples/equilib/e10 "examples:equilib:e10")
* [Help-file on Loops and Conditions](/matcalc_docu/reference/syntax "reference:syntax")
* [Part II showing how to visualize min G\* and P using GNUPlot](/matcalc_docu/howtosimulate/physical/mingstar/vis "howtosimulate:physical:mingstar:vis")

Complementary files
-------------------

Click [here](/matcalc_docu/howtosimulate/physical/mingstar/howto_-_g-star_-_vcn.mcs "howtosimulate:physical:mingstar:howto_-_g-star_-_vcn.mcs (9.3 KB)") to view the script for this HowTo manual.

Main document
=============

Physical description of the example
-----------------------------------

The basis of this example is the calculation of the minimum nucleation energy, G\*. This value is a function of γ - interfacial energy and ΔG0 - driving force change while nucleation:

![G^∗ = {{16pi}/{3}} ∗ {{{gamma_0}^3}/{{Delta G}^2}}](/wiki/lib/plugins/mathpublish/img.php?img=8d0e8bbd7a65352ca39d79afa3402012 "G^∗ = {{16pi}/{3}} ∗ {{{gamma_0}^3}/{{Delta G}^2}}")

It is necessary to use loops in this example, as the calculation of a single G\* value is of rather little importance. It is necessary to calculate *all* values for G\* in the range of interest. In this example we calculate the most likely nucleus composition for a Vanadium-Carbo-Nitride (VCN) at 400°C with varying the amounts of V and N, respectively. However, as the energies of G\* are in the range of 1E-20, which are not easily imaginable, it is more comfortable to work with the nucleation probability P.

![P = e^({-G^∗}/{{k_b} ∗ T})](/wiki/lib/plugins/mathpublish/img.php?img=fcbbeb36d2481870273637c1328194b7 "P = e^({-G^∗}/{{k_b} ∗ T})")

kb is the Boltzmann constant and T is the temperature in Kelvin. By normalizing P with Pmax an array with values between 0 and 1 are created, where 0 represents a low probability and 1 a very high probability of nucleus composition. Equation two shows, due to the minus in front of G\*, that a minimum of G\* results in a maximum of P.

I order to calculate G\* according to equation 1, *MatCalc* uses the variables CIE (Interfacial energy) and DFM (Driving force). The evaluation of both is done automatically when calculating an equilibrium, however the driving force is zero, as soon as the phase is present (e.g. nucleated, precipitated,…). To calculate G\*, the phase fraction of the phase in question has to be fixed to zero. This will lead to a positive driving force, which can be used in the calculation to get correct results.

Setup system
------------

Start with the regular **setup and load an iron thermodynamic database** (sample or full version). Diffusion data is not needed:

```
open-thermo-database mc_sample_fe.tdb                  $ open thermodynamic database

select-elements C N V                                  $ select elements
select-phase fcc_a1 bcc_a2                             $ select phases

read-thermodyn-database                                $ read thermodynamic database

$ steel composition ...
enter-composition wp c=0.2 n=0.01 v=0.145
```

The values for N and V are just starting values, and will be permutated in the course of this calculation. Feel free to change C to other values if you are interested in more carbon containing alloys.

**Setup the phases needed for the calculation:**

```
change-phase-status fcc_a1 f s s                       $ suspend austenite
change-phase-status fcc_a1#01 f s s                    $ suspend fcc_a1#01 phase

create-new-phase fcc_a1 c :Fe,V%:C%,N%: VCN
Change-phase-status VCN f e s                          $ set enforce major
                                                         constituents flag
change-phase-status VCN f f s                          $ set fixed phase fraction
change-phase-status VCN p 0.0                          $ set phase fraction to zero
```

In a first step, we suspend the automatically created complex carbo-nitride phase (fcc\_a1#01), in favor of a manually created composition set. Pay attention to the last 2 code lines, where we fix the phase fraction of VCN to zero, to obtain positive driving forces!

**Create arrays and functions:**

```
$ create a global array to store results
create-global-array G_star_array
create-global-array G_star_array_no_xy
create-global-array P_array
create-global-array P_array_no_xy

$ define function for G_star
set-function-expression G_star 16*pi/3*(cie$VCN)^3/(dfm$VCN/vm)^2
set-function-expression P_nucl exp(-G_star/(kB*T))
```

Create the necessary arrays, to have a place to save the results to. Note, that we create two arrays for G\* and P. One with description of x- and y-values, one without. The functions for G\* and P are entered in the lower portion. These will be used in the loops to come.

**Set loop and condition parameters and calculate initial equilibrium:**

```
$ Define variables
set-variable-value Vmin 0.10                  $ lower boundary for V
set-variable-value Vmax 0.50                  $ upper boundary for V
set-variable-value Vint 35                    $ Steps in the loop
set-variable-value Nmin 0.0                   $ lower boundary for N
set-variable-value Nmax 0.50                  $ upper boundary for V
set-variable-value Nint 15                    $ Steps in the loop
set-variable-value max_P_nucl 0               $ Define max Nucleation probability
set-variable-value test_temp 400              $ test temperature 

$ Calculate initial equilibrium
set-temperature-celsius test_temp             $ set temperature
set-automatic-startvalues                     $ initialize variables
calculate-equilibrium                         $ calculate equilibrium at test temperature
```

The upper part of this code snippet defines variables for the loops (boundaries and steps) and the testing temperature. Change the 400°C to other temperatures, if you want to investigate this parameters' influence. As usual, before starting with anything in *MatCalc*, an initial equilibrium is calculated.

Loops and conditions
--------------------

This codeblock is the working horse of this script. It calculates both G\* and P, and fills all the tables. In the end, it normalizes the nucleation probability. A discussion of this code and its features will follow thereafter. The '@' is used to blank the system feedback in the *MatCalc* console. This should increase readability and to avoid large portions of code being printed over and over:

```
$ make loop for V and N content. Fe will be modified inversely to V, C inversely to N
@ set-variable-value row_count 0    $ index variable

$ first loop is for V 
@ for (i;Vmin..Vmax:Vint)
@ $   show-expression i
@   set-variable-value col_count 0    $ index variable
@   for (j;Nmin..Nmax:Nint)
@ $       show-expression j
@      $ assign compositions
@      set-variable-value x_V i
@      set-variable-value x_N j
@      
@      $ check plausibility
@      if (x_V<=0)
@         set-variable-value x_V 1e-6
@      endif
@      if (x_N<=0)
@         set-variable-value x_N 1e-6
@      endif
@      
       show-expression x_V x_N
@
@      $ fill first line (header)
@      if (row_count==0)
@         set-array-value G_star_array 0 col_count+1 x_N
@         set-array-value P_array 0 col_count+1 x_N
@      endif 
@      $set first column value
@      if (col_count==0)
@         set-array-value G_star_array row_count+1 0 x_V 
@         set-array-value P_array row_count+1 0 x_V
@      endif 
@      
@      $ set u-fraction constraint in nucleation phase
@      change-phase-status VCN c V x x_V   
@      change-phase-status VCN c N x x_N   
       
@      $ calculate equilibrium to determine the chemical driving force
@      calculate-equilibrium
       
@      $ store in array
@      if ((dfm$VCN>0.0)&(cie$VCN>0.0))
@         set-array-value G_star_array row_count+1 col_count+1 G_star
@         set-array-value G_star_array_no_xy row_count col_count G_star
@         set-array-value P_array row_count+1 col_count+1 P_nucl
@         set-array-value P_array_no_xy row_count col_count P_nucl
@ $         show-expression row_count col_count
@      else
@         set-array-value G_star_array row_count+1 col_count+1 0.0
@         set-array-value G_star_array_no_xy row_count col_count 0.0
@         set-array-value P_array row_count+1 col_count+1 0.0
@         set-array-value P_array_no_xy row_count col_count 0.0
@      endif
@      
@      $ remember maximum P_nucl
@      if (P_nucl>max_P_nucl)
@         set-variable-value max_P_nucl P_nucl
@      endif
@
@      $ increment counter
@      set-variable-value col_count col_count+1
@  endfor
   
@  $ increment counter
@  set-variable-value row_count row_count+1
@ endfor


@ $ finally normalize nucleation probability
@ set-variable-value row_count 0    $ index variable
@ for (i;Vmin..Vmax:Vint)
@ $   show-expression i
@   set-variable-value col_count 0    $ index variable
@   for (j;Nmin..Nmax:Nint)
@      $ normalize
@      set-array-value P_array row_count+1 col_count+1 P_array[row_count+1]....
....[col_count+1]/max_P_nucl
@      set-array-value P_array_no_xy row_count col_count P_array_no_xy[row_count]....
....[col_count]/max_P_nucl
@      $ increment counter
@      set-variable-value col_count col_count+1
@  endfor
@  $ increment counter
@  set-variable-value row_count row_count+1
@ endfor
```

**Attention**: When copy&pasting the code from above, remove the '…. ….' sections and set the command into one line!

Detailed discussion of the loops
--------------------------------

**Part 1 - Initialize and setup loops and arrays:**

```
$ make loop for V and N content. Fe will be modified inversely to V, C inversely to N
@ set-variable-value row_count 0    $ index variable

$ first loop is for V 
@ for (i;Vmin..Vmax:Vint)
@ $   show-expression i
@   set-variable-value col_count 0    $ index variable
@   for (j;Nmin..Nmax:Nint)
@ $       show-expression j
@      $ assign compositions
@      set-variable-value x_V i
@      set-variable-value x_N j
@      
@      $ check plausibility
@      if (x_V<=0)
@         set-variable-value x_V 1e-6
@      endif
@      if (x_N<=0)
@         set-variable-value x_N 1e-6
@      endif
@      
       show-expression x_V x_N
@
@      $ fill first line (header)
@      if (row_count==0)
@         set-array-value G_star_array 0 col_count+1 x_N
@         set-array-value P_array 0 col_count+1 x_N
@      endif 
@      $set first column value
@      if (col_count==0)
@         set-array-value G_star_array row_count+1 0 x_V 
@         set-array-value P_array row_count+1 0 x_V
@      endif
```

This portion of code focuses on the setup of the arrays. It starts by initializing the 'row count' variable (which keeps track of the actual row), and the 'col count' (which does basically the same for the columns). After that, we set the auxiliary variables x\_V and x\_N, which are used in equilibrium calculations. As 'i' and 'j' are the runtime variables, we want to introduce those auxiliary ones to keep the code clean and easily readable! A quick check for plausibility follows (it is not possible for any atom to be negatively existing ![:-D](/wiki/lib/images/smileys/biggrin.svg)). The last two conditions are responsible for naming the x- and y-values of the arrays.

**Part 2 - Calculate G\* and P:**

```
@      $ set u-fraction constraint in nucleation phase
@      change-phase-status VCN c V x x_V   
@      change-phase-status VCN c N x x_N   
       
@      $ calculate equilibrium to determine the chemical driving force
@      calculate-equilibrium
       
@      $ store in array
@      if ((dfm$VCN>0.0)&(cie$VCN>0.0))
@         set-array-value G_star_array row_count+1 col_count+1 G_star
@         set-array-value G_star_array_no_xy row_count col_count G_star
@         set-array-value P_array row_count+1 col_count+1 P_nucl
@         set-array-value P_array_no_xy row_count col_count P_nucl
@ $         show-expression row_count col_count
@      else
@         set-array-value G_star_array row_count+1 col_count+1 0.0
@         set-array-value G_star_array_no_xy row_count col_count 0.0
@         set-array-value P_array row_count+1 col_count+1 0.0
@         set-array-value P_array_no_xy row_count col_count 0.0
@      endif
@      
@      $ remember maximum P_nucl
@      if (P_nucl>max_P_nucl)
@         set-variable-value max_P_nucl P_nucl
@      endif
@
@      $ increment counter
@      set-variable-value col_count col_count+1
@  endfor
   
@  $ increment counter
@  set-variable-value row_count row_count+1
@ endfor
```

This second part is where the real calculations are performed. We start off by setting the u-fraction constraints to our phase, in order to get different results depending on the actual chemical composition.

After calculating the equilibrium, the values will get stored in the corresponding arrays, if both conditions (positive driving force and interfacial energy) are fulfilled. Else, the spot in the array will be filled with 0.

In order to normalize the nucleation probability afterwards, we have to keep track of the highest P, which is done in the following condition.

The last two arguments simply increase the column-/row-count by one, for the next run-through of the loop.

**Part 3 - Normalization of P:**

```
@ $ finally normalize nucleation probability
@ set-variable-value row_count 0    $ index variable
@ for (i;Vmin..Vmax:Vint)
@ $   show-expression i
@   set-variable-value col_count 0    $ index variable
@   for (j;Nmin..Nmax:Nint)
@      $ normalize
@      set-array-value P_array row_count+1 col_count+1 P_array[row_count+1]....
....[col_count+1]/max_P_nucl
@      set-array-value P_array_no_xy row_count col_count P_array_no_xy[row_count]....
....[col_count]/max_P_nucl
@      $ increment counter
@      set-variable-value col_count col_count+1
@  endfor
@  $ increment counter
@  set-variable-value row_count row_count+1
@ endfor
```

In this final part of the script, the whole P-array will be worked through and all values are divided by the previously found P-max. This leads to normalized values, which come in handy for plotting and visualization of the results, and give a good answer to the question of 'most likely nucleus composition'.

Consecutive articles
====================

In order to visualize the obtained data, either use your own plotting tool of choice, or go to [part II](/matcalc_docu/howtosimulate/physical/mingstar/vis "howtosimulate:physical:mingstar:vis"), where the procedure of plotting will be shown using opensource software GNUPlot.

![](/wiki/lib/exe/taskrunner.php?id=howtosimulate%3Aphysical%3Amingstar%3Acalc&1788352992)