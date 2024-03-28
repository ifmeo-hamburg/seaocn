# Syllabus (SuSe24)

Seagoing Oceanography

## Meeting times

This class meets on Tuesdays from 08:15 - 9:45 in Bu53 133, and on Tuesdays from 10:00 - 11:45 in Geom. 1335 for the required computer lab section.  

## Instructor information

Prof. Eleanor Frajka-Williams

- Office: Bu53 244
- E-mail: eleanor.frajka@uni-hamburg.de
- Phone: 
- Office hours: TBD

(course_assistant)=
Emelie Breunig
- Office: Bu53 25X
- e-mail: emelie.breunig@uni-hamburg.de



```{admonition} Greetings!
This is a new course for SuSe2024, where we are going to try to develop your insight into how to handle observational data using examples which are unique to observations (rather than generic data handling for oceanographic data) and also engage in practical thinking and planning about seagoing research expeditions.
```

## Purpose of the Course

Broadly speaking, the purpose of this course is to teach you to think carefully about making and using *in situ* oceanographic observations.  This course is complementary to the more theoretical or numerical courses you will take, when you learn about what the ocean does according to theory or models.  Here, you think critically about how *measurement principles* affect the data reported by *in situ* oceanographic instruments, and how treatment of incomplete information (a necessity with observations) can affect calculated quantities.

To develop your intuition, we are taking a practical approach - using data collected from one or another research cruise, which you will then process and perform basic analyses.  For this first version of the course, the focus will be on CTD data as it is the fundamental measurement of physical oceanography and *if you end up participating in a research cruise* you have a high chance of encountering CTD data.  We will align most of the practical work with a case study of measuring the Atlantic meridional overturning circulation (or AMOC).


## Course objectives

The overarching objective is that after this course, you will be able to design a seagoing expedition, collect, handle and process *in situ* oceanographic data towards answering a specific research question.

Note however, that we cannot do everything!  
- Towards designing a seagoing expedition, you will think particularly about how to timetable an expedition to meet your observational needs (but we will spend less time discussing how to decide your observational needs, which would be against a particular research hypothesis or question).  We'll also look at the formal process of writing a proposal for shiptime in the German system, the international requirement for dipclears, considerations of timing, logistics, risks and costs.
- For collecting, handling and processing data, you'll get a little experience with setting up and downloading a CTD instrument, but more of the focus will be on what you do with the data once it is on a computer in raw format.  This will then include the standard processing and conversion steps, evaluating the data quality (what can go wrong, and how do you identify it in a dataset), and carrying out practical examples of onward processing steps to see how data treatment choices can affect your calculation in the end.

Three main things I want you to be able to do at the end of this course:

1. Navigate the process of cruise planning from *after* having a research idea, to planning and proposing a cruise.

2. Given a CTD dataset, be able to handle the data in raw format, identify from data whether there may be a problem and address it, and evaluate whether your processing steps may be affecting your calculated results.

3. Peform standard manipulations of oceanographic data, including  creating typical plot types, basic time series analysis, filtering, gridding and gap filling, calculating salinity, density, buoyancy frequency, dynamic height, horizontal density gradients, geostrophic velocity and ocean transports.


