
```{admonition} Preparation (before class)
**Was due** This is the week when you need to prepare a slide with a figure which uses observations and equations together.  These should be added to the `shared_paper/` folder in the gitlab. 
```

# Instruments and platforms (*change week*)

```{margin} Moodle link
PDF of slides [here](https://lernen.min.uni-hamburg.de/mod/resource/view.php?id=185190)\ 
*Added 16 April*
```

We did "Instruments and platforms" this week (3) instead of week 4, since we didn't have enough of the papers uploaded for the discussion on Equations v data (was week 3).

This will be a whirlwind introduction to the platforms, sensors and instruments we have for measuring the ocean.  



## Lecture session - what we did

- Discussion of what is a "platform" and various platforms available for oceanography
- <span style="color:red;">Reminder(!)</span> that everyone was supposed to have uploaded their paper example, and that you must do so by Friday 19 April, to the gitlab `shared_paper/` folder.
- Reminder: that 10% of the course grade is determined from participation.  This will start from week 4.  For anyone who has already done this, it will be "bonus" so that if a later participation is missed, it will not count against you (up to the number that you have completed so far).

## Practical session - what we did

- Installing `pyGMT` turned out to be a challenge.  For folks using `conda` to manage environments, it took a while to download and install the package with required dependencies.  For folks not using `conda`, there were issues with `pip` but reasonably clear instructions are given on the [pyGMT website](https://www.pygmt.org/dev/install.html#) including needing to use an `[all]` option to get optional dependencies and various issues with kernels and paths.  <span style="color:red;">Read the docs on the [pyGMT website](https://www.pygmt.org/dev/install.html#)</span>.

- Downloading data from [ICDC](https://www.cen.uni-hamburg.de/en/icdc/data/atmosphere/reanalysis-atmosphere.html) was also not straightforward.  It turns out that you can only download without barrier if you're on the MPIM/CEN network; eduroam is not enough.   Since most students were working on their personal computers with eduroam for internet, this didn't work.
    - Solution 1: Log into the computers in the lab and download there.  Then move the file (30mb each) to your local computer.  "Moving" the file meant putting it on some cloud service (e.g., Google drive) and then downloading.
    - Solution 2: Get an account at ICDC.  To request an account, use the ICDC website: [contact form](https://www.cen.uni-hamburg.de/en/icdc/about-icdc/contact.html).  This may be possible for students, but is not verified.
    - Solution 3: *Not yet implemented*, figure out how to transfer files between your computer and the lab computers.  This may be possible by following or modifying the instructions on the [CEN-IT FAQ](https://www.cen.uni-hamburg.de/en/facilities/cen-it/support/faq.html#v-4455736).  
    - Solution 4: Use the lab computers for your practical exercises.  If you choose this option, you will have easier access to ICDC for data.  However, you will also need to use git from the command line rather than from an application (like "GitHub Desktop").

- By the end of the session, it appeared that all students who were present had git working on their computer.  This means: Being able to use git to commit your changes, and push them to the respository online, **not** uploading files to the repository using your web browswer.  




```{admonition} Lab topic: Maps
We will start making maps of spatial data in python.  You may be familiar with [cartopy](https://scitools.org.uk/cartopy/docs/latest/).  We will instead look at [pyGMT](https://www.pygmt.org/latest/).

See [Ex3](../exercise/exercise-map.ipynb) and check the Reading assignment ({cite:t}`Krause-Tomczak-1995`).  You may also want to browse the projections available at [pyGMT projections](https://www.pygmt.org/dev/projections/index.html).
```
