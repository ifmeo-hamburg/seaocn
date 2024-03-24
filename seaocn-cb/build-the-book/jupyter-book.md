
#  Installation

For this, I assume you already have git.  If not, then you'll also need to get [git](https://git-scm.com/downloads).

## Install jupyterbook w/cookiecutter

```
pip install -U cookiecutter jupyter-book
```
this installs both `jupyter-book` and `cookiecutter` which we are using as a template to publish the book to GitHub Pages.

## Activate an environment 
From [cookiecutter](https://github.com/executablebooks/cookiecutter-jupyter-book), the first step is to create a virtual environment for creating the book:

The first step creates the environment called `mybook` and the second step activitates the environment in the terminal you're working in.
```
conda create --name mybook python=3.8 -y
conda activate mybook
```
This uses [conda](https://docs.conda.io/en/latest/) for dependencies.  Each time you want to use the environment, only run the second line.



## Create the cookiecutter jupyterbook

Choose a directory *within which* your book will be located. For me, this was `OzMess-UHH/`. 

1. Navigate to your chosen directory (e.g., `OzMess-UHH/`)

2. Run the code to create the book

    ```
    jupyter-book create --cookiecutter .
    ```
    Running the code will prompt you for 
        - your Name (e.g., Jane Smith), 
        - your github username *or organisation* (e.g., `ifmeo-hamburg` is the organisation name I used) - this is used in generating the `_config.yml` file for the `url: https://github.com/<USER>/<book_slug>`, 
        - choose the bookslug (e.g., `ozmess-cb`), and the appropriate license (I used defaults).



3. (optional) **Manually rename** the first directory with your <book_slug> to something else, for better keeping track of what's happening where.  Here, I renamed this to `coursebook-OzMess`. 

4. Navigate into the cookiecutter book level to build the html-version of the book (e.g., in `coursebook-OzMess/`)

    ```
    jupyter-book build ozmess-cb/
    ```
