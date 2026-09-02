Nucleation [MatCalc Documentation]



Nucleation
----------

This tab contains all options in relation to the nucleation of precipitates.

[![ Nucleation](/reference/dialogs/img/phasestatus/phase_status-f8-nucleation.png " Nucleation")](/reference/dialogs/img/phasestatus/phase_status-f8-nucleation.png "reference/dialogs/img/phasestatus/phase_status-f8-nucleation.png")

1. **[Nucleation model:](/reference/dialogs/phasestatus/nucleation/model "reference/dialogs/phasestatus/nucleation/model")** [1)](#fn__1) Choose the nucleation model from the dropdown box.
2. **[Nucleus composition:](/reference/dialogs/phasestatus/nucleation/composition "reference/dialogs/phasestatus/nucleation/composition")** [2)](#fn__2) Choose the nucleus composition from the dropdown box.
3. **Nucleation constant**: [3)](#fn__3)
4. **Incubation time constant**: [4)](#fn__4)
5. **Minimum precipitation radius**: [5)](#fn__5)
6. **Account for coherent misfit stress**: [6)](#fn__6)
7. **Account for excess vacancy contribution**: [7)](#fn__7)
8. **Take into account shape factor**: [8)](#fn__8)
9. **Nucleate only with valid major constituents**: [9)](#fn__9)
10. **Restrict nucleation to precipitation domain**: [10)](#fn__10)
11. **Nucleation sites**: [11)](#fn__11)

    * *bulk (homogenous)*: Parameter - b.
    * *dislocations*: Parameter - d
    * *grain boundary (diff. geometry!)*: Parameter - g
    * *grain boundary edge*: Parameter - e
    * *grain boundary corner*: Parameter - c
    * *subgrain boundary*: Parameter - s
    * *subgrain boundary edge*: Parameter - m
    * *subgrain boundary corner*: Parameter - x
12. **Other precipitates**: Settings for other precipitates.
13. **Add**: [12)](#fn__12) other precipitates.
14. **Remove**: [13)](#fn__13) other precipitates.
15. **Nucleate at precipitate surface**: [14)](#fn__14)
16. **Equivalent interface energy**: [15)](#fn__15)
17. **Minimum transformation radius**: [16)](#fn__16)
18. **Maximum transformation radius**: [17)](#fn__17)
19. **Inherit parent composition**: [18)](#fn__18)

[1)](#fnt__1)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N N

[2)](#fnt__2)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N C

[3)](#fnt__3)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N U

[4)](#fnt__4)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N T

[5)](#fnt__5)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N D

[6)](#fnt__6)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N F

[7)](#fnt__7)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N V

[8)](#fnt__8)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N H

[9)](#fnt__9)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N J

[10)](#fnt__10)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N P Y virtual $ Y - Yes, virtual - domain name

[11)](#fnt__11)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N S $ Find site parameters below

[12)](#fnt__12)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N S P fcc\_a1 bcc\_a2 $ Write all phases at the end to add them

[13)](#fnt__13)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N S P
$ Write a blank space at the end to remove all phases

[14)](#fnt__14)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N O S

[15)](#fnt__15)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N O E

[16)](#fnt__16)
, [17)](#fnt__17)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N O R min max

[18)](#fnt__18)

SET\_PRECIPITATION\_PARAMETER fcc\_a1\_p0 N O I

![](/wiki/lib/exe/taskrunner.php?id=reference%3Adialogs%3Aphasestatus%3Anucleation&1788353213)