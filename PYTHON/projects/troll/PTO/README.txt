###############
# COMPILATION #
###############

-----------
# Windows #

1. Install python3.11 or higher
(instruction)
https://www.python.org/downloads/

2. Add python to PATH
(instruction)
https://datatofish.com/add-python-to-windows-path/

3. Install dependencies
> cd source_v1.0.1
> python -m pip install -r requirements.txt

4. Compile
> flet pack main.py --name PTO_win --icon <path to icon>

5. Change main icon with "Resource Hacker" app
(download)
http://www.angusj.com/resourcehacker/
(instruction)
https://www.wikihow.com/Change-the-Icon-for-an-Exe-File

---------
# Linux #

1. Install python3.11

2. Install dependencies
$ cd source_v1.0.1
$ python -m pip install -r requirements.txt

3. Compile
$ flet pack main.py --name PTO_win --icon <path to icon>

4. Change main icon
(it is not possible?)
https://stackoverflow.com/questions/64532266/how-to-set-iconor-ico-file-on-executable-file-in-linux-system

##############
# CHANGE LOG #
##############

-----------------
# Version 1.0.1 #

- Added app title;
- 'exceptions' excluded from 'ostatok';
- bug_01 fixed; (check bugs/bug_01.txt);
- Added egg (year=4321).
