
# Assignment - moored CTDs

Two moored CTDs were deployed on the WB2 mooring of the RAPID array at 26.5°N and 76.75°W at 2000m depth in 3800m water depth.  They were deployed in late December/early January 2021 and recovered in early 2023.  This was a trial deployment of an RBR concerto CTD against a microCAT.

**Aim:** Your task is to evaluate the moored CTD data, correcting for obvious errors and quantifying bias.  After corrections, you must make a determination of whether the data are usable for calculating geostrophic transport in the Atlantic.

**Tips and hints:** 

From the first assignment, it was determined that the pressure on the RBR was reading "off" by about 10.41 dbar.  This is based on the RBRconcerto being about 1m higher than the SBE9 when on the rosette, and the pressure correction contributes a few tenths of a milli-PSU to the salinity.  This difference should be applied to the RBR pressure.

- Assume that the temperature is OK.

- Check whether the conductivity is OK against the calibration cast.

- Compare the conductivity between the moored records.

See also [assignment 1 moored](../assignment/assignment-1-moored.md)

**Data:** The data files are available [here](https://www.dropbox.com/scl/fo/72z9cg5y8hq1cwt0tkqpt/ALozWIs3ys1SVx0NNwyuM0E?rlkey=66tvxlm8ga7zbw4mvrsnxccmx&dl=0) in netCDF format (following Rauschenbach's code).  You may also want to read the cruise report for the deployment on cruise DY129, and recovery in 2023 on the R/V Endeavour.  


**Directions:** Evaluate the datasets and correct the data where possible.  Produce a summary report for your "customer", an interested scientist who needs to decide whether the instrument is fit for the purpose of measuring ocean circulation.  

Submit the report on the Moodle, and the git repository on Github classroom.  Your grade will be assigned on the basis of the report and the repository.  See [Report requirements](../assignment/report-specs) for formatting details.


----

<!--# Variations for assignment 2 (TBD)

You will additionally be expected to use the calibration cast data to determine offsets between the sensors and the ship-board CTD.  Corrections should attempt both a conductivity offset and a conductivity slope correction.-->