## Resources
**The course Moodle site**
I will post links to websites relevant to the course here, as well as datasets that you will need for the projects and exercises.  I will also open a [Moodle forum](https://lernen.min.uni-hamburg.de/course/view.php?id=3675#section-0) where you can post questions/comments to each other, or to me and the course assistant.  If a topic or question is of general interest/information, then I prefer you use the moodle forum rather than e-mailing me individually.  **Please check the Moodle for any updates to the schedule.**

## Expectations for students

You are expected to start the course with a basic understanding of ocean processes - you should have an idea of why we measure salinity, and how density appears in the equations of motion.  This knowledge will be assumed.  Additionally, we expect you already have some experience with a programming language.   We will cover some of this in the course (specifically, Python), but if your Python is relatively weak, then please do your best not to get behind.  It will be very difficult to catch up otherwise.  You may find some additional online resources for working on your python skills.  See for example [Python for Earth Scientists](https://github.com/ltauxe/Python-for-Earth-Science-Students/blob/master/_TableOfContents.ipynb).

**Participation is expected.** This will take several forms during the course: preparation for discussion topics to be held during class, presentation of figures at the start of the class from the previous week's computer session, and formal (graded) presentations after reports on projects are handed in.  You learn more (and enjoy it more) when you're engaged with the course and the material.




## Evaluation

Unless otherwise specified, assignments (reports) are due **Wednesdays at 23:59**.

1. The **two projects** form the core assessment of the course: One focusing on data handling and treating instrumental issues and the second including a further calculation of a more complicated dataset, where you will additionally assess how the measurement strategy, and/or  gridding or processing steps affect a final calculation of interest.  You are encouraged to work on these in class and to discuss with classmates during the lab sessions.  However the work graded will be individual.  

2. One **group assignment** to produce the core elements of a cruise proposal.

3. Participation and in-class assignments.  During the course, you may be asked to present work from a previous week's practical exercise.  

## Grading procedures

```{list-table} Grading
:width: 100
:widths: 70 30
:header-rows: 1

* - Grade component 
  - Weight
* - In-class and participation
  - 10%
* - Group assignment: Cruise planning
  - 10%
* - Assignment 1: Python
  - 40%
* - Assignment 2: Python
  - 40%
* - **Total**
  - 100%
```

## Late assignment policy

The good news is that you can sugmit an assignment up to **5 (five)** days late (with the exception of the group projects).  I will base this on the Moodle timestamp for when the work was submitted. (1 second to 24 hours late = 1 day late.  24:00:01 hours to 48:00:00 hours late is 2 days late.) The bad news is that you will lose 10% each day it is late.  (1 day late = graded score x 90%.  2 days late = graded score x 80%).  Late work makes a class harder to administer.  If you have a good excuse (such as being very sick), you should contact the instructor as soon as is practicable.  

## Succeeding in the course

My aim is for you all to be successful in this course, however you will need to put in effort, thought, curiousity, programming time, to make this happen.  You are strongly encouraged to discuss ideas and problems with each other, including discussing approaches for the coding assignments.  Collaboration not only helps get the job done, it teaches you how to explain your ideas to others.  However, for marked assignments, you must write the actual code and report alone. 

This is a fine line.  You will have some unmarked (ungraded) assignments where you can share code snippets with each other and work together more closely.  In these cases, you may have some pieces of code in your repository which are identical to another student's code.  If this is the case, please note the original author(s) of the code as a comment in the code.  If you then reuse this code for the marked assignment, that is acceptable.  If new code is needed for the marked assignment, this should *not* be copied from another student.  Instead, you can discuss approaches together, but should write your code individually.

### Getting help

If you realise you are not understanding things as well as you could, or are finding yourself lost during practicals, please take note of these opportunities to support your learning:

- **Your peers:** Working together with other people learning the same material is an excellent way to gain a deeper understanding of concepts. I highly recommend exchanging contact information and meeting up to discuss the class or practials.
- **Lab sessions:** Lab sessions are timetabled as required and led by the [course assistant](#course-assistant).  Their purpose is to help you work through problems and gain practical experience.
- **For clarifications on the assessment:** Please ask the instructor during office hours, or post questions on the course forum (if you can do so without giving away the solution).  For questions and clarifications on formative problems, you may confer with your peers, course assistant, instructor and on the forum.
- **Errors/typos:** For these and other issues that may be useful for the whole class to be aware of, please use the forum.

Is this course taking too much of your time?  It is timetabled as taking 124 hours of your time outside of class meeting times.  This is about 9 hours per week.  If on average you are spending significantly more than this, please let me know via e-mail.  Sometimes it is hard to judge the difficulty of the course, and your message can let me know when there is a problem.

