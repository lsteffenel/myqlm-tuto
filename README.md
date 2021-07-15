
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lsteffenel/myqlm-tuto/HEAD?filepath=0_Start_Here.ipynb)


# Getting Start


## Before starting: know your environment
If you are running this tutorial in [mybinder.org](https://mybinder.org/v2/gh/lsteffenel/myqlm-tuto/HEAD?filepath=0_Start_Here.ipynb), be aware that they have a small tolerance for idle machines. As a consequence, a session that is considered "idle" for more than 10 minutes is shutdown and you have to relaunch it again.

To avoid such problems, please try the following:

* keep the tutorial pages always in the foreground
* from the "main" page (click on the logo at the top-left), open a terminal (on the right, look for "New" button and choose "New->Terminal"

With these two hints you shall not have many problems. If your session is deleted, just recreate it again (exercices are made to be sufficiently short).

Also, if your Python kernel fails (sometimes it happens), just try to relaunch it, no worries.

Now, have a nice tutorial sections, that starts with a bit of lecture.

### Alternative environments

Besides mybinder.org, you can run this tutorial in your own computer. This can be done by:
* installing myQLM -> follow the instructions on [myQLM website](https://myqlm.github.io/myqlm_specific/install.html) 
* run a docker container --> `docker run -p 8080:8080 lsteffenel/myqlm-tuto`


## Program for today

1. [Introduction to Quantum Computing](1_Intro_Quantum_Prog.ipynb) - before start coding, this section gives you more elements to understand what is quantum computing from the viewpoint of a software developer. 
2. [Writing a Quantum Program](2_writing_quantum_program.ipynb) - in this section, you will be presented with the basic program structure using Python and myQLM libraries.
3. [Example EPR Pair](3_example_epr_pair.ipynb) - this section presents a complete (but simple) example.
4. [Advanced elements](4_advanced_elements.ipynb) - a few more details on advanced programming elements: gates, control, measurement, circuit export.
5. [Simulation](5_simulation_overview.ipynb) - once you have a program, it's time to simulate the quantum circuit.
6. [Run analysis](6_run_analysis.ipynb) - a rapid overview on how to analyse the results from your simulation.
7. [Exercices](7_Exercices.ipynb) - Hands-on exercices to start developing your own programs

In addition, you can check our [Cheat Sheet](CheatSheet.ipynb) and also the list of [available gates](available_gates.ipynb).



## Credits: 

These documents were developed for the tutorial session on quantum computing introduction at the [4th HPC Summer School 2021](https://cybercolombia.org/program-2021/). The material will remain available at [github](https://github.com/lsteffenel/myqlm-tuto).

### Authors
* Jean-François Couturier (Université de Reims Champagne Ardenne)
* Luiz Angelo Steffenel (Université de Reims Champagne Ardenne)
* Carlos Jaime Barrios Hernandez (Universidad Industrial de Santander)
* Gilberto Javier Diaz Toro (Universidad Industrial de Santander/Université de Reims Champagne Ardenne)

Note: Part of the material is based on [myQLM tutorial](https://github.com/lsteffenel/myqlm-tuto) and the excellent article from [Michel Vanhoutte](https://www.linkedin.com/pulse/understanding-quantum-computing-software-developers-michael-vanhoutte/).
