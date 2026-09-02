Syntax for Conditions, Loops and other commands [MatCalc Documentation]



### Table of Contents

* [Syntax for Conditions, Loops and other commands](#syntax_for_conditions_loops_and_other_commands)

  + [IF-condition](#if-condition)
  + [WHILE-loop](#while-loop)
  + [FOR-loop](#for-loop)
  + [MatCalc built-in functions](#matcalc_built-in_functions)

Syntax for Conditions, Loops and other commands
-----------------------------------------------

This page contains in-depth information on how to use if-conditions, for- and while-loops as well as other commands, which could come in handy at some point.

Have a look at the following demonstration examples, which make excessive use of random numbers, conditions and loops:

* Random number generator -  [Random generator script](/reference/syntax/random.mcs "reference/syntax/random.mcs (3 KB)")
* The*MatCalc*Game -  [The MatCalc game](/reference/syntax/thematcalcgame.mcs "reference/syntax/thematcalcgame.mcs (8.9 KB)")
* Roulette -  [Casino Royal](/reference/syntax/roulette.mcs "reference/syntax/roulette.mcs (8.8 KB)")

### IF-condition

```
if (x>5)
   send-console-string 'The value of x is larger than 5'
endif
```

An if-condition can be used whenever a condition has to be checked (e.g./ Version number check at the beginning of each MatCalc script). The example above checks if the variable **x** is larger than the arbitrary value of **5**. If the condition is TRUE, the command after the if will be performed. If it is FALSE, it will not be performed. Note that an if-condition is always ended with an **endif**.

```
if (x>5)
   send-console-string 'The value of x is larger than 5'
elseif (x==5)
   send-console-string 'The value of x is exactly 5'
else
   send-console-string 'The value of x is 4 or lower'
endif
```

The code portion above is quite similar to the first one, however it shows other possible events. In case, that x is not larger than 5, the first `send-console-string` will not be performed, and the next **elseif** condition will be checked for its validity. If x has *exactly* the value of 5 (This is checked with the double equals sign **==**), the second string will be displayed. For *all* other events, the command written after **else** will be performed. The if-condition is again closed by the endif command.

**Note**: Always keep the difference between the *assigning* equals sign **=** and *comparing* equals sign **==** in mind. E.g.:

```
 x=5 ... x is assigned the value of 5 (not available in MatCalc)
x==5 ... x is checked if it has a value of 5
```

**Attention**: It is NOT possible to have a comment in the same line as a loop or condition, e.g.:

```
if(x==1)   $ DO NOT comment after a condition/loop. This results in an error
   s-v-v value 1
endif

----

$ Always comment before....
if(x==1)
   $ ... or after the condition
   s-v-v value 1
endif
```

### WHILE-loop

The **while**-loop will run a specific code portion for as long as the condition set for the while-loop is true:

```
while(continue==1)
   send-console-string 'Infinite loop'
endwhile
```

If the script comes to the portion written above, it will result in an infitine loop if the variable *continue* has a value of 1. The loop will always check the value and it will not stop as long as the value of *continue* is anything but 1.

```
while(continue==1)
   input-variable-value continue "Enter 1 to continue"
endwhile
```

We have inserted a user-input now within the loop. The user can now manually change the value of *continue* which results in either a repetition of the loop (if set to 1) or an end of the loop (anything but 1).

### FOR-loop

The **for**-loop has its main purpose in increasing a runtime variable which can be used thereafter. Another use can be found within the use of TTP scripts. Imagine to split the TTP calculation into 3 areas, of different resolution: From 1000 to 900C, the temperature step will be 10C, from 900 to 500 it will be 20C, and from there on it will be 50C. This can be realized with for-loops!

```
for(i;1..5)
   set-variable-value i i
   show-expression i
endfor
```

The portion shown above will run from 1 to 5 and increase the value of i with every repetition. To put the for-loop to a real use, another command is needed:

```
for(i;1..5)
   format-variable-string test %d i
   set-variable-value number#test 0
endfor

test ... Varible which gets the value of i
%d ..... Wildcard which shows that i is an integer value
i ...... Runtime variable and number
# ...... Put the hash key in front of a string, to use its 'value'
```

**Format-variable-string** creates a string out of a number. In the first step, i has a value of 1, which gets assigned to test. In the next line, the variable number#test gets created and receives a value of 0. As test is a string, #test will write its value instead of the string 'test'. Therefore, the second line will create a variable named number1 and assign the value 0. In the next step, i increases to 2. This value gets assigned to test. Therefore the variable number2 with the value 0 gets created.

```
format-variable-string test %d 5
send-console-string test
--> Output: test
send-console-string #test
--> Output: 5
```

This is an easy way of creating many variables automatically. Have a look at the 'Random number generation' script linked above for more information on the automatic creation variables.

There are two ways how the steps of a for-loop can be set: The automatical way has been used already without mentioning it, where the interval from x..y gets split in intervals with stepwidth 1. By adding an additional parameter, the step-width can be controlled by either splitting into intervals ( / ) or by setting a fixed step-width ( ; ).

```
for(i;1..100/5)
$ The interval from 1 to 100 is split into 5 intervals. 
$ The values for i are therefore: 1, 20, 40, 60, 80, 100.

for(i;1..100;7)
$ The step-width is set to 7. 
$ The values of i are therefore: 1, 8, 15, 22, 29, ..., 85, 92, 99.
```

### MatCalc built-in functions

* Random function

  + rand for interval ]0,1[
  + randz for interval [0,1[
  + random for interval [0,1][1)](#fn__1)
* Mathematical operators

  + sin
  + cos
  + tan

[1)](#fnt__1)

if you want to generate a **distribution of natural numbers** using floor or ceil functions, you must use **rand** or **randz** (with floor) instead, which exclude the upper limit of 1. E.g. for a distribution of numbers between 2 and 10 you can use: *2+floor(randz\*9)*

![](/wiki/lib/exe/taskrunner.php?id=reference%3Asyntax&1788352868)