# Assignment - Geostrophy

Using the thermal wind equation, we can estimate the vertical shear in meridional velocity based on zonal density gradients.  However, the method assumes accurate measurements of salinity and an assumed level-of-no-motion.  How do these assumptions affect the accuracy of a transport estimate?

**Aim:** The purpose of this assignment is to evaluate the sensitivity of a geostrophic transport calculation to choices made during the calculation.

**Tips and hints:**

1. You have available hydrographic section data and mooring data (see data section below).

2. Set up code to calculate the geostrophic transport from (i) hydrographic sections and (ii) between moorings.  Focus on a narrow region at the western boundary of the Atlantic (e.g., between 77°W and 72°W).  You will want to implement a method where you can change the reference level.

3. Some useful calculations: Take a look at your data sources (use at least one ship-based source and one moored source). What time periods are availble?  You will want to run any comparison over the same time period.

4. You will need a metric or metrics over which to evaluate.  Recommended: the transport of the Antilles Current (see {cite:t}`Meinen-etal-2019`) or deep western boundary current (see {cite:t}`Johns-etal-2008`).   

5. Vary the choice of geostrophic reference level according to choices in the published literature for 26°N region.  (See e.g., {cite:t}`Bryden-etal-2005` or {cite:t}`Atkinson-etal-2012` or {cite:t}`Johnson-etal-2008`).  Evaluate the effect of your choice on the metric.



**Data:** Data available include the CTD data from
<!--- 24°N hydrographic sections 
    - with [CTD data at CCHDO](https://cchdo.ucsd.edu/search?bbox=-75,-60,20,65) and Filter for the "A05" section.  Complete sections were done and are available here from 1992, 1998, 2004, 2010, 2011, 2015 and 2020.  Note that the 2022 section is a partial section only.  
        <!--- *Not* recommended to download the LADCP data for the hydrographic sections: Note that LADCP data were taken, but appear to be available on the [BODC](https://www.bodc.ac.uk/data/bodc_database/currents/search/) website.  You need a geographic search for 24-30°N, -80° to -10°E (negative for west).  Then narrow the choice to ADCP and you get about 252 items.  You need a login to proceed.    -->
- the WBTS data [ftp://ftp.aoml.noaa.gov/phod/pub/WBTS/Global_Class](ftp://ftp.aoml.noaa.gov/phod/pub/WBTS/Global_Class) or [https://ftp.aoml.noaa.gov/phod/pub/WBTS/Global_Class](https://ftp.aoml.noaa.gov/phod/pub/WBTS/Global_Class) with <!--both velocity and-->  CTD information.
- RAPID array data at [RAPID download page](https://rapid.ac.uk/rapidmoc/rapid_data/datadl.php), with CTD information.
<!--- RAPID velocity data only through 2013 at [dropbox link](https://www.dropbox.com/scl/fo/3ppzqg3wwm79y2zcxmdwo/h?rlkey=mchs1407xx8dlvjiggask775u&dl=0) and in `*.mat` format.-->

 *Note* if the files are large (larger than 10 GB) you should not commit them to the repository.  To avoid committing you can add the file name to your `*.gitignore` before committing to your repository.

**Directions:** Produce a summary report and git repository of your analysis.  See [Report requirements](../assignment/report-specs) for formatting details.

<!--# Variations for assignment 2

6. Now try applying a salinity bias.  If the west was biased salty by 0.001, how  would the transport metric change?  By 0.003?  Can you specify how much of a bias is permissable on the basis of a desired transport accuracy?
-->
