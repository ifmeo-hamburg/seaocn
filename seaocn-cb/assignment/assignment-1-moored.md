
# Assignment - moored CTDs

Two moored CTDs were deployed on the WB2 mooring of the RAPID array at 26.5°N and 76.75°W at 2000m depth in 3800m water depth.  They were deployed in late December/early January 2021 and recovered in early 2023.  This was a trial deployment of an RBR concerto CTD against a microCAT.

**Aim:** Your task is to evaluate the moored CTD data, correcting for obvious errors and quantifying bias.  After corrections, you must make a determination of whether the data are usable for calculating geostrophic transport in the Atlantic.

**Tips and hints:** 

1. You have microCAT and RBR data for both the deployment (Jan 2021 - spring 2023) and the calibration casts. Calibration casts can be used to compare the moored instruments to the ship-board CTD.

2.  You will want to think about how you regrid data from one time grid to another in order to make a comparison.  The sample rates on the two moored CTDs differ.  You have options for regridding, e.g. linear interpolation, nearest neighbor interpolation, bin averaging.  Justify your choice.

3. Some calculations you may find useful: Correlations, significant difference between the mean of two datasets.

4. Using a statistical threshold (like values differing by more than 6 standard deviations from a rolling average are outliers) to identify and remove (or correct, if possible) salinity "dropouts".  Note that these may be due to critters getting in /near the conductivity sensor.

5. Your code should produce useful figures for evaluating the data, including T-S diagrams, time series of the whole record and of particular features that you'd like to point out or discuss.  Visual displays of the biases should also be created.

**Data:** The data files are available [here](https://www.dropbox.com/scl/fo/tooio0tnefchv4yo9qikl/h?rlkey=9lvwk0xq4y8wdunk7up90hv3k&dl=0).  You may also want to read the cruise report for the deployment on cruise DY129, and recovery in 2023 on the R/V Endeavour.  

```{seealso}
Take a look at [pyRSKtools](https://docs.rbr-global.com/pyrsktools/guides/getting-started-guide.html) for loading `*.rsk` data into python.

For the microCAT, the `*.use` file is a text file, and should be read into python by first stripping/removing the header, and then loading the data line by line.  The header field called "Columns" describes the data in the columns, where `YY` is year, `MM` is month, `DD` is day, `HH` is decimal hour, `T` is temperature, `C` conductivity and `P` pressure.
```


**Directions:** Evaluate the datasets and correct the data where possible.  Produce a summary report for your "customer", an interested scientist who needs to decide whether the instrument is fit for the purpose of measuring ocean circulation.  

Submit the report on the Moodle, and the git repository on Github classroom.  Your grade will be assigned on the basis of the report and the repository.  See [Report requirements](../assignment/report-specs) for formatting details.


----

<!--# Variations for assignment 2 (TBD)

You will additionally be expected to use the calibration cast data to determine offsets between the sensors and the ship-board CTD.  Corrections should attempt both a conductivity offset and a conductivity slope correction.-->