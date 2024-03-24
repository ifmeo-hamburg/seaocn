# Assignment 1 - moored CTDs

Two moored CTDs were deployed on the WB2 mooring of the RAPID array at 26.5°N and 76.75°W at 2000m depth in 3800m water depth.  They were deployed in late December/early January 2021 and recovered in early 2023.  This was a trial deployment of an RBR concerto CTD against a microCAT.

**Aim:** Your task is to evaluate whether the RBR concerto data is useable after checks and corrections.

**Tips and hints** 

1. You have microCAT and RBR data for both the deployment (Jan 2021 - spring 2023) and the calibration casts. You may want to look at these calibration casts to compare the data to each other and to the ship-board CTD on a profile.

2.  You will want to think about how you regrid data from one time grid to another.  The sample rates on the two moored CTDs differ.  You have options for regridding, e.g. linear interpolation, nearest neighbor interpolation, bin averaging.  Justify your choice.

3. Some calculations you may find useful: Correlations, significant difference between the mean of two datasets.

4. Using a statiscal threshold (like values differing by more than 6 standard deviations from a rolling average are outliers) to identify and remove salinity "dropouts".  Note that these may be due to critters getting in /near the conductivity sensor.

**Data:** The data files are available in the git repository.  

**Directions:** Produce a summary report and git repository of your analysis.  See [Report requirements](../assignment/report-specs) for formatting details.

You may also want to read the cruise report for the deployment on cruise DY129, and recovery in 2023 on the R/V Endeavour.

----

And some further details here