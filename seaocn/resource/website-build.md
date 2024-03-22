# Setting up a jupyter book

Troubleshooting the page and getting it to appear properly in GitHub Pages took a little while.  I'll try to document the successful steps here.

Some useful references:
- [JupyterBook.org: Create your first book](https://jupyterbook.org/en/stable/start/your-first-book.html) - However the instructions are slightly different than the later instructions for [JupyterBook.org: GitHub Pages](https://jupyterbook.org/en/stable/publish/gh-pages.html) so what I've done is an amalgamation of the two.
- [cookiecutter-jupyter-book (repository)](https://github.com/executablebooks/cookiecutter-jupyter-book) - this is a flavour of jupyterbook which includes a GitHub Actions workflow, specifically for deploying the jupyterbook you've created onto github.

## Installing necessary items

### Install jupyterbook w/cookiecutter

```
pip install -U cookiecutter jupyter-book
```
this installs both `jupyter-book` and `cookiecutter` which we are using as a template to publish the book to GitHub Pages.

### Activate an environment 
From [cookiecutter](https://github.com/executablebooks/cookiecutter-jupyter-book), the first step is to create a virtual environment for creating the book:

The first step creates the environment called `mybook` and the second step activitates the environment in the terminal you're working in.
```
conda create --name mybook python=3.8 -y
conda activate mybook
```
This uses [conda](https://docs.conda.io/en/latest/) for dependencies.  Each time you want to use the environment, only run the second line.

### Create the book

Choose a directory within which your book will be located.   

- For me, this was `coursebook-Seaocn/`. 

Running the cookiecutter code will prompt you for your Name, github username, name and slug for the course, etc.  

- Since I am hosting them on an *organisation* in github, ``ifmeo-hamburg`` this is what should be used for the github username, since it appears in the generated `_config.yml` file as `url: https://github.com/ifmeo-hamburg/<book-slug>`.

From within `teaching/SeaOcn-UHH/`, to generate the initial jupyter book structure and template files, I run
```
jupyter-book create --cookiecutter coursebook-Seaocn/
```


<!--# pip install ghp-import  # This wasn't working with git authentication
jupyter-book create --cookiecutter mybookpath/
```-->

in `coursebook-Seaocn/seaocn/`
<!--#jupyter-book toc from-project seaocn/-->
```
jupyter-book build seaocn/
```

### Prepare the repository

I followed the steps on [cookiecutter](https://github.com/executablebooks/cookiecutter-jupyter-book):

***On GitHub.com***

Create a new [GitHub repository](https://github.com/new).  

- I changed the "owner" to the organisation "ifmeo-hamburg", and
- Gave it a repository name "seaocn" which does not have to match your local repository name
- Set the repository to "Public" 
- Leave UNTICKED the "add a Readme file"
- Leave UNTICKED the choose a license

Note: These last two are important since otherwise the repository will not be empty, and when you first try to push to it, you will need to reconcile the divergent parts.

***On local computer:***

Setup the `.gitignore` file within the directory `onlinebook/seaocn-online`.  Here, I added .DS_Store since Mac's like to make this funny little piece of code.  To create/edit the file in this directory, I used `pico .gitignore` and added the lines
```
.DS_Store
```
<!--_build/-->

Prepare to load it online on Git to deploy as GitHub Pages.  From within `coursebook-OzMess/ozmess_coursebook`, 
```
git init
git add .
git commit -m "first commit"
git remote add origin git@github.com:ifmeo-hamburg/ozmess.git
```
This all worked, but the following line threw an authentication error
```
git push -u origin main
```


```{tip}
This is where you need to use the access token you've created (*but NOT put anywhere within the repository*)

    git config --global credential.helper '!f() { sleep 1; echo "username=<USER>:token=<TOKEN>"; }; f'
    
and

    git remote set-url origin https://<USER>:<TOKEN>@github.com/ifmeo-hamburg/seaocn

```

Then you should be able to


```
git push -u origin main
```

<!--
```
cp -r mylocalbook/* myonlinebook/
```
So modified for my paths, this becomes
```
cp -r mybookpath/seaocn/* onlinebook/seaocn-online/
```
-->
<!--#cp -r mylocalbook/* myonlinebook/
#git subtree push --prefix _build origin gh-pages-->

### Edit the GitHub Actions workflow

The [cookiecutter](https://github.com/executablebooks/cookiecutter-jupyter-book) contains a workflow to publish automatically to the `gh-pages` branch of your repository.  However, I found that it was failing to run.

This workflow is named `deploy-book` and can be found in the file `.github/workflows/deploy.yml` in the directory `onlinebook/seaocn-online`.  If you're on a Mac and looking for it in the Finder, you won't see it.  (The leading `.` means that it is hidden.)  To see hidden files, while in the Finder window use a `Command+Shift+Dot` (the period key). 

Open the `deploy.yml` file on your local computer.  I needed to change the following lines:

- L26 `- uses: actions/checkout@v3` to `- uses: actions/checkout@v4`
- L30 `uses: actions/setup-python@v4` to `uses: actions/setup-python@v5`
- L47 `path: "_build/html"` to `path: "seaocn/_build/html"`
- L52 `uses: actions/deploy-pages@v2` to `uses: actions/deploy-pages@v4`




## Use of tokens

To authenticate with GitHub, you need to generate a personal access token.  Username and password will not work.

I followed instructions here:
[https://www.squash.io/how-to-authenticate-git-push-with-github-using-a-token/](https://www.squash.io/how-to-authenticate-git-push-with-github-using-a-token/)

**On GitHub.com** 

1. Login and click your profile in the top right, then select "Settings"

2. Scroll down on the left side bar and click "Developer settings" and select "Personal access tokens (classic)"

3. Click on the "Generate new token (classic)" button.

4. Give it a descriptive name (I put my name and the repository I'm using it for in the name, e.g., "eleanorfrajka-seaocn").  But note that it is not repository-specific.

5. Select the desired scopes: For git operations you need to select the "repo" scope.

6. Click on the "Generate token" button at the bottom of the page.

7. GitHub will generate a token and show it to you *once*. Copy this token and put it somewhere useful but **not in your github repository**.  This is like a password, and you don't want to share your password.  If for some reason you want to keep it in your repository, then add it *only* on your local computer e.g. in a filename like "token.txt" and immediately add that filename to your ".gitignore" file.  But generally, *do not* put it in your repository.

```{note}
Do not put this token *anywhere* within your git repository!
```

**On your local computer**

1. Open a terminal window or command prompt

2. Set the token as a credential helper by running the following command, replacing `<TOKEN>` with your generated token,

    git config --global credential.helper '!f() { sleep 1; echo "username=<USER>:token=<TOKEN>"; }; f'

<!--
#ghp-import -n -p -f _build/html
-->

```{seealso}
- create gh-pages branch in existing repo 
https://jiafulow.github.io/blog/2020/07/09/create-gh-pages-branch-in-existing-repo/

- Authentication for git push with token
https://www.squash.io/how-to-authenticate-git-push-with-github-using-a-token/
```



## To create 
```git checkout gh-pages
git commit -m "Add files"
git push origin gh-pages
git checkout main```

---
Ok, after pushing to a gh-pages, the website is viewable here; https://ifmeo-hamburg.github.io/seaocn/intro.html
But it's possible that all I needed to do was to create the empty gh-pages and then the deploy script would work

# Regenerating the book after changes

## Step 1
```
conda activate mybook
```

## Step 2: Using jupyter-book, OR

The standard code to regenerate the build locally on your computer is

called from my directory `~/onlinebook/seaocn-online/`, where inside this directory are the directories `~/onlinebook/seaocn-online/seaocn/_build/` is
```
jupyter-book build seaocn
```

This will tell you where on your computer to find the regenerated files.

### Step 2: Continuous rebuild using sphinx

To setup with sphinx, I followed instructions here (https://jupyterbook.org/en/stable/sphinx/index.html)

```
pip install sphinx-autobuild
jupyter-book config sphinx seaocn-online/seaocn
```

Then serve the local, run from within the directory `~/onlinebook/`.
```
sphinx-autobuild seaocn-online/seaocn seaocn-online/seaocn/_build/html -b html 
```
Or from within the directory `~/onlinebook/seaocn-online/`,
```
sphinx-autobuild seaocn seaocn/_build/html -b html 
```
requires: https://pypi.org/project/sphinx-autobuild/
