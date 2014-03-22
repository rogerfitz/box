The Nice Package
=================
Django webapp for The Nice Package

While django-simple-captcha is cool in production it is a pain to setup. I recommend commenting it out in users/forms.py and believing that it works but here's a url to use it http://stackoverflow.com/questions/4011705/python-the-imagingft-c-module-is-not-installed

* * *

Python Setup
===========

0.0) Mountain Lion (OSX 10.8) to Mavericks (OSX 10.9)
-----------------------

If you updated from Mountain Lion (OSX 10.8) to Mavericks (OSX 10.9) you will need clean up your python environment.

0.1) Anacondas
---------------

If you have Anacondas installed you'll need to remove it. To do that get the path

    $ conda info

This will print out the path of where Anacondas is installed. Remove it

    $ sudo rm -r your/anacondas/path

0.2 Virtualenv
---------------

You'll need to remove and reinstall virtualenv

    $ pip uninstall virtualenv
    $ pip install virtualenv

1) Python Version
------------------

Make sure you are using Python version 2.7.x

    $ python --version

If your using a different version of Python visit the Python site to learn more about version 2.7 and download the latest stable build:
http://www.python.org/download/releases/2.7/

2) Install pip Python Package Manager
-------------------------------------

Enter the following command to make sure you have pip installed on a global level

    $ pip help

If pip is not found then run the following command

    $ easy_install pip

3) Install Virtualenv
---------------------

If you don't already have virtualenv installed use pip to install the package. Virtualenv allows you to manage different Python projects, and their dependencies, within a local scope this eliminating dependency conflicts

    $ pip install virtualenv

Enter the following command to make sure virtualenv install correctly

    $ virtualenv --help

* * *

Local Setup
===========

1) Clone from master or your own fork of master
-----------------------------------------------

    $ git clone https://github.com/rogerfitz/box.git

2) Change into the root directory for Box you just clones and create a new virtualenv
-------------------------------------------------------------------------------------

    $ virtualenv --distribute venv

This will create a new virtual environment called venv (which will be a directory) within the project. You'll then want to activate the new virtualenv:

    $ source venv/bin/activate

Your command line prompt should now be prefixed with (venv). To exit the virtual environment enter:

    (venv)$ deactivate

3) Installing Requirements
--------------------------

If you are on Mac and using OSX 10.9 (Mavericks) chances are your entire Python dev setup is not functional. Follow these instructions: http://attentionshard.wordpress.com/2013/10/25/os-x-mavericks-fixing-broken-python-development-environments/

Once you have everything squared away you should be able to run the following command to install all project requirements:

    (venv)$ pip install -r requirements.txt

Note: You might have an error using the right version of Python if you also use Anacondas. Check out this StackOverflow: http://stackoverflow.com/questions/21635107/pip-executes-the-wrong-python-library-versions-inside-virtual-env

4) Setup Local Django Development
---------------------------------

Obtain the custom_settings.py file by emailing the admin directly. Once you have this settings file you need to change one thing, the BASE_DIR variable:

    BASE_DIR = "/your/path/to/box"

Next, make sure you have MySQL install. If not signup on Oracle's website and download the correct disk image for Mac or Ubuntu.

    $ sudo mysql
    mysql> create database box

Now you should be able to sync the database and run the development server.

    $ venv/bin/python manage.py syncdb
    $ venv/bin/python manage.py runserver

Now go to the development server `http://127.0.0.1:8000/`. You should now see the homepage.

NOTE: Since you changed your custom_settings to reflect your personal environment, and since it should not live on github, make sure you do NOT commit custom_settings.py

