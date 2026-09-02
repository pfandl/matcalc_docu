TechPaper #2011006: Linking MatCalc with third-party software [MatCalc Documentation]



### Table of Contents

* [TechPaper #2011006: Linking MatCalc with third-party software](#techpaper_2011006linking_matcalc_with_third-party_software)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [MATLAB](#matlab)

    - [Choosing the right libraries](#choosing_the_right_libraries)
    - [Using the mex-compiled version](#using_the_mex-compiled_version)
    - [Using the MatCalc shared libraries directly](#using_the_matcalc_shared_libraries_directly)
  + [Mathematica](#mathematica)

    - [Preparations](#preparations)
    - [Installing the port](#installing_the_port)
    - [Using the port](#using_the_port)
    - [Example](#example)
  + [External links](#external_links)

    - [MATLAB](#matlab1)
    - [Mathematica](#mathematica1)

TechPaper #2011006: Linking MatCalc with third-party software
=============================================================

Compatibility
-------------

MatCalc version: 5.43 - …   
Author: Y. Shan   
Created: 2011-08-24   
Revisions: 2017-03-21, updated MATLAB port for MatCalc 6

Objectives
----------

This paper provides information on using *MatCalc* libraries with third-party softwares such as *MATLAB*, *Mathematica*,…

Related documents
-----------------

None

Main document
=============

MATLAB
------

### Choosing the right libraries

First of all, make sure which **MATLAB architecture** is used (whether **32-bit** or **64-bit**). This can be seen on the *About MATLAB* page. The libraries used must be the **same** as the MATLAB architecture!

Furthermore there will be **shared libraries** and **static libraries** depending on the method chosen. The library extensions are as followed:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Windows** | **Mac** | **Linux** |
| shared | \*.dll | \*.dylib | \*.so |
| static | \*.lib | \*.a | \*.lib |

### Using the mex-compiled version

#### Compiling in MatCalc 5

For this method you **need**:

For compiling:

1. the mex-source files from *MatCalc*: **mc.h** and **mc.cpp**
2. the static **mc\_core** library
3. the static QtCore and QtGui libraries (**QtGui4.**\* and **QtCore4.**\*)

For using the compiled binary:

1. the compiled binary (more details below)
2. the shared QtCore and QtGui libraries

Note: you can skip the compiling step if you already possess a compiled mex binary, but this can lead to problems on *MATLAB* versions other than the version which the binary has been compiled on.

For compiling you need a C-compiler. If you don't already have one you can use the [GCC 4.3 compiler](http://ftp.gnu.org/gnu/gcc/ "http://ftp.gnu.org/gnu/gcc/")(warning: MATLAB does **not support** higher gcc compiler) or find one from this [list](http://www.mathworks.com/support/compilers/previous_releases.html "http://www.mathworks.com/support/compilers/previous_releases.html"). To compile the *MatCalc* mex-files make sure that you have all files in the current working dir on *MATLAB* and type

Windows,Linux:

```
mex mc.cpp mc_core.lib QtCore4.lib QtGui4.lib
```

Mac:

```
mex mc.cpp mc_core.a QtCore4.a QtGui4.a
```

This should generate a mc-mex binary for your system which you can use like a normal MATLAB function. Depending on your system it can have following extensions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Windows** | **Mac(Intel)** | **Linux** |
| 32bit | mc.mexw32 | mc.mexmaci | mc.mexglx |
| 64bit | mc.mexw64 | mc.mexmaci64 | mc.mexa64 |

Note: Older *MATLAB* versions only use the \*.mex extension.

#### Compiling in MatCalc 6

In Matlab find the folder, in which MatCalc 6 is installed, and browse to /external/matlab. Here you can find the two files **mc.cpp** and **mc.h**. Type

```
mex mc.cpp ../../libmc_core.a
```

Note: You may need administrator rights in Matlab for generating the mex file. Alternatively you can move the 3 files (**mc.cpp**,**mc.h** and **libmc\_core.a**) into a seperate folder and compile there.

#### Using the compiled mex binary

The mex binary can be used like a normal ***MATLAB* function** which takes one ***input\_string*** and returns a ***result***:

```
 [result] = mc(input_string)
```

The *input\_string* is a ***MatCalc* command** which you would also use in the console in *MatCalc*. The *result* is a number indicating errors. If *result* is 0 everything was ok (see MCM\_ERRORS… (missing link)).

You don't have to type the options or parameters of a command. If not given, *MATLAB* will ask for the necessary input in a same manner as in the console version of *MatCalc*.

You can **access *MatCalc* variables** with the command

```
 my_variable = mc(1,'variable_name');
```

which stores the *MatCalc* *variable\_name* (e.g. F$\*, T,…) into *my\_variable*.

For example if you want to run your script in *MATLAB* just wrap every line of your script with a mc('…').

Note: the GUI commands of *MatCalc* are disabled.

Note2: if you run the mex file from a different folder than the standard MatCalc installation folder, you have to specify the MatCalc folder in order to read your license, databases, etc. properly. To do this, use the `SET_APPLICATION_DIRECTORY` command.

##### Example for a simple \*.m script

```
% this is a simple MATLAB script demonstrating the usage of the MatCalc mex binary

mc('USE_MODULE core')                                       % switch module to core

mc('OPEN_THERMODYN_DATABASE mc_sample_fe.tdb')              % open the steel database
mc('SELECT_ELEMENTS C FE VA')                               % select elements
mc('SELECT_PHASES BCC_A2 CEMENTITE FCC_A1 GRAPHITE LIQUID') % select phases
mc('READ_THERMODYN_DATABASE')                               % read the database

mc('ENTER_COMPOSITION wp C=0.4')                            % set the composition

mc('SET_TEMPERATURE_CELSIUS 700')                           % set the temperature
mc('SET_AUTOMATIC_STARTVALUES')                             % and
mc('CALCULATE_EQUILIBRIUM')                                 % calculate equilibrium

mc('SET_STEP_OPTION R 400 1600 L 25')                       % define step parameters
mc('STEP_EQUILIBRIUM')                                      % and do step calculation

% get phase data
i = 0;                                                      % iterator for buffer data
while (mc(['LOAD_BUFFER_STATE ' int2str(i)]) == 0)          % iterate until buffer end
    i = i+1;                                                % increase iterator
    T(i) = mc(1,'T');                                       % get data...
    F_LIQ(i) = mc(1,'F$LIQUID');
    F_FCC(i) = mc(1,'F$FCC_A1');
    F_BCC(i) = mc(1,'F$BCC_A2');
    F_CEM(i) = mc(1,'F$CEMENTITE');
    F_GRA(i) = mc(1,'F$GRAPHITE');
end

% plot in MATLAB
plot(T,F_LIQ,T,F_FCC,T,F_BCC,T,F_CEM,T,F_GRA)
legend('F$LIQUID','F$FCC_A1','F$BCC_A2','F$CEMENTITE','F$GRAPHITE')
```

[![](/matcalc_docu/techpapers/software/img/mex-test.png)](/wiki/lib/exe/detail.php?id=techpapers%3Asoftware%3Alink_external&media=techpapers/software/img/mex-test.png "techpapers:software:img:mex-test.png")

### Using the MatCalc shared libraries directly

For this method you **need**:

1. the shared *MatCalc* and QtGui,QtCore (only in MatCalc 5) libraries
2. a header file containing the functions you want to use (in MatCalc 6 found in /external/api)

To load the shared library into *MATLAB* simply use

```
loadlibrary('mc_core.dll','my_header.h')
```

To call a function use

```
calllib('mc_core','function_name',input parameters...)
```

for example:

```
calllib('mc_core','MCC_InitializeKernelPath','./')
```

Mathematica
-----------

### Preparations

Before using the MatCalc port for Mathematica, you should make sure, that you have a Mathematica with working MathLink installed. The port for mathematica can be found in the installation dir of MatCalc and is called **mc\_command.exe**.

### Installing the port

Start Mathematica and set the working directory to the MatCalc installation dir. Alternatively you can copy the **mc\_command.exe** in a folder of your choice and set the directory to this folder instead. If you have installed Matcalc in **C:/Program Files/MatCalc** then the command in Mathematica is

```
 SetDirectory["C:/Program Files/MatCalc"]
```

The next step is to install the MatCalc port. This is done with

```
 link = Install["mc_command.exe"]
```

A command prompt should now pop up, which is the output window for MatCalc. If you close this, the link is automatically separated and you have to install MatCalc again.

To uninstall the MatCalc port use

```
 Uninstall[link]
```

### Using the port

The MatCalc port comes with three functions:

|  |  |
| --- | --- |
| MCInit[path] | Initializes MatCalc in 'path' |
| MCCommand[command] | Process 'command' as a MatCalc console command |
| MCGetVariable[variable] | Returns the current value of 'variable' |

You should always call the **MCInit** function before using the other functions. This initializes MatCalc in the given 'path', reads the license in 'path' and also the preset defaults located in 'path'/preset (if you use your standard MatCalc installation dir everything should be ok). This function only needs to be run once.

Now you can use **MCCommand** to process the standard MatCalc commands as in the console, like calling scripts or setting up a simulation. For example

```
 MCCommand["run-script-file ./scripts/script_menu/templates/miscellaneous/file_export/file_export.mcs"]
```

To get MatCalc variables, use the **MCGetVariable** function, e.g.

```
 temperature = MCGetVariable["T"]
```

Note: The output of **MCInit**, **MCReadLicense** and **MCCommand** is an integer indicating the result of the process. If the integer is zero an error occured.

### Example

The following example shows how to install the MatCalc port, run the file\_export script and extracting variables into Mathematica

```
SetDirectory["C:/Program Files/MatCalc"]
link = Install["mc_command.exe"]
MCInit["/."]
MCCommand["run-script-file ./scripts/script_menu/templates/miscellaneous/file_export/file_export.mcs"]
temperature = MCGetVariable["T"]
phase_fraction_cementite = MCGetVariable["F$CEM"]
```

External links
--------------

### MATLAB

1. [MATLAB homepage](http://www.mathworks.com/products/matlab/ "http://www.mathworks.com/products/matlab/")
2. [MATLAB documentation for external interfaces](http://www.mathworks.com/help/pdf_doc/matlab/apiext.pdf "http://www.mathworks.com/help/pdf_doc/matlab/apiext.pdf")
3. [Information about supported and compatible compilers](http://www.mathworks.com/support/compilers/previous_releases.html "http://www.mathworks.com/support/compilers/previous_releases.html")
4. [Guide for setting up gcc compiler 4.3 for ubuntu](https://help.ubuntu.com/community/MATLAB#MEX_functions "https://help.ubuntu.com/community/MATLAB#MEX_functions")

### Mathematica

1. [Mathematica homepage](http://www.wolfram.com/mathematica/ "http://www.wolfram.com/mathematica/")
2. [Mathematica documentation for MathLink](http://reference.wolfram.com/mathematica/tutorial/MathLinkAndExternalProgramCommunicationOverview.html "http://reference.wolfram.com/mathematica/tutorial/MathLinkAndExternalProgramCommunicationOverview.html")

![](/wiki/lib/exe/taskrunner.php?id=techpapers%3Asoftware%3Alink_external&1788353010)