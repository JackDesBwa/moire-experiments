Moiré experiments
=================

This repo is used for experiments about `moiré effect <https://en.wikipedia.org/wiki/Moir%C3%A9_pattern>`_. It will be a collection of test scripts, not a fancy finished software.

interactive.qml
---------------
This is a simple shader/qml script (Qt5 library) to display computed images in interactive way
Launch with *qmlscene interactive.qml*
It assumes graptings are saved as /tmp/i1.png and /tmp/i2.png
Move with button1 and turn with button2 of the mouse

1_simple_initial
----------------
First tentative with naive code (WORKS)
Two linear gratings with different frequency create a 3rd linear frequency

2_round
-------
Not expected but interesting result
Two almost linear gratings create circular pattern

3_cross_circle
--------------
Circular grating with a cross emerging pattern
Result of try and errors with equations

4_spiral
--------
Circular gratings with spiral emerging pattern
Result of try and errors with equations

5_pseudoinv
-----------
Use maths to 'invert' phase and have approximative rendered pattern computed
Need work to have better results

6_pseudoinv_color
-----------------
Generate two gratings that overlaps into a colored image
