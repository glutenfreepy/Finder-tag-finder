import datetime
import os
import sys
from time import sleep

import finder_colors
import notifications

# check every 30 minutes for 4 hours
INTERVAL_IN_MINUTES = 30
NUMBER_OF_INTERVALS = 8

USER_DESKTOP_PATH = os.environ['HOME'] + '/Desktop'


def search_for_green_labeled_files(folder_to_search):
    for root, dirs, files in os.walk(folder_to_search, topdown=True):
        for item in dirs:
            obj_path = (root + '/' + str(item))
            obj_color = finder_colors.get(obj_path)
            if obj_color == 'green':
                print(obj_path)
                notifications.desktop_popup("Green Label Found", obj_path)


def main():
    now = datetime.datetime.now()
    n = len(sys.argv)
    if n == 2:
        x = NUMBER_OF_INTERVALS
        while x != 0:
            search_path = sys.argv[1]
            print("")
            print("Searching this location for directories tagged green:")
            print(search_path)
            print("*" * 50)
            print("Found:")
            search_for_green_labeled_files(search_path)
            print("*" * 50)
            print("Search completed at {}.".format(now))
            x = x-1
            print("Filechecker will check {} more times every {} minutes".format(x, INTERVAL_IN_MINUTES))
            sleep(INTERVAL_IN_MINUTES * 60)
    elif n == 1:
        print("Please provide a path to search")
    else:
        print("Too many arguments.  If your path has spaces, be sure to wrap it in quotes")


if __name__ == "__main__":
    main()
