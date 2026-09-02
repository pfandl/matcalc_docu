MatCalc internal variables [MatCalc Documentation]



### Table of Contents

* [MatCalc internal variables](#matcalc_internal_variables)

  + [test\_result](#test_result)
  + [is\_td\_database\_open](#is_td_database_open)
  + [is\_td\_database\_read](#is_td_database_read)
  + [is\_diff\_database\_read](#is_diff_database_read)
  + [is\_phys\_database\_read](#is_phys_database_read)
  + [active\_frame\_id](#active_frame_id)
  + [last\_plot\_id](#last_plot_id)
  + [last\_bc\_index](#last_bc_index)

MatCalc internal variables
==========================

*MatCalc* uses a list of internal variables, which can be accessed at any time to check for various states. A list of them, and their use, is presented below:

test\_result
------------

Gets a boolean value of 0 or 1, depending on the result of one of the following commands:

```
test-exist-td-database
test-exist-mob-database 
test-exist-ph-database
```

These commands access the internal variables below, and save the return value to the \*test\_result\* variable. Can be used to test for the existence of a database, and automatically selecting a different one if the preferred one can not be found:

```
test-exist-td-database mc_fe.tdb $ Check if database is present
if (test_result==1)
   open-thermodyn-database mc_fe.tdb $ Thermodynamic database
else
   test-exist-td-database mc_x_FeAlCCrMnMoNNbSiVW.tdb 
   if (test_result==1)
      open-thermodyn-database mc_x_FeAlCCrMnMoNNbSiVW.tdb $ Thermodynamic database
   else
      send-dialog-string "No valid database found. Visit matcalc website and download
       the free 'mc_x_FeAlCNNbTi' database."
      stop_run_script
   endif
endif
```

is\_td\_database\_open
----------------------

Has a value of 1 if the thermodynamic database has been opened. Not necessarily read yet!

is\_td\_database\_read
----------------------

Has a value of 1 if the thermodynamic database has been read.

is\_diff\_database\_read
------------------------

Has a value of 1 it the diffusion/mobility database has been read.

is\_phys\_database\_read
------------------------

Has a value of 1 if the physical database has been read.

active\_frame\_id
-----------------

This variable refers to the most actual frame. The \*most actual\* is always the one which has been accessed recently, or in the case of a new frame creation, the newly created one. Using the following code, a variable can be assigned to the actual frame, in order to address it by a name instead of a number:

```
set-variable-value histogram_frame active_frame_id
```

You can now use 'histogram\_frame' whenever you want to access and interact with the frame, instead of having to use the number which is assigned to the frame automatically. This approach is especially recommended when more frames are used and manipulated alternately.

```
$ Instead of...
move-gui-window 3 x-pos y-pos x-size y-size
$ ... you can use:
move-gui-window histogram_frame x-pos y-pos x-size y-size
```

This leads to easier-to-read scripts and minimizes errors due to erroneous numbering.

last\_plot\_id
--------------

This variable is comparable to the '.' (Period-sign) used in the scripting to address the most recent plot. By using this internal variable, a plot can be assigned a unique name, which makes modifying and editing this plot easier compared to the oftentimes misleading numbers assigned by *MatCalc*. These errors root in the difference of numberation from plots and frames. While plots are continuously numbered throughout all frames, and always start with #0, a user-created frame starts with number #3, as #0 through #2 are occupied by 'Output', 'Phase details' and 'Phase summary', respectively.   
Use the internal variable in the same way as the active\_frame\_id above:

```
set-variable-value phasefraction-plot last_plot_id
```

Instead of using the plot's number, you can now always use 'phasefraction-plot'.

last\_bc\_index
---------------

Comparable to 'last\_plot\_id', this variable represents the most recent boundary-condition index. Can be used in MC simulations, in a similar way as shown above.

![](/wiki/lib/exe/taskrunner.php?id=reference%3Ainternal&1788352869)