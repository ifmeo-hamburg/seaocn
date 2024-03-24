
# Running Python (Windows)

So you've gotten python installed, but you don't remember how to run it. 

See [Quick Start guide (external)](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html)

# Running Python (Mac)


In the terminal window, run

```
jupyter notebook
```

It may be best if you've navigated to the directory where you'd like to work (or nearby). 

```{tip}
If you're *sure* you've used it on your computer before, but jupyter notebook is not running (e.g., Jupyter command `jupyter-notebook` was not found.`) then you may have activated an environment where you haven't yet installed Jupyter.

You can either deactivate the environment

    conda deactivate

Or install jupyter-lab in the environment

    conda install -c conda-forge jupyterlab=4.0.7 notebook=7.0.6

or with `pip` (jupyterlab)

    pip install jupyterlab 

or 

    pip install jupyter-notebook

```
