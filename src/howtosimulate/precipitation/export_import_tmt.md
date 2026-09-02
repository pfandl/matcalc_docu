Exporting/importing thermo-mechanical treatments [MatCalc Documentation]



### Table of Contents

* [Exporting/importing thermo-mechanical treatments](#exporting_importing_thermo-mechanical_treatments)

  + [Compatibility](#compatibility)
  + [Objectives](#objectives)
  + [Related documents](#related_documents)
* [Main document](#main_document)

  + [Export a TMT](#export_a_tmt)
  + [Import a TMT](#import_a_tmt)
  + [Preparation of the file for TMT import](#preparation_of_the_file_for_tmt_import)

Exporting/importing thermo-mechanical treatments
================================================

Compatibility
-------------

MatCalc version: 6.02 - …   
Author: P. Warczok   
Created: 2020-04-15   
Revisions:

Objectives
----------

In this document, the procedures for exporting and importing the thermo-mechanical treatments (commonly abbreviated as “TMT” in MatCalc) using a text file is described. Additionally, the preparation of the text file for an import of the custom treatment is demonstrated.

Related documents
-----------------

1. [Thermo-mechanical treatment file structure](/matcalc_docu/reference/tmt_file "reference:tmt_file")

Main document
=============

While GUI editor or console/script commands allow for convenient and neat definition of the simulated thermo-mechanical cycle, its application meets the limits for treatments containing many segments. Moreover, it is not straightforward to automate the input process through these means. To overcome these problems, the export/import functionality of the treatments via a text file was introduced.

Export a TMT
------------

Thermo-mechanical treatments can be stored in a text file. This file is created by MatCalc

* in GUI editor (menu “Global” → “Thermo-mech. treatments”), by selecting the relevant treatment in “available ™ treatments” list, clicking on “Write” button and defining the file name and destination directory.
* in console/script, with “export-tm-treatment tm-treatment-name= export-file-name=“ command. If “export-file-name” contains only the filename (without a specific path), the file will be exported into the current working directory.

Import a TMT
------------

The text files can be imported into the thermomechanical treatments:

* in GUI editor (menu “Global” → “Thermo-mech. treatments”), by clicking on “Read” button and selecting the relevant file
* in console/script, with “import-tm-treatment import-file-name=“ command. If “import-file-name” contains only the filename (without a specific path), MatCalc will look for the file in the current working directory.

Preparation of the file for TMT import
--------------------------------------

The file describing the thermo-mechanical treatment needs to have a specific structure in order to be recognised by MatCalc. An overview of this structure is discussed  [here](/matcalc_docu/reference/tmt_file "reference:tmt_file")  and can be easily experienced when a treatment defined with GUI editor or script/console commands is exported into the text file. One can notice that such a file contains a comprehensive parameter definition range. The treatment data that the user would like to import need not to contain that amount of information. Still, some structure features must be kept. Let us demonstrate it on a simple example.

The starting point is the data describing the bloom cooling stored at room temperature given in the table below.

| Time [h] | Temperature [°C] |
| --- | --- |
| 0 | 1400 |
| 1 | 1280 |
| 2 | 1170 |
| 3 | 1070 |
| 4 | 980 |
| 5 | 900 |
| 6 | 830 |
| 7 | 760 |
| 8 | 690 |
| 9 | 640 |
| 10 | 580 |
| 11 | 540 |
| 12 | 490 |
| 13 | 450 |
| 14 | 420 |
| 15 | 380 |
| 16 | 350 |
| 17 | 320 |
| 18 | 300 |
| 19 | 270 |
| 20 | 250 |
| 21 | 230 |
| 22 | 210 |
| 23 | 200 |
| 24 | 180 |

These two columns would be the content of **'Data'** section. Still, two modifications will be performed. The first one is just the removal of the very first line, as it contains only the information on the start temperature - this will be provided later on. The second modification is the multiplication by 3600, as MatCalc interprets the time in seconds, while the provided data was given in hours.

```
[data]
1*60*60 1280
2*60*60 1170
3*60*60 1070
4*60*60 980
5*60*60 900
6*60*60 830
7*60*60 760
8*60*60 690
9*60*60 640
10*60*60 580
11*60*60 540
12*60*60 490
13*60*60 450
14*60*60 420
15*60*60 380
16*60*60 350
17*60*60 320
18*60*60 300
19*60*60 270
20*60*60 250
21*60*60 230
22*60*60 210
23*60*60 200
24*60*60 180
[/data]
```

Now, it is necessary to explain MatCalc the meaning of the columns. This is done, as follows:

```
[format]
column=absolute_time
column=end_temperature
[/format]
```

In the **'Variables'** section, the mandatory entry about the segment code needs to be given. Value of **'3'** is taken here, so that MatCalc looks for segment end temperature and duration time. Although, the segment duration times are not provided in **'data'** section, MatCalc is smart enough to figure these out from the 'absolute time' column.

```
[variables]
segment-code=3
[/variables]
```

At last, the information about the tmt start temperature and the name is specified.

```
[global]
tmt-name=Cooling
start-temperature=1400
[/global]
```

One could add some comments to the file for an easier comprehension for the reader. Any such line shall start with a dollar-sign (**'$'**). Of course, the comments are not mandatory.

The complete file describing the above cooling curve that can be imported to MatCalc has the following content:

```
$ Below are the temperature-time data to be imported.
$ Time is given in hours here so every time record has to be multiplied
$ by 3600 so that MatCalc recognizes it properly (MatCalc operates with seconds)
[data]
1*60*60 1280
2*60*60 1170
3*60*60 1070
4*60*60 980
5*60*60 900
6*60*60 830
7*60*60 760
8*60*60 690
9*60*60 640
10*60*60 580
11*60*60 540
12*60*60 490
13*60*60 450
14*60*60 420
15*60*60 380
16*60*60 350
17*60*60 320
18*60*60 300
19*60*60 270
20*60*60 250
21*60*60 230
22*60*60 210
23*60*60 200
24*60*60 180
[/data]
$ Interpretation of the columns is given below (the first column is absolute time,
$ the second one is the end temperature of the segment)
[format]
column=absolute-time
column=end-temperature
[/format]

$ Definition of tmt name and tmt start temperature
[global]
tmt-name=cooling
start-temperature=1400
[/global]

$ Definition of default segment-code is mandatory
$ In this case, the value of "3" is set
$ (MatCalc looks for segment end temperature and duration time)
$ (Duration time is calculated from "absolute time" column)
[variables]
segment-code=3
[/variables]
```

![](/wiki/lib/exe/taskrunner.php?id=howtosimulate%3Aprecipitation%3Aexport_import_tmt&1788352863)