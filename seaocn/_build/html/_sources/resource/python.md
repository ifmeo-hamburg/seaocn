# Python 

## Installing packages (Windows)

Ok, we are presuming some previous knowledge, but to help you get past some hurdles experienced, see tips below:

* If you try to run some code with an "import" line, and you get an error, this is likely because you don't have the package installed (on your computer) and python is trying to load it.  

- How to fix this (Windows): You need to install the package using conda.  If you're using "Anaconda", then find the Anaconda prompt in the application.  See how here: [https://saturncloud.io/blog/how-to-access-anaconda-command-prompt-in-windows-10-64bit/#2](https://saturncloud.io/blog/how-to-access-anaconda-command-prompt-in-windows-10-64bit/#2).  Then you need to install the missing package with conda.

Some packages you will need:

- [Gibbs Seawater Toolbox (GSW)](https://pypi.org/project/gsw/) - see installation instructions here
- [xarray](https://docs.xarray.dev/en/latest/getting-started-guide/installing.html#instructions) - see installation for xarray and necessary other packages (dask, netCDF4, bottleneck).  This is a *very useful* data format/package for netcdf files (many ocean/climate datasets).
- [pycnv](https://pypi.org/project/pycnv/) - for importing Seabird format `*.cnv` datafiles

You may also need:
- [pandas](https://pandas.pydata.org) - simpler than xarray.  Avoid, but may be needed.  
- [numpy](https://numpy.org/install/) - multi-dimensional arrays
- [matplotlib](https://matplotlib.org/stable/users/getting_started/) - plotting tools, similar to Matlab style

Potentially of interest:
- [ocean data parser](https://github.com/cioos-siooc/ocean-data-parser) - but only has pip install instructions [here](https://cioos-siooc.github.io/ocean-data-parser/dev/get_started/installation/).  If you've been using conda and you'd like to use pip instead, you can use conda to install pip.  See some info [here](https://stackoverflow.com/questions/19042389/conda-installing-upgrading-directly-from-github)

## Installing packages (Mac)

Use pip install.

## Environments

More advanced: It's best to work inside an environment.  This controls the version of each of the packages that you have installed, so that the code is more likely to run smoothly on another person's computer.  Some background on [conda environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

