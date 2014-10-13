Python Sphero Examples
--
This repository contains few examples of programming [Sphero](http://www.gosphero.com/) using [Python language](https://www.python.org/) and the [Sphero Python client library](https://github.com/faulkner/sphero) for a total programming/Python/robotics newbie.

Configuration
--
Make sure that Python is installed on your machine, as well as Python Sphero client module:
```sh
pip install sphero
```
Add Sphero device to the OS (double tap the Orb to wake it up and pair it to your PC via bluetooth). Then, on the top of each source code file, find the line:
```python
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP") 
```
and make sure that an appropriate device name is set. Should the Sphero be properly paired and the Sphero's device name correctly set, you can go ahead, run the code and have fun with it!

Usage
--
Run examples with:
```sh
python spheroCircle.py
```
After you've finished games & stuff, tell the Sphero to go to sleep:
```sh
python spheroSleep.py
```

Notes
--
This software has been tested on OS X 10.9 and Sphero 2.0. And it works. On my computer. ;-) Also, check out awesome educational materials on an official Sphero's [Education site](http://www.gosphero.com/education/) that partially inspired the code snippets here. Aw, did I mention that [Sphero](http://www.gosphero.com/) is really cool for playing and learning and (playing and learning)?

License
--
CC
