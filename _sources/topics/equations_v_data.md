
```{margin} Gitlab link
[shared_papers/](https://gitlab.rrz.uni-hamburg.de/ifmeo/teaching/IfM_SeaOcean/uhh-seaocean-2024/exercises-seaocn/-/tree/main/shared_papers?ref_type=heads)
```
```{admonition} Preparation (before class)
**For 19 April:** This is the week when you need to prepare a slide with a figure which uses observations and equations together.  These should be added to the `shared_paper/` folder in the gitlab. 

Note: This was for 16 April, but only received 6 submissions.
```

```{margin} Moodle link
PDF of Krause [here](https://lernen.min.uni-hamburg.de/pluginfile.php/407209/mod_resource/content/1/8-1_krause.pdf)\
*Added 16 April*
```
```{admonition} Preparation (before computer practical)
- **Read** {cite:t}`Krause-Tomczak-1995` before completing your mapping exercise.
```

# Equations v data

We will discuss what kinds of data can be recorded in order to enable further calculations with the data after the fact.

This should be based on what students bring to class.

```{margin} Moodle link
PDF of slides [here](https://lernen.min.uni-hamburg.de/pluginfile.php/407853/mod_resource/content/2/equations_v_data-seaocn.pdf)\ 
*Added 23 April*
```

## Lecture session - what we did

After a brief discussion about teaching vs learning, and the reasoning behind what we're doing here (to start you the students thinking about how we set up field programs or analysis plans based on the desired endpoint), we went through the slides submitted by everyone on a paper, then reduced the list to 3 papers to discuss in groups of 3-4 students.  These were

- Flexas et al. using the Omega equation

- Hansen et al. (2023) estimating transports with in situ and altimetry

- Bilo + Johns (202X) tracing the spread of LSW  using PV from Argo data.

Discussions were focused on identifying (first 3) and then thinking about (4) - the choices and decisions being made in order to get towards answering the question, designing the field program and computing the main figure.

1. What is the question or problem being solved?  What do they want to know about the ocean?  Why use observations (as opposed to some other tool)?

2. What data are being used?  What type/parameter, what is the resolution (time, horizontal space, vertical) and what was the thinking behind the sampling strategy?

3. What's the main figure that demonstrates the take home message, or the new information about the ocean?

4. What had to be done to get to this main figure?  

    - What were the requirements of the data (need to be "quasi-synoptic", need to be high vertical resolution, need to resolve tidal variations, need a certain minimum horizontal resolution, need high accuracy to measure small changes)?

    - What choices needed to be made in the: sampling strategy, processing steps, calculations (discretization, gap-filling, filtering)?


```{margin} Moodle link
PDF of Bryden [here](https://lernen.min.uni-hamburg.de/mod/resource/view.php?id=185751)
*Added 23 April*
```
```{admonition} Lab topic - Transport 
You will use data from hydrographic sections to compute geostrophic transport.  

See [Ex4](../exercise/exercise-geostrophy.ipynb). You may find it useful to read {cite:t}`Bryden-etal-2005` (or references therein about computing geostrophic transports from sections).
```

```{warning} 
~~**For 30 April:** You should have read {cite:t}`Krause-Tomczak-1995` before the computer practical on Apr 23, and prepared figures for the `shared_figure/` folder from [exercise 3 - maps](../exercise/exercise-map.ipynb).~~

**On 23 April:** We made the *pyGMT* part of Exercise 3 optional.  Note: ONLY the pyGMT part.  You should still be able to make filled-in color maps, and I am hoping that if you don't use pyGMT, then you have some ability to use `cartopy`.  If not, then I recommend still working through `pyGMT` in your own time.  Next week, we will discuss figures for those of whom they are available, and also the reading (see above, Krause paper).
```

