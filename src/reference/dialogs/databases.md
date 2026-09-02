Thermodynamic databases [MatCalc Documentation]



Thermodynamic databases
=======================

The thermodynamic setup is the starting point of every calculation performed with the GUI. The user has to choose the database, elements and phases. If necessary, a diffusion and physical database can be read as well. Most functions of the MatCalc GUI are not available, until the system is set up.

[![Thermodynamic setup ](/matcalc_docu/reference/dialogs/img/databases/thermodynamic_setup-f5.png "Thermodynamic setup ")](/matcalc_docu/reference/dialogs/img/databases/thermodynamic_setup-f5.png "reference:dialogs:img:databases:thermodynamic_setup-f5.png")

1. **Module selection**: Choose one of the three database types to read. The last two options are only available if the thermodynamic database has been read.

   * *Thermodynamics*: Thermodynamic database with element and phase selection. Central point of each thermodynamic equilibrium calculation and simulation. Most modules won't be accessible if no phases are loaded.   

     ```
     open-thermodyn-database mc_fe.tdb
     read-thermodyn-database
     ```

     \\It is important to note that opening and reading the thermodynamic database will delete all existing data or simulation results!
   * *Diffusion data*: Diffusion database for thermo-kinetic simulations. If no diffusion database is read, an error will occur when trying to perform kinetic simulations.   

     ```
     read-mobility-database mc_sample_fe.ddb
     ```
   * *Physical data*: Contains density of phases as a function of temperature and chemical composition. This is needed to calculate the misfit of phases and the conversion from molar fraction to volume fraction.   

     ```
     read-physical-database PhysData.pdb
     ```
2. **Database quick selector**: The drop-down list contains previously loaded database. Open the drop-list to select recently used databases and to open them instantaneously.
3. **Cancel selection**: Clears the database selection. Use this button to access the 'Open…' button again once you have selected a database and want to switch to another one.
4. **Open/Read**:

   * *Open*: Opens an file selection window to select a database.
   * *Read*: Once a database has been opened and the elements and phases have been selected, press this button to read the database into memory. Use this button if you plan to load a diffusion/physical database as well. Use Read & Close to proceed to MatCalc directly.
5. **Elements**: Shows a list of all elements available in the selected database as well as a list of their reference states.   

   ```
   select-elements B C Co Cr Cu Fe
   ```
6. **Phases**:

   * *phase*: Shows a list of all phases which can be selected based on the current selection of elements.
   * *constituents*: Constituents of each sublattice are shown in the second column. Each sublattice is separated by a colon.
   * *relative importance*: The third column shows the relative importance of the particular phase for typical simulations. High indexed values are more important/more often used than phases with lower index.
   * *comment*: Gives additional information and important features for each phase. The comment is also displayed if you move the mouse over the list item.
7. **Close**: Closes the dialog window, without applying any saves or changes. Use this button also if you have manually read the database and want to close the dialog window without reading the database again.
8. **Read & Close**: Reads the selected database values and subsequently closes the database selection window.

![](/wiki/lib/exe/taskrunner.php?id=reference%3Adialogs%3Adatabases&1788353002)