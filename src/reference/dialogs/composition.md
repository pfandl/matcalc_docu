Nominal composition [MatCalc Documentation]



Nominal composition
===================

After setting up the system in the database dialog, the chemical composition is usually entered in the *nominal composition* dialog box. Forgetting to do so represents a common source for strange and unexpected simulation results, simply because the chemical composition is not correctly defined. *MatCalc* tries to remember the chemical composition of precious simulations and initializes the composition values accordingly.

[![ Nominal composition dialog box](/reference/dialogs/img/composition/nominal_composition-chemical_composition_f7.png " Nominal composition dialog box")](/reference/dialogs/img/composition/nominal_composition-chemical_composition_f7.png "reference/dialogs/img/composition/nominal_composition-chemical_composition_f7.png")

1. **Element**: The element column lists all loaded elements in alphabetical order.
2. **Reference element**: One element is set as the reference elements. Its chemical composition will automatically be set with the residual value to 100% and can not be set manually. Double click this field to change the reference element.   

   ```
   set-reference-element Fe
   ```
3. **Amount**: Shows the amount of each element in the unit selected in the bottom part of this dialog. Double click this field to change its chemical composition.   

   ```
   enter-composition wp C=0.2
   ```
4. **Set reference element**: Alternative method to set the highlighted element to the reference element.
5. **Change (F2)**: Alternative method to change the chemical composition of the highlighted item.
6. **Unit selection**:

   * *mole fraction*: Chemical composition in mole fraction (e.g./ Fe3C/ 0.25C, 0.75Fe).   

     ```
     enter-composition x c=0.25  $ Mole fraction
     enter-composition xp c=0.25 $ Mole percent
     ```
   * *u-fraction*: Chemical composition in the form of substitutional site fractions. Typically used for the setup of para-equilibrium conditions (e.g./ Fe3C/ 0.33C, 1.0Fe).   

     ```
     enter-composition u c=0.33  $ u-fraction
     enter-composition up c=33 $ u-percent
     ```
   * *weight fraction*: Chemical composition in weight fraction (e.g./ Fe3C/ 0.067C, 0.933Fe).   

     ```
     enter-composition w c=0.067  $ weight fraction
     ```
   * *weight percent*: Chemical composition as weight percent (e.g./ Fe3C/ 6.7%C, 93.3%Fe).   

     ```
     enter-composition wp c=6.67 $ weight percent
     ```
7. **Save to file**: not yet implemented.
8. **Open file**: not yet implemented.
9. **View file**: not yet implemented.

This dialog can also be utilized to convert from one unit to another. Simply enter the nominal composition on one unit and select another unit. *MatCalc* automatically converts to the new units and displays the values in the dialog.

![](/wiki/lib/exe/taskrunner.php?id=reference%3Adialogs%3Acomposition&1788353002)