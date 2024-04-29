
# Assignment - Gliders

Marine gliders, a type of long-endurance autonomous underwater vehicle, are becoming more pervasive as a tool for making ocean observations.  However, there are still uncertainties as to how good the data are.  This includes uncertainties in the quality (accuracy) of the fundamental physical oceanographic measurements: temperature and salinity.

**Aim:** Your task is to evaluate a glider dataset, identifying potential errors and offsets between temperature and/or salinity between up-casts and downcasts.  You will determine whether there is a bias, and apply a correction to the glider data, then evaluate the uncertainty in the horizontal density gradients resulting.

**Tips and hints:**

1. You have a choice of glider data, either from the Labrador Sea (a L1 dataset from the TERIFIC project, on a Teledyne Slocum) or a Seaexplorer from the VOTO missions.  For this exercise, no auxiliary ship-based data will be used.

2. You will want to set up a method to regrid glider data from a sawtooth pattern to a regular horizontal grid.  For assignment 1, you can use horizontal linear interpolation onto a regular distance grid.

3. Some calculations you may find useful:  Differences between temperature/salinity/density between the upwards (climb) of a glider dive-cycle and the downwards (dive).  What is the difference on average (mean and median)?  As a function of depth (so plot the difference as a profile)?  Are there time periods in the dataset where the average difference is larger or smaller?

4. Are there time periods or conditions where you would expect the dive/climb difference to be larger or smaller?

**Data:** The data files are available ... TBD.  

**Directions:** Evaluate the glider dataset and apply a correction where possible.  Produce a summary report for your "customer", a hobbyist user of glider data who wants to know whether they can trust horizontal density gradients computed from gliders, or whether this is beyond the capability of this observational approach. 

Submit the report on the Moodle, and the git repository on Github classroom.  Your grade will be assigned on the basis of the report and the repository.  See [Report requirements](../assignment/report-specs) for formatting details.

----

<!--# Variations for assignment 2 (TBD)

Update the method using horizontal optimal interpolation (rather than horizontal linear interpolation).  Apply a larger or smaller bias, and evaluate for what choices of horizontal decorrelation scale, and what salinity bias, the bias would give spurious values of negative Ertel PV.
-->