Contents of the menu bar [MatCalc Documentation]



### Table of Contents

* [Contents of the menu bar](#contents_of_the_menu_bar)

  + [1. File](#file)
  + [2. Edit](#edit)
  + [3. Global](#global)
  + [4. Calc](#calc)
  + [5. Cells](#cells)
  + [6. Monte Carlo](#monte_carlo)
  + [7. Script](#script)
  + [8. View](#view)
  + [9. Help](#help)

Contents of the menu bar
========================

This section contains information on the menu bar and its functions. Detailed information will be provided with a link, or can be found directly in the  [corresponding](/reference/dialogs "reference/dialogs") section.

[![ MatCalc menu bar](/reference/menu/img/6101002_menubar.png " MatCalc menu bar")](/reference/menu/img/6101002_menubar.png "reference/menu/img/6101002_menubar.png")

1. File
-------

[![ File section](/reference/menu/img/6101002_menu_file.png " File section")](/reference/menu/img/6101002_menu_file.png "reference/menu/img/6101002_menu_file.png")

1. **New** (Ctrl+N): Opens a dialog box which asks for the desired file type (MatCalc workspace, Script file, Text file)
2. **Open** (Ctrl+O): Loads a previously saved file (workspace, script, …)
3. **Save** (Ctrl+S): Saves the actual project, only asks for a file name and location if the project was not saved before.
4. **Save as…**: Saves the actual project, always asks for a file name and location.
5. **Close Window** (Ctrl+W): Closes the current active window
6. **Close Workspace** (Ctrl+Shift+W): Closes the open workspace with prior asking to save.
7. **Working directory…**: Change the working directory.
8. **Recent working dirs…**: Shows a list of previously used working directories to choose from.
9. **Workspace info…**\*: Opens the workspace info dialog, to both enter and review workspace information. Close with the 'Save + Close' button, or else changes will be lost.
10. **Print** (Ctrl+P): Prints the content of the 'Phase summary' window
11. **Settings**: Opens 'Settings' dialog (License management, user directory settings)
12. **Recent files …**: Shows a list of previously open script files to choose from.
13. **Recent workspaces …**: Shows a list of previously open workspace files to choose from.
14. **Exit** (Ctrl+Q): Closes MatCalc with prior asking to save.

2. Edit
-------

The following commands only work properly in a script file editor. All their functions are similar to other text editors!

[![ Edit section](/reference/menu/img/6101002_menu_edit.png " Edit section")](/reference/menu/img/6101002_menu_edit.png "reference/menu/img/6101002_menu_edit.png")

1. **Undo** (Ctrl+Z): Undo your last command.
2. **Redo** (Ctrl+Y): Redo your last command.
3. **Cut** (Ctrl+X): Copies and deletes a marked text.
4. **Copy** (Ctrl+C): Copies a marked text.
5. **Paste** (Ctrl+V): Pastes a previously copied or cut text to the cursor position.
6. **Find…** (Ctrl+F): Opens a dialog box to find a wanted string. Offers options to search 'case sensitive' (Upper and lower case letters are considered), 'match whole word' (whole word has to be found, not only a segment), 'look backwards' (Search backwards for the string).
7. **Find next** (Ctrl+G): Searches for the next string with the search parameters entered at the find dialog box.

3. Global
---------

[![ Global section](/reference/menu/img/6101002_menu_global.png " Global section")](/reference/menu/img/6101002_menu_global.png "reference/menu/img/6101002_menu_global.png")

1. **[Databases ...](/reference/dialogs/databases "reference/dialogs/databases")** (F5): Opens the 'Databases' dialog.
2. **[Composition ...](/reference/dialogs/composition "reference/dialogs/composition")** (F7): Opens the 'Composition' dialog.
3. **[Phase status ...](/reference/dialogs/phasestatus "reference/dialogs/phasestatus")** (F8): Opens the 'Phase status' dialog.
4. **[Precipitation domains ...](/reference/dialogs/precipitation "reference/dialogs/precipitation")** (Ctrl+F8): Opens the 'Precipitation domains' dialog.
5. **[Thermo-mech. treatments ...](/reference/dialogs/heattreatments "reference/dialogs/heattreatments")** (Alt+F8): Opens the 'Thermo-mechanical treatment' dialog.
6. **[CalcStates](/reference/menu/calcstates "reference/menu/calcstates")**: Offers a dropout menu to choose options from.
7. **[Buffers](/reference/menu/buffers "reference/menu/buffers")**: Offers a dropout menu to choose options from.
8. **[TTP-Buffer](/reference/menu/ttpbuffer "reference/menu/ttpbuffer")**: Offers a dropout menu to choose options from.
9. **[Tables and Arrays](/reference/dialogs/tables "reference/dialogs/tables")**: Opens the 'Tables and Arrays' dialog.
10. **[Transformations ...](/reference/dialogs/transformations "reference/dialogs/transformations")**: Opens the 'Transformations' dialog.
11. **Conditional commands**: Opens the 'Conditional commands' dialog
12. **[Variables & Functions](/reference/dialogs/variables "reference/dialogs/variables")** (F6): Opens the 'Variables & Functions' dialog.

4. Calc
-------

[![ Calc section](/reference/menu/img/6101002_menu_calc.png " Calc section")](/reference/menu/img/6101002_menu_calc.png "reference/menu/img/6101002_menu_calc.png")

1. **Set start values** (Ctrl+Shift+F): Sets automatic start values. All phases are set to their nominal composition according to major constituents. Good method to create a starting point.
2. **Apply tangent construction** (Ctrl+Shift+A): Applies parallel tangent construction to evaluate data for unstable phases.
3. **Equilibrium …** (Ctrl+E): Opens the 'Calculate equilibrium' dialog. Enter desired temperature to calculate equilbrium, use 'C ↔ K' to change values from Celsius to Kelvin. Pressure dialog box has no functionality so far.
4. **[Stepped calculation ...](/reference/dialogs/stepped "reference/dialogs/stepped")** (Ctrl+T): Opens the 'Stepped calculation' dialog.
5. **[Search phase boundary ...](/reference/dialogs/search "reference/dialogs/search")** (Ctrl+Shift+T): Opens the 'Search phase boundary' dialog.
6. **[Scheil calculation ...](/reference/dialogs/scheil "reference/dialogs/scheil")** (Ctrl+H): Opens the 'Scheil calculation' dialog.
7. **[Microstructure simulation ...](/reference/dialogs/preckinetics "reference/dialogs/preckinetics")** (Ctrl+K): Opens the 'Microstructure simulation' dialog.
8. **[TTP-diagram ...](/reference/dialogs/ttpdiagram "reference/dialogs/ttpdiagram")** (Ctrl+Alt+K): Opens the 'TTP-diagram' dialog.
9. **Calc nucleus compositions** (Ctrl+Shift+K): Calculates nucleus compositions for precipitate phase according to their respective model settings.
10. **Stop current action** (Esc): Stops the current calculation, simulation, …
11. **[Special](/reference/menu/special "reference/menu/special")**: Shows the special dropout menu.

5. Cells
--------

[![ Simulation section](/reference/menu/img/6101002_menu_cells.png " Simulation section")](/reference/menu/img/6101002_menu_cells.png "reference/menu/img/6101002_menu_cells.png")

1. **Grid …**: Functionality not implemented yet!
2. **Materials …**: Functionality not implemented yet!
3. **Cell properties …**: Functionality not implemented yet!
4. **Start simulation …** (Ctrl+J): Starts cells simulation.

6. Monte Carlo
--------------

[![ Monte Carlo section](/reference/menu/img/6101002_menu_monte.png " Monte Carlo section")](/reference/menu/img/6101002_menu_monte.png "reference/menu/img/6101002_menu_monte.png")

1. **Start simulation …** (Ctrl+R): Starts Monte Carlo simulation.

7. Script
---------

[![ Script section](/reference/menu/img/6101002_menu_script.png " Script section")](/reference/menu/img/6101002_menu_script.png "reference/menu/img/6101002_menu_script.png")

1. **Run script …** (Shift+F2): Opens the 'Run script' dialog. Specify path to run a specific script. Most recent run script will stay in the dialog box.
2. **Open template …**: Opens a file browser to the template folder of MatCalc.
3. **Examples**: Shows a dropout menu to the provided template script files with MatCalc 6 syntax.
4. **Examples\_5**: Shows a droput menu to the provided template script files with MatCalc 5 syntax.
5. **Python**: Shows a droput menu to the provided template script files in Python language
6. **User scripts**: Shows a dropout menu to templates and scripts, saved in the 'script\_menu' folder stored in the user data directory.

8. View
-------

[![ View section](/reference/menu/img/6101002_menu_view.png " View section")](/reference/menu/img/6101002_menu_view.png "reference/menu/img/6101002_menu_view.png")

1. **Show**: Shows a dropout menu to toggle various GUI function windows (Console, Options, Variables, Nodes).
2. **Select window font …**: Opens a dialog window to change font, size and other font related settings.
3. **Select application style …**: Choose the style sheet for MatCalc which fits you the most.
4. **Create new window …** (Ctrl+M): Opens the create new window dialog, with a great variety of plot types to choose from.
5. **Create new user defined window** (Ctrl+Shift+M): Opens a dialog window with pre-defined and user-definable plots to choose from.
6. **Display window IDs**: Toggle to show/hide the window IDs in the title bar.
7. **Restore window positions** (Alt+Shift+R): Restore the position of MatCalc, console, options and variables window.
8. **Edit series data …** (Ctrl+D): Choose a plot and manually edit the data of a series.
9. **[Series](/reference/menu/series "reference/menu/series")**: Select a plot an choose one of various functions.
10. **Completer**: Shows a dropout menu to enable/disable the completer. Further the style for commands can be changed: Uppercase/Lowercase letters and Underline/Minus.
11. **Update all window contents** (Ctrl+U): Manually update all windows.
12. **Update current window contents** (Ctrl+Shift+U): Manually update the window in focus.
13. **Freeze update** (Ctrl+I): Stop updating a window.
14. **Windows …**: Shows a dropout menu with all open windows. Clicking it brings it on top.

9. Help
-------

[![ Help section](/reference/menu/img/6101002_menu_help.png " Help section")](/reference/menu/img/6101002_menu_help.png "reference/menu/img/6101002_menu_help.png")

1. **Documentation**: Opens the MatCalc documentation site in the web browser.
2. **Version Info**: Opens the MatCalc version information site in the web browser.
3. **Software Updates**: Functionality not implemented yet!
4. **About**: Opens a message dialog with information on the installed MatCalc version and licenses.
5. **Report a problem / suggest a feature**: Opens the window allowing message & file submission to Support service

![](/wiki/lib/exe/taskrunner.php?id=reference%3Amenu&1788352868)