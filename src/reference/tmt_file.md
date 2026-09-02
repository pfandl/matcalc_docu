Thermo-mechanical treatment file structure [MatCalc Documentation]



### Table of Contents

* [Thermo-mechanical treatment file structure](#thermo-mechanical_treatment_file_structure)

  + ['Data' section](#data_section)
  + ['Format' section](#format_section)
  + ['Variables' section](#variables_section)
  + ['Global' section](#global_section)
  + [Comments](#comments)
  + [Example](#example)

Thermo-mechanical treatment file structure
==========================================

MatCalc has the functionality of exporting and importing the thermo-mechanical treatments via a text file. This file has a specific structure and consists of the following sections:

* **'Data'** section
* **'Format'** section
* **'Variables'** section
* **'Global'** section

The features of these sections are discussed below:

'Data' section
--------------

This section consist of lines, with each line consisting of a bunch of separated number/text values. Each line corresponds to a single segment. The order of the lines corresponds to the segment order, i.e. the first line describes the first segment, the second line describes the second segment, etc. Each value corresponds to a specific parameter, as described in **'Format'** section. Alternatively, one could describe this section as a bunch of separated columns, each column consisting of number/text values. Each column describes the evolution of the given parameter (defined in **'Format'** section) through the subsequent segments. This section is delimited with **'*[data]*'** and **'*[/data]*'** tags.

'Format' section
----------------

This section consists of the list of parameters defined in **'Data'** section. It allows MatCalc to interpret and address the values given there. It means that the number of lines (each starting with **'*column=*'** string) should match the number of parameters defined in each line of **'Data'** section. In other words, the number of lines in **'Format'** section should match the number of columns in **'Data'** section. Furthermore, the order of the lines in **'Format'** section should correspond with the order the columns in the **'Data'** section, as it tells MatCalc what parameter the column values refer to. Hence, any changes in the order or number of the lines in this section should be reflected in the corresponding modifications in the **'Data'** section. This section is delimited with **'*[format]*'** and **'*[/format]*'** tags.

'Variables' section
-------------------

This section consists of the default parameter value definitions. The values defined here are used in every segment if there is no other definition in **'Data'** section. This means that the values given here are overwritten by the relevant values in **'Data'** section. Please, note that MatCalc always has a default value for the segment parameters, so this section actually allows to modify these. Currently, this section has to include the definition of the default segment code (starting with **'*segment-code=*'** string) - accepted values for this parameter are:

* **'1'** for segment end temperature and cooling/heating rate
* **'2'** for cooling/heating rate and segment duration time
* **'3'** for segment end temperature and duration time
* **'4'** for accumulated strain

This section is delimited with **'*[variables]*'** and **'*[/variables]*'** tags.

'Global' section
----------------

This section contains the parameter values which have the global meaning - it means that this are relevant for the whole treatment rather than for the segments. An example of the parameters defined here are treatment name or treatment start temperature. The values given here overwrite parameter values defined in any other section, e.g. the treatment start temperature given here defines the start temperature of the very first segment, regardless of the definitions included in **'Variables'** or **'Data'** section. These two definitions: tmt name (**'*tmt-name=*'**) and tmt start temperature (**'*start-temperature=*'**) are mandatory. The global section is delimited with **'[global]'** and **'[/global]'** tabs.

***NOTE***

The sections can be ordered at will, so that the above given order needs not to be maintained. In fact, files exported by MatCalc have a reversed order.

Comments
--------

Besides these sections, comments can be also added anywhere in the file. As usual, these lines serve the communication with user and may contain some useful information (e.g. explanations for various lines). Every comment has to start with a dollar symbol (**'$'**). Comments can be put in separate lines or added at the end of any command line - in the latter case, some blanks should introduced before '$'-sign.

Example
-------

Below, an example of the file describing the thermomechanical treatment from Tutorial 17 is presented.

```
$**********************************************************************
$ this file contains heat treatment data information for MatCalc 6.01
$ and higher.$ 
$ description:
$ 
$ - segment code (1 ... use T_end and T_dot)
$                    (2 ... use T_dot and delta_time)
$                    (3 ... use T_end and delta_time)
$                    (4 ... use accumulated strain)
$**********************************************************************

[global]
	file-version=2.0
	tmt-name="sample_ht"
	start-temperature=1400
	field-separator=\\t
[/global]

[variables]
	segment-code=1
	segment-start-temperature=1000
	end-temperature=1000
	heating-cooling-rate=0
	delta-time=1
	absolute-time=-1
	accumulated-strain=0
	strain-rate=0
	stress-load=0
	deformation-control-mode=1
	load-control-mode=1
	eps-dot-axis=0
	store-intervals=25
	increment-for-store-intervals=1.1
	use-logarithmic-store-intervals=1
	initialize-microstructure-data=0
	reset-excess-vacancy-fraction=0
	reset-recrystallized-fraction=0
	break-up-precipitates=0
	release-gb-precipitates=0
	reset-trap-partitioning-ratio=0
	reset-store-counter=0
	log-scale-factor=1.1
	inherit-prec-domain=1
	precipitation-domain=
	beta-scale-for-store=0
	pre-segment-script=
	post-segment-script=
	segment-comment=
[/variables]
[format]
	column=segment-code
	column=segment-start-temperature
	column=end-temperature
	column=heating-cooling-rate
	column=delta-time
	column=absolute-time
	column=accumulated-strain
	column=strain-rate
	column=stress-load
	column=deformation-control-mode
	column=load-control-mode
	column=eps-dot-axis
	column=store-intervals
	column=increment-for-store-intervals
	column=use-logarithmic-store-intervals
	column=initialize-microstructure-data
	column=reset-excess-vacancy-fraction
	column=reset-recrystallized-fraction
	column=break-up-precipitates
	column=release-gb-precipitates
	column=reset-trap-partitioning-ratio
	column=reset-store-counter
	column=log-scale-factor
	column=inherit-prec-domain
	column=precipitation-domain
	column=beta-scale-for-store
	column=pre-segment-script
	column=post-segment-script
	column=segment-comment
[/format]
[data]
1	1400	600	-1	800	0	0	"0.0"	"0.0"	1	1	0	25	0	1	0	0	0	0	0	0	0	1.1	0	"austenite"	98.3471	"\nset-precipitation-parameter precipitate-or-domain-name = FCC_A1#01_P0 nucleation-sites = grain-boundaries\nset-precipitation-parameter precipitate-or-domain-name = FCC_A1#01_P1 nucleation-sites = none"	"\nset-precipitation-parameter precipitate-or-domain-name = FCC_A1#01_P1 nucleation-sites = dislocations"	""	
1	600	25	-1	575	800	0	"0.0"	"0.0"	1	1	0	25	0	1	0	0	0	0	0	0	0	1.1	0	"ferrite"	98.3471	""	""	""	
1	25	850	1	825	1375	0	"0.0"	"0.0"	1	1	0	25	0	1	0	0	0	0	0	0	0	1.1	0	"ferrite"	98.3471	""	""	""	
1	850	1100	1	250	2200	0	"0.0"	"0.0"	1	1	0	25	0	1	0	0	0	0	0	0	0	1.1	0	"austenite"	98.3471	""	""	""	
3	1100	1100	0	7200	2450	0	"0.0"	"0.0"	1	1	0	25	0	1	0	0	0	0	0	0	0	1.1	0	"austenite"	98.3471	""	""	""	
1	1100	600	-1	500	9650	0	"0.0"	"0.0"	1	1	0	25	0	1	0	0	0	0	0	0	0	1.1	0	"austenite"	98.3471	""	""	""	
1	600	25	-1	575	10150	0	"0.0"	"0.0"	1	1	0	25	0	1	0	0	0	0	0	0	0	1.1	0	"ferrite"	98.3471	""	""	""	
[/data]
```

![](/wiki/lib/exe/taskrunner.php?id=reference%3Atmt_file&1788352869)