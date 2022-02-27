# Finder-tag-finder
Watches a macOS folder path for folders tagged with a specific color and alerts you with a popup and an audible alert
when found.

The code currently searches for green tags in 30 minute intervals over the course of 4 hours.

Usage:
python main.py /full/path/to/folder/to/watch

Use case:
This was created for users who have a need to watch a mounted server volume for incoming work, which appears as folders 
that are labeled with green Finder tags.

This was written for users do not have admin rights on their (mac) work computers, and thusly cannot install modules or run cron jobs.  

Because of these constraints, this is initially written in python2 to utilize the mac builtin version of python.
