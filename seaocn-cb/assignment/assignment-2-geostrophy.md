---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Assignment 1


## Lab overview

**Aim:** The purpose of this assignment is to get you started with loading netCDF files, making figures and exporting figures to `*.png` files in Python.

**Learning outcomes:** At the end of this lab, you will be able to:

1. Load `nc`-files

2. Make a variety of figures including:
- a map (with coastlines marked)
- multiple line plots (time series) on a single axis
as well as annotate the figures and alter the colors and symbols used.

3. Evaluate code in an `*.ipynb` file, use *comments*.

4. Export figures in `*.png` format.

5. Use python libraries including: `matplotlib`, `xarray`

**Data:** The data files are available in the git repository.  

**Directions:** Answer the questions. You will also create a git repository with your code and 3 figures.

----
## Exercises
```{code-cell}
def make_fig(figsize):
    from matplotlib import rcParams, cycler
    import matplotlib.pyplot as plt
    import numpy as np
    plt.ion()

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    N = 10
    data = [np.logspace(0, 1, 100) + .2 * np.random.randn(100) + ii for ii in range(N)]
    data = np.array(data).T
    cmap = plt.cm.coolwarm
    rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


    from matplotlib.lines import Line2D
    custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                    Line2D([0], [0], color=cmap(.5), lw=4),
                    Line2D([0], [0], color=cmap(1.), lw=4)]

    fig, ax = plt.subplots(figsize=figsize)
    lines = ax.plot(data)
    ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
make_fig(figsize=(10, 5))
```


### Choose a site

Which site did you select?

### Create a notebook

Create an `*.ipynb` notebook containing the commands for this assignment.  Enter your commands in this window as you go along.

Name the file `lab1_plotting.ipynb`

### Load the data

Import necessary packages.  If you are missing any of these packages, please refer to [Resources: Python](../resource/python).

```
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
```

Import the dataset for the side you've selected.  Use the `print` command to see what has been loaded into your workspace.

**Comment the code**.  Preceding a line of code, add a comment in plain language to describe what the line of code is doing.

Note that comments in python are anything following the hash `#` symbol.

```{seealso}
See [How to use a python comment (external)](https://www.coursera.org/tutorials/python-comment?utm_medium=sem&utm_source=gg&utm_campaign=B2C_EMEA__coursera_FTCOF_career-academy_pmax-multiple-audiences-country-multi&campaignid=20858198824&adgroupid=&device=c&keyword=&matchtype=&network=x&devicemodel=&adposition=&creativeid=&hide_mobile_promo&gad_source=1&gclid=CjwKCAjwte-vBhBFEiwAQSv_xWfTbvEVGHJFclnneF5umIjP7dejb-zEN01wFFl_-1YPkdHnvzyElRoCYSgQAvD_BwE) for more information.
```

### Where is your site?  

Determine the latitude and longitude from the variables you've loaded.

### Fig 1. Make a map

Plot your site location using the `plt` command from `matplotlib`.  This command takes two inputs, in this case the x- and y-locations.  

- Experiment with optional additional inputs to change the symbol used for plotting (e.g., a circle or an x).

- To add context, add the coastlines to the figure.  First load the coastlines file, and then add another plot to your figure.

- Give the axes meaningful labels on the x- and y-axis (e.g., Longitude and Latitude).

- Make the coastlines thicker so they are easier to see.

- Use the `fontsize` option to increase the size of the font on the x- and y-annotations.

- Export the figure into a `*.png` format.  Name it `lab1_figure1.png`.

### Fig 2. Plot a time series

Plot the time series in red, using the time vector as the first input to the `plt` command and the sea surface temperature as the second input.

- What did you enter in the command window?

- Calculate the mean of the sea surface temperature time series.  What is the mean?

- Add the mean to the plot as a horizontal line

- Add a legend to the plot with names for the data

- Check the x-axis labels and experiment with replotting with time in another format.

- Export the figure as `lab1_figure2.png`.

```{seealso}
[Datacamp: Line plots with multiple lines](https://www.datacamp.com/tutorial/matplotlib-tutorial-python?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720818&utm_adgroupid=157156373751&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=691747307008&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9061056&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-eu_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-feb24&gad_source=1&gclid=CjwKCAjwte-vBhBFEiwAQSv_xXfFxBtd2VQDuYFYjE_oxEoteuw3LBK0epaNxiE3fLomsPbAZeyD4BoCKQwQAvD_BwE)
```

### Temporal coverage and resolution

- What time period do your data span?

- Determine the start date more accurately by extracting the first time point from your dataset.

    When do the data start?

- What is the temporal resolution of the data (aka, how far apart are successive measurements in time)?  This can be determined a number of ways.

    - print the first 3 elements of the time vector 
    - plot a few time dates to the screen
    - Calculate the difference between successive time measurements using the diff command

    What is the temporal resolution of the data?

### Characterise the data

- Calculate the median of the data

- Calculate the standard deviation of the data

- Calculate the maximum of the data

- Calculate the minimum of the data

- What is the range of the data (max minus min)

### Fig 3. Data distribution

- Using `plt.bar()`, create a histogram of the sea surface temperature data.

- Add a vertical line to show where the median is.

- Add appropriate x- and y-axis labels.  Make the fontsize legible.

- Export the figure as `lab1_figure3.png`.

```{seealso}
[Datacamp: Drawing bar plots](https://www.datacamp.com/tutorial/matplotlib-tutorial-python?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720818&utm_adgroupid=157156373751&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=691747307008&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9061056&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-eu_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-feb24&gad_source=1&gclid=CjwKCAjwte-vBhBFEiwAQSv_xXfFxBtd2VQDuYFYjE_oxEoteuw3LBK0epaNxiE3fLomsPbAZeyD4BoCKQwQAvD_BwE)
```

### Commit your code

Commit your code including figures in a `figures/` subdirectory into the git repository for the assignment.