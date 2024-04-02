# Python

If you don't already have python, you can follow instructions on the [Software Carpentry website](https://carpentries.github.io/workshop-template/install_instructions/#python).  Note that their instructions are based on using Anaconda.  

# Python packages

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

We need various packages as above.  For environment management, we use `conda`.  

```{seealso}
Managing environments with [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
```

Choose a directory where you will work on the python for this course.  Navigate to the directory in a terminal window.
The basic command is something like `conda create --name <my-env>`  where you replace `<my-env>` with the name of your environment.  Let's call it `seaocn_env`.  But we'll try to install a lot of the necessary pieces at once:
```
conda create --channel conda-forge --name seaocn_env xarray gsw python pandas gsw dask netCDF4 bottleneck numpy matplotlib jupyterlab nb_conda jupyter-book ipykernel nb_conda_kernels
conda activate seaocn_env
```

```{note}
To install an individual package with conda, you can use

    conda install -c conda-forge <package>

```

We need a few more packages that seem to only have `pip` instructions
```
pip install pycnv
pip install git+https://github.com/cioos-siooc/ocean-data-parser.git
conda env export > environment.yml
```
This has created a list of the current environment which you can get from this repository [environment.yml (repository)](https://github.com/ifmeo-hamburg/seaocn/blob/main/environment.yml).  If you download this into your working directory, you can activate the environment:
```
conda env create -f environment.yml
```
Then before you start working, activate the environment using
```
conda activate seaocn_env
jupyter-lab
```

Now, when you start `jupyter-lab` you'll see that you can select the environment `seaocn_env`.  Or, when you open an existing python notebook (`*.ipynb` file), in the upper right corner you can select the environment (e.g., `seaocn_env` and tick the box to always open with preferred kernel).

```{note}
If it's been a while since you installed conda, you can update it with

    conda update -n base -c conda-forge conda

But your conda will tell you when you need to do this
```

```{note}
If you want to recreate your environment with conda, after adding a few things, you can do a

    conda deactivate
    conda remove --name seaocn_env --all

And then start fresh with the `conda create` code above, appending the extra packages in the intial install.
```

### Problems with jupyter-book and kernels

My jupyter-book didn't know about my environment seaocn_env.  This should *not* be a problem for students, but is a problem when i want to execute this book (the course  notes) which contain packages that aren't in my base installation of python on my computer.

```
pico $HOME/.jupyter/jupyter_config.json
```
and add the lines
```
{
  "CondaKernelSpecManager": {
    "kernelspec_path": "--user"
  }
}
```
After saving this, I was able to run
```
python -m nb_conda_kernels list
```
and it appeared to add my kernels.

Then making the jupter book worked without errors.


```{seealso}
https://fcollonval.medium.com/conda-environments-in-jupyter-ecosystem-without-pain-e9fab3992fb7
```
(seaocn_env) 18:20 ~/Library/Mobile Documents/com~apple~CloudDocs/Work/teaching/SeaOcn-UHH $ python -m nb_conda_kernels list

## Environments

More advanced: It's best to work inside an environment.  This controls the version of each of the packages that you have installed, so that the code is more likely to run smoothly on another person's computer.  Some background on [conda environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

