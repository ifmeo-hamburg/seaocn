# Assignment - To-yos

A CTD on a ship can be used in a to-yo fashion: This means that the CTD is lowered and raised while the ship is steaming slowly, and the CTD is not raised out of the water in between casts.  The advantage of this approach is in delivering high horizontal resolution data and saving time.

**Aim:** Your task is to evaluate the effect of different gridding procedures on the calculation of horizontal density gradients.

**Code requirements:** In addition to whatever code is required to accomplish the aim, your code should also include a section to compute and display important, basic information about the dataset.  This includes a simple display of where the CTD was, what the nominal (average, minimum, maximum) horizontal resolution was, how quickly the CTD was raised or lowered, and how quickly the ship was steaming.  These should be included in the beginning of your report to enable an interested reader to repeat the procedure on a future cruise.


<!-- (linear interpolation vs optimal interpolation) on The purpose of this assignment is to build some clean, easy-to-use code to work with to-yo data in real-time on a ship.  Here we ignore any data calibration problems, and instead aim for clear figures and well-documented code for easy edits.  -->

**Tips and hints**

1. You have CTD data from the MSM121 cruise in September 2023.  

2. You will want to implement at least 2 methods to regrid data onto a regular horizontal distance grid (rather than the sawtooth pattern of the to-yo).  For example, this could include a horizontal linear interpolation and a horizontal optimal interpolation.  

3. You will then want to estimate horizontal density gradients along the section for both methods of gridding.  Vary your gridding choices systematically, and evaluate how this affects your onward calculations.

4. Your code should produce useful figures for quick evaluation of the data, including T-S diagrams, a section plot of temperature, salinity and density with the sawtooth pattern overlaid, and visual displays of the onward calculations (horizontal density gradients).
<!--2. Make a variety of figures including:
- a map (with coastlines marked)
- multiple line plots (time series) on a single axis
as well as annotate the figures and alter the colors and symbols used.

3. Evaluate code in an `*.ipynb` file, use *comments*.

4. Export figures in `*.png` format.

5. Use python libraries including: `matplotlib`, `xarray`-->

**Data:** The data files are available in the git repository.  

**Directions:** Evaluate the datasets and demonstrate your chosen methods for interpolation, and the effect the choices have on onward calculations.  Produce a summary report for your "customer", an interested scientist who needs to decide whether and how to carry out a to-yo operation on an upcoming cruise, and once data are available, how to evaluate what kinds of phenomena can be seen.  

Submit the report on the Moodle, and the git repository on Github classroom.  Your grade will be assigned on the basis of the report and the repository.  See [Report requirements](../assignment/report-specs) for formatting details.


<!--# Variations for assignment 2

Apply gridding methods to the velocity data as well; onward calculations to include Ertel PV in addition to the horizontal density gradients of assignment 1.   More complete sensitivity test of how the calculation depends on the methods/choices.

-->