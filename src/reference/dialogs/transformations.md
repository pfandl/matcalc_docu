Transformations [MatCalc Documentation]



Transformations
---------------

The transformation dialog can be used to create 'solid transformations'. These represent recipes for how one phase in a *MatCalc* simulation ought to be transformed into another one. Typical application of transformations are the transformation of delta-ferrite into austenite in the Scheil simulation of peritectic reactions in steel (see, e.g., example *E20-3* -  [Accounting for the peritectic reaction](/examples/equilib/e20/e20_3 "examples/equilib/e20/e20_3")), or the transformation of one matrix phase into another one when evaluating the heat capacity of systems during DSC experiments.

A transformation is typically applied to phases which have *dormant* phase status. The transformation can occur according to different strategies

* The standard **full equilibrium** or **constrained (para-) equilibrium** condition is used to determine the phase fractions as a result of an equilibrium simulation. This is the common selection when using transformations in Scheil-Gulliver simulations.
* Alternatively, the transformation can be performed according to an **Avrami equation** with parameters $n$ and $k$. The transformed fraction $f$ is evaluated from the equation   
  \[ f = 1-exp(-kx^n) \]   
  The limits of the transformation are defined by the transformation start and end temperature.
* For martensitic transformations, the Koistinen-Marburger equation can be used also. The transformation is then evaluated from   
  \[ f=1-exp(-n(M\_s-T))\]   
  The limits of the transformation are given by the transformation start temperature, which is interpreted as the martensite start temperature $M\_s$. The end temperature is not used in the Koistinen-Marburger equation.
* For highest flexibility, the transformation progress can also be defined in terms of a table, where the phase fraction of the product phase is given in terms of X/Y pairs between the limits of the transformation start and end temperature.

Below, the dialog options are described in more detail.

[![ Transformations](/reference/dialogs/img/transformations/transformations.png " Transformations")](/reference/dialogs/img/transformations/transformations.png "reference/dialogs/img/transformations/transformations.png")

1. **Create new transformation**: Create a new transformation object.
2. **Remove**: remove existing transformation.
3. **Rename**: rename existing transformation.
4. **Transform From**: A transformation always involves one phase which will be transformed into another. This selection defines the parent phase.
5. **Transform To**: Product phase, into which the parent phase will be transformed.
6. **Transformation equilibrium phase**: When using the transformation options *full equilibrium* and *constrained equilibrium*, an equilibrium phase must be created that is used to evaluate the transformed fraction. This phase can be created automatically by using the *Create transformation equilibrium phase* button.
7. **Create transformation equilibrium phase**: Creates a transformation phase with the suffix '\_T' and a transformation solid phase with the suffix '\_TS'.
8. **Maximum phase fraction**: Usually, the transformation converts the entire parent phase into a product phase. With this setting, the total transformed fraction can be limited to a smaller value.
9. **Status**: When selecting 'active', the transformation will be applied in the next simulation.
10. **Full equilibrium**: The full, unconstrained equilibrium simulation will be used to evaluate the transformed fraction.
11. **Constrained equilibrium**: Para-equilibrium will be used to evaluate the transformed fraction.
12. **Avrami type**: Selection of this option activates the Avrami equation for controlling the transformation progress.
13. **n-factor for Avrami type**: $n$ value in Avrami equation.
14. **k-factor for Avrami type**: $k$ value in Avrami equation.
15. **Koistinen-Marburger type**: Selection of this option activates the Koistinen-Marburger equation for controlling the transformation progress.
16. **n-factor for Koistinen-Marburger type**: $n$ value in Avrami equation.
17. **Manual ratio**: Use a table to control the transformation progress.
18. **data from table**: Corresponding table name.
19. **Start temperature**: Apply transformation only below the start temperature.
20. **Stop temperature**: Finish transformation at the stop temperature.
21. **Temperature in Celsius**: C ↔ K.

![](/wiki/lib/exe/taskrunner.php?id=reference%3Adialogs%3Atransformations&1788353003)