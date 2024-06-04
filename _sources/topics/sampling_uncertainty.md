

# Sampling & Uncertainty

```{margin} Moodle link
PDF of slides [here](https://lernen.min.uni-hamburg.de/pluginfile.php/411403/mod_resource/content/1/2024-lecture-sampling_uncertainty-seaocn.pdf)\    
*Added 2 June (draft)*
```

We will discuss issues of uncertainty specific to field oceanography (as distinct from e.g., laboratory sciences).  We will not discuss in detail error propagation or statistical techniques.

```{seealso}
If you need to *do* uncertainty analysis, please see {cite:t}`Coleman-Steele-1999` chapters 2 "Statistical Considerations in Measurement Uncertainties", chapter 3 "Planning an Experiment: General Uncertainty Analysis" and maybe chapter 4 "Designing an Experiment: Detailed Uncertainty Analysis".

Or, for a straightforward description of practical error handling for oceanography, see {cite:t}`Emery-Thomson-2004`, chapter 3 "Statistical Methods and Error Handling".  
```

```{admonition} Lab topic - Working with glider data
Note: This exercise is more advanced, showing how data can be dynamically loaded.  [Exercise 7](../exercise/exercise-glider-demo.ipynb).
```
<!--*Please try to catch up on the exercises.*  From week 5/6 you will have an assignment in python.  It will build on the python and methods you've been developing so far, but will require you to creatively combine what you've learned to make progress.
-->

```{admonition} For 2 weeks from now
We will talk about "good scientific practice", sometimes also called "scientific integrity" or "research ethics". 

Recommended: Read snippets of {cite:t}`DFG-code-2022`, especially guidelines 12-14.  The whole thing is only 28 pages long.  


Additionally or alternatively, find a statement on good scientific practice from a funding agency in another country or at UHH, or see the resources below:
- Browse the DFG Research Integrity website [here](https://wissenschaftliche-integritaet.de/en/).
- UK BBSRC (biology): [here](https://www.ukri.org/who-we-are/bbsrc/our-policies-and-standards/safeguarding-good-scientific-practice/)
- US NSF: [Scientific integrity in "Post Award Requirements"](https://new.nsf.gov/policies/pappg/24-1/ch-11-other-post-award-requirements#m-scientific-integrity-b09) and [Responsible and Ethical Conduct of Research](https://www.nsf.gov/od/recr.jsp).
- Online Ethics Center for engineering and science [here](https://onlineethics.org/resources) including e.g., [Infusing Ethics in Research Groups: A Bottom-Up Context-Specific Approach](https://advances.asee.org/infusing-ethics-in-research-groups-a-bottom-up-context-specific-approach/)
- UHH's Research Integrity office [here](https://www.uni-hamburg.de/en/forschung/wissenschaftliche-integritaet.html) and [bylaws (German only)](https://www.uni-hamburg.de/en/forschung/wissenschaftliche-integritaet/gute-wissenschaftliche-praxis/satzung.html); also [training offers](https://www.uni-hamburg.de/en/forschung/wissenschaftliche-integritaet/gute-wissenschaftliche-praxis/weiterbildung-netzwerke.html).

We will specifically discuss authorship, documentation and the role of research software in reproducible science.
```