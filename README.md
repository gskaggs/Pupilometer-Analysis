# Pupilometer Analysis 

This is the analysis programming used to conduct research on the efficacy of various wavelengths of light in producing acute pupillary responses.

diameter.py takes 4 arguments on a single line from stdin: 
input image name, output image name, pixel width, epsilon.

where pixel width is the estimated width in mm each pixel of the pupil represents, and epsilon is the maximal pixel intensity which is still considered dark enough to be inside the pupil. 

diameter.py runs a BFS flood fill algorithm to determine the pupil's horizontal and vertical diameters, and produces a new image with the pupil outlined in blue.

Executing run.sh will run the file with the example config arguments in config.txt and will redirect the result to output.txt.

Limitations: The pupil must be centered in the provided image.
