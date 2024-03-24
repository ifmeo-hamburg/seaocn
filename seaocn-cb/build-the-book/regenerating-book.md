
#  Regenerating the book after changes

## Build the book

1. Open a terminal window or command prompt

2. Navigate to where your book is located (for me, this is in `~/coursebook-OzMess/`)

3. Activate the conda environment

    conda activate mybook

4. Rebuild the html book 

    There are two ways to do this:

    **Using the `jupyter-book` command:** The standard code to regenerate the build locally on your computer is called from my directory `~/coursebook-OzMess/`, where inside this directory are the directories `~/coursebook-OzMess/ozmess-cb/_build/` is
    
    ```
    jupyter-book build coursebook-OzMess/ozmess-cb
    ```

    Note, if you accidently try to build `coursebook-OzMess/` which is the cookiecutter object, you'll get an error that you're missing a table of contents: "Couldn't find a Table of Contents file. To auto-generate one, run".  This is a good warning that you're trying to do this from the wrong directory.

    This will output to the terminal screen the location where on your computer you can find the regenerated files (and can be entered into your browser window to view)

    <!--
    file:///Users/eddifying/Library/Mobile%20Documents/com~apple~CloudDocs/Work/teaching/SeaOcn-UHH/2024-SeaOcn/05-github/onlinebook/seaocn-online/seaocn/_build/html/resource/website-build.html
    -->

    **Or continuously, using `sphinx-autobuild`**


    ```
    jupyter-book config sphinx coursebook-OzMess/ozmess-cb
    sphinx-autobuild coursebook-OzMess/ozmess-cb coursebook-OzMess/ozmess-cb/_build/html -b html 
    ```
    The first command will generate the required  `conf.py` file for autobuild.  This is run from the directory `~/OzMess-UHH/` containing `coursebook-OzMess/ozmess-cb/`, and writes the `conf.py` file into `coursebook-OzMess/ozmess-cb/`.

    The second command serves the local version of the generated book files.

    ```{tip}
    The first time you want to use sphinx, you will need to install it
    
        pip install sphinx-autobuild

    More information is:

    - [Jupyter book and sphinx](https://jupyterbook.org/en/stable/sphinx/index.html)

    - [Jupyter book and sphinx](https://jupyterbook.org/en/stable/explain/sphinx.html)

    - [autobuild with sphinx](https://github.com/executablebooks/jupyter-book/issues/1455)

    - [autobuild](https://pypi.org/project/sphinx-autobuild/)
    ```

## Push changes to github.com


From within `coursebook-OzMess/`,

```
git add .
git commit -m "a commit message"
git remote add origin git@github.com:ifmeo-hamburg/ozmess.git
git push -u origin main
```

## Adding pages

New content pages are added as `*.md` Markdown files in the root or subdirectories of `ozmess-cb`.  To add yaml frontmatter, use
```
jupyter-book myst init path/to/markdownfile.md
```

