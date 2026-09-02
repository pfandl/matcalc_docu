TechPaper #2011005: MatCalc software architecture [MatCalc Documentation]



### Table of Contents

* [TechPaper #2011005: MatCalc software architecture](#techpaper_2011005matcalc_software_architecture)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Programming environment](#programming_environment)
  + [Software architecture](#software_architecture)

    - [User interface](#user_interface)

TechPaper #2011005: MatCalc software architecture
=================================================

Compatibility
-------------

MatCalc version: 5.0 - …   
Author: E. Kozeschnik   
Created: 2011-07-05   
Revisions:

Objectives
----------

This paper provides information on the internal software architecture of *MatCalc*, the interconnection between the modules and possibilities for linking with external code.

Related documents
-----------------

None

Main document
=============

Programming environment
-----------------------

The *MatCalc* software is written in C++. It is developed within the [MS Visual Studio](http///en.wikipedia.org/wiki/Visual_studio "http///en.wikipedia.org/wiki/Visual_studio") environment (Windows platform) and the [Qt Creator](http///en.wikipedia.org/wiki/Qt_Creator "http///en.wikipedia.org/wiki/Qt_Creator") environment (Mac OSX and Linux).

The window management of the *MatCalc* GUI version, as well as the platform-independent streaming operations of GUI (mcg) and command-line version (mcc), are handled by the ([Qt Developer Framework](http///en.wikipedia.org/wiki/Qt_(framework) "http://en.wikipedia.org/wiki/Qt_(framework)")).

Graphical output of diagrams / plots is realized with the [Qwt graphics library](http///qwt.sourceforge.net/Qwt library "http///qwt.sourceforge.net/Qwt library"). Output of Monte Carlo simulation states is done using the OpenGL language implementation within the Qt libraries.

Software architecture
---------------------

The *MatCalc* package is designed in the form of modules, with a strict separation between the user interfaces and the core modules. This is sketched in the following diagram.

[![  Software architecture of //MatCalc//](/techpapers/software/img/matcalc_structure.png "  Software architecture of //MatCalc//")](/techpapers/software/img/matcalc_structure.png "techpapers/software/img/matcalc_structure.png")

### User interface

The *MatCalc* package provides two front ends to the user to control the software behavior.

* The *MatCalc* GUI software **mcg**. This front end is fully visual and allows for pre-processing, simulation as well as post processing. The GUI version stores all information in **workspace** files with the file extension '\*.mcw'.
* The command-line interface **mcc**. This front end has all the features of the GUI version, except for graphical post-processing and window management. Results are stored in **binary files** with a file extension of '\*.mcb'. The GUI version can also process (open, read and write) binary files.

Both file versions (mcg and mcc) are delivered with the software package. Typically, the GUI version is used by most users for routine calculations because you can setup simulations and evaluate the results in one program. The command-line implementation of *MatCalc* is ideal for batch processing of lengthy simulations, where you can start the simulations on some server, run the jobs in the background and evaluate the results later with 'mcg'.

*MatCalc* also provides several features for exporting data to external software. See the corresponding article [techpapers:software:export | Exporting for external post-processing]].

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Asoftware%3Aarchitecture&1788353009)