#!/usr/bin/env python
# coding: utf-8

# # 2. Fitting a trend
# 
# 
# ## Lab overview
# 
# **Aim:** The purpose of this lab is to get you started with elementary time series analysis: fitting a trend and a polynomial to a time series.
# 
# **Learning outcomes:** At the end of this lab, you will be able to:
# 1. Calculate a linear trend given a time series, and determine its slope and y-offset.
# 2. Calculate a polynomial fit to the time series, and determine the acceleration.
# 3. Gain basic familiarity with Python `xarray` data arrays, and familiarity with indices and NaNs.
# <!--4. Use the functions including: nanmean, detrend, polyfit, polyval, disp, grid, find, isnan, sqrt, and the operators ==, ~ and .^2.-->
# 
# **Data:** You will work with the time series of carbon dioxide concentration from the Mauna Loa site.
# 
# **Directions:** Answer the questions, create an `*.ipynb` and one figure.
# 
# ----
# ## Exercises
# 
# ### Create a notebook
# 
# Create an `*.ipynb` containing the commands for this assignment.  Name it `lab-2-fitting.ipynb`.
# 
# ### Load the data
# 
# The data are in a netCDF file.  netCDF is a common file format for oceanographic and climate data.  They can be handled several ways, but `xarray` has a number of convenient features.

# In[1]:


import xarray as xr


# **Working with data arrays.**  Use the `print` command to see what is in your data array.  A data array is a bit like a file folder, with different variable types in it.
# 
# 
# ```{seealso}
# The [xarray user guide (external)](https://docs.xarray.dev/en/stable/user-guide/index.html), especially for this lab on
# - [Data structures](https://docs.xarray.dev/en/stable/user-guide/data-structures.html)
# - [Indexing and selecting data](https://docs.xarray.dev/en/stable/user-guide/indexing.html)
# ```
# 
# ### Fig 1. Time series
# 
# Here you will plot the Maona Loa time series of CO2.  Plot the CO2 data against time.  
# 
# Note that some of the data are invalid, which is given by the value -99.99.  Replace these with `NaNs` using indexing.
# 
# - How many invalid values were there?
# 
# Replot the time series.  Try adding a grid using `plt.grid()`.  Now try adding only horizontal grid lines.  Try reformating the x-axis labels.  
# 
# - Save the figure as `lab2_figure1.png`.
# 
# 
# ### Explore the data
# 
# - What is the mean of the data?  
# 
# ```{seealso}
# [xarray: Computation](https://docs.xarray.dev/en/stable/user-guide/computation.html)
# ```
# 
# - What is the max?
# 
# - What is the min?
# 
# - How many years long is the record?
# 
# - How quickly (in ppm/yr) is the concentration of CO2 increasing?  Approximate, using your answers above.
# 
# ### Fig 2. Annual cycle
# 
# - Extract the January data from the time series.  See how in [xarray: Time series data](https://docs.xarray.dev/en/stable/user-guide/time-series.html).  
# 
# - Calculate the mean for January
# 
# - Write a loop to calculate this for each month, January through December
# 
# - Store these values into a new data array with a variable length of 12.
# 
# - Plot the seasonal cycle, calculated as monthly averages, in a new figure.  Save this figure as `lab2_figure2.png`.
# 
# ### Fitting a trend
# 
# - Find a line of best fit to the original data.  Read how to use the function [xarray.Dataset.polyfit](https://docs.xarray.dev/en/stable/generated/xarray.Dataset.polyfit.html).  You should use the time dimension as your coordinate along which to fit the 1st degree polynomial (a line).  
# 
# - What is the slope of the line?
# 
# - Convert this to units of ppm/year.
# 
#   *Question for thought:* How does this compare to the slope you calculated above?
# 
# - Using your linear regression, what CO_2 concentration would you predict in 1960?  Use the function [xarray.polyval](https://docs.xarray.dev/en/stable/generated/xarray.polyval.html#xarray.polyval) to compute this.
# 
# - What is the true value in 1960?  Use `xarray` functions to extract the year of 1960 and calculate an average over that year.
# 
# - Add the line of best fit to your original plot of the full dataset (or replot here).
# 
# 
# - Now fit a polynomial of degree 2 (a quadratic).  Recall that a 1st order polynomial has the form
# 
#   $$Ax + B$$
# 
#   where $A$ is the slope.  A second degree polynomial has the form
# 
#   $$Ax^2 + Bx + C$$
# 
#   where $A$ is the acceleration.  What are the units on $A$?
# 
# - Add this polynomial as a third curve.
# 
# - **Clean up the plot.**  This means, add a legend, axes labels, fix the time axis annotations if needed, and fix the fontsize to be legible even if the figure is small.
# 
# ```{note}
# In future exercises, you will be expected to clean up all plots without reminders.  All plots should have axes labelled (with units!), legible font size (bigger than you think) and appropriate axis ranges.  Legends should be used whenever more than one quantity is plotted.
# ```
# 
# - Save the figure as `lab2_figure1.png`, overwriting your first version.
# 
# 
# 
# 
# ### Commit your code
# 
# Commit your code including figures in a `figures/` subdirectory into the git repository for the assignment.
