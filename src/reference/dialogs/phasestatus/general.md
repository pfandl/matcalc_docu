General [MatCalc Documentation]



General
-------

[![ General](/matcalc_docu/reference/dialogs/img/phasestatus/phase_status-f8-general.png " General")](/matcalc_docu/reference/dialogs/img/phasestatus/phase_status-f8-general.png "reference:dialogs:img:phasestatus:phase_status-f8-general.png")

1. **Flags**: Represent the properties of phases

   * *active*: Phase has a mole fraction greater 0.
   * *fixed phase fraction*: phase fraction is fixed and will not change during calculation.
   * *dormant*: Fixes phase fraction and chemical composition. Still contributes to calculations.
   * *suspended*: Phase will not be considered in further calculations. Phase fraction is set to 0.
   * *matrix phase*: Phase is matrix phase
   * *enforce major constituents*: Major constituents are enforced (e.g.: Use this if carbides-nitrides are mixed up.)
   * *magnetic contribution*: Magnetic contribution on the thermodynamics is considered
   * *dispersed (diffusion)*:
   * *GBB variables without magnetic contribution*:
2. **fixed phase u-fraction**: Phase has a fixed u-fraction.
3. **value for fixed phase u-fraction**: Value for fixed u-fraction.
4. **Display for mole fraction of phase**: Shows the current value of phase fraction for selected phase.
5. **Set amount of mole fraction of phase**: Set the mole fraction of selected phase manually.
6. **Adjust Reference phase**:
7. **Set as Reference phase**:
8. **Normalize all**:
9. **Display for constituents**: Displays all constituents of the selected phase. Sub-Lattices are separated by colons (:).
10. **Major constituents**: Both display and dialog box to manually set the major constituents. Sub-Lattices are separated by colons. Press 'Set now' to save the major constituents. In the dialog box that opens, choose between resetting and initializing the phase now, or do it later manually. DO NOT forget to set the major constituents, or else any changes made will be lost!

![](/wiki/lib/exe/taskrunner.php?id=reference%3Adialogs%3Aphasestatus%3Ageneral&1788353212)