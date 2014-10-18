#Python Sphero Examples & Tutorials

This repository contains materials for programming [Sphero](http://www.gosphero.com/) using [Python language](https://www.python.org/) and the [Sphero Python client library](https://github.com/faulkner/sphero) for a total programming/Python/robotics newbie.

Directory ```tutorials``` contains a complete guide that introduces each Sphero function step by step with explanation, hints, scaffolding code and microtasks, meanwhile ```examples``` is a place, where fully functional and standalone examples are placed for your experiments.

##Configuration

Make sure that Python is installed on your machine, as well as Python Sphero client module:
```sh
pip install sphero
```
Add Sphero device to the OS (double tap the Orb to wake it up and pair it to your PC via bluetooth). Then, on the top of each source code file, find the line:
```python
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP") 
```
and make sure that an appropriate device name is set. Should the Sphero be properly paired and the Sphero's device name correctly set, you can go ahead, run the code and have fun with it!

##Usage

###Examples

Run examples with:
```sh
python spheroCircle.py
```
After you've finished games & stuff, tell the Sphero to go to sleep:
```sh
python spheroSleep.py
```

###Tutorials

Basically, each main directory beginning with a number is a group of smaller tasks, that utilize a specific area of Sphero programming. Explore four sections, namely:
* 1. Hello Sphero
* 2. Sphero basics
* 3. Advanced movement
* 4. Sphero guess game

Each small task is to be done one by one, beginning from the first task. To start the tutorial, open the ```1_<taskname>.py``` file in Sublime, ekhm I meant some good text editor you surely have. There is a description of each task with microtask listed. You may freely modify each file and run it over and over again using simply ```python sometask.py```.

Those examples will guide you through communicating with Sphero, modifying its state (colors or backled light), rotating it and rolling. Last task is also a good practice for Python beginners, where a goal is to implement a game of guessing the number, step by step using feature-oriented programming, where each new functionality is added to old ones in each and only step.

###Notes

This software has been tested on OS X 10.9 and Sphero 2.0. I also use Python 2.7 legacy ```raw_input```, so be aware of that when your Python > 3 explodes. Fore more spherexperience check out awesome educational materials on the official Sphero's [Education site](http://www.gosphero.com/education/) that partially inspired the code snippets here. Aw, did I mention that [Sphero](http://www.gosphero.com/) is really cool for playing and learning and (playing and learning)?

###License
CC, I mean go fork it & contribute!
