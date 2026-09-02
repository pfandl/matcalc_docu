Structure [MatCalc Documentation]



Structure
---------

[![ Structure](/reference/dialogs/img/phasestatus/phase_status-f8-structure.png " Structure")](/reference/dialogs/img/phasestatus/phase_status-f8-structure.png "reference/dialogs/img/phasestatus/phase_status-f8-structure.png")

1. **Young's modulus**:

   ```
   SET_PRECIPITATION_PARAMETER fcc_a1_p0 T E
   ```
2. **Poisson's ratio**:

   ```
   SET_PRECIPITATION_PARAMETER fcc_a1_p0 T R
   ```
3. **Anti-Phase-Boundary energy**:

   ```
   SET_PRECIPITATION_PARAMETER fcc_a1_p0 T A
   SET_PRECIPITATION_PARAMETER fcc_a1_p0 T Y P $ Pair dislocations
   SET_PRECIPITATION_PARAMETER fcc_a1_p0 T Y S $ Single dislocations
   ```
4. **Volumetric misfit**:

   ```
   SET_PRECIPITATION_PARAMETER fcc_a1_p0 T M
   $ (Y)es for automatic / (N)o for manual values
   ```
5. **Burger's vector**:

   ```
   SET_PRECIPITATION_PARAMETER fcc_a1_p0 T B
   $ (Y)es for automatic / (N)o for manual values
   ```
6. **Coherency radius**:

   ```
   SET_PRECIPITATION_PARAMETER fcc_a1_p0 T O
   $ (Y)es for automatic / (N)o for manual values
   ```
7. **Shearable radius**:

   ```
   $ no command
   ```
8. **Ignore for precipitation strengthening**:

   ```
   SET_PRECIPITATION_PARAMETER fcc_a1_p0 T S I
   ```
9. **C (Ashby-Orowan)**:

   ```
   SET_PRECIPITATION_PARAMETER fcc_a1_p0 T S 1
   ```
10. **C' (dislocation line tension)**:

    ```
    SET_PRECIPITATION_PARAMETER fcc_a1_p0 T S 2
    ```
11. **C'' (modulus strengthening)**:

    ```
    SET_PRECIPITATION_PARAMETER fcc_a1_p0 T S 3
    ```
12. **Modulus strengthening: m**:

    ```
    SET_PRECIPITATION_PARAMETER fcc_a1_p0 T S M
    ```
13. **Alpha value of coupling of strength contributions**:

    ```
    SET_PRECIPITATION_PARAMETER fcc_a1_p0 T S A
    ```
14. **Beta value of coupling of strength contributions**:

    ```
    SET_PRECIPITATION_PARAMETER fcc_a1_p0 T S B
    ```

![](/wiki/lib/exe/taskrunner.php?id=reference%3Adialogs%3Aphasestatus%3Astructure&1788353213)