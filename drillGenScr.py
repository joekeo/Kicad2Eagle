#Name of the file to Load
fileName = 'gamepad-PTH-drl.gbr'
typeOfDrill = 'Via ' #'Via ''#leave the extra space
#define an file name for the output
outputName = fileName + 'Script'

#create a file to save the script and set the grid size
f= open(outputName,"w+")
f.write("GRID MM;\n")
f.close()

#re open the file to append the script's lines
f= open(outputName,"a+")

#Dictionary for the holes apertures.
apertures = {}
activeDrill = ""
#Load the file to make the drill script
lines = [line.rstrip('\n') for line in open(fileName)]

#iterate thru all the file's lines
for i in range(0,len(lines)):
    #print lines[i]
    #append the values of the apertures
    if lines[i].find("AD")>-1:
        #get the info of the name and size of aperture
        rubbish1, appInf = lines[i].split("AD")
        appId,appSize = appInf.split("C,")
        #update the apertures dictionary for later use
        apertures.update({appId:appSize[:-2]})

    #split the lines to analyse the drill position and size
    impStuff, rubbish1 = lines[i].split("*")

    #fin the active drill bit
    if impStuff in apertures:
        activeDrill = apertures[impStuff]
        f.write("Change drill " + activeDrill + ";\n")
    #get the position of the holes
    if impStuff[0] == "X":
        holePositon, rubbish1 = impStuff.split("D")
        xPos, yPos = holePositon.split("Y")
        xPos = xPos[1:len(xPos)]
        fxPos = float(xPos)/1000000
        fyPos = float(yPos)/1000000
        f.write(typeOfDrill + activeDrill + " (" + str(fxPos) + " " + str(fyPos) + ");\n" )




print apertures
