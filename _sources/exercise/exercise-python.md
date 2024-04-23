# Exercise 0b - Python


**Aim:** The purpose of this exercise is to get python running.

**Context:** For this course, you can work with python either on your own computer on the university computers.  Note, at this point, instructions are not yet verified for using python on the university computers.

**Goals:** At the end of this exercise, you will be able to

- Run python with jupyter notebooks 
- (Optional) Run jupyter-lab
- (Optional) Create and use `conda` to manage environments
- Install python packages (e.g., `gsw`, `pandas`, `xarray`)
- Create a python notebook with packages installed, add it to your repository, commit to the repository and then push to remote.
- Edit the `readme.md` file within your folder in the shared repository, adding the *specific steps* needed to get jupyter running on  your computer.

**Measure of success:** We will see the updated `readme.md` file within your folder on the shared repository, and a python notebook *where the cell importing packages has been run successfully*.

<hr>

## Step 1: Check whether you have python installed

In Mac or Linux, at the command line, type
```
python --version
```

For example, mine says
```
(base) 9:34 ~ $ python --version
Python 3.9.5
```

If it's not installed, see: [Python installation](../resource/python).

Once you verify that python is installed, you have two options for moving forward:
- Get jupyter running on your computer.
- (Optional) Environment management with conda (and jupyter lab) [below](#slightly-more-advanced-step-2-setting-up-a-conda-environment)
*Either* option is acceptable for this course.


```{seealso}
- [Jupyter notebook v Jupyter lab (external)](https://saturncloud.io/blog/what-is-the-difference-between-jupyter-notebook-and-jupyterlab/#:~:text=If%20you%20are%20already%20familiar,is%20the%20way%20to%20go.)
```


## Step 2 (Optional): Conda environment 

Conda environments are a way to manage different installations of packages for different projects.  This can help avoid incompatibilities between various packages (but which aren't all needed for a piece of code), or to specify which version of python you were running when you wrote some code, so that 10 years down the line if it doesn't work with the most modern python, you have a chance of reverting to an earlier version.

Start by reading the basics about [conda environments (external link)](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/02-working-with-environments/index.html#:~:text=Key%20Points-,A%20Conda%20environment%20is%20a%20directory%20that%20contains%20a%20specific,activate%20(%20conda%20deactivate%20)%20commands.).  

```{note}
Key points from the link above:
- A Conda environment is a directory that contains a specific collection of Conda packages that you have installed.
- You create (remove) a new environment using the `conda create` (`conda remove`) commands.
- You activate (deactivate) an environment using the `conda activate` (`conda deactivate`) commands.
- You install packages into environments using `conda install`; you install packages into an *active* environment using `pip install`.
- You should install each environment as a sub-directory inside its corresponding project directory
- Use the `conda env list` command to list existing environments and their respective locations.
- Use the `conda list` command to list all of the packages installed in an environment.
```

- For Mac users, you will probably want `conda` and `pip` installed on your computer.

You can get conda here: [https://conda.io/projects/conda/en/latest/user-guide/install/index.html](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).  I would recommend *miniconda* (Here is the direct link for [installing miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)).  If you already have Anaconda, that is fine too.

- To create an environment to use for the work in this course, use the `conda create` command as:
```
conda create --channel conda-forge --name seaocn_env python pandas numpy xarray dask netCDF4 bottleneck scipy matplotlib cartopy cmocean pygmt gsw jupyterlab nb_conda ipykernel nb_conda_kernels erddapy argopy tqdm
```
<!--conda create --channel conda-forge --name seaocn_env xarray python pandas gsw dask netCDF4 bottleneck numpy matplotlib jupyterlab nb_conda jupyter-book ipykernel nb_conda_kernels pygmt cartopy scipy cmocean erddapy argopy tqdm-->
Note that it can be advantages to install all your packages at once since `conda` (or `mamba`) need to cross-check packages for compatibility upon installation.

- Then activate the environment and install missing packages with pip:
```
conda activate seaocn_env
pip install pycnv==0.4.2
```

Note that in the above, we've added `jupyterlab` as a package to be installed with `conda`.

## Step 3: Get Jupyter running

- Install either [jupyterlab or jupyternotebook](https://docs.jupyter.org/en/latest/#where-do-i-start).

```{note}
If you already have Anaconda, then jupyter lab comes by default as [explained here](https://test-jupyter.readthedocs.io/en/latest/install.html).
```

- Get Jupyter running on your computer.  The specific steps will depend on how it's been installed.  See instructions [here (external)](https://docs.jupyter.org/en/latest/running.html).  

- Record the steps you need to take to start jupyter!   **Specifically, put these steps into your `readme.md` within your folder in the shared git repository.**.


## Step 4: Create a new python notebook

- Create a new  notebook following the file-naming convention.

```{admonition} Naming convention: Zeroeth notebook
Name your notebook following the convention `Ex<A>-<Lastname>-seaocn.ipynb` where you replace the `<A>` with the exercise number (or number/letter combo), and `<Lastname>` with your lastname.
```

- Within this notebook, create a first cell to import the packages we'll be using during this course.  This starter example should have:

```{code}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import gsw
import pycnv
```

If any of these packages fail to run, then first *check which kernel you're using*. You want to use the kernel corresponding to the conda environment you created, `seaocn_env`.  This should be available from where you can edit the python notebook, as a dropdown menu in the upper right corner.  Or revisit your installations, or [python packages](../resource/python) for tips on how to install them.


- Now add a cell above your `import` cell, and change the format of the cell from "code" to "markdown".  Within this markdown cell, add some text, for example:

```{code}
# My Seaocn python notebook

- Author: <My name>
- Purpose: Verify package installation
- Date: <Today's date>

This **worked**!  But *not sure* what to do next.

<hr>
```

After adding text to the cell, run it as you would a python code cell.  Note that running the cell changes the formatting based on the markdown formatting commands you've provided.