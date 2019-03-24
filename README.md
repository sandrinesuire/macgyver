Help MacGyver to escape !
===========================

Short description of this project
---------------------------------

A 2D maze in which MacGyver is locked. The exit is supervised by a guard. To distract him, you need to gather the 
following elements (scattered in the labyrinth): a needle, a small plastic tube and ether. 
They will allow MacGyver to create a syringe and lull our guard into sleep.

Specificities of the game
-------------------------
* Only one level, the structure (start, location of the walls, arrival), is recorded in a file. 
* MacGyver is controlled by the arrow keys on the keyboard.
* The objects are randomly distributed in the labyrinth and change with each new game.
* The game window is a square of 15 squares.
* MacGyver retrieve an object simply by moving on it.
* MacGyver wins if he shows up in front of the guardian with all the objects, if he misses objects he dies.
* The program must be standalone, that is it can be run on any computer.

Specificities of the code
-------------------------
* Version the code using Git and post it on Github. 
* Respect the best practices of PEP 8.
* Develop in a virtual environment using Python 3.
* Use the shakespear language.

Install
-------

Virtual environment Linux & Mac
```
pip install virtualenv
virtualenv -p python3 env
source env/bin/activate
```

virtual environment Windows
```
python -m venv env
env\Scripts\activate.bat
```

Mac Don't forget  to update pip before install libraries
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Install the libraries
```
pip install -r requirements.txt
```

Play
----  
Launch start file
```
python start.py
```

Tests
-----
For testing this project run 
```
pytest
```

Platforms
---------
This application was testing on three platforms
* Mac OSX Mojave 10.14.3 + python 3.6.5
* Windows 10 pro 1803 + python 3.7.2
* Ubuntu 18.10 + python 3.6.7

Settings
--------
The labyrinth file is setting on map.txt, you can change the locations as you want (thanks to respect the logic of the 
game).

Remarks
-------
This is a project of validation of competence. Thank you for not offering pull request. You always can open an issues 
and post your remarks. The program is developed under linux (Ubuntu 18.04 64bit).
