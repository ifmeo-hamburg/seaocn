# Assignment 1 - CTD profiles


**Aim:** The purpose of this assignment is to evaluate the sensitivity of CTD profiles (and various derived quantities) to the choices made during Seabird processing for constants applied in align CTD and cell thermal mass correction.

**Learning outcomes:** At the end of this lab, you will be able to:

1. Apply align CTD and cell thermal mass corrections to Seabird CTD data

2. Evaluate whether your chosen parameters are appropriate.

**Data:** You should use CTD profiles from one of the exercises (at least 1000~m water depth) and available in raw.

**Directions:** Produce a summary report and git repository of your analysis.

----
## Guiding questions

### Background

- What is the align CTD and cell thermal mass correction procedure?  Why do we need to do them?

- How do the numbers in the software relate to what is going on in the sensor?

### Data

- Where are your data from (lat, lon, cruise name, region)?  and when?

### Objective

Your objective is to evaluate the sensitivity of *something* to do with the CTD profile to a range of choices made for align CTD and cell thermal mass.

- What values are typical for the align CTD?  

- What values are typical for cell thermal mass?  

Check the literature (e.g. Emery and Thomsen or Lueck 1990, or the Seasoft manual).

## Choosing a metric

For the "*something*", you should identify 1--2 metrics to try to quantitatively assess which parameter value is correct.  

- Think about the profiles and what the parameter values are doing.  Do you have an idea of what a "bad" profile outcome looks like?  I.e. if you give the software something very wrong for align CTD and positive, what does the resulting profile look like?  Or very wrong and negative?

- Use what you understand about why we apply these corrections, and your experience with testing a few values, to decide on a metric for evaluating which parameter choice is "right".

## Evaluating sensitivity

- You will need to run the Seabird processing for a range of values at small increments.  This would be done on the seagoing laptop computer(s).  You can share the various processed versions with the other folks doing this assignment.

- OR, code Seabird processing in your python.  The behaviour of alignCTD is straightforward (offset in time).  Cell thermal mass is more complicated.

