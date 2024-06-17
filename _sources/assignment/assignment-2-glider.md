
# Assignment - Gliders

Marine gliders, a type of long-endurance autonomous underwater vehicle, are becoming more pervasive as a tool for making ocean observations.  However, there are still uncertainties as to how good the data are.  This includes uncertainties in the quality (accuracy) of the fundamental physical oceanographic measurements: temperature and salinity.

**Aim:** Your task is to use a glider dataset to describe a process in the ocean.  

**Tips and hints:**

1. You have a choice of glider datasets from [VOTO](https://voiceoftheocean.org) which have been loaded into `xarray` datasets.  See below for the data in netcdf format.  To decide which of the two datasets you want to use, you can look at the data in the demonstration code [exercise 7](../exercise/exercise-glider-demo.ipynb) which also has some useful demonstration code for creating a basic section plot.

2. Choose **one** phenomenon to describe.  This could be, e.g. for the storm, how the vertical stratification changes before, during and after the storm.  Or for the Baltic inflow, how the temperature in the near surface water (at 20m) changes through the year.

3. Where possible, quantify what you see.  When did something happen (on what date/month), how cold/warm was the water (degrees Celcius, g/kg or no units), what was the top-to-bottom stratification  which could be calculated (buoyancy frequency in the Gibbs seawater toolbox) or estimated as the difference in density between two fixed depths.  

4. Read the guidance in point 2 and 3 again.  *Instead of spending time looking at a large number of qualitative things in the dataset, choose one thing, and try to quantify what you see.*  

4. Note that the dataset is in an `xarray` format, but it is still complicated to use.  I.e., the location changes, the time changes, etc.  Plan to spend some time figuring out where the glider was at what time period.  You can choose then to subselect data within a smaller box (e.g., if the glider is making a section back and forth, consider only one end of the section, or the middle of the section).

**Data:** The data files are available in `*.nc`. See [here](https://www.dropbox.com/scl/fo/kpccb8qdprnzk1j8fztwd/AIkHEqaT0q9kzxTsEN2gi84?rlkey=8iindnibrifbim31ydvx2vc4o&dl=0).  These are:

<!--    - [Aland_Sea_nrt_stack.nc](https://www.dropbox.com/scl/fi/qj411iu7c7wkt3x1bl4hi/Aland_Sea_nrt_stack.nc?rlkey=kkb71b62ns0iihrrbr0tc9cxc&dl=0) (37mb)-->
- [Bornholm_nrt_stack.nc](https://www.dropbox.com/scl/fi/6n13ax6czpg92rx84h6mp/Bornholm_nrt_stack.nc?rlkey=vmbpvpe1msxum9izkbfgdkspj&dl=0) (15mb, Baltic inflow)

- [Hans_storm_nrt_stack.nc](https://www.dropbox.com/scl/fi/0a5b2ad1ovt8urbe8uck6/Hans_storm_nrt_stack.nc?rlkey=5s5nucwbi62pyn1jowxly5qg1&dl=0) (5.5mb, only Bornholm)
<!--    - [Bloom_nrt_stack.nc](https://www.dropbox.com/scl/fi/d9f9oe7pq9tlr1vvzr9rh/Bloom_nrt_stack.nc?rlkey=6yaar6wn1lhopynmx8gg9ujt2&dl=0) (26mb)-->
 

**Directions:** Evaluate the glider dataset and describe what you've found. Produce a summary report for your "customer", a scientist who would like to target your phenomenon in more detail.  Make at least 3 recommendations for either (i) what else to use the data for, or (ii) how to adjust the data collection to better capture details of the phenomenon.

Submit the report on the Moodle, and the git repository on Github classroom.  Your grade will be assigned on the basis of the report and the repository.  See [Report requirements](../assignment/report-specs) for formatting details.

----

<!--# Variations for assignment 2 (TBD)

Update the method using horizontal optimal interpolation (rather than horizontal linear interpolation).  Apply a larger or smaller bias, and evaluate for what choices of horizontal decorrelation scale, and what salinity bias, the bias would give spurious values of negative Ertel PV.
-->