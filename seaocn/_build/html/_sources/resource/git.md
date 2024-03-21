# Git

## Git on Windows

### Software needed

For beginners, please download and install:
- [git](https://git-scm.com/downloads) - this is the software for version control of your code on your computer, and syncing the local changes with changes on a repository online.
- [miniconda (python + jupyter)](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html) - you can install this with miniconda, but if you already have anaconda, then you don't need to install anything new.
- [github desktop](https://desktop.github.com) - this is a desktop application which gives you a graphical user interface for working with git.  When you install this, it will prompt you to sign in.  You *do not* need to sign in.  There is a greyed out option "skip this step".  Go ahead and skip it.

### Cloning the course repositories

Once you have the software installed, you will want to first clone the class repository.  The repositories we use will live on the UHH gitlab server: [https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/ifm-ozmess/ozmess-2024](https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/ifm-ozmess/ozmess-2024).  Within this folder, there are several individual 'repositories'.  You will want to clone each of them.

Each of these is an individual "repository":
1. Lab 1 Cell thermal mass - [https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/ifm-ozmess/ozmess-2024/lab-1-cell-thermal-mass](https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/ifm-ozmess/ozmess-2024/lab-1-cell-thermal-mass)
2. Lab 2 Salinity accuracy and precision - [https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/ifm-ozmess/ozmess-2024/lab-2-salinity-accuracy-and-precision](Lab 2 Salinity accuracy and precision)
3. Field excursion - [https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/ifm-ozmess/ozmess-2024/field-excursion-cuxhaven](https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/ifm-ozmess/ozmess-2024/field-excursion-cuxhaven)

You may need to "request access" to the repository.  

1. Access the **course group gitlab**: [https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/ifm-ozmess/ozmess-2024](https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/ifm-ozmess/ozmess-2024) and select a repository.

2. If you are prompted to request access, then do so.  You will need to log in with your B-kennung.

Then you need to clone the repository.  For this, have a 

1. A browswer window open (edge, chrome, safari, firefox, etc) and navigate to the **group gitlab**.  

2. Github desktop (purple)

Decide where on your computer you want these folders to live.  If you don't specify, the default is something like `Documents\GitHub\lab-2-Salinity-accuracy-and-precision`.  

1a. In Github desktop, select "clone a repository", and click the "URL" at the right.

2a.  In the browser window, select the address of the repository you would like to clone first.  Copy this address (starting with https:)

1b. In Github desktop, past the URL of the repository into the first text box.  The second text box will auto-populate with a location on your computer.  If you'd like to change this from default, use the button to the right to pick where these will live.  Click "ok" or "next".  *Authentication will fail.* Kein problem.

2b. In the browswer window on the chosen repository (must match the one you used in the previous step), click on "settings" at the bottom of the list to the left.  Choose "Access tokens".  Near the top right, click "Add new token".  Give it a name (maybe your name).  Choose an expiration date at least 1 month in the future but no more than 12 months into the future.  Select a role "maintainer".  Scroll down over all the choices and click "create project access token".  In the green bar that appears, click the "clipboard" button to copy this token.

1c.  In Github desktop, enter your B-kennung in the top text bar "username", but for "password" paste the access token that you just copied.  Click "next".

You should now have cloned the repository.  Check that the repository (which may be an empty folder) lives on your computer.  

**Repeat this step for the other course repositories.**

# Super-brief explanation of git

Git is keeping track of changes to your files within the local repository (your copy of the course folder on your computer).  When you change a file in the folder, git knows.  How do you know it knows?  If you go into your Github desktop (purple icon, desktop app) and choose the repository you're working in in the dropdown menu on the left, and you have changed a file, the filename  for the file with changes will appear in a list, and to the right you can preview the changes that have been made (previous commit and current edited version).  

After you've been working on a file for a while (a day, an hour, 5 minutes, etc), e.g. a piece of code in your repository on your computer, and you've made some important changes, you will want to tell git to save a snapshot of these changes.  To do this you click **commit** in Github desktop.  This will then make git store a version according to the point in time when you clicked commit.  *Advanced tip: in the commit message, you can write something useful to describe the changes, like "added a new function to load data from a microcat".*  So far, only your own computer knows about these changes.

When you want to share these changes with your group, i.e. have these changes show up in the repository on the gitlab.rrz.uni-hamburg.de location, then you need to **push** the changes.  This is a button to the right in your Github desktop (or top right), where you click.  This will then make the changes appear in the online copy of the repository.

When your group member has made changes, and you want these changes to appear in your copy of the code on your own computer, then you need to **fetch** these changes from the version on gitlab.rrz.uni-hamburg.de.  This will not overwrite any of your files.  It will simply add what they have done.

**Note:** For beginner usage, I recommend that you all keep a separate copy of your python code to start with.  If you work on the same piece of code, it's possible for you to delete something and commit it to your repository (on your own computer), and for someone else to edit the same thing without deleting it and commit it on their own computer.  If you both then push these changes to the repository, or you fetch your colleagues changes from the online repository onto your computer, you will get a **conflict** which needs to be merged manually.

Read more: [https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)

