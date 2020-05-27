# Pupilometer Analysis 

This project's purpose is to measure pupil size given infared images of the eye. The code is planned to be used in research conducted at the UT Austin Dell Medical School for the development of novel theraputic treatments for patients with Multiple Sclerosis.

## Configuration
diameter.py takes 4 space-separated arguments on a single line from stdin: 
1. input image file name
1. output image file name
1. pixel width
1. epsilon

where **pixel width** is the estimated width in mm each pixel of the pupil represents and **epsilon** is the maximal pixel intensity which is still considered dark enough to be inside the pupil. 

## Algorithm
*diameter.py* runs a breadth first search (BFS) flood-fill algorithm to determine the pupil's horizontal and vertical diameters, and produces a new image with the pupil outlined in blue. It prints the pupil's diameters to stdout and saves the output image at the directed file name.

## Execution
Calling the script *run.sh* will run *diameter.py* with the example config arguments in *config.txt* and will redirect the resulting text to *output.txt*.

## Examples
#### Input image:
![GitHub Logo](/input.png)

#### Output Image:
![GitHub Logo](/output.png)

## Limitations 
The pupil must be centered in the provided image. If it's not, *diameter.py* will give an error message to stdout.
