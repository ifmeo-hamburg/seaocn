# Exercise A2 - Python


**Aim:** The purpose of this exercise is to get python running.

**Context:** For this course, you can work with python either on your own computer on the university computers.  Note, at this point, instructions are not yet verified for using python on the university computers.

**Goals:** At the end of this exercise, you will be able to

- Run python with jupyter notebooks 
- (Optional) Run jupyter-lab
- (Optional) Create and use `conda` to manage environments
- Install python packages (e.g., `gsw`, `pandas`, `xarray`)
- Create a python notebook with packages installed, add it to your repository, commit to the repository and then push to remote.

**Measure of success:** We will see a python notebook in the course repository, in your folder, where the cell importing packages has been run successfully.

<hr>

# Step 1: Check whether you have python installed

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
- Option 1: Get it done.  Follow the more straightforward steps [below](#step-2-basic-usage)
- Option 2: Environment management with conda (and jupyter lab) [below](#slightly-more-advanced-step-2-setting-up-a-conda-environment)
*Either* option is acceptable for this course.


```{seealso}
- [Jupyter notebook v Jupyter lab (external)](https://saturncloud.io/blog/what-is-the-difference-between-jupyter-notebook-and-jupyterlab/#:~:text=If%20you%20are%20already%20familiar,is%20the%20way%20to%20go.)
```

(basic=)
# Step 2: Basic usage


# (slightly more advanced) Step 2: Setting up a conda environment

Note: If you go via the "more advanced" route of a conda environment and jupyter lab, you will likely need to allocate more time to troubleshooting your installation.


## Step 2: Setting up a conda environment

For Mac users, you will probably want `conda` and `pip` installed on your computer.

You can get conda here: [https://conda.io/projects/conda/en/latest/user-guide/install/index.html](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).  I would recommend *miniconda* (Here is the direct link for [installing miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)).  If you already have Anaconda, that is fine too.

We will also use jupyter notebooks in this course.

## Step 3: Installing jupyterlab

Jupyter 

You can install jupyterlab with conda

    conda install -c conda-forge jupyterlab=4.0.7 notebook=7.0.6

Since we recommend managing your environments, then conda (as above) is the better way to install it.  Otherwise you can use pip: [https://jupyter.org/install](https://jupyter.org/install).

If you already have Anaconda, then jupyter lab comes by default [explained here](https://test-jupyter.readthedocs.io/en/latest/install.html).

## Now, open this notebook in jupyter notebook.

Please record for yourself the steps you took to get jupyter running on your computer.

## (optional) setting up an environment

On a Mac, in a terminal window, you will create an environment using a specified version of python.

```
conda create --name seaocn_env python=3.8 -y
conda activate seaocn_env
```
