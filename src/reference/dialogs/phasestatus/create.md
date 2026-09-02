Create new phase [MatCalc Documentation]



### Create new phase

[![ Create new phase](/reference/dialogs/img/phasestatus/phase_status-f8-general-create_new_phase.png " Create new phase")](/reference/dialogs/img/phasestatus/phase_status-f8-general-create_new_phase.png "reference/dialogs/img/phasestatus/phase_status-f8-general-create_new_phase.png")

* *Equilibrium*: Creates an equilibrium phase with the same constituents and major constituents as its parent phase, denoted as \*#01, \*#02, …   

  ```
  create-new-phase fcc_a1 e   $ FCC_A1 is parent phase
  ```
* *Precipitate* (\_Pnn): Creates a precipitate phase with the same constituents and major constituents as its parent phase, denoted as \_p0, \_p1, …   

  ```
  create-new-phase fcc_a1 p
  ```
* *Composition Set*: Creates a composition set with the thermodynamic data of its parent phase. Constituents, major constituents and name can be freely chosen.   

  ```
  create-new-phase fcc_a1 c :Nb%,V:C%,N: NbC   
  $ FCC_A1 is parent phase, c is composition set,
  $ :First-sublattice:Second-sublattice: % represents major constituents
  $ Name of new phase
  ```
* *Transformation-equilib (\_S)*: Creates a transformation-equilibrium phase, which is needed for Scheil-Guliver calculations. Can also be created 'on-the-fly' from the Scheil calculation dialog box.   

  ```
  create-new-phase fcc_a1 s
  ```

![](/wiki/lib/exe/taskrunner.php?id=reference%3Adialogs%3Aphasestatus%3Acreate&1788353212)