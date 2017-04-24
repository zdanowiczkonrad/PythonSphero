# Python Sphero Examples & Tutorials

This repository contains materials for easy learning of programming [Sphero](http://www.gosphero.com/) using [Python language](https://www.python.org/) and the [Sphero Kulka API](https://github.com/karol-szuster/kulka) by [Karol Szuster](https://github.com/karol-szuster). It is designed for a total programming/Python/robotics newbie.

Directory ```tutorials``` contains a complete guide that introduces each Sphero function step by step with explanation, hints, scaffolding code and microtasks, meanwhile ```examples``` is a place, where fully functional and standalone examples are placed for your experiments.

## Configuration

Make sure that Python is installed on your machine, as well as Python Sphero client module:
```sh
pip install kulka
```
Add Sphero device to the OS (double tap the Orb to wake it up and pair it to your PC via bluetooth). Then, You may use the kulka to connect with the device (knowing it's mac address) in such way:
```python
from kulka import Kulka
from random import randint

with Kulka('01:02:03:04:05:06') as kulka:
    kulka.set_inactivity_timeout(3600)
    kulka.roll(randint(0, 255), randint(0, 359))
```
Should the Sphero be properly paired and the Sphero's device mac correctly set, you can go ahead, run the code and have fun with it!

## Usage

### Examples

Run examples with:
```sh
python spheroCircle.py
```
After you've finished games & stuff, tell the Sphero to go to sleep:
```sh
python spheroSleep.py
```

### Tutorials

Basically, each main directory beginning with a number is a group of smaller tasks, that utilize a specific area of Sphero programming. Explore four sections, namely:
* 1. Hello Sphero
* 2. Sphero basics
* 3. Advanced movement
* 4. Sphero guess game

Each small task is to be done one by one, beginning from the first task. To start the tutorial, open the ```1_<taskname>.py``` file in Sublime, ekhm I meant some good text editor you surely have. There is a description of each task with microtask listed. You may freely modify each file and run it over and over again using simply ```python sometask.py```.

Those examples will guide you through communicating with Sphero, modifying its state (colors or backled light), rotating it and rolling. Last task is also a good practice for Python beginners, where a goal is to implement a game of guessing the number, step by step using feature-oriented programming, where each new functionality is added to the old ones in each and only step.

In order to promote an awesome Polish language, all comments and namings are Polish words ;) A jeżeli rozumiesz co tutaj jest napisane, zapraszam Cię na świetne szkolenia dla początkujących programistów Pythona (i nie tylko) organizowanych przez Geek Girls Carrots, gdzie na żywo prowadzimy uczestników przez te zadania.

### Notes

This software has been tested on Windows and Linux with Sphero1/2 and has code improvements that significantly reduced problems with timeouts and connection drops. Moreover, it is Python 2.x and Python 3.x compatible. There's a known issue with running this code on OS X, that is related to limited compatibility of [bluetooth connector](https://github.com/karulis/pybluez) with this platform. If you would like to try this code on OS X, please checkout our [first release](https://github.com/zdanowiczkonrad/PythonSphero/releases/tag/v1.0.0) using [default Sphero API lib](https://github.com/faulkner/sphero) (beware, it is Python 2.x compatible only). For more sphero-experience check out awesome educational materials on the official Sphero's [Education site](http://www.gosphero.com/education/) that partially inspired the code snippets here. Aw, did I mention that [Sphero](http://www.gosphero.com/) is really cool for playing and learning and (playing and learning)?

### License
CC
