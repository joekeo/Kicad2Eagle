# Kicad2Eagle
Small Python script that creates an eagle script to import the drills and vias into eagle provided that the drillfile is in Gerber format.

To import a Kicad .brd to eagle.

*using mm and 4:6 units
**only imports round vias and holes (?)
***have a separate files for plated and not plated holes.

1. Plot the the Kicad board and export the drill file in gerber format (im using this nightly build version Version: no-vcs-found-ad9916e~61~ubuntu16.04.1, release build)

2. Copy this script into the folder with the exported files

3. Open the script with your editor of choice

4. Modify the 2nd line with the name of the drill gerber file that you want to import and the 3rd with either 'Hole ' or 'Via ' 
    depending if it is plated or not plated hole.

5. Run the script and prey that it works

6. Either copy the text of the output file to an Eagle script or save the file on your eagle script folders

7. Run the script in you desired eagle board.

8. import the rest of the gerbers into the board to have a coplete pcb

9. Profit.
