# Finder-tag-finder
Watches a given path for folders tagged with a color and alerts you with a popup and an audible alert
when found.

The code currently checks for green tags in 30 minute intervals over the course of 4 hours.

Usage:
python main.py /full/path/to/folder/to/watch

Use case:
This was created a friend who to needs to constantly check mounted smb server volume for incoming work.  When new freelance work becomes available, it appears as folders that are labeled with green Finder tags.

This was written for users who work on a company-owned machine, so they do not have admin rights on their (mac) work computers, and thusly cannot install software modules or run cron jobs.  

Because of these constraints, this is initially written in python2 to utilize the mac builtin version of python.

Roadmap:
- Python3 version
- switch to argparse for customizable options (e.g. searching for different color tags, or different time intervals
- Gui?
