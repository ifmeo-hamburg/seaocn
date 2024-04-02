# Exercise 0a - Git 


**Aim:** The purpose of this exercise is to get you working with git.

**Context:** For this course, we will use a single repository for un-graded exercises.  Within this repository, you will each have your own directory with your working files.  Note this is for un-graded exercises, where you are *encouraged* to work collaboratively with people in the class.

**Goals:** At the end of this exercise, you will have

- Cloned the course repository on your computer/UHH account
- Created a directory within the repository *following the naming convention*
- Created a file called `readme.md` within your directory.
- Pushed the repository (with your new file and directory) back to the course repository
- Verified that you can see the changes (with your directory) on the web
- Edited the `readme.md` including instructions for *you* on how to edit your files and push/fetch them from the repository.
- Created a `pull` or `merge` request tagged with instructors to let us know it worked.

**Measure of success:** We will receive your `pull` request, including your folder in the course repository with a `readme.md` file that has been populated with notes.

<hr>

## Step 1: Check whether you have git installed.

````{margin}
```{attention}
Note to instructor: These instructions need to be updated - based on troubleshooting for students during practicals.
```
````
On a Mac or linux, in a terminal window, run

```
git --version
```
If it runs, you have git.

On Windows, you can possibly find it by searching in the start menu.



### If you don't have git, install it

Please refer to [Resources: Git and Python](../resource/git).

Or see [Installing Git (external)](https://www.linode.com/docs/guides/how-to-install-git-on-linux-mac-and-windows/)

## Step 2: Clone the course repository for exercises
  
```{note}
The instructions below assume you are using GitHub desktop which is a desktop application for interacting with any online git (i.e., you do not need a github account.)  See also [Resources: Git and Python](../resource/git) for installation of GitHub desktop.
```

Once you have git installed, you will want to clone the class repository.  The repositories we use will live on the UHH gitlab server **group gitlab**: [https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/IfM_SeaOcean/uhh-seaocean-2024](https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/IfM_SeaOcean/uhh-seaocean-2024). Within this folder, there may be multiple individual "repositories" or "projects", and multiple "subgroups".  For today, you will want to clone the repository for exercises.

The "Exercises" repository is [https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/IfM_SeaOcean/uhh-seaocean-2024/exercises-seaocn](https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/IfM_SeaOcean/uhh-seaocean-2024/exercises-seaocn).

Now you will clone the repository.  For this, have a

1. A web browser window open (edge, chrome, safari, firefox, etc) and navigate to the **group gitlab**.  

2. Github desktop app open (purple)

Decide where on your computer you want the repository folder to live.  If you don't specify, the default is something like `Documents\GitHub\<repository-name>`. You can put it anywhere, but *make a note of where you put it so you can find it again.*

1a. In Github desktop, select "clone a repository", and click the "URL" at the right.

2a.  In your web browser window, select the address of the repository you would like to clone first.  Copy this address (starting with https:)

1b. In Github desktop, past the URL of the repository into the first text box.  The second text box will auto-populate with a location on your computer.  If you'd like to change this from default, use the button to the right to pick where these will live.  Click "ok" or "next".  *Authentication will fail.* Kein problem.

2b. In the browser window on the chosen repository (must match the one you used in the previous step), click on "settings" at the bottom of the list to the left.  Choose "Access tokens".  Near the top right, click "Add new token".  Give it a name (maybe your name).  Choose an expiration date at least 1 month in the future but no more than 12 months into the future.  Select a role "maintainer".  Scroll down over all the choices and click "create project access token".  In the green bar that appears, click the "clipboard" button to copy this token.

1c.  In Github desktop, enter your B-kennung in the top text bar "username", but for "password" paste the access token that you just copied.  Click "next".

You should now have cloned the repository.  Check that the repository (which may be an empty folder) lives on your computer.  

<hr>

## Step 3: Make your directory in the repository 

You should do this *on your local computer* or on the UHH computer, *not* in a browser window viewing the respository at gitlab.rrz.uni-hamburg.de.  There, the "remote repository" is located.

1. Create a folder. On your computer, navigate to where you have cloned the repository, and create a new folder (aka directory).  

    ```{admonition} Naming convention: your folder

    Please name your folder `seaocn-exercises-<Lastname>` where you replace `<Lastname>` with your last name.

    Naming conventions will be *important* in this course.   Here they are particularly important because--to start with--the `.gitignore` file in the directory is initialised with the directory names of the course participants so that you do not always download the changes they make to their course files.  
    ```

2. Add a file named `readme.md`.  Here the ending `*.md` means that it is a markdown file, which is a simple formating or "markup" language.  (In contrast, Latex and html are more complicated "markup" language.

    ```{seealso}
    You will use markdown to add slightly fancier comments in your python notebooks.  To find out more, see [Getting Started with Markdown (external link)](https://www.markdownguide.org/getting-started/).
    ```
    
    Edit your `readme.md` file to include the location (on your computer) of where the repository files can be found, and instructions for yourself about running git.  This should be detailed enough that you can find it again as you're working through the files. 

    When you realise there is more information/notes you want to take about how to get git and (later) python running on your computer, make these notes here!
    
3. Push your local repository to the remote (at gitlab.rrz.uni-hamburg.de).  **Note, this may be the trickiest step.**

You may need to 

- Request access to the repository.  If so, you will need to log in with your B-kennung, and use the three dots in the upper right to select "request access". This will need to be manually approved by e.g. Emelie or Eleanor, so it will take a little time.

- Generate a personal access token (see above).


## Step 4: Verify success

Go to [https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/IfM_SeaOcean/uhh-seaocean-2024/exercises-seaocn](https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/IfM_SeaOcean/uhh-seaocean-2024/exercises-seaocn) and check that your repository exists.

Create a pull request.