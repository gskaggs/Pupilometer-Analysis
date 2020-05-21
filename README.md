# Pupilometer-Analysis-Programming

The analysis programming used to conduct research on the efficacy of various wavelengths of light in producing acute pupillary responses.

diameter.py takes 4 arguments on a single line from stdin: 
input image name, output image name, pupil width, epsilon.

where pupil width is the estimated width in mm each pixel of the pupil represents, and epsilon is the maximal pixel intensity which is still considered dark enough to be inside the pupil. 

diameter.py runs a BFS flood fill algorithm to determine the pupil's horizontal and vertical diameters, and produces a new image with the pupil outlined in blue.

Limitations: The pupil must be centered in the provided image.